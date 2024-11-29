
MODULE OpenMM_Types
    implicit none

    ! Global Constants


    ! Type Declarations

    type OpenMM_AmoebaVdwForce
        integer*8 :: handle = 0
    end type

    type OpenMM_AmoebaWcaDispersionForce
        integer*8 :: handle = 0
    end type

    type OpenMM_HippoNonbondedForce
        integer*8 :: handle = 0
    end type

    type OpenMM_AmoebaGeneralizedKirkwoodForce
        integer*8 :: handle = 0
    end type

    type OpenMM_AmoebaMultipoleForce
        integer*8 :: handle = 0
    end type

    type OpenMM_AmoebaTorsionTorsionForce
        integer*8 :: handle = 0
    end type

    ! Enumerations

    integer*4, parameter :: OpenMM_False = 0
    integer*4, parameter :: OpenMM_True = 1
    integer*4, parameter :: OpenMM_AmoebaVdwForce_NoCutoff = 0
    integer*4, parameter :: OpenMM_AmoebaVdwForce_CutoffPeriodic = 1
    integer*4, parameter :: OpenMM_AmoebaVdwForce_Buffered147 = 0
    integer*4, parameter :: OpenMM_AmoebaVdwForce_LennardJones = 1
    integer*4, parameter :: OpenMM_AmoebaVdwForce_None = 0
    integer*4, parameter :: OpenMM_AmoebaVdwForce_Decouple = 1
    integer*4, parameter :: OpenMM_AmoebaVdwForce_Annihilate = 2

    integer*4, parameter :: OpenMM_HippoNonbondedForce_NoCutoff = 0
    integer*4, parameter :: OpenMM_HippoNonbondedForce_PME = 1
    integer*4, parameter :: OpenMM_HippoNonbondedForce_ZThenX = 0
    integer*4, parameter :: OpenMM_HippoNonbondedForce_Bisector = 1
    integer*4, parameter :: OpenMM_HippoNonbondedForce_ZBisect = 2
    integer*4, parameter :: OpenMM_HippoNonbondedForce_ThreeFold = 3
    integer*4, parameter :: OpenMM_HippoNonbondedForce_ZOnly = 4
    integer*4, parameter :: OpenMM_HippoNonbondedForce_NoAxisType = 5

    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_NoCutoff = 0
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_PME = 1
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Mutual = 0
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Direct = 1
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Extrapolated = 2
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_ZThenX = 0
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Bisector = 1
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_ZBisect = 2
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_ThreeFold = 3
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_ZOnly = 4
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_NoAxisType = 5
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_LastAxisTypeIndex = 6
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Covalent12 = 0
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Covalent13 = 1
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Covalent14 = 2
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_Covalent15 = 3
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_PolarizationCovalent11 = 4
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_PolarizationCovalent12 = 5
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_PolarizationCovalent13 = 6
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_PolarizationCovalent14 = 7
    integer*4, parameter :: OpenMM_AmoebaMultipoleForce_CovalentEnd = 8


END MODULE OpenMM_Types

MODULE OpenMM
    use OpenMM_Types; implicit none
    interface


        ! OpenMM::AmoebaVdwForce
        subroutine OpenMM_AmoebaVdwForce_create(result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) result
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_destroy(destroy)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) destroy
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_Lambda(result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            character(*) result
        end subroutine
        function OpenMM_AmoebaVdwForce_getNumParticles(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 OpenMM_AmoebaVdwForce_getNumParticles
        end function
        function OpenMM_AmoebaVdwForce_getNumParticleTypes(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 OpenMM_AmoebaVdwForce_getNumParticleTypes
        end function
        function OpenMM_AmoebaVdwForce_getNumTypePairs(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 OpenMM_AmoebaVdwForce_getNumTypePairs
        end function
        subroutine OpenMM_AmoebaVdwForce_setParticleParameters(target, particleIndex, &
parentIndex, &
sigma, &
epsilon, &
reductionFactor, &
isAlchemical, &
typeIndex)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 particleIndex
            integer*4 parentIndex
            real*8 sigma
            real*8 epsilon
            real*8 reductionFactor
            integer*4 isAlchemical
            integer*4 typeIndex
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_getParticleParameters(target, particleIndex, &
parentIndex, &
sigma, &
epsilon, &
reductionFactor, &
isAlchemical, &
typeIndex)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 particleIndex
            integer*4 parentIndex
            real*8 sigma
            real*8 epsilon
            real*8 reductionFactor
            integer*4 isAlchemical
            integer*4 typeIndex
        end subroutine
        function OpenMM_AmoebaVdwForce_addParticle(target, parentIndex, &
sigma, &
epsilon, &
reductionFactor, &
isAlchemical)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 parentIndex
            real*8 sigma
            real*8 epsilon
            real*8 reductionFactor
            integer*4 isAlchemical
            integer*4 OpenMM_AmoebaVdwForce_addParticle
        end function
        function OpenMM_AmoebaVdwForce_addParticle_1(target, parentIndex, &
typeIndex, &
reductionFactor, &
isAlchemical)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 parentIndex
            integer*4 typeIndex
            real*8 reductionFactor
            integer*4 isAlchemical
            integer*4 OpenMM_AmoebaVdwForce_addParticle_1
        end function
        function OpenMM_AmoebaVdwForce_addParticleType(target, sigma, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            real*8 sigma
            real*8 epsilon
            integer*4 OpenMM_AmoebaVdwForce_addParticleType
        end function
        subroutine OpenMM_AmoebaVdwForce_getParticleTypeParameters(target, typeIndex, &
sigma, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 typeIndex
            real*8 sigma
            real*8 epsilon
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setParticleTypeParameters(target, typeIndex, &
sigma, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 typeIndex
            real*8 sigma
            real*8 epsilon
        end subroutine
        function OpenMM_AmoebaVdwForce_addTypePair(target, type1, &
type2, &
sigma, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 type1
            integer*4 type2
            real*8 sigma
            real*8 epsilon
            integer*4 OpenMM_AmoebaVdwForce_addTypePair
        end function
        subroutine OpenMM_AmoebaVdwForce_getTypePairParameters(target, pairIndex, &
type1, &
type2, &
sigma, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 pairIndex
            integer*4 type1
            integer*4 type2
            real*8 sigma
            real*8 epsilon
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setTypePairParameters(target, pairIndex, &
type1, &
type2, &
sigma, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 pairIndex
            integer*4 type1
            integer*4 type2
            real*8 sigma
            real*8 epsilon
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setSigmaCombiningRule(target, sigmaCombiningRule)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            character(*) sigmaCombiningRule
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_getSigmaCombiningRule(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            character(*) result
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setEpsilonCombiningRule(target, epsilonCombiningRule)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            character(*) epsilonCombiningRule
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_getEpsilonCombiningRule(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            character(*) result
        end subroutine
        function OpenMM_AmoebaVdwForce_getUseDispersionCorrection(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 OpenMM_AmoebaVdwForce_getUseDispersionCorrection
        end function
        subroutine OpenMM_AmoebaVdwForce_setUseDispersionCorrection(target, useCorrection)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 useCorrection
        end subroutine
        function OpenMM_AmoebaVdwForce_getUseParticleTypes(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 OpenMM_AmoebaVdwForce_getUseParticleTypes
        end function
        subroutine OpenMM_AmoebaVdwForce_setParticleExclusions(target, particleIndex, &
exclusions)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 particleIndex
            type (OpenMM_IntArray) exclusions
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_getParticleExclusions(target, particleIndex, &
exclusions)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 particleIndex
            type (OpenMM_IntArray) exclusions
        end subroutine
        function OpenMM_AmoebaVdwForce_getCutoffDistance(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            real*8 OpenMM_AmoebaVdwForce_getCutoffDistance
        end function
        subroutine OpenMM_AmoebaVdwForce_setCutoffDistance(target, distance)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            real*8 distance
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setCutoff(target, cutoff)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            real*8 cutoff
        end subroutine
        function OpenMM_AmoebaVdwForce_getCutoff(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            real*8 OpenMM_AmoebaVdwForce_getCutoff
        end function
        subroutine OpenMM_AmoebaVdwForce_getNonbondedMethod(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            type (OpenMM_AmoebaMultipoleForce_NonbondedMethod) result
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setNonbondedMethod(target, method)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            type (OpenMM_AmoebaMultipoleForce_NonbondedMethod) method
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_getPotentialFunction(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            type (OpenMM_AmoebaVdwForce_PotentialFunction) result
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setPotentialFunction(target, potential)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            type (OpenMM_AmoebaVdwForce_PotentialFunction) potential
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setSoftcorePower(target, n)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 n
        end subroutine
        function OpenMM_AmoebaVdwForce_getSoftcorePower(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 OpenMM_AmoebaVdwForce_getSoftcorePower
        end function
        subroutine OpenMM_AmoebaVdwForce_setSoftcoreAlpha(target, alpha)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            real*8 alpha
        end subroutine
        function OpenMM_AmoebaVdwForce_getSoftcoreAlpha(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            real*8 OpenMM_AmoebaVdwForce_getSoftcoreAlpha
        end function
        subroutine OpenMM_AmoebaVdwForce_getAlchemicalMethod(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            type (OpenMM_AmoebaVdwForce_AlchemicalMethod) result
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_setAlchemicalMethod(target, method)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            type (OpenMM_AmoebaVdwForce_AlchemicalMethod) method
        end subroutine
        subroutine OpenMM_AmoebaVdwForce_updateParametersInContext(target, context)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            Context context
        end subroutine
        function OpenMM_AmoebaVdwForce_usesPeriodicBoundaryConditions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaVdwForce) target
            integer*4 OpenMM_AmoebaVdwForce_usesPeriodicBoundaryConditions
        end function

        ! OpenMM::AmoebaWcaDispersionForce
        subroutine OpenMM_AmoebaWcaDispersionForce_create(result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) result
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_destroy(destroy)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) destroy
        end subroutine
        function OpenMM_AmoebaWcaDispersionForce_getNumParticles(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            integer*4 OpenMM_AmoebaWcaDispersionForce_getNumParticles
        end function
        subroutine OpenMM_AmoebaWcaDispersionForce_setParticleParameters(target, particleIndex, &
radius, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            integer*4 particleIndex
            real*8 radius
            real*8 epsilon
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_getParticleParameters(target, particleIndex, &
radius, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            integer*4 particleIndex
            real*8 radius
            real*8 epsilon
        end subroutine
        function OpenMM_AmoebaWcaDispersionForce_addParticle(target, radius, &
epsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 radius
            real*8 epsilon
            integer*4 OpenMM_AmoebaWcaDispersionForce_addParticle
        end function
        subroutine OpenMM_AmoebaWcaDispersionForce_updateParametersInContext(target, context)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            Context context
        end subroutine
        function OpenMM_AmoebaWcaDispersionForce_getEpso(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getEpso
        end function
        function OpenMM_AmoebaWcaDispersionForce_getEpsh(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getEpsh
        end function
        function OpenMM_AmoebaWcaDispersionForce_getRmino(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getRmino
        end function
        function OpenMM_AmoebaWcaDispersionForce_getRminh(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getRminh
        end function
        function OpenMM_AmoebaWcaDispersionForce_getAwater(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getAwater
        end function
        function OpenMM_AmoebaWcaDispersionForce_getShctd(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getShctd
        end function
        function OpenMM_AmoebaWcaDispersionForce_getDispoff(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getDispoff
        end function
        function OpenMM_AmoebaWcaDispersionForce_getSlevy(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 OpenMM_AmoebaWcaDispersionForce_getSlevy
        end function
        subroutine OpenMM_AmoebaWcaDispersionForce_setEpso(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_setEpsh(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_setRmino(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_setRminh(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_setAwater(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_setShctd(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_setDispoff(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        subroutine OpenMM_AmoebaWcaDispersionForce_setSlevy(target, inputValue)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            real*8 inputValue
        end subroutine
        function OpenMM_AmoebaWcaDispersionForce_usesPeriodicBoundaryConditions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaWcaDispersionForce) target
            integer*4 OpenMM_AmoebaWcaDispersionForce_usesPeriodicBoundaryConditions
        end function

        ! OpenMM::HippoNonbondedForce
        subroutine OpenMM_HippoNonbondedForce_create(result)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) result
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_destroy(destroy)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) destroy
        end subroutine
        function OpenMM_HippoNonbondedForce_getNumParticles(target)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 OpenMM_HippoNonbondedForce_getNumParticles
        end function
        function OpenMM_HippoNonbondedForce_getNumExceptions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 OpenMM_HippoNonbondedForce_getNumExceptions
        end function
        subroutine OpenMM_HippoNonbondedForce_getNonbondedMethod(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            type (OpenMM_AmoebaMultipoleForce_NonbondedMethod) result
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_setNonbondedMethod(target, method)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            type (OpenMM_AmoebaMultipoleForce_NonbondedMethod) method
        end subroutine
        function OpenMM_HippoNonbondedForce_getCutoffDistance(target)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 OpenMM_HippoNonbondedForce_getCutoffDistance
        end function
        subroutine OpenMM_HippoNonbondedForce_setCutoffDistance(target, distance)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 distance
        end subroutine
        function OpenMM_HippoNonbondedForce_getSwitchingDistance(target)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 OpenMM_HippoNonbondedForce_getSwitchingDistance
        end function
        subroutine OpenMM_HippoNonbondedForce_setSwitchingDistance(target, distance)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 distance
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_getExtrapolationCoefficients(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            type (OpenMM_DoubleArray) result
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_setExtrapolationCoefficients(target, coefficients)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            type (OpenMM_DoubleArray) coefficients
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_getPMEParameters(target, alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_getDPMEParameters(target, alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_setPMEParameters(target, alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_setDPMEParameters(target, alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_getPMEParametersInContext(target, context, &
alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            Context context
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_getDPMEParametersInContext(target, context, &
alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            Context context
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        function OpenMM_HippoNonbondedForce_addParticle(target, charge, &
dipole, &
quadrupole, &
coreCharge, &
alpha, &
epsilon, &
damping, &
c6, &
pauliK, &
pauliQ, &
pauliAlpha, &
polarizability, &
axisType, &
multipoleAtomZ, &
multipoleAtomX, &
multipoleAtomY)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 charge
            type (OpenMM_DoubleArray) dipole
            type (OpenMM_DoubleArray) quadrupole
            real*8 coreCharge
            real*8 alpha
            real*8 epsilon
            real*8 damping
            real*8 c6
            real*8 pauliK
            real*8 pauliQ
            real*8 pauliAlpha
            real*8 polarizability
            integer*4 axisType
            integer*4 multipoleAtomZ
            integer*4 multipoleAtomX
            integer*4 multipoleAtomY
            integer*4 OpenMM_HippoNonbondedForce_addParticle
        end function
        subroutine OpenMM_HippoNonbondedForce_getParticleParameters(target, index, &
charge, &
dipole, &
quadrupole, &
coreCharge, &
alpha, &
epsilon, &
damping, &
c6, &
pauliK, &
pauliQ, &
pauliAlpha, &
polarizability, &
axisType, &
multipoleAtomZ, &
multipoleAtomX, &
multipoleAtomY)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 index
            real*8 charge
            type (OpenMM_DoubleArray) dipole
            type (OpenMM_DoubleArray) quadrupole
            real*8 coreCharge
            real*8 alpha
            real*8 epsilon
            real*8 damping
            real*8 c6
            real*8 pauliK
            real*8 pauliQ
            real*8 pauliAlpha
            real*8 polarizability
            integer*4 axisType
            integer*4 multipoleAtomZ
            integer*4 multipoleAtomX
            integer*4 multipoleAtomY
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_setParticleParameters(target, index, &
charge, &
dipole, &
quadrupole, &
coreCharge, &
alpha, &
epsilon, &
damping, &
c6, &
pauliK, &
pauliQ, &
pauliAlpha, &
polarizability, &
axisType, &
multipoleAtomZ, &
multipoleAtomX, &
multipoleAtomY)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 index
            real*8 charge
            type (OpenMM_DoubleArray) dipole
            type (OpenMM_DoubleArray) quadrupole
            real*8 coreCharge
            real*8 alpha
            real*8 epsilon
            real*8 damping
            real*8 c6
            real*8 pauliK
            real*8 pauliQ
            real*8 pauliAlpha
            real*8 polarizability
            integer*4 axisType
            integer*4 multipoleAtomZ
            integer*4 multipoleAtomX
            integer*4 multipoleAtomY
        end subroutine
        function OpenMM_HippoNonbondedForce_addException(target, particle1, &
particle2, &
multipoleMultipoleScale, &
dipoleMultipoleScale, &
dipoleDipoleScale, &
dispersionScale, &
repulsionScale, &
chargeTransferScale, &
replace)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 particle1
            integer*4 particle2
            real*8 multipoleMultipoleScale
            real*8 dipoleMultipoleScale
            real*8 dipoleDipoleScale
            real*8 dispersionScale
            real*8 repulsionScale
            real*8 chargeTransferScale
            integer*4 replace
            integer*4 OpenMM_HippoNonbondedForce_addException
        end function
        subroutine OpenMM_HippoNonbondedForce_getExceptionParameters(target, index, &
particle1, &
particle2, &
multipoleMultipoleScale, &
dipoleMultipoleScale, &
dipoleDipoleScale, &
dispersionScale, &
repulsionScale, &
chargeTransferScale)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 index
            integer*4 particle1
            integer*4 particle2
            real*8 multipoleMultipoleScale
            real*8 dipoleMultipoleScale
            real*8 dipoleDipoleScale
            real*8 dispersionScale
            real*8 repulsionScale
            real*8 chargeTransferScale
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_setExceptionParameters(target, index, &
particle1, &
particle2, &
multipoleMultipoleScale, &
dipoleMultipoleScale, &
dipoleDipoleScale, &
dispersionScale, &
repulsionScale, &
chargeTransferScale)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 index
            integer*4 particle1
            integer*4 particle2
            real*8 multipoleMultipoleScale
            real*8 dipoleMultipoleScale
            real*8 dipoleDipoleScale
            real*8 dispersionScale
            real*8 repulsionScale
            real*8 chargeTransferScale
        end subroutine
        function OpenMM_HippoNonbondedForce_getEwaldErrorTolerance(target)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 OpenMM_HippoNonbondedForce_getEwaldErrorTolerance
        end function
        subroutine OpenMM_HippoNonbondedForce_setEwaldErrorTolerance(target, tol)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            real*8 tol
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_getLabFramePermanentDipoles(target, context, &
dipoles)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            Context context
            type (OpenMM_Vec3Array) dipoles
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_getInducedDipoles(target, context, &
dipoles)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            Context context
            type (OpenMM_Vec3Array) dipoles
        end subroutine
        subroutine OpenMM_HippoNonbondedForce_updateParametersInContext(target, context)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            Context context
        end subroutine
        function OpenMM_HippoNonbondedForce_usesPeriodicBoundaryConditions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_HippoNonbondedForce) target
            integer*4 OpenMM_HippoNonbondedForce_usesPeriodicBoundaryConditions
        end function

        ! OpenMM::AmoebaGeneralizedKirkwoodForce
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_create(result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) result
        end subroutine
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_destroy(destroy)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) destroy
        end subroutine
        function OpenMM_AmoebaGeneralizedKirkwoodForce_getNumParticles(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            integer*4 OpenMM_AmoebaGeneralizedKirkwoodForce_getNumParticles
        end function
        function OpenMM_AmoebaGeneralizedKirkwoodForce_addParticle(target, charge, &
radius, &
scalingFactor)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 charge
            real*8 radius
            real*8 scalingFactor
            integer*4 OpenMM_AmoebaGeneralizedKirkwoodForce_addParticle
        end function
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_getParticleParameters(target, index, &
charge, &
radius, &
scalingFactor)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            integer*4 index
            real*8 charge
            real*8 radius
            real*8 scalingFactor
        end subroutine
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_setParticleParameters(target, index, &
charge, &
radius, &
scalingFactor)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            integer*4 index
            real*8 charge
            real*8 radius
            real*8 scalingFactor
        end subroutine
        function OpenMM_AmoebaGeneralizedKirkwoodForce_getSolventDielectric(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 OpenMM_AmoebaGeneralizedKirkwoodForce_getSolventDielectric
        end function
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_setSolventDielectric(target, dielectric)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 dielectric
        end subroutine
        function OpenMM_AmoebaGeneralizedKirkwoodForce_getSoluteDielectric(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 OpenMM_AmoebaGeneralizedKirkwoodForce_getSoluteDielectric
        end function
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_setSoluteDielectric(target, dielectric)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 dielectric
        end subroutine
        function OpenMM_AmoebaGeneralizedKirkwoodForce_getIncludeCavityTerm(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            integer*4 OpenMM_AmoebaGeneralizedKirkwoodForce_getIncludeCavityTerm
        end function
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_setIncludeCavityTerm(target, includeCavityTerm)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            integer*4 includeCavityTerm
        end subroutine
        function OpenMM_AmoebaGeneralizedKirkwoodForce_getProbeRadius(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 OpenMM_AmoebaGeneralizedKirkwoodForce_getProbeRadius
        end function
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_setProbeRadius(target, probeRadius)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 probeRadius
        end subroutine
        function OpenMM_AmoebaGeneralizedKirkwoodForce_getSurfaceAreaFactor(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 OpenMM_AmoebaGeneralizedKirkwoodForce_getSurfaceAreaFactor
        end function
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_setSurfaceAreaFactor(target, surfaceAreaFactor)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            real*8 surfaceAreaFactor
        end subroutine
        subroutine OpenMM_AmoebaGeneralizedKirkwoodForce_updateParametersInContext(target, context)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            Context context
        end subroutine
        function OpenMM_AmoebaGeneralizedKirkwoodForce_usesPeriodicBoundaryConditions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaGeneralizedKirkwoodForce) target
            integer*4 OpenMM_AmoebaGeneralizedKirkwoodForce_usesPeriodicBoundaryConditions
        end function

        ! OpenMM::AmoebaMultipoleForce
        subroutine OpenMM_AmoebaMultipoleForce_create(result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) result
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_destroy(destroy)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) destroy
        end subroutine
        function OpenMM_AmoebaMultipoleForce_getNumMultipoles(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 OpenMM_AmoebaMultipoleForce_getNumMultipoles
        end function
        subroutine OpenMM_AmoebaMultipoleForce_getNonbondedMethod(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_AmoebaMultipoleForce_NonbondedMethod) result
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_setNonbondedMethod(target, method)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_AmoebaMultipoleForce_NonbondedMethod) method
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getPolarizationType(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_AmoebaMultipoleForce_PolarizationType) result
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_setPolarizationType(target, type)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_AmoebaMultipoleForce_PolarizationType) type
        end subroutine
        function OpenMM_AmoebaMultipoleForce_getCutoffDistance(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 OpenMM_AmoebaMultipoleForce_getCutoffDistance
        end function
        subroutine OpenMM_AmoebaMultipoleForce_setCutoffDistance(target, distance)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 distance
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getPMEParameters(target, alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_setPMEParameters(target, alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        function OpenMM_AmoebaMultipoleForce_getAEwald(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 OpenMM_AmoebaMultipoleForce_getAEwald
        end function
        subroutine OpenMM_AmoebaMultipoleForce_setAEwald(target, aewald)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 aewald
        end subroutine
        function OpenMM_AmoebaMultipoleForce_getPmeBSplineOrder(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 OpenMM_AmoebaMultipoleForce_getPmeBSplineOrder
        end function
        subroutine OpenMM_AmoebaMultipoleForce_getPmeGridDimensions(target, gridDimension)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_IntArray) gridDimension
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_setPmeGridDimensions(target, gridDimension)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_IntArray) gridDimension
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getPMEParametersInContext(target, context, &
alpha, &
nx, &
ny, &
nz)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            Context context
            real*8 alpha
            integer*4 nx
            integer*4 ny
            integer*4 nz
        end subroutine
        function OpenMM_AmoebaMultipoleForce_addMultipole(target, charge, &
molecularDipole, &
molecularQuadrupole, &
axisType, &
multipoleAtomZ, &
multipoleAtomX, &
multipoleAtomY, &
thole, &
dampingFactor, &
polarity)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 charge
            type (OpenMM_DoubleArray) molecularDipole
            type (OpenMM_DoubleArray) molecularQuadrupole
            integer*4 axisType
            integer*4 multipoleAtomZ
            integer*4 multipoleAtomX
            integer*4 multipoleAtomY
            real*8 thole
            real*8 dampingFactor
            real*8 polarity
            integer*4 OpenMM_AmoebaMultipoleForce_addMultipole
        end function
        subroutine OpenMM_AmoebaMultipoleForce_getMultipoleParameters(target, index, &
charge, &
molecularDipole, &
molecularQuadrupole, &
axisType, &
multipoleAtomZ, &
multipoleAtomX, &
multipoleAtomY, &
thole, &
dampingFactor, &
polarity)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 index
            real*8 charge
            type (OpenMM_DoubleArray) molecularDipole
            type (OpenMM_DoubleArray) molecularQuadrupole
            integer*4 axisType
            integer*4 multipoleAtomZ
            integer*4 multipoleAtomX
            integer*4 multipoleAtomY
            real*8 thole
            real*8 dampingFactor
            real*8 polarity
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_setMultipoleParameters(target, index, &
charge, &
molecularDipole, &
molecularQuadrupole, &
axisType, &
multipoleAtomZ, &
multipoleAtomX, &
multipoleAtomY, &
thole, &
dampingFactor, &
polarity)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 index
            real*8 charge
            type (OpenMM_DoubleArray) molecularDipole
            type (OpenMM_DoubleArray) molecularQuadrupole
            integer*4 axisType
            integer*4 multipoleAtomZ
            integer*4 multipoleAtomX
            integer*4 multipoleAtomY
            real*8 thole
            real*8 dampingFactor
            real*8 polarity
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_setCovalentMap(target, index, &
typeId, &
covalentAtoms)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 index
            type (OpenMM_AmoebaMultipoleForce_CovalentType) typeId
            type (OpenMM_IntArray) covalentAtoms
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getCovalentMap(target, index, &
typeId, &
covalentAtoms)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 index
            type (OpenMM_AmoebaMultipoleForce_CovalentType) typeId
            type (OpenMM_IntArray) covalentAtoms
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getCovalentMaps(target, index, &
covalentLists)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 index
            std::vector< std::vector< int > > covalentLists
        end subroutine
        function OpenMM_AmoebaMultipoleForce_getMutualInducedMaxIterations(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 OpenMM_AmoebaMultipoleForce_getMutualInducedMaxIterations
        end function
        subroutine OpenMM_AmoebaMultipoleForce_setMutualInducedMaxIterations(target, inputMutualInducedMaxIterations)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 inputMutualInducedMaxIterations
        end subroutine
        function OpenMM_AmoebaMultipoleForce_getMutualInducedTargetEpsilon(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 OpenMM_AmoebaMultipoleForce_getMutualInducedTargetEpsilon
        end function
        subroutine OpenMM_AmoebaMultipoleForce_setMutualInducedTargetEpsilon(target, inputMutualInducedTargetEpsilon)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 inputMutualInducedTargetEpsilon
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_setExtrapolationCoefficients(target, coefficients)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_DoubleArray) coefficients
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getExtrapolationCoefficients(target, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_DoubleArray) result
        end subroutine
        function OpenMM_AmoebaMultipoleForce_getEwaldErrorTolerance(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 OpenMM_AmoebaMultipoleForce_getEwaldErrorTolerance
        end function
        subroutine OpenMM_AmoebaMultipoleForce_setEwaldErrorTolerance(target, tol)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            real*8 tol
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getLabFramePermanentDipoles(target, context, &
dipoles)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            Context context
            type (OpenMM_Vec3Array) dipoles
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getInducedDipoles(target, context, &
dipoles)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            Context context
            type (OpenMM_Vec3Array) dipoles
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getTotalDipoles(target, context, &
dipoles)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            Context context
            type (OpenMM_Vec3Array) dipoles
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getElectrostaticPotential(target, inputGrid, &
context, &
outputElectrostaticPotential)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            type (OpenMM_Vec3Array) inputGrid
            Context context
            type (OpenMM_DoubleArray) outputElectrostaticPotential
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_getSystemMultipoleMoments(target, context, &
outputMultipoleMoments)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            Context context
            type (OpenMM_DoubleArray) outputMultipoleMoments
        end subroutine
        subroutine OpenMM_AmoebaMultipoleForce_updateParametersInContext(target, context)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            Context context
        end subroutine
        function OpenMM_AmoebaMultipoleForce_usesPeriodicBoundaryConditions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaMultipoleForce) target
            integer*4 OpenMM_AmoebaMultipoleForce_usesPeriodicBoundaryConditions
        end function

        ! OpenMM::AmoebaTorsionTorsionForce
        subroutine OpenMM_AmoebaTorsionTorsionForce_create(result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) result
        end subroutine
        subroutine OpenMM_AmoebaTorsionTorsionForce_destroy(destroy)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) destroy
        end subroutine
        function OpenMM_AmoebaTorsionTorsionForce_getNumTorsionTorsions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 OpenMM_AmoebaTorsionTorsionForce_getNumTorsionTorsions
        end function
        function OpenMM_AmoebaTorsionTorsionForce_getNumTorsionTorsionGrids(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 OpenMM_AmoebaTorsionTorsionForce_getNumTorsionTorsionGrids
        end function
        function OpenMM_AmoebaTorsionTorsionForce_addTorsionTorsion(target, particle1, &
particle2, &
particle3, &
particle4, &
particle5, &
chiralCheckAtomIndex, &
gridIndex)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 particle1
            integer*4 particle2
            integer*4 particle3
            integer*4 particle4
            integer*4 particle5
            integer*4 chiralCheckAtomIndex
            integer*4 gridIndex
            integer*4 OpenMM_AmoebaTorsionTorsionForce_addTorsionTorsion
        end function
        subroutine OpenMM_AmoebaTorsionTorsionForce_getTorsionTorsionParameters(target, index, &
particle1, &
particle2, &
particle3, &
particle4, &
particle5, &
chiralCheckAtomIndex, &
gridIndex)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 index
            integer*4 particle1
            integer*4 particle2
            integer*4 particle3
            integer*4 particle4
            integer*4 particle5
            integer*4 chiralCheckAtomIndex
            integer*4 gridIndex
        end subroutine
        subroutine OpenMM_AmoebaTorsionTorsionForce_setTorsionTorsionParameters(target, index, &
particle1, &
particle2, &
particle3, &
particle4, &
particle5, &
chiralCheckAtomIndex, &
gridIndex)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 index
            integer*4 particle1
            integer*4 particle2
            integer*4 particle3
            integer*4 particle4
            integer*4 particle5
            integer*4 chiralCheckAtomIndex
            integer*4 gridIndex
        end subroutine
        subroutine OpenMM_AmoebaTorsionTorsionForce_getTorsionTorsionGrid(target, index, result)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 index
            std::vector< std::vector< std::vector< double > > > result
        end subroutine
        subroutine OpenMM_AmoebaTorsionTorsionForce_setTorsionTorsionGrid(target, index, &
grid)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 index
            std::vector< std::vector< std::vector< double > > > grid
        end subroutine
        subroutine OpenMM_AmoebaTorsionTorsionForce_setUsesPeriodicBoundaryConditions(target, periodic)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 periodic
        end subroutine
        function OpenMM_AmoebaTorsionTorsionForce_usesPeriodicBoundaryConditions(target)
            use OpenMM_Types; implicit none
            type (OpenMM_AmoebaTorsionTorsionForce) target
            integer*4 OpenMM_AmoebaTorsionTorsionForce_usesPeriodicBoundaryConditions
        end function


    end interface
END MODULE OpenMM
