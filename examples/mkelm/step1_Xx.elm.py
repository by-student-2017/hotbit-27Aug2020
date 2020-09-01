from hotbit.parametrization.atom import KSAllElectron
from hotbit.parametrization.util import IP_EA
from time import asctime

""" 
Create the element file for Xx
- contains the single-particle energy levels
- Hubbard parameter U
- FWHM-value (calculated from U)
- possibly comments about the parametrization
"""

# element to parametrize
element= 'Xx'
# lowest orbital that can accept electrons
add_orb= 'addor'
# sometimes adding full electron causes the convergence problems,
# so add a fraction of an electron and interpolate
add=  adde
# highest occupied orbital
remove_orb = 'remor'
# how many electrons to remove
remove =  remne

# solve the atom with charges add, 0 and remove,
# and calculate ionization potential and electron affinity
IP, EA, atom = IP_EA(element, remove_orb, add_orb, remove, add)

# the Hubbard parameter is then
U = IP-EA

# save the results into an element file
f = open("Xx.elm",'w')
print >> f, "symbol=%s" % element
print >> f, "comment="
print >> f, asctime()
print >> f, "Energy levels from DFT"
# an empty line after the comments
print >> f, ""
for va in atom.get_valence_energies():
    print >> f, "epsilon_%s= %0.6f" % va
print >> f, "U= %0.6f" % U
print >> f, "FWHM= %0.6f" % (1.32856/U)
f.close()

# save the radial parts of the wave functions
atom.write_unl("Xx.elm")
