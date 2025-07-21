<div align="center";>
  <h1>Ion Channel Simulation and Analysis Guide</h1>

  Welcome! This is my repository for a streamlined and reproducable method of ion channel simulation and analysis through atomistic and coarse grained means.
</div> 

## Table of Contents

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
- [Coarse Graining](#coarse-graining)
- [Methodology](#methodology)
  * [Atomistic](#atomistic)
  * [Coarse Grain](#coarse-grain)
  * [Lipid Membranes](#lipid-membranes)
  * [Solvation](#solvation)
  * [Simulation](#simulation)
- [Analysis](#analysis)
- [Resources](#resources)
- [References](#references)

## Overview
The focus of this repository is to provide a set of tips, tools, and scripts for mass simulation of ion channels in an easily reproducible method. Included are overviews of relevant softwares for ion channel simulation, discussion of the utility and limitations of coarse graining, an overview of the methodology of simulation, discussion on relevant characteristics of channels for analysis, and resources/references to learn more. Expanded discussions can be found in the listed folders above.

## Software
### Charmm-Gui

Charmm-Gui is a web-based platform designed for the interactive construction of complex biological systems for simulation. It has compatibility with a variety of simulation packages such as NAMD, CHARMM, OpenMM, LAMMPS, AMBER, GENESIS, Tinker, Desmond, and of most relevance, GROMACS. Due to the complex nature of atomistic ion channel systems, developing the simulation environments by oneself can be rather laborious. Thus Charmm-Gui serves the role of readily developing these complex biological systems through a stream-lined interface. More information can be found here.

### ChimeraX

ChimeraX is computational biology visualization program used in rendering proteins for visual analysis. While PyMol is typically recommended over ChimeraX, the usage for ChimeraX lies with its in built modeller functionality. Ion channels are typically constructed using the method of cryogenic electron microposcy, which while a powerful tool often can lack the resolution for the accurate rendering of fringe side chain elements of said channels. Thus, the usage for ChimeraX where peripheral elements can be accurately reconstructed for usage in simulation. More information can be found here.

### GROMACS

GROMACS is a high performance suite of tools molecular dynamic simulation and output analysis. GROMACS is highly versatile, functional, and compatible with virtually every step of the process for ion channel simulation construction and operation. Insane, Martini3, and Vermouth all rely on the platform of GROMACS for many operations. Simulation scripts for GROMAC's simulations can eb found here, while more information on other uses can be found here.

### Insane

Insane is a versatile tool 

### Martini3
### MDAnalysis
### PyMol
### Vermouth-Martinize2

## Coarse Graining

## Methodology

### Atomistic
### Coarse Grain
### Lipid Membranes
### Solvation
### Simulation

## Analysis

## Resources

## References


