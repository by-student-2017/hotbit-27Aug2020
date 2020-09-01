from hotbit.parametrization.atom import KSAllElectron
from box.data import data
Bohr = 0.52917725750691647

# The element parameters, r0 must be in Bohrs
elem1 = 'C'
r0_cov_1 = data[elem1]['R_cov']/Bohr
r0_factor_1 = 1.85
r0_1 = r0_cov_1 * r0_factor_1

elem2 = 'C'
r0_cov_2 = data[elem2]['R_cov']/Bohr
r0_factor_2 = 1.85
r0_2 = r0_cov_2 * r0_factor_2

# Calculate wave functions for the confined isolated atoms
atom1 = KSAllElectron(elem1, confinement={'mode':'quadratic', 'r0':r0_1})
atom1.run()

atom2 = KSAllElectron(elem2, confinement={'mode':'quadratic', 'r0':r0_2})
atom2.run()

# Produce png-files from the radial parts of the wave functions
atom1.plot_Rnl()
atom2.plot_Rnl()


# Add this to the previous script
from hotbit.parametrization.slako import SlaterKosterTable

# Slater-Koster table limits and the number of points
R1 = 1
R2 = 10
N = 50

# The output file
file = '%s_%s_no_repulsion.par' % (elem1, elem2)

# Create the Slater-Koster table
sk = SlaterKosterTable(atom1, atom2)
sk.run(R1, R2, N)
sk.write(file)
sk.plot()