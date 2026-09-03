# Ion Channel Simulation Analysis

Analysis and plotting pipelines for molecular dynamics simulations of ion
channels, built on GROMACS output and MDAnalysis.

Each notebook covers one class of analysis and can be run on its own: clone the
repository, install the requirements, and run any notebook end to end. They share
one configuration module so that settings common to all of them cannot drift
apart.

## Layout

```
channel_config.py                 shared settings and plotting primitives
GeneralIonChannelAnalysis.ipynb
ProteinChannel.ipynb
ProteinLipidNetwork.ipynb
ProteinProteinNetwork.ipynb
requirements.txt
.gitignore
```

`channel_config.py` is the single place the shared settings live. Notebooks must
be run from the directory containing it (the repository root), which is the
default if you launch `jupyter lab` there.

## The notebooks

| Notebook | What it does | Inputs |
|---|---|---|
| **GeneralIonChannelAnalysis.ipynb** | RMSD, RMSF, radius of gyration and system energies. Protomer-averaged RMSF, variability across conditions, and B-factor structures for viewing flexibility on the structure. | `.xvg` from `gmx rms`, `rmsf`, `gyrate`, `energy` |
| **ProteinChannel.ipynb** | Pore radius profiles along the conduction pathway via HOLE. Profile alignment, constriction detection, and pore surface meshes. | `.pdb` + `.xtc`, plus the external HOLE program |
| **ProteinLipidNetwork.ipynb** | Protein–lipid distances and per-residue contact probabilities. Identifies candidate lipid binding sites per species. | Full-system `.gro` + `.xtc` |
| **ProteinProteinNetwork.ipynb** | Residue–residue contact networks, split into intra-subunit, adjacent and diagonal classes. Finds pairs whose contacts trend monotonically with a condition. | Protein-only `.gro` + `.xtc` |

## Quick start

```bash
pip install -r requirements.txt
jupyter lab
```

Every notebook opens with `USE_DEMO_DATA = True`, which generates small
synthetic inputs and runs the whole pipeline without any real trajectories. Use
this to confirm the installation works and to see what each output looks like
before pointing anything at your own data.

To use your own simulations, set `USE_DEMO_DATA = False` and either edit
`DATA_ROOT` or set the environment variable:

```bash
export MD_DATA_ROOT=/scratch/$USER/channel_runs
```

> The demo data is fabricated. It has the right shape and plausible magnitudes,
> and in some cases a signal is planted deliberately so the detection code has
> something to find, but none of it means anything physically.

## Shared conventions

All four notebooks follow the same structure, so once you have read one the
others should be navigable:

1. **Imports**
2. **Configuration** — the only cell you normally edit
3. **Condition grid** — the set of simulations, described once
4. **Demo data** — optional synthetic inputs
5. **Analysis classes and functions**
6. **Plotting**
7. **Analysis** — everything below this heading runs the pipeline

**Shared settings live in `channel_config.py`, not in the notebooks.** Change the
protomer count, the condition grid, the domain boundaries, the unit conversions
or the plot style there and every notebook picks it up. Each notebook's own
configuration cell holds only what is specific to it: which files to read, where
to write output, and its analysis parameters.

`channel_config.py` also provides the pieces every notebook plots with —
`ConditionGrid`, the automatic tick helpers, the colour ramp and the domain
bands — so a fix to any of them applies everywhere at once.

Other shared conventions:

- **Units.** Every notebook works internally in **ångström** and **nanoseconds**.
  GROMACS writes nm and ps, so conversion happens at load time.
- **Residue numbering.** Residue numbers are read from the input files and shifted
  by `RESIDUE_OFFSET[model_level]`, so a coarse-grained model that renumbers from
  1 and an all-atom model that carries the real numbering both end up on one
  common scheme. `DOMAIN_SEGMENTS` is given in those real residue numbers.
- **No hard-coded paths or slices.** Paths are built by `build_path()`; groups of
  runs are selected with `grid.where(salinity_mm=50)` rather than `[0:6]`.
- **Outputs.** Each notebook writes to `results/<NOTEBOOK_SLUG>/`, so sibling
  notebooks cannot overwrite each other's figures. Set `SAVE_FIGURES = True` to
  save as figures are drawn.

## Expected data layout

```
<DATA_ROOT>/
├── reference/
│   └── channel_reference.pdb
├── coarse/
│   ├── 305K05/                 # 305 K, 50 mM
│   │   ├── RMSDProtein.xvg     # GeneralIonChannelAnalysis
│   │   ├── RMSFProtein.xvg
│   │   ├── RGProtein.xvg
│   │   ├── NPTEnergy.xvg
│   │   ├── NPT.gro             # ProteinLipidNetwork (full system)
│   │   ├── NPT.xtc
│   │   ├── NPTProteinCenter.gro   # ProteinProteinNetwork
│   │   ├── NPTProteinCenter.pdb   # ProteinChannel
│   │   └── NPTProteinCenter.xtc
│   └── ...
└── atomistic/
    └── ...
```

The directory name for each condition is produced by `build_condition_dirname()`.
If your layout differs, override that function and `build_path()` in the
configuration cell — no analysis code needs to change.

Each notebook's opening markdown lists the exact `gmx` commands that generate
its inputs.

## Adapting to a different channel

The defaults describe a tetrameric TRPV1-like channel simulated across six
temperatures and three salinities. To adapt:

In `channel_config.py` (once, for all four notebooks):

1. `N_PROTOMERS` — 4 for TRP and most K⁺ channels, 5 for pLGICs, 3 for ASIC/P2X.
2. `RESIDUE_OFFSET` / `RESIDUE_NUMBER_ORIGIN` — align numbering with your construct.
3. `TEMPERATURES_K` / `SALINITIES_MM` — or whatever conditions you varied.
4. `DOMAIN_SEGMENTS` — **replace these.** The defaults are example values for a
   TRPV1-like construct and the domain names are inferred from residue ranges,
   not authoritative.
5. `condition_dirname()` — if your directories are not named `305K05`.

In the individual notebooks:

6. `FILENAMES` — if your `.xvg` / `.gro` / `.xtc` files are named differently.
7. `CONTACT_CUTOFF` / `CONTACT_THRESHOLD` / `LIPID_RESNAMES` /
   `PROTEIN_SELECTION` — force-field and resolution dependent; see the notebooks
   that use them.

## A note on HOLE

`ProteinChannel.ipynb` uses `mdahole2`, which is only a Python wrapper. The
actual HOLE program is separately licensed and cannot be installed with `pip`.
Get it from [holeprogram.org](https://www.holeprogram.org/) and put the binary
on `PATH`, or set `HOLE_EXECUTABLE` to its absolute path. The notebook checks
before doing any work and runs in demo mode without it.

## Repository housekeeping

Notebook outputs are stripped from version control, which keeps diffs small and
prevents absolute data paths leaking through cell output. To make that automatic:

```bash
pip install nbstripout
nbstripout --install     # run once, inside the repository
```

## Caveats

- Smoothing and the switching function used in contact time series are
  presentation choices. Statistics are computed from raw data.
- Variance and trend detection across a handful of conditions are **ranking
  heuristics**, not statistics to quote. Corroborate any hit structurally.
- Coarse-grained and all-atom results are not directly comparable in absolute
  terms — different cutoffs and different particle definitions. Compare trends.
- Error bars, where present, come from block averaging and assume the blocks are
  independent. Treat them as a lower bound.
