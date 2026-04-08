import os
from openmm import CustomCompoundBondForce, CustomCentroidBondForce
from OpenSMOG import SBM
from lxml import etree
from pathlib import Path
from contextlib import redirect_stdout


class SBM(SBM):

    initmsg=R"""
    ##################### OpenSMOGmod (v2.0) ###########################

        OpenSMOGmod: A patch for OpenSMOG adding support for:-
            1) Expressions with more than 2 or 4 atoms.
            2) Potential for Centre-of-Mass (COM) restrain.

        The code is tested to be compatible with OpenSMOG v1.2 but
        should work with v1.1.1 and above. Please run checks/tests
        before using the code. 
        
        Please report issues at github.com/digvijaylp/OpenSMOGmod.
        
        Copyright (C) <2023-present>  <Digvijay Lalwani Prakash>
        This program is released under the MIT License. 
        A copy of MIT License is included along with this program.

    ####################################################################    
    """

    print (initmsg)
    list_of_potential_terms = ['manyparticle','com_pull']
    mod_forceApplied=False

    def _splitForces_COM_pull(self):
        #center-of-mass restrain
        com_data=self.mod_data['com_pull']
        n_forces =  len(com_data[3])
        forces = {}
        for n in range(n_forces):
            forces[com_data[3][n]] = [com_data[0][n], com_data[1][n], com_data[2][n],com_data[4][n]]
        self.com_pull = forces

    def _splitForces_manyparticle(self):
        #many particle force
        cont_data=self.mod_data['manyparticle']
        n_forces =  len(cont_data[3])
        forces = {}
        for n in range(n_forces):
            forces[cont_data[3][n]] = [cont_data[0][n], cont_data[1][n], cont_data[2][n]]
        self.manyparticle = forces
        
    def _customCOMForce(self, name, data):
        #first set the equation
        """ '|' is used as a delimiter between number of interacting
        groups and the expression for potential energy between those groups"""
        if '|' in data[0]:
            data[0] = (data[0].split('|'))
            Ngroups = int(data[0][0])
            customExp = data[0][1]
        else:
            Ngroups = 2 #default
            customExp = data[0]
        pull_ff = CustomCentroidBondForce(Ngroups,customExp)

        #second add the atom groups
        groupAtom_ndx = {}
        for group in data[-1]: #data[4]
            if int(group['index']) <= 0:
                SBM.opensmog_quit('Group index must be a positive integer')
            """atom index format atoms='b1:e1:i1,b2,e2,i2' will load atoms
            in range b1 to e1 with interval i1 and from b2 to e2 with interval i2"""
            group_atoms = [x.split(':')+['1'] for x in group['atoms'].split(',')]
            group_atoms = [list(range(int(x[0]),int(x[1])+1,int(x[2]))) for x in group_atoms]            
            group_atoms = [x-1 for ndx_range in group_atoms for x in ndx_range]
            groupAtom_ndx[int(group['index'])-1] = group_atoms
        #groups are to be loaded in the order of their specified index
        groupAtom_ndx = [groupAtom_ndx[x] for x in range(Ngroups)]
        for group in groupAtom_ndx:
            pull_ff.addGroup(group)

        #third set the number of variable
        for pars in data[1]:
            pull_ff.addPerBondParameter(pars)

        #fourth, apply the bonds from each pair of atom groups and the related variables.
        pars = [pars for pars in data[1]]            

        for iteraction in data[2]:
            group_ = [int(iteraction[chr(k+ord('i'))])-1 for k in range(Ngroups)]
            parameters = [float(iteraction[k]) for k in pars]
            pull_ff.addBond(group_, parameters)
        self.forcesDict[name] =  pull_ff
        pull_ff.setForceGroup(self.forceCount)
        self.forceCount +=1

    def _customManyParticleForce(self, name, data, pbc):
        #first set the equation
        """ '|' is used as a delimiter between numbre of particles
        and the expression for potential energy between them"""
        if '|' in data[0]:        
            data[0] = (data[0].split('|'))
            Nparticles = int(data[0][0])
            customExp = data[0][1]
        else:
            Nparticles = 2 #default
            customExp = data[0]
        contacts_ff = CustomCompoundBondForce(Nparticles,customExp)
        contacts_ff.setUsesPeriodicBoundaryConditions(pbc)

        #second set the number of variable
        for pars in data[1]:
            contacts_ff.addPerBondParameter(pars)

        #third, apply the bonds from each pair of atoms and the related variables.
        pars = [pars for pars in data[1]]

        for iteraction in data[2]:
            atom_index_ = [int(iteraction[chr(k+ord('i'))])-1 for k in range(Nparticles)]
            parameters = [float(iteraction[k]) for k in pars]
            contacts_ff.addBond(atom_index_, parameters)

        #forth, if the are global variables, add them to the force
        if self.constants_present==True:
            for const_key in self.data['constants']:
                contacts_ff.addGlobalParameter(const_key,self.data['constants'][const_key])
        self.forcesDict[name] =  contacts_ff
        contacts_ff.setForceGroup(self.forceCount)
        self.forceCount +=1


    def import_mod2OpenSMOG(self,text_xml=None,file_xml=None):
        R"""
        Args:

            file_xml (file, required if text_xml is None)
                OpenSMOGmod *.xml* file with <OpenSMOGmod> as root element. The file must contain at least one of the OpenSMOGmod potential terms (manyparticle or com_pull). Please refer to the documentation for details on the format of the xml file.
            OR
            text_xml (str, required if file_xml is None)
                OpenSMOGmod XML string from derived from *OpenSMOGmod* Processing Instruction(s) in the OpenSMOG *.xml* file. 
        """

        #create root
        if text_xml is not None:
            root=etree.fromstring(text_xml)
        if file_xml is not None:
            root=etree.parse(file_xml)

        xml_data={}
        modmissing=0
        for mp in self.list_of_potential_terms:
            if root.find(mp) is None: modmissing+=1
        if modmissing!=0:
            SBM.opensmog_quit('No OpenSMOGmod potential term found. Please import SBM directly from OpenSMOG. OpenSMOGmod potential terms include: '+str(self.list_of_potential_terms))
            

        #center of mass COM restrain
        Force_Names=[]
        Expression=[]
        Parameters=[]
        AtomGroups = []
        Party=[]
        self.com_pull_present=False
        if root.find('com_pull') != None:
            self.com_pull_present=True
            com_pull_xml=root.find('com_pull')
            for i in range(len(com_pull_xml)):
                #Potential name
                for name in com_pull_xml[i].iter('pull_type'):
                    Force_Names.append(name.attrib['name'])
                #Potential expression
                for expr in com_pull_xml[i].iter('expression'):
                    expr_string=expr.attrib['expr']
                    if 'num' in expr.attrib:
                        if '|' in expr_string:
                            SBM.opensmog_quit('Expression for COM pull potential cannot contain '|' if number of interacting groups is specified as an attribute.')  
                        expr_string='%s|%s'%(expr.attrib['num'],expr_string)
                    Expression.append(expr_string)
                #internal parameters
                internal_Param=[]
                for par in com_pull_xml[i].iter('parameter'):
                    internal_Param.append(par.text)
                Parameters.append(internal_Param)
                #atom groups
                internal_groups=[]
                for grp in com_pull_xml[i].iter('group'):
                    internal_groups.append(grp.attrib)
                AtomGroups.append(internal_groups)
                # Ntuple
                internal_party=[]
                for grpparty in com_pull_xml[i].iter('interaction'):
                    internal_party.append(grpparty.attrib)
                Party.append(internal_party)
            xml_data['com_pull']=[Expression,Parameters,Party,Force_Names,AtomGroups]
        else: print('No COM pull potential found in xml file.')

        ## custom many particle force 
        Force_Names=[]
        Expression=[]
        Parameters=[]
        Party=[]
        self.manyparticle_present=False
        if root.find('manyparticle') != None:
            self.manyparticle_present=True
            manyparticle_xml=root.find('manyparticle')
            for i in range(len(manyparticle_xml)):
                #Potential name
                for name in manyparticle_xml[i].iter('manyparticle_type'):
                    Force_Names.append(name.attrib['name'])
                #Potential expression
                for expr in manyparticle_xml[i].iter('expression'):
                    expr_string=expr.attrib['expr']
                    if 'num' in expr.attrib:
                        if '|' in expr_string:
                            SBM.opensmog_quit('Expression for many particle potential cannot contain '|' if number of interacting particles is specified as an attribute.')  
                        expr_string='%s|%s'%(expr.attrib['num'],expr_string)
                    Expression.append(expr_string)
                #internal parameters
                internal_Param=[]
                for par in manyparticle_xml[i].iter('parameter'):
                    internal_Param.append(par.text)
                Parameters.append(internal_Param)
                # Party
                internal_party=[]
                for atomparty in manyparticle_xml[i].iter('interaction'):
                    internal_party.append(atomparty.attrib)
                Party.append(internal_party)
            xml_data['manyparticle']=[Expression,Parameters,Party,Force_Names]
        else: print('No many particle potential found in xml file.')        

        self.mod_data=xml_data
        
        if not (self.mod_forceApplied):
            if self.manyparticle_present==True:
                self._splitForces_manyparticle()
                for force in self.manyparticle:
                    print('\tAugmenting many particle force {:} from OpenSMOGmd'.format(force))
                    self._customManyParticleForce(force, self.manyparticle[force], self.pbc)
                    self.system.addForce(self.forcesDict[force])
            if self.com_pull_present==True:   
                self._splitForces_COM_pull()
                for force in self.com_pull:
                    print('\tAugmenting COM restrain force {:} from OpenSMOGmd'.format(force))
                    self._customCOMForce(force, self.com_pull[force])
                    #self.system.addForce(self.forcesDict[force])
            self.mod_forceApplied=True

        if text_xml is not None:
            print ('\nLoaded additional force field terms from XML Processing Instructions.')
        elif file_xml is not None:
            print ('\nLoaded additional force field terms from XML Mod-file')

    def validate_OpenSMOGmod(self,text_xml=None,file_xml=None):
        R"""
        Args:

            file_xml (file, required if text_xml is None)
                OpenSMOGmod *.xml* file with <OpenSMOGmod> as root element. The file must contain at least one of the OpenSMOGmod potential terms (manyparticle or com_pull). Please refer to the documentation for details on the format of the xml file.
            OR
            text_xml (str, required if file_xml is None)
                OpenSMOGmod XML string from derived from *OpenSMOGmod* Processing Instruction(s) in the OpenSMOG *.xml* file. 
        """
        path = 'OpenSMOGmod.xsd'
        pt = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(pt,path)
        xmlschema_doc = etree.parse(filepath)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        
        if text_xml is None:
            if file_xml == None:
                SBM.opensmog_quit('Could not find OpenSMOGmod XML file or Processing Instructions.')
            if not os.path.exists(file_xml):
                SBM.opensmog_quit('Could not find OpenSMOGmod XML file or Processing Instructions.')
            xml_doc=etree.parse(file_xml)
        elif text_xml is not None:
            xml_doc=etree.fromstring(text_xml)
             
        result=xmlschema.validate(xml_doc)
        log=xmlschema.error_log
        if not result:
            SBM.opensmog_quit('The OpenSMOGmod section does not adhere to the required schema. Error message:\n\n'+str(log)+'\n\n')

        return result,log

    def loadProcessingInstructions(self, Xmlfile):
        R"""
        Args:

            Xmlfile (file, required):
                Same OpenSMOG  *.xml* file must contain Processing Instructionn(s)).
        """
        PItree=etree.parse(Xmlfile)
        modpotentials='<OpenSMOGmod>\n'
        PIs=PItree.xpath('//processing-instruction("OpenSMOGmod")')
        for pi in PIs:
            if pi.target=='OpenSMOGmod':
                modpotentials+=pi.text
        modpotentials+='</OpenSMOGmod>'

        self.validate_OpenSMOGmod(text_xml=modpotentials)

        self.import_mod2OpenSMOG(text_xml=modpotentials)

        return

    def loadModXML(self, modXmlfile):
        R"""
        Args:

            Xmlfile (file, required):
                OpenSMOGmod *.xml* file must contain manyparticle and/or com_pull potential terms with <OpenSMOGmod> as root element. 
        """
        self.validate_OpenSMOGmod(file_xml=modXmlfile)

        self.import_mod2OpenSMOG(file_xml=modXmlfile)

    def loadSystemFiles (self, Grofile, Topfile, Xmlfile, Modfile=None):
        R"""Args:

            Grofile (file, required):
                Initial structure for the MD simulations in *.gro* file format generated by SMOG2 software with the flag :code:`-OpenSMOG`.  (Default value: :code:`None`).
            Topfile (file, required):
                Topology *.top* file format generated by SMOG2 software with the flag :code:`-OpenSMOG`. The topology file lists the interactions between the system atoms except for the "Native Contacts" potential that is provided to OpenSMOG in a *.xml* file. (Default value: :code:`None`).
            Xmlfile (file, required):
                The *.xml* file can contain the information that defines the "Contact" and nonbonded potentials. The *.xml* file is generated by SMOG2 software with the flag :code:`-OpenSMOG`, which support custom potential functions. (Default value: :code:`None`).
            Modfile (file, optional):
                OpenSMOGmod *.xml* file with <OpenSMOGmod> as root element. The file must contain at least one of the OpenSMOGmod potential terms (manyparticle or com_pull). If not priveded, the code will look for <?OpenSMOGmod....?> Processing Instructions in the Xmlfile. 
        """

        self.loadSystem(Grofile=Grofile, Topfile=Topfile, Xmlfile=Xmlfile)
        print ('\n')
        if Modfile is None or len(Modfile)==0: 
            self.loadProcessingInstructions(Xmlfile=Xmlfile)
        else: 
            self.loadModXML(modXmlfile=Modfile)
        print ('\n')
        return       
        
            

        
