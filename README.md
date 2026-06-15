<div align="center";>
  <h1>Ion Channel Simulation and Analysis Guide</h1>
  
  Welcome! This is my repository for a streamlined and reproducable method of ion channel simulation and analysis through atomistic and coarse grained means.
</div> 

## :notebook_with_decorative_cover: Table of Contents

- [Overview](#overview)
- [Software](#software)
  * [Charmm-Gui](#charmm-gui)
  * [ChimeraX](#chimerax)
  * [GROMACS](#gromacs)
  * [Insane](#insane)
  * [Martini3](#martini3)
  * [MDAnalysis](#mdanalysis)
  * [PyMol](#pymol)
  * [Vermouth-Martinize2](#vermouth-martinize2)
- [Methodology](#methodology)
  * [Atomistic](#atomistic)
  * [Coarse Grain](#coarse-grain)
- [Analysis](#analysis)
- [Resources](#resources)
- [References](#references)

## Overview
The focus of this repository is to provide a set of tips, tools, and scripts for mass simulation of ion channels in an easily reproducible method. Included are overviews of relevant softwares for ion channel simulation, discussion of the utility and limitations of coarse graining, an overview of the methodology of simulation, discussion on relevant characteristics of channels for analysis, and resources/references to learn more. These methods and scripts have been used successfully for the simulation and analysis of the ion channel TRPV1, with a link to the paper found here. Relevant scripts and files can be found in the listed folders above.

## Software
### Charmm-Gui

Charmm-Gui is a web-based platform designed for the interactive construction of complex biological systems for simulation. It has compatibility with a variety of simulation packages such as NAMD, CHARMM, OpenMM, LAMMPS, AMBER, GENESIS, Tinker, Desmond, and of most relevance, GROMACS. Due to the complex nature of atomistic ion channel systems, developing the simulation environments by oneself can be rather laborious. Thus Charmm-Gui serves the role of readily developing these complex biological systems through a stream-lined interface. More information can be found <a href="https://www.charmm-gui.org/">here</a>.

### ChimeraX

ChimeraX is computational biology visualization program used in rendering proteins for visual analysis. While PyMol is typically recommended over ChimeraX for visualization, the usage for ChimeraX lies with its in built modeller functionality. Ion channels are typically constructed using the method of cryogenic electron microposcy, which while a powerful tool often can lack the resolution for the accurate rendering of fringe side chain elements of said channels. Thus, the usage for ChimeraX where peripheral elements can be accurately reconstructed for usage in simulation. More information can be found <a href="https://www.cgl.ucsf.edu/chimerax/">here</a>.

### GROMACS

GROMACS is a high performance suite of tools for molecular dynamics simulation and output analysis. GROMACS is highly versatile, functional, and compatible with virtually every step of the process for ion channel simulation construction and operation. The packages Insane, Martini3, and Vermouth in fact all rely on the platform of GROMACS for many operations. Simulation scripts for GROMAC's simulations can be found here, while more information on other uses can be found <a href="https://www.gromacs.org/">here</a>.

### Insane

Insane (INSert membrANE) is a tool for the insertion of proteins, particularly ion channels, into complex lipid membranes and the solvation of these systems. Lipids are taken from a list of existing lipid models from Martini3 as well as additional loaded lipid compositions. Proteins are inserted into the membrane with exact compositions of lipid membranes subject to user discretion. Insane is incredibly helpful for the creation of complex coarse-grained systems of a protein, solvent, and lipid membrane. The Github for insane can be found <a href="https://github.com/Tsjerk/Insane">here</a>.

### Martini3

Martini3 is a generic coarse grain force field designed for a variety of biomolecular dynamic simulations. The force field utilizes a 4 to 1 mapping scheme for coarse graining, where on average every four atoms is mapped to one represenative bead. These beads are given a number of subtypes to ensure proper matching with underlying atomistic makeups. Interactions between beads are based either on reproductions of experimental partitioning free energies between polar and apolar syetms from a variety of chemical compositions for non-bonded interactions or on atomistic simulations for bonded interactions. These interactions, to reduce complexity, are restricted to five main types: polar, nonpolar, a-polar, charged, and halogen. Martini3 is the backbone of which all coarse grain ion channel simulations are built. Information on the force field itself can be found <a href="https://www.nature.com/articles/s41592-021-01098-3">here</a> while information on the usage of the forcefield can be found<a href="https://cgmartini.nl/">here</a>. 

### MDAnalysis

MDAanlysis is a suite of open source tools for the analysis of molecular dynamic systems. It enables the seamless reading and writing of simulation data, allowing users to efficiently analyze molecular structures and dynamics, including particle-based trajectories and individual coordinate frames. It also includes powerful atom selection commands for extracting subsets of structures and supports trajectory transformations. MDAnalysis is built and operated in the Python programming language, and allows for the relatively easy analysis of all manner of systems. This software serves as the undercurrent to all analysis done of ion channel simulations. Further information can be found <a href="https://www.mdanalysis.org/">here</a>.

### PyMol

PyMol is an open source 3D visualization software capable of customizable protein and trajectory display. It is useful for both the reassurance of simulation setup correctness as well as for the visualization of complete trajectories for analysis and publishing. A link to the software can be found <a href="https://pymol.org/">here</a>.

### Vermouth-Martinize2

Martinize2 is a software package aimed at producing coarse grained structures for Martini3 from atomistic structures in GROMACS. Vermouth (VERsatile, MOdular, and Universal Tranformation Helper) is the python library that powers Martinize2 conversions. Martinize2 is crucial for the fast and effective conversion of high complexity proteins, such as ion channels, into coarse grain components. Due to the ease of use, the software is invaluable for rapid conversion of complex atomistic proteins into easily readable coarse grain variants. The Github for the package can be found <a href="https://github.com/marrink-lab/vermouth-martinize">here</a>.

## Coarse Graining

Coarse grain modeling, or coarse graining, are the methods that aim at simulating the behavior of complex systems using a simplified representation. This simplified representation permits the allows increased simulation times at the expense of molecular detail. Functionally, this involves combining groups of atoms into representative beads and then simulating the new beaded system with the hopes of observing relevant behaviors at significantly reduced computatational cost. Given the size and complexity of systems of ion channels, coarse graining proves to be an invaluable tool for the study of ion channel conformational dynamics. 

## Methodology

Below is an overview of the process of construction of ion channel and simulation environments using atomistic and coarse grain methodologies. All tools used are referenced above. Additionally, relevant tutorials and papers are provided below. These methods were used in the simulation of the ion channel TRPV1. 

### Atomistic

1. Protein selection and repair:
2. Membrane insertion:
3. Solvation:
4. Simulation:

### Coarse Grain

1. Protein selection and repair:
2. Coarse graining:
3. Membrane insertion:
4. Solvation:
5. Simulation: 

## Analysis

## Resources



## References

- Charmm-Gui:
  + [S. Jo, T. Kim, V.G. Iyer, and W. Im (2008) CHARMM-GUI: A Web-based Graphical User Interface for CHARMM.](http://dx.doi.org/10.1002/jcc.20945)
  + [B.R. Brooks, C.L. Brooks III, A.D. MacKerell, Jr., L. Nilsson, R.J. Petrella, B. Roux, Y. Won, G. Archontis, C. Bartels, S. Boresch, A. Caflisch, L. Caves, Q. Cui, A.R. Dinner, M. Feig, S. Fischer, J. Gao, M. Hodoscek, W. Im, K. Kuczera, T. Lazaridis, J. Ma, V. Ovchinnikov, E. Paci, R.W. Pastor, C.B. Post, J.Z. Pu, M. Schaefer, B. Tidor, R. M. Venable, H. L. Woodcock, X. Wu, W. Yang, D.M. York, and M. Karplus (2009) CHARMM: The Biomolecular Simulation Program.](http://dx.doi.org/10.1002/jcc.21287)
  + [J. Lee, X. Cheng, J.M. Swails, M.S. Yeom, P.K. Eastman, J.A. Lemkul, S. Wei, J. Buckner, J.C. Jeong, Y. Qi, S. Jo, V.S. Pande, D.A. Case, C.L. Brooks III, A.D. MacKerell Jr, J.B. Klauda, and W. Im (2016) CHARMM-GUI Input Generator for NAMD, GROMACS, AMBER, OpenMM, and CHARMM/OpenMM Simulations using the CHARMM36 Additive Force Field.](http://dx.doi.org/10.1021/acs.jctc.5b00935)
  + [E.L. Wu, X. Cheng, S. Jo, H. Rui, K.C. Song, E.M. Dávila-Contreras, Y. Qi, J. Lee, V. Monje-Galvan, R.M. Venable, J.B. Klauda, and W. Im (2014) CHARMM-GUI Membrane Builder Toward Realistic Biological Membrane Simulations.](http://dx.doi.org/10.1002/jcc.23702)
  + [S. Jo, J.B. Lim, J.B. Klauda, and W. Im (2009) CHARMM-GUI Membrane Builder for Mixed Bilayers and Its Application to Yeast Membranes.](http://dx.doi.org/10.1016/j.bpj.2009.04.013)
  + [S. Jo, T. Kim, and W. Im (2007) Automated Builder and Database of Protein/Membrane Complexes for Molecular Dynamics Simulations.](http://dx.doi.org/10.1371/journal.pone.0000880)
  + [J. Lee, D.S. Patel, J. Ståhle, S-J. Park, N.R. Kern, S. Kim, J. Lee, X. Cheng, M.A. Valvano, O. Holst, Y. Knirel, Y. Qi, S. Jo, J.B. Klauda, G. Widmalm, and W. Im (2019) CHARMM-GUI Membrane Builder for Complex Biological Membrane Simulations with Glycolipids and Lipoglycans.](http://dx.doi.org/10.1021/acs.jctc.8b01066)
  + [S. Park, Y.K. Choi, S. Kim, J. Lee, and W. Im (2021) CHARMM-GUI Membrane Builder for Lipid Nanoparticles with Ionizable Cationic Lipids and PEGylated Lipids.](http://dx.doi.org/10.1021/acs.jcim.1c00770)
  + [S. Gee, K.J. Glover, N.J. Wittenberg, and W. Im (2024) CHARMM-GUI Membrane Builder for Lipid Droplet Modeling and Simulation.](https://doi.org/10.1002/cplu.202400013)
  + [T.P. Brown, D.E. Santa, B.A. Berger, L. Kong, N.J. Wittenberg, and W. Im (2024) CHARMM GUI Membrane Builder for oxidized phospholipid membrane modeling and simulation.](https://doi.org/10.1016/j.sbi.2024.102813)
  + [S. Feng, S. Park, Y.K. Choi, and W. Im (2024) CHARMM-GUI Membrane Builder: Past, Current, and Future Developments and Applications.](https://doi.org/10.1021/acs.jctc.2c01246)
- ChimeraX:
  + [UCSF ChimeraX: Tools for structure building and analysis. Meng EC, Goddard TD, Pettersen EF, Couch GS, Pearson ZJ, Morris JH, Ferrin TE. Protein Sci. 2023 Nov;32(11):e4792.](https://onlinelibrary.wiley.com/doi/10.1002/pro.4792)
  + [UCSF ChimeraX: Structure visualization for researchers, educators, and developers. Pettersen EF, Goddard TD, Huang CC, Meng EC, Couch GS, Croll TI, Morris JH, Ferrin TE. Protein Sci. 2021 Jan;30(1):70-82.](https://www.ncbi.nlm.nih.gov/pubmed/32881101)
  + [UCSF ChimeraX: Meeting modern challenges in visualization and analysis. Goddard TD, Huang CC, Meng EC, Pettersen EF, Couch GS, Morris JH, Ferrin TE. Protein Sci. 2018 Jan;27(1):14-25.](https://www.ncbi.nlm.nih.gov/pubmed/28710774)
- GROMACS:
  + [Abraham, M., Alekseenko, A., Andrews, B., Basov, V., Bauer, P., Bird, H., Briand, E., Brown, A., Doijade, M., Fiorin, G., Fleischmann, S., Gorelov, S., Gouaillardet, G., Gray, A., Irrgang, M. E., Jalalypour, F., Johansson, P., Kutzner, C., Łazarski, G., … Lindahl, E. (2025). GROMACS 2025.3 Manual (2025.3). Zenodo](https://doi.org/10.5281/zenodo.16992569)
- Insane:
  + [Tsjerk A. Wassenaar, Helgi I. Ingólfsson, Rainer A. Böckmann, D. Peter Tieleman, and Siewert J. Marrink Journal of Chemical Theory and Computation (2015) 11 (5), 2144-2155](https://pubs.acs.org/doi/10.1021/acs.jctc.5b00209)
- Martini3:
  + [Souza, P.C.T., Alessandri, R., Barnoud, J. et al. Martini 3: a general purpose force field for coarse-grained molecular dynamics. Nat Methods 18, 382–388 (2021).](https://doi.org/10.1038/s41592-021-01098-3)
- PyMol:
  + [The PyMOL Molecular Graphics System, Version 3.0 Schrödinger, LLC.](https://pymol.org/#page-top)
- Simulation Parameters:
  + 
- Vermouth-Martini2:
  + [P C KroonF GrunewaldJ BarnoudM van TilburgP C T SouzaT A WassenaarS J Marrink (2023) Martinize2 and Vermouth: Unified Framework for Topology GenerationeLife12:RP90627](https://doi.org/10.7554/eLife.90627.1)
