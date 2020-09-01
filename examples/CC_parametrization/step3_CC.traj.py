import numpy as np
from ase.build import bulk
from ase.calculators.espresso import Espresso
from ase.collections import dcdft
from ase.io import read, write, Trajectory

# making dimer.traj
traj = Trajectory('dimer.traj','w') # create Trajectory object
dx = 0.1 #scaling factor
list1=[0,0,0] # position of first atom
list2=[0,0,0.5] # will store new position of second atom
vec_2 = np.array(list2) - np.array(list1) # vector pointing from 1 to 2
norm_2 = np.linalg.norm(vec_2, ord=2) # get norm
vec_2 = [x/norm_2 for x in vec_2] # get unit vector
for i in range(4):
        ss = [dx*x for x in vec_2] #scale vector
        list2 = np.array(list2) + np.array(ss) # move second atom
        dimer = Atoms('CC',positions=[list1, list2]) # create ASE atom object
        dimer.calc = Espresso(pseudopotentials=pseudopotentials)
        dft_energy = dimer.get_potential_energy()
        traj.write(dimer,energy = (dft_energy)) # write dft energy to trajectory file
        dx += 0.1

# making bulk.traj
#https://wiki.fysik.dtu.dk/ase/tutorials/deltacodesdft/deltacodesdft.html?highlight=dft%20calculatin#ase.utils.deltacodesdft.delta
pseudopotentials = {'C': 'C.pbe-n-kjpaw_psl.1.0.0.UPF'}
for symbol in ['C']:
    traj = Trajectory('bulk.traj'.format(symbol), 'w')
    for s in range(94, 108, 2):
        bulk = dcdft[symbol]
        bulk.set_cell(bulk.cell * (s / 100.0)**(1.0 / 3.0), scale_atoms=True)
        bulk.calc = Espresso(pseudopotentials=pseudopotentials, kpts=(6, 6, 6))
        dft_energy = bulk.get_potential_energy()
        print s,dft_energy
        traj.write(bulk, energy = (dft_energy))
