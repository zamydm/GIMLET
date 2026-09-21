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
  * [CHARMM-GUI](#charmm-gui)
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

### CHARMM-GUI
CHARMM-GUI is a software that has been developed to provide a web-based graphical user interface to generate various input files and molecular systems to facilitate and standardize the usage of common and advanced simulation techniques. Invaluable due to the range of capabilities of the software and most relevant to ion channel simulation due to its capability of building complex, atomistic membranes, the software is an excellent addition to an ion channel analysis pipeline. More information on the software can be found [here](https://charmm-gui.org/).

### Charmm36
The Charmm36 forcefield . More information on the forcefield and how to download it can be found [here](https://mackerell.umaryland.edu/charmm_ff.shtml).

### ChimeraX


### GROMACS
GROMACS is a versatile package to perform molecular dynamics simulations. Used in ion channel study for system assembly, solvation, simulation, and analysis, GROMACS serves as the cornerstone of ion channel work. More information about GROMACS can be found [here](https://www.gromacs.org/).

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

### CHARMM-GUI
- S. Jo, T. Kim, and W. Im (2007) Automated Builder and Database of Protein/Membrane Complexes for Molecular Dynamics Simulations. PLoS ONE 2(9):e880 
- S. Jo, T. Kim, V.G. Iyer, and W. Im (2008) CHARMM-GUI: A Web-based Graphical User Interface for CHARMM. J. Comput. Chem. 29:1859-1865
- B.R. Brooks, C.L. Brooks III, A.D. MacKerell, Jr., L. Nilsson, R.J. Petrella, B. Roux, Y. Won, G. Archontis, C. Bartels, S. Boresch, A. Caflisch, L. Caves, Q. Cui, A.R. Dinner, M. Feig, S. Fischer, J. Gao, M. Hodoscek, W. Im, K. Kuczera, T. Lazaridis, J. Ma, V. Ovchinnikov, E. Paci, R.W. Pastor, C.B. Post, J.Z. Pu, M. Schaefer, B. Tidor, R. M. Venable, H. L. Woodcock, X. Wu, W. Yang, D.M. York, and M. Karplus (2009) CHARMM: The Biomolecular Simulation Program. J. Comput. Chem. 30:1545-1614
- S. Jo, J.B. Lim, J.B. Klauda, and W. Im (2009) CHARMM-GUI Membrane Builder for Mixed Bilayers and Its Application to Yeast Membranes. Biophys. J. 97:50-58 
- E.L. Wu, X. Cheng, S. Jo, H. Rui, K.C. Song, E.M. Dávila-Contreras, Y. Qi, J. Lee, V. Monje-Galvan, R.M. Venable, J.B. Klauda, and W. Im (2014) CHARMM-GUI Membrane Builder Toward Realistic Biological Membrane Simulations. J. Comput. Chem. 35:1997-2004 
- J. Lee, X. Cheng, J.M. Swails, M.S. Yeom, P.K. Eastman, J.A. Lemkul, S. Wei, J. Buckner, J.C. Jeong, Y. Qi, S. Jo, V.S. Pande, D.A. Case, C.L. Brooks III, A.D. MacKerell Jr, J.B. Klauda, and W. Im (2016) CHARMM-GUI Input Generator for NAMD, GROMACS, AMBER, OpenMM, and CHARMM/OpenMM Simulations using the CHARMM36 Additive Force Field. J. Chem. Theory Comput. 12:405-413
- J. Lee, D.S. Patel, J. Ståhle, S-J. Park, N.R. Kern, S. Kim, J. Lee, X. Cheng, M.A. Valvano, O. Holst, Y. Knirel, Y. Qi, S. Jo, J.B. Klauda, G. Widmalm, and W. Im (2019) CHARMM-GUI Membrane Builder for Complex Biological Membrane Simulations with Glycolipids and Lipoglycans. J. Chem. Theory Comput. 15:775-786
- S. Park, Y.K. Choi, S. Kim, J. Lee, and W. Im (2021) CHARMM-GUI Membrane Builder for Lipid Nanoparticles with Ionizable Cationic Lipids and PEGylated Lipids. J. Chem. Inf. Model. 61:5192-5202
- S. Gee, K.J. Glover, N.J. Wittenberg, and W. Im (2024) CHARMM-GUI Membrane Builder for Lipid Droplet Modeling and Simulation. ChemPlusChem. 89:e202400013
- T.P. Brown, D.E. Santa, B.A. Berger, L. Kong, N.J. Wittenberg, and W. Im (2024) CHARMM GUI Membrane Builder for oxidized phospholipid membrane modeling and simulation. Curr. Opin. Struct. Biol. 86:102813
- S. Feng, S. Park, Y.K. Choi, and W. Im (2024) CHARMM-GUI Membrane Builder: Past, Current, and Future Developments and Applications. J. Chem. Theory Comput. 19:2161-2185
- S.J. Park and W. Im (2026) CHARMM-GUI Quick Bilayer: Simple and Intuitive One-Stop Membrane Bilayer Builder. J. Mol. Biol. in press 

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
