from ase import *
from hotbit import *
from hotbit.parametrization.fitting import RepulsiveFitting

import numpy as np

from ase.build import bulk
from ase.calculators.espresso import Espresso
from ase.collections import dcdft
from ase.io import read, write, Trajectory

# force the hotbit to use CC-table where the repulsion is missing
tables = {'CC':'C_C_no_repulsion.par', 'others':'default'}

# for parametrization calculations it might be good idea to increase
# the convergence criteria
mixer_values = {'name':'anderson', 'convergence':1e-9}

# the fitting object (element1, element2, r_cut)
rep=RepulsiveFitting('C','C', 2.0)

# now use various methods if RepulsiveFitting to collect information about V_rep'(R)
# For each fitting method one must provide a suitable tight-binding calculator,
# i.e., one that has correct charge and other parameters.

# for dimer append_energy_curve is suitable
calc = Hotbit(mixer=mixer_values, tables=tables, txt='-')
rep.append_energy_curve(1, calc, 'dimer.traj', label='dimer',color='yellow')

# append energy curve can be used if there are many bond lengths of the
# same lengths, and the rest can be ignored (e.g. chain)
#rep.append_energy_curve(1, calc, 'chain.traj', label='chain')

# if there are different bond lengths, then append_homogeneous_structure
# can be used. If the reference (DFT) calculations was charged,
# then another calculator must be created with correct charge.
#calc = Hotbit(mixer=mixer_values, tables=tables, txt='-', charge=-1)
#rep.append_homogeneous_cluster(0.5, calc, 'homog.traj',label='homogeneous', color='green')

# The append_energy_curve method also works with periodic calculations.
# ASE-trajectory contains the pbc-info, but for now one must disable
# the SCC with bulk calculations.
#calc_bulk = Hotbit(mixer=mixer_values, tables=tables, txt='-', SCC=False)
#rep.append_energy_curve(1, calc_bulk, 'bulk.traj', label='bulk')
tab={'CC':'C_C_no_repulsion.par'}
elm={'C':'C.elm'}
mixer={'name':'Anderson','mixing_constant':0.1,'convergence':1E-9}
calc1 = Hotbit(txt='-',elements=elm,mixer=mixer,tables=tab,SCC=False,kpts=(6,6,6))
rep.append_scalable_system(weight=1.0,calc=calc1,atoms='bulk.traj',comment='bulk C')

# make the fit
rep.fit()

# write final parametrization file
rep.write_par('C_C_no_repulsion.par',filename='C_C_repulsion.par')
#rep.write_par("C_C.par")

# check if the fitting looks reasonable (produces a pdf)
rep.plot()