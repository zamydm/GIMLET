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
  * [CHARMM36](#charmm36)
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

### CHARMM36
The Charmm36 forcefield is a modern atomistic forcefield useful for the simulation of biomolecular systems. Due to its integration into CHARMM-GUI and its support in GROMACS, the CHARMM36 forcefield is an excellent forcefield for ion channel simulation. More information on the forcefield and how to download it can be found [here](https://mackerell.umaryland.edu/charmm_ff.shtml).

### ChimeraX
ChimeraX is an extensible program for the interactive visualization and analysis of molecular structures and trajectories. While PyMOL is better used for visualization of protein structures, ChimeraxX's integration with Modeller makes it a useful software for the easy construction of missing loops for ion channels. More information on ChimeraX can be found [here](https://www.cgl.ucsf.edu/chimerax/).

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

The workflow below is written to be channel-agnostic. All structure names, file names, box dimensions, lipid counts, and ion counts are placeholders written as `<...>` or as generic names such as `protein.pdb` and `system.gro`. Substitute the values appropriate to the channel and membrane environment being studied.

The pipeline has three stages that share a common starting point: a repaired protein structure is prepared once, then built into either an atomistic system, a coarse-grained system, or both.

### Protein Repair

Experimental structures of ion channels are frequently missing loops, termini, and side chains. These gaps must be modeled before the structure can be simulated or else the results will be flawed. While my methodology is built upon the usage of modeller, more modern softwares like AlphaFold are equally if not more viable.

**1. Obtain the structure**

Download the most complete and highest-resolution experimental structure of the channel available from the [RCSB PDB](https://www.rcsb.org/). Where several depositions exist, prefer the most recent one with the fewest unresolved residues and the conformational state of interest (for example open, closed, or desensitized). This selection method will ensure the highest accuracy of simulation to real physiological conditions.

**2. Identify missing regions in ChimeraX**

Open the structure and display the sequence for each chain to locate unresolved residues:

```
seq chain /A
```

Repeat for each chain in the assembly. For a homomultimeric channel, the same gaps usually appear in every subunit, and each subunit can be repaired independently.

**3. Model the missing loops**

Use `Tools → Sequence → Model Loops` to call Modeller through ChimeraX, with the following settings:

- Model only the internal structure — that is, the unresolved regions internal to the chain rather than the disordered termini, which generally should not be invented as these regions are largely nonphysical.
- Keep one adjacent flexible residue on each side of the gap so that the modeled loop can be joined to the resolved structure without strain. Leaving strain within the simulation can cause simulations to crash prematurely.
- Set the number of models as high as can be generated without the ChimeraX session disconnecting. More models means better sampling of loop conformations.
- Select the model with the most negative zDOPE score, which is the best-scoring model by Modeller's statistical potential.
- Save the selected model as a `.pdb` file.

**4. Merge separately modeled chains**

If loops were modeled chain by chain, the resulting structures must be recombined into a single file. In PyMOL:

```
load chain_a.pdb
load chain_b.pdb
select all
save repaired_protein.pdb
```

PyMOL saves to the home directory by default unless a full path is given.

**5. Clean the structure**

Remove `HETATM` records — crystallographic waters, detergents, co-purified lipids, ligands, and ions — unless a given heteroatom is explicitly part of the intended model. These records are a common source of atom clashes and of parameterization failures later in the pipeline.

The output of this stage is a single, gap-free `repaired_protein.pdb` used as the input for both the atomistic and the coarse-grained branches below.

### Atomistic

The atomistic branch uses CHARMM-GUI to build and equilibrate a membrane-embedded system in the CHARMM36 force field, then finishes system preparation in GROMACS.

#### Building the membrane system in CHARMM-GUI

Upload `repaired_protein.pdb` to the CHARMM-GUI Membrane Builder and work through the builder with the following considerations.

**Protonation.** The default pH of 7.00 is appropriate for a physiological system unless the study specifically targets pH-dependent gating.

**Orientation.** Use PPM 2.0 to orient the protein relative to the bilayer normal. This places the transmembrane region in agreement with hydrophobic-belt expectations and avoids generating a protein that intersects the bilayer. Apply a small translation along z (on the order of a few angstroms) if the resulting placement is offset relative to where the transmembrane helices should sit. Include pore water so that the conduction pathway is hydrated from the start rather than relying on water to diffuse in during equilibration.

**Box dimensions.** The lateral dimensions must be large enough that the protein cannot interact with its own periodic image. Allow a minimum of 10 Å between the protein and the box edge beyond the nonbonded cutoff. The exact dimensions will depend on the exact protein selected. Note that larger dimensions, while preventing self-interaction of the protein, also increases the computational cost of simulation. Add approximately 30 Å of water on each side of the bilayer to prevent the periodic images from interacting through the z-axis.

**Lipid composition.** Choose a lipid mixture that reflects the native membrane environment of the channel being studied, and build the leaflets asymmetrically where the experimental evidence supports it. Enter lipids by absolute number rather than by ratio. Specifying numbers directly is what allows the box to be driven to the target dimensions while keeping the upper and lower leaflets equal in area, which prevents the bilayer from developing a spurious curvature or tension at the start of the simulation.

**Salt.** Do not add salt in CHARMM-GUI. Ions are added manually with `gmx genion` in the next stage. CHARMM-GUI jobs cannot be re-run with modifications, so any change to the ionic conditions would otherwise require rebuilding the entire system from scratch — an expensive proposition when several ionic conditions are being compared.

**Equilibration and output.** Run the builder's NPT equilibration at the physiological temperature relevant to the tissue being modeled. Download the GROMACS input set; the LAMMPS, NAMD, and OpenMM sets can be saved at the same time if the system is to be cross-validated in another engine.

#### Finishing the system in GROMACS

**1. Neutralize the system**

Run `gmx genion` first simply to determine the net charge of the system, then again to neutralize it. A `.tpr` is required as input, so generate one from a minimal ion-placement `.mdp`:

```bash
gmx grompp -f ions.mdp -c system.gro -p topol.top -o ions.tpr
gmx genion -s ions.tpr -o system_neutral.gro -p topol.top -pname SOD -nname CLA -neutral
```

Ions are placed by replacing water molecules. Most common and relevant ion species for ion channel simulation are Na+, K+, and Cl- given the natural frequency of these ions. Addiitional/different ions can be added if desired; determine the subject of study  Confirm that the force field and ion topology `.itp` files referenced in `topol.top` are updated after every run, including failed ones, since a partially written topology will silently carry over.

**2. Add ions to the target concentration**

Repeat `grompp` and `genion` once per ion species, chaining the output of each call into the next. Each species is added as a matched number of cations and anions on top of the already-neutralized system:

```bash
gmx grompp -f ions.mdp -c system_neutral.gro -p topol.top -o ions_species1.tpr
gmx genion -s ions_species1.tpr -o system_species1.gro -p topol.top -np <N> -pname SOD -nn <N> -nname CLA

gmx grompp -f ions.mdp -c system_species1.gro -p topol.top -o ions_species2.tpr
gmx genion -s ions_species2.tpr -o system_ions.gro -p topol.top -np <M> -pname POT -nn <M> -nname CLA
```

Calculate `<N>` and `<M>` from the target molar concentration and the solvent volume of the box, and record the resulting ion counts for each condition so that the composition of every system in a series is reproducible. Make sure the topology includes an `.itp` entry for every ion species added.

**3. Build index groups**

Analysis and the temperature/pressure coupling groups in the `.mdp` files both depend on a well-defined index file:

```bash
gmx make_ndx -f system_ions.gro -o index.ndx
```

Define three working groups — `Protein`, `Membrane`, and `Solvent`. The membrane group is the union of every lipid species group, and the solvent group is the union of water and all ion groups. Group numbers are assigned per system and will not match between builds, so read them off the listing that `make_ndx` prints rather than reusing numbers from a previous system:

```
13 | 14 | 15 | 16 | 17 | 18 | 19
name <new_group_number> Membrane

20 | 21 | 22 | 23
name <new_group_number> Solvent
```

### Coarse Grain

The coarse-grained branch maps the repaired atomistic structure into the Martini 3 force field, equilibrates the protein in solvent, and then rebuilds it into a bilayer with insane. Working at coarse-grained resolution extends the accessible timescale by orders of magnitude at a fraction of the cost, which is what makes long-timescale gating and lipid-interaction studies tractable.

#### Mapping the protein with Martinize2

Review the available options first, since the useful flags vary by protein and by Martini release:

```bash
martinize2 -h
```

Then map the repaired structure:

```bash
martinize2 -f repaired_protein.pdb -x protein_cg.pdb -o protein_cg.top \
  -ff martini3001 -dssp -elastic -p backbone -pf 1000
```

Notes on the flags and on the files this produces:

- `-dssp` assigns secondary structure, which Martini uses to set backbone bonded parameters.
- `-elastic` applies an elastic network. Add or tune it when the coarse-grained protein does not maintain the tertiary structure expected from the atomistic model; without it, large multidomain channels tend to drift apart.
- `-p backbone -pf 1000` writes position restraints on the backbone beads with a force constant of 1000 kJ mol⁻¹ nm⁻².
- Delete any remaining `HETATM` atoms before mapping. They frequently produce clashes that cause Martinize2 to fail or to map nonsense beads.

Edit the generated `.itp` so that the hard-coded restraint force constant becomes an adjustable one that can be switched on and off, and scaled, from the `.mdp` file:

```
[ position_restraints ]
#ifdef POSRES
#ifndef POSRES_FC
#define POSRES_FC 1000.00
#endif
1    1    POSRES_FC    POSRES_FC    POSRES_FC
#endif
```

#### Equilibrating the coarse-grained protein

Equilibrate the protein in solvent before inserting it into a bilayer, so that any strain introduced by the mapping is relaxed outside the membrane.

**1. Build a solvated box with insane**

```bash
insane -f protein_cg.pdb -o protein_solvated.gro -p protein_solvated.top \
  -x <X> -y <Y> -z <Z> -center -sol W -salt <concentration>
```

This places the protein in a box of the given dimensions (in nm), centers it, and solvates it with Martini water and ions. Update the `.top` and `.gro` files afterwards so the protein is properly included and so that ion names match the Martini 3 naming convention.

**2. Build an index file and minimize**

```bash
gmx make_ndx -f protein_solvated.gro -o index.ndx
gmx grompp -f energy_minim.mdp -c protein_solvated.gro -p protein_solvated.top -o em.tpr
gmx mdrun -v -deffnm em
```

Define a `Solvent` group combining water and ions, again reading group numbers from the `make_ndx` listing.

**3. Equilibrate**

```bash
gmx grompp -f equilibration.mdp -c em.gro -p protein_solvated.top -n index.ndx \
  -o equilibration.tpr -maxwarn 1
gmx mdrun -v -deffnm equilibration
```

This relaxes the structure further so that it is stable when transferred into the membrane system.

**4. Extract the equilibrated protein**

```bash
gmx trjconv -s equilibration.tpr -f equilibration.gro -o protein_cg_stable.pdb -pbc mol -center
```

The extracted structure is the input for membrane insertion.

#### Inserting the protein into a bilayer

```bash
insane -f protein_cg_stable.pdb -o system_cg.gro -p topol.top \
  -x <X> -y <Y> -z <Z> -center -dm <z_shift> \
  -l <LIPID>:<n> -l <LIPID>:<n> -u <LIPID>:<n> -u <LIPID>:<n> \
  -sol W -salt 0.00 \
  -alname <LIPID> -alhead '<head beads>' -allink "<link beads>" -altail "<tail beads>"
```

- `-l` and `-u` specify the lower and upper leaflet composition. Use the same lipid types and the same leaflet asymmetry as the atomistic system so that the two resolutions are directly comparable.
- `-dm` shifts the bilayer along z. Use it to match the membrane position produced by CHARMM-GUI in the atomistic build.
- `-alname`, `-alhead`, `-allink`, and `-altail` define lipids that are not in the insane library by giving their bead topology explicitly. Any custom lipid used in the atomistic membrane will usually need to be defined this way.
- Set the salt concentration to zero here. insane only adds NaCl, so all ion species are added afterwards with `gmx genion`, which allows mixed-salt conditions to be built.
- Confirm that the protein is correctly oriented in the bilayer before continuing; an inverted or tilted insertion will not recover during equilibration.

#### Restraining the upper leaflet

Unrestrained coarse-grained bilayers of this size tend to flex and sway on long timescales, which contaminates membrane-protein contact analysis. Add an optional z-restraint to a subset of upper-leaflet lipids by defining a copy of one phospholipid species under a new residue name — identical parameters, plus the restraint block — and substituting it for a fraction of that species in the upper leaflet:

```
#ifdef DPOS_Z_RES
 [ position_restraints ]
 ; ai  funct  fcx    fcy    fcz
   2    1     0      0      POS_Z_RES
#endif
```

Guidelines for applying the restraint:

- Apply it only in the upper leaflet. Restraining both leaflets restricts the natural expansion and undulation of the bilayer.
- Apply it to phosphate beads, which remain within their own leaflet. Do not restrain sterols, diglycerides, or ceramides, which flip between leaflets and would be held in place unphysically.
- Restrain at least roughly 20% of the upper-leaflet lipids to suppress large-scale flexing; fewer anchor points are not enough to hold the leaflet flat.

#### Defining and adding ions

Ion names must match the `.itp` definitions in the Martini 3 topology. Species that are not distributed with the force field need a new molecule type. For example, a distinct monovalent cation can be defined as:

```
;;;;;; Potassium ion
[moleculetype]
; molname     nrexcl
  PK          1

[atoms]
;id    type    resnr    residu    atom    cgnr    charge    mass
 1     TQ5     1        ION       PK      1       1.0       39.098
```

Then add each species in turn, exactly as in the atomistic branch:

```bash
gmx grompp -f ions.mdp -c system_cg.gro -p topol.top -o ions_species1.tpr
gmx genion -s ions_species1.tpr -o system_cg_species1.gro -p topol.top -np <N> -pname NA -nn <N> -nname CL

gmx grompp -f ions.mdp -c system_cg_species1.gro -p topol.top -o ions_species2.tpr
gmx genion -s ions_species2.tpr -o system_cg_ions.gro -p topol.top -np <M> -pname PK -nn <M> -nname CL
```

Record the ion counts used for each condition so the coarse-grained and atomistic systems can be matched.

#### Building index groups

```bash
gmx make_ndx -f system_cg_ions.gro -o index.ndx
```

As in the atomistic branch, define `Protein`, `Membrane`, and `Solvent` groups by combining the individual lipid, water, and ion groups, then name them:

```
13 | 14 | 15 | 16 | 17 | 18 | 19
name <new_group_number> Membrane

21 | 22 | 23 | 24
name <new_group_number> Solvent
```

Group numbers differ between the atomistic and coarse-grained systems and between builds, so always take them from the current `make_ndx` listing.

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

### CHARMM36
- Vanommeslaeghe, K. Hatcher, E. Acharya, C. Kundu, S. Zhong, S. Shim, J. E. Darian, E. Guvench, O. Lopes, P. Vorobyov, I. and MacKerell, Jr. A.D. "CHARMM General Force Field (CGenFF): A force field for drug-like molecules compatible with the CHARMM all-atom additive biological force fields," Journal of Computational Chemistry 31: 671-90, 2010, PMC2888302
- Klauda, J.B., Venable, R.M., Freites, J.A., O'Connor, J.W., Tobias, D.J., Mondragon-Ramirez, C., Vorobyov, I., MacKerell, Jr., A.D., and Pastor, R.W. "Update of the CHARMM All-Atom Additive Force Field for Lipids: Validation on Six Lipid Types," Journal of Physical Chemistry B, 114: 7830-7843, 2010
- Vanommeslaeghe, K., and MacKerell Jr., A.D., "Automation of the CHARMM General Force Field (CGenFF) I: bond perception and atom typing," Journal of Chemical Informationa and Modeling, 52: 3144-3154, 2012, PMC3528824
- Vanommeslaeghe, K., Raman, E.P., and MacKerell Jr., A.D., "Automation of the CHARMM General Force Field (CGenFF) II: Assignment of bonded parameters and partial atomic charges, Journal of Chemical Informationa and Modeling, 52: 3155-3168, 2012, PMC3528813
- Yu, W., He, X., Vanommeslaeghe, K. and MacKerell, A.D., Jr., "Extension of the CHARMM General Force Field to Sulfonyl-Containing Compounds and Its Utility in Biomolecular Simulations," Journal of Computational Chemistry, 33: 2451-2468, 2012, PMC3477297
- Best, R.B., Zhu, X., Shim, J., Lopes, P.E.M., Mittal, J., Feig, M., and MacKerell Jr., A.D. "Optimization of the additive CHARMM all-atom protein force field targeting improved sampling of the backbone phi, psi and side-chain chi1 and chi2 dihedral angles," Journal of Chemical Theory and Computation, 8: 3257-3273, 2012, PMC3549273
- Soteras Gutierrez, I., Lin, F.-Y., Vanommeslaeghe, K., Lemkul, J.A., Armacost, K.A., Brooks, Cl., III, and MacKerell, A.D., Jr., "Parametrization of Halogen Bonds in the CHARMM General Force Field: Improved treatment of ligand-protein interactions," Bioorganic & Medicinal Chemistry, In Press, 2016
- Huang, J., Rauscher, S., Nawrocki, G., Ran, T., Feig, M, de Groot, B.L., Grubmuller, H., and MacKerell, A.D., Jr., "CHARMM36m: An Improved Force Field for Folded and Intrinsically Disordered Proteins," Nature Methods, 14:71-73, 2016, PMC5199616

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
