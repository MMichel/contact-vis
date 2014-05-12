ContactVis
==========

Python package for simple protein residue-residue contact map plotting.
[Available on PyPi](https://pypi.python.org/pypi/ContactVis).


Usage
=====

``plot_contact_map.py [-h] [-o OUTFILE] [-f FACTOR] [--c2 C2]
                    [--psipred_horiz PSIPRED_HORIZ] [--pdb PDB]
                    [--heavy] [--chain CHAIN]
                    fasta_file contact_file``


To reproduce the different examples in the ``test`` folder run the following commands (when you are in the ``test`` folder):

Simple map of the given contact file with coloring according to contact probability:
``python ../plot_contact_map.py sequence.fasta predicted.contacts -o cm_simple``

Comparison to contacts from the native PDB structure (pairwise CB-atom distance with 8Å cutoff):
``python ../plot_contact_map.py sequence.fasta predicted.contacts -o cm_pdb.pdf --pdb native_structure.pdb``

Compare two different predicted contact maps to each other and to a native PDB structure and include secondary structure information along the diagonal (red: helix, blue: sheet):
``python ../plot_contact_map.py sequence.fasta predicted.contacts -o cm_compare_pdb.pdf --pdb native_structure.pdb --c2 predicted.contacts2 --psipred_horiz psipred.horiz``
