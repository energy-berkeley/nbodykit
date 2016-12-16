from mpi4py_test import MPITest
from nbodykit.lab import *
from nbodykit.algorithms.fof import FOF, HaloFinder
from nbodykit import setup_logging

# debug logging
setup_logging("debug")

@MPITest([1, 4])
def test_fof(comm):
    cosmo = cosmology.Planck15

    CurrentMPIComm.set(comm)

    # zeldovich particles
    source = Source.ZeldovichParticles(cosmo, nbar=3e-3, redshift=0.55, BoxSize=512., Nmesh=128, rsd=[0, 0, 1], seed=42)

    # compute P(k,mu) and multipoles
    fof = FOF(source, linking_length=0.2, nmin=20)

    fof['HaloLabel'].save("FOF-label-%d" % comm.size)

    halos = HaloFinder(source, fof['HaloLabel'])
    halos['Position'].save("FOF-label-%d" % comm.size)
    halos['Velocity'].save("FOF-label-%d" % comm.size)
    halos['Length'].save("FOF-label-%d" % comm.size)
