<!-- Title, overview, and badges. -->
<div align="center">

  <h1>GIMLET: GROMACS Ion-channel Multiscale Library: Examples & Tools</h1>

  <p>
    A repository for a streamlined and reproducible method of ion channel simulation and analysis through atomistic and coarse grained means in GROMACS.
  </p>

</div>

<!-- Table of Contents -->
## :notebook_with_decorative_cover: Table of Contents
- [Overview](#overview)
- [Software Guide](#software-guide)
  * [Charmm-Gui](#charmm-gui)
  * [Charmm36](#charmm36)
  * [ChimeraX](#chimerax)
  * [GROMACS](#gromacs)
  * [Hole2](#hole2)
  * [Insane](#insane)
  * [Martini3](#insane)
  * [MDAnalysis](#mdanalysis)
  * [Modeller](#modeller)
  * [PyMol](#pymol)
  * [Vermouth-Martinize2](#vermouth-martinize2)
- [Simulation Guide](#simulation-guide)
  * [Protein Repair](#protein-repair)
  * [Atomistic](#atomistic)
  * [Coarse Grain](#coarse-grain)
  * [Analysis](#analysis)
- [Contact](#contact)
- [References](#references)

## Overview

## Software Guide

### Charmm-Gui

### Charmm36

### ChimeraX

### GROMACS
GROMACS is a versatile package to perform molecular dynamics simulations. Used in ion channel 

### Hole2
Hole2 is a program for the analysis of the pore dimensions of an ion channel. Useful for studying the conformational dynamics of a protein either as a structure or over a trajectory, though it is limited in application through MDAHole2 to atomistic simulations currently. More information about Hole2 can be found at its Github [here](https://github.com/osmart/hole2) or at its website [here](https://www.holeprogram.org/). 

### Insane
Insane (INSert membrANE) is a versatile tool to build coarse-grained simulation systems containing solutes, lipid bilayers, and/or solvents. For the simulation of ion channels in coarse grain environments, which depend heavily on their membranes and surrounding solvents/ions, this tool excels in the complex process of protein insertion into a membrane, simple. More information about Insane can be found at their Github [here](https://github.com/Tsjerk/Insane).

### Martini3
Martini3 is a generic coarse-grained force field suited for molecular dynamics simulations of a broad variety of biomolecular systems. The force field has been parameterized in a systematic way, combining top-down and bottom-up strategies: non-bonded interactions are mostly based on the reproduction of experimental partitioning free energies between polar and apolar phases of a large number of chemical compounds, whereas bonded interactions are typically derived from reference all-atom simulations. The model is based on a four-to-one mapping scheme, i.e. on average four heavy atoms and associated hydrogens are represented by a single interaction center. This reduction of atomistic systems to coarse-grain allows for the extension of simulation time beyond what would be possible for full atomistic methodologies at a fraction of the computational cost, making them a useful tool for extended study of protein dynamics. More information on Martini3 can be found [here](https://cgmartini.nl/).

### MDAnalysis
MDAnalysis is a suite of python tools for the analysis of molecular dynamics trajectories across multiple formats. Particularly helpful for contact analysis and its MDAHole integration, this library is critical for the effective analysis of ion channel simulations. More information on MDAnalysis can be found [here](https://www.mdanalysis.org/).

### Modeller
Modeller is a program for the comparative protein structure modeling by satisfaction of spatial restraints. Capable of modeling absent loops of a protein from the protein sequence, it is an important software for filling in missing loops in ion channels for simulation. More information on Modeller can be found [here](https://salilab.org/modeller/).

### PyMOL
PyMOL is molecular visualization software capable of rendering both structures and trajectories from a a variety of forcefields. It is useful for the visual checking of simulation results and for the visualization of results for a paper. More information about PyMOL can be found [here](https://pymol.org/).

### Vermouth-Martinize2
Vermouth (VERsatile, MOdular, and Universal Tranformation Helper) is the python library that powers the software Martinize2, a software that aims to produce coarse-grained structures in the Martini3 forcefield and topology files from an atomistic input. This software is designed to work in tandem with the GROMACS engine. More information about Vermouth can be found [here](https://vermouth-martinize.readthedocs.io/en/latest/index.html) and the Github for Martinize2 can be found [here](https://github.com/marrink-lab/vermouth-martinize).

## Simulation Guide 

### Protein Repair

### Atomistic

### Coarse Grain

### Analysis

## Contact

<div align="center">

  Zachary Sottoriva - zamydm@iastate.edu
  
  Please cite the following: INSERT MY PAPER CITATION HERE

</div>

## References

### GROMACS

### Hole2
- Smart, O. S.; Neduvelil, J. G.; Wang, X.; Wallace, B. A.; Sansom, M. S. P. HOLE: A Program for the Analysis of the Pore Dimensions of Ion Channel Structural Models. Journal of Molecular Graphics 1996, 14 (6), 354–360. https://doi.org/10.1016/s0263-7855(97)00009-x

### Insane
- Ozturk, T. N., König, M., Carpenter, T. S., Pedersen, K. B., Wassenaar, T. A., Ingólfsson, H. I., & Marrink, S. J. (2024). Building complex membranes with Martini 3. In Methods in Enzymology (Vol. 701, pp. 237-285). Academic Press. https://doi.org/10.1016/bs.mie.2024.03.010

### Martini3
- Souza, P.C.T., Alessandri, R., Barnoud, J. et al. Martini 3: a general purpose force field for coarse-grained molecular dynamics. Nat Methods 18, 382–388 (2021). https://doi.org/10.1038/s41592-021-01098-3

### MDAnalysis
- R. J. Gowers, M. Linke, J. Barnoud, T. J. E. Reddy, M. N. Melo, S. L. Seyler, D. L. Dotson, J. Domanski, S. Buchoux, I. M. Kenney, and O. Beckstein. MDAnalysis: A Python package for the rapid analysis of molecular dynamics simulations. In S. Benthall and S. Rostrup, editors, Proceedings of the 15th Python in Science Conference, pages 98-105, Austin, TX, 2016. SciPy, doi:10.25080/majora-629e541a-00e.
- N. Michaud-Agrawal, E. J. Denning, T. B. Woolf, and O. Beckstein. MDAnalysis: A Toolkit for the Analysis of Molecular Dynamics Simulations. J. Comput. Chem. 32 (2011), 2319-2327, doi:10.1002/jcc.21787. PMCID:PMC3144279

### Modeller
- A. Sali & T.L. Blundell. Comparative protein modelling by satisfaction of spatial restraints. J. Mol. Biol. 234, 779-815, 1993.
- M.A. Marti-Renom, A. Stuart, A. Fiser, R. Sánchez, F. Melo, A. Sali. Comparative protein structure modeling of genes and genomes. Annu. Rev. Biophys. Biomol. Struct. 29, 291-325, 2000.
- A. Fiser, R.K. Do, & A. Sali. Modeling of loops in protein structures, Protein Science 9. 1753-1773, 2000.
- B. Webb, A. Sali. Comparative Protein Structure Modeling Using Modeller. Current Protocols in Bioinformatics 54, John Wiley & Sons, Inc., 5.6.1-5.6.37, 2016.

### Vermouth-Martinize2
- Peter C Kroon, Fabian Grünewald, Jonathan Barnoud, Marco van Tilburg, Chris Brasnett, Paulo CT Souza, Tsjerk A Wassenaar, Siewert J Marrink (2025) Martinize2 and Vermouth provide a unified framework for molecular topology generation eLife 12:RP90627
