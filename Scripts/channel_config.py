"""Shared configuration and plotting primitives for the ion channel notebooks.

This module holds everything that must be the same in every notebook in this
repository: where the data lives, the grid of simulations, the channel topology,
the structural domain boundaries, and the plotting primitives. Change a value
here and every notebook picks it up.

Notebook-specific settings - which files to read, where to write output, and any
analysis parameters - stay in each notebook's configuration cell.

Usage
-----
Notebooks are expected to sit in the same directory as this file:

    import channel_config as cc
    from channel_config import *      # shared settings and helpers

    USE_DEMO_DATA = True
    NOTEBOOK_SLUG = "my_analysis"
    FILENAMES = {"topology": "NPT.gro"}
    DATA_ROOT = cc.resolve_data_root(USE_DEMO_DATA)

The star import only exports the names listed in `__all__`, all of which are
shared and read-only. Per-notebook values such as DATA_ROOT are deliberately not
exported, so there is no chance of a notebook picking up a stale copy.

Design note
-----------
This module holds no mutable per-notebook state. `ConditionGrid` is given a
path-building function rather than reaching for a global, so two notebooks
reading different files can each build a grid without interfering.
"""

import os
import re
import itertools
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import ScalarFormatter

__all__ = [
    # simulation grid
    "MODEL_LEVELS", "TEMPERATURES_K", "SALINITIES_MM",
    "Condition", "ConditionGrid", "condition_dirname",
    # channel topology
    "N_PROTOMERS", "RESIDUE_OFFSET", "RESIDUE_NUMBER_ORIGIN",
    # domains
    "DOMAIN_SEGMENTS", "describe_domain", "add_domain_bands",
    # units
    "NM_TO_ANGSTROM", "PS_TO_NS",
    # style
    "FONTSIZE", "TEMPERATURE_COLORS", "resolve_colors",
    # tick helpers
    "nice_ticks", "apply_ticks", "decade_ticks",
]


# ===========================================================================
# 1. Where the data lives
# ===========================================================================
# Relative paths by default, so nothing machine-specific is committed. Override
# per machine with the MD_DATA_ROOT environment variable:
#     export MD_DATA_ROOT=/scratch/$USER/channel_runs
REAL_DATA_ROOT = Path(os.environ.get("MD_DATA_ROOT", "data")).expanduser()
DEMO_DATA_ROOT = Path("demo_data")

# Root of the per-notebook output directories.
RESULTS_ROOT = Path("results")

FIGURE_FORMAT = "png"
FIGURE_DPI = 300


def resolve_data_root(use_demo_data):
    """Return the data root for this run: the demo tree or the real one."""
    return DEMO_DATA_ROOT if use_demo_data else REAL_DATA_ROOT


def make_output_dir(notebook_slug):
    """Create and return `results/<notebook_slug>/`.

    Each notebook writes to its own subdirectory so that two notebooks saving a
    figure of the same name cannot overwrite one another.
    """
    path = RESULTS_ROOT / notebook_slug
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_figure(fig, name, output_dir, enabled=False,
                figure_format=None, dpi=None):
    """Write `fig` into `output_dir` when `enabled`.

    Notebooks normally wrap this so the call site stays short:

        def save_figure(fig, name):
            return cc.save_figure(fig, name, OUTPUT_DIR, SAVE_FIGURES)
    """
    if not enabled:
        return None
    figure_format = FIGURE_FORMAT if figure_format is None else figure_format
    dpi = FIGURE_DPI if dpi is None else dpi
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")
    path = Path(output_dir) / f"{safe}.{figure_format}"
    fig.savefig(path, dpi=dpi)
    print(f"  saved {path}")
    return path


# ===========================================================================
# 2. The simulation grid
# ===========================================================================
# MODEL_LEVELS are the independent sets of simulations to compare - here a
# coarse-grained and an all-atom description of the same channel. Use a single
# entry (e.g. ("atomistic",)) if you only ran one.
MODEL_LEVELS = ("coarse", "atomistic")

# Each (temperature, salinity) pair is one simulation.
TEMPERATURES_K = (305, 310, 315, 320, 325, 330)
SALINITIES_MM = (50, 100, 150)


def condition_dirname(temperature_k, salinity_mm):
    """Return the directory name for one simulation condition.

    The default reproduces the ``305K05`` convention: temperature in kelvin
    followed by salinity in units of 10 mM, zero padded to two digits.

    To use a different convention, redefine `build_path` in the notebook that
    needs it, or change this function to affect every notebook at once::

        return f"T{temperature_k:.0f}_NaCl{salinity_mm:.0f}mM"
    """
    return f"{temperature_k:.0f}K{salinity_mm / 10:02.0f}"


# ===========================================================================
# 3. Channel topology
# ===========================================================================
# Number of identical subunits.
#   4 -> TRP channels, most K+ channels     5 -> pLGICs (nAChR, GLIC, GABA-A)
#   3 -> ASIC, P2X                          1 -> monomeric / no averaging
N_PROTOMERS = 4

# Added to the residue numbers a model level writes, so that every model level
# ends up on one common numbering scheme (that of the reference structure).
#
# Example: a coarse model that renumbers its residues from 1 while the construct
# actually begins at 199 needs an offset of 198; an all-atom run that already
# carries the real numbering needs 0.
RESIDUE_OFFSET = {
    "coarse": 198,
    "atomistic": 0,
}

# First real residue number of the modelled construct, after the offset above.
RESIDUE_NUMBER_ORIGIN = 199


# ===========================================================================
# 4. Unit conversion
# ===========================================================================
# GROMACS writes nm and ps. Every notebook works internally in angstrom and ns.
# Note MDAnalysis already returns angstrom, so these apply to .xvg input only.
NM_TO_ANGSTROM = 10.0
PS_TO_NS = 1.0e-3


# ===========================================================================
# 5. Structural domains
# ===========================================================================
# EXAMPLE VALUES for a TRPV1-like construct, given in REAL RESIDUE NUMBERS on
# the common numbering scheme above (i.e. the numbers you would read off a
# structure or a paper).
#
# REPLACE THESE with the domain boundaries of your own channel. The names below
# were inferred from the residue ranges and are not authoritative. Set the list
# to [] to omit the domain bands from every plot in every notebook.
DOMAIN_SEGMENTS = [
    {"name": "ARD",                "start": 199, "end": 361, "color": "#DC050C"},
    {"name": "Pre-S1",             "start": 362, "end": 418, "color": "#E8601C"},
    {"name": "S1",                 "start": 419, "end": 430, "color": "#F1932D"},
    {"name": "S1-S2 linker",       "start": 431, "end": 464, "color": "#F6C141"},
    {"name": "S2",                 "start": 465, "end": 504, "color": "#F7F056"},
    {"name": "S2-S3 linker",       "start": 505, "end": 533, "color": "#CAE0AB"},
    {"name": "S3",                 "start": 534, "end": 559, "color": "#90C987"},
    {"name": "S4",                 "start": 560, "end": 575, "color": "#4EB265"},
    {"name": "S4-S5 linker",       "start": 576, "end": 598, "color": "#7BAFDE"},
    {"name": "S5",                 "start": 599, "end": 655, "color": "#1965B0"},
    {"name": "Pore helix",         "start": 656, "end": 691, "color": "#882E72"},
    {"name": "Selectivity filter", "start": 692, "end": 715, "color": "#AE76A3"},
    {"name": "S6 / TRP helix",     "start": 716, "end": 754, "color": "#D1BBD7"},
]


# ===========================================================================
# 6. Plot styling
# ===========================================================================
FONTSIZE = 22

# Sequential colour ramp, one colour per temperature. Must be at least as long
# as TEMPERATURES_K.
TEMPERATURE_COLORS = ("#EAECCC", "#FEDA8B", "#FDB366",
                      "#F67E4B", "#DD3D2D", "#A50026")


def apply_style(fontsize=None):
    """Set the shared matplotlib style. Call once, from the config cell."""
    fontsize = FONTSIZE if fontsize is None else fontsize
    plt.rcParams.update({
        "font.size": fontsize,
        "axes.labelsize": fontsize,
        "xtick.labelsize": fontsize,
        "ytick.labelsize": fontsize,
        "legend.fontsize": fontsize,
        "figure.autolayout": True,
        "savefig.bbox": "tight",
    })


def describe_config(data_root, use_demo_data, output_dir):
    """Print the resolved configuration, and sanity check it."""
    print(f"Shared config : {Path(__file__).name}")
    print(f"Data root     : {Path(data_root).resolve()}")
    print(f"Demo mode     : {use_demo_data}")
    print(f"Model levels  : {', '.join(MODEL_LEVELS)}")
    print(f"Conditions    : {len(TEMPERATURES_K)} temperatures x "
          f"{len(SALINITIES_MM)} salinities = "
          f"{len(TEMPERATURES_K) * len(SALINITIES_MM)} runs per model level")
    print(f"Protomers     : {N_PROTOMERS}")
    print(f"Output dir    : {Path(output_dir).resolve()}")

    if len(TEMPERATURE_COLORS) < len(TEMPERATURES_K):
        raise ValueError(
            "TEMPERATURE_COLORS needs at least one colour per entry in "
            f"TEMPERATURES_K ({len(TEMPERATURE_COLORS)} < "
            f"{len(TEMPERATURES_K)}). Edit channel_config.py.")
    missing_offsets = [m for m in MODEL_LEVELS if m not in RESIDUE_OFFSET]
    if missing_offsets:
        raise ValueError(
            f"RESIDUE_OFFSET has no entry for {missing_offsets}. "
            "Every model level needs one. Edit channel_config.py.")


# ===========================================================================
# 7. Condition grid
# ===========================================================================
#  Rather than maintaining lists of file paths by hand (which is where index
#  bugs creep in), the set of simulations is described once and every later
#  selection is a query against it. `grid.where(salinity_mm=50)` returns the
#  positions of those runs, so slicing is never hard coded as [0:6] or [12:18].
# ===========================================================================

@dataclass(frozen=True)
class Condition:
    """One simulation condition: a single point on the grid."""

    temperature_k: float
    salinity_mm: float

    @property
    def temperature_label(self):
        return f"{self.temperature_k:.0f}K"

    @property
    def salinity_label(self):
        return f"{self.salinity_mm:.0f} mM"

    def __str__(self):
        return f"{self.temperature_label} / {self.salinity_label}"


class ConditionGrid:
    """An ordered set of simulation conditions, with lookup helpers.

    The ordering is salinity-major (all temperatures at the first salinity, then
    all temperatures at the second, ...). Every list of loaded data follows this
    same order, because file lists are generated from the grid.

    Parameters
    ----------
    temperatures_k, salinities_mm : sequence
        The grid axes.
    path_builder : callable
        ``path_builder(model_level, temperature_k, salinity_mm, key) -> Path``.
        Passed in rather than taken from a global, so notebooks reading
        different files can each build a grid independently.
    """

    def __init__(self, temperatures_k, salinities_mm, path_builder):
        self.temperatures_k = tuple(temperatures_k)
        self.salinities_mm = tuple(salinities_mm)
        self._path_builder = path_builder
        self.conditions = [
            Condition(temperature_k=t, salinity_mm=s)
            for s, t in itertools.product(self.salinities_mm, self.temperatures_k)
        ]

    def __len__(self):
        return len(self.conditions)

    def __iter__(self):
        return iter(self.conditions)

    def __getitem__(self, index):
        return self.conditions[index]

    def where(self, temperature_k=None, salinity_mm=None):
        """Return the indices of conditions matching the given constraints.

        Any argument left as None is a wildcard::

            grid.where(salinity_mm=50)       # every temperature at 50 mM
            grid.where(temperature_k=305)    # every salinity at 305 K
        """
        indices = []
        for i, cond in enumerate(self.conditions):
            if temperature_k is not None and cond.temperature_k != temperature_k:
                continue
            if salinity_mm is not None and cond.salinity_mm != salinity_mm:
                continue
            indices.append(i)
        if not indices:
            raise KeyError(
                f"No condition matches temperature_k={temperature_k}, "
                f"salinity_mm={salinity_mm}. "
                f"Available temperatures: {self.temperatures_k}; "
                f"salinities: {self.salinities_mm}")
        return indices

    def paths(self, model_level, key, indices=None):
        """Return the path to `key` for the selected conditions, in order."""
        indices = range(len(self)) if indices is None else indices
        return [
            self._path_builder(model_level, self.conditions[i].temperature_k,
                               self.conditions[i].salinity_mm, key)
            for i in indices
        ]

    def labels(self, indices=None, by="temperature"):
        """Return human-readable labels for a subset of conditions."""
        indices = range(len(self)) if indices is None else indices
        if by == "temperature":
            return [self.conditions[i].temperature_label for i in indices]
        if by == "salinity":
            return [self.conditions[i].salinity_label for i in indices]
        return [str(self.conditions[i]) for i in indices]

    def report_missing(self, model_level, key, indices=None):
        """List the expected files that are not present on disk."""
        return [p for p in self.paths(model_level, key, indices) if not p.is_file()]

    def describe(self):
        """Print the grid in load order."""
        print(f"{len(self)} conditions, in load order:")
        for i, cond in enumerate(self):
            print(f"  [{i:2d}] {cond}")


# ===========================================================================
# 8. Plotting primitives
# ===========================================================================
#  Tick positions are computed from the data rather than hard coded, so the same
#  helpers work whatever the length or scale of the input.
# ===========================================================================

def nice_ticks(vmin, vmax, n_ticks=8, label_every=1, fmt="{:g}"):
    """Return (positions, labels) for a readable axis over [vmin, vmax].

    Positions land on a 1/2/5 x 10^n step so labels stay round. `label_every=2`
    labels every second tick and blanks the rest, which keeps dense axes legible
    at large font sizes.
    """
    if not np.isfinite([vmin, vmax]).all() or vmax <= vmin:
        return [vmin, vmax], [fmt.format(vmin), fmt.format(vmax)]

    raw_step = (vmax - vmin) / max(n_ticks - 1, 1)
    magnitude = 10.0 ** np.floor(np.log10(raw_step))
    for multiple in (1, 2, 2.5, 5, 10):
        step = multiple * magnitude
        if step >= raw_step:
            break

    start = np.floor(vmin / step) * step
    stop = np.ceil(vmax / step) * step
    positions = np.arange(start, stop + 0.5 * step, step)
    positions = positions[(positions >= vmin - 1e-9) & (positions <= vmax + 1e-9)]
    labels = [fmt.format(p) if i % label_every == 0 else ""
              for i, p in enumerate(positions)]
    return list(positions), labels


def apply_ticks(ax, which, lo, hi, n_ticks=8, label_every=1):
    """Place ticks on one axis of `ax` over [lo, hi].

    Large magnitudes get matplotlib's mathtext formatter, which factors out a
    common power of ten instead of printing it on every tick - the difference
    between "-1.12e+06" on every label and a single "x10^6" in the corner.
    """
    positions, labels = nice_ticks(lo, hi, n_ticks=n_ticks, label_every=label_every)
    axis = ax.xaxis if which == "x" else ax.yaxis
    (ax.set_xticks if which == "x" else ax.set_yticks)(positions)

    magnitude = max(abs(lo), abs(hi))
    if magnitude >= 1.0e4 or 0.0 < magnitude < 1.0e-3:
        formatter = ScalarFormatter(useMathText=True)
        formatter.set_powerlimits((-3, 4))
        axis.set_major_formatter(formatter)
        axis.get_offset_text().set_fontsize(FONTSIZE * 0.8)
    else:
        (ax.set_xticklabels if which == "x" else ax.set_yticklabels)(labels)
    return positions


def decade_ticks(vmin, vmax):
    """Return (positions, labels) marking each power of ten in [vmin, vmax]."""
    lo = int(np.floor(np.log10(vmin)))
    hi = int(np.ceil(np.log10(vmax)))
    positions = [10.0 ** e for e in range(lo, hi + 1)]
    labels = [rf"$10^{{{e}}}$" for e in range(lo, hi + 1)]
    keep = [(p, l) for p, l in zip(positions, labels) if vmin <= p <= vmax]
    if not keep:
        return positions, labels
    return [p for p, _ in keep], [l for _, l in keep]


def resolve_colors(colors, n_series):
    """Pick a colour per series, cycling the configured ramp if needed."""
    if colors is not None:
        return list(colors)[:n_series]
    if n_series <= len(TEMPERATURE_COLORS):
        return list(TEMPERATURE_COLORS)[:n_series]
    cmap = plt.get_cmap("viridis")
    return [cmap(v) for v in np.linspace(0, 1, n_series)]


def add_domain_bands(ax, segments=None, height=0.035, show_legend=False):
    """Draw the structural domains as a colour strip along the bottom of `ax`.

    `segments` are in real residue numbers, matching the x axis. Coordinates are
    blended: x in data units, y in axes fractions, so the strip stays pinned to
    the bottom whatever the y limits.

    Call this after xlim is set. Each band is clamped to the visible range: the
    bands are drawn with clip_on=False so they can sit slightly below the axes,
    which means an unclamped band extending past the axis would be included in
    the tight bounding box and inflate the saved figure enormously.
    """
    segments = DOMAIN_SEGMENTS if segments is None else segments
    if not segments:
        return ax
    x_lo, x_hi = ax.get_xlim()
    transform = ax.get_xaxis_transform()
    drawn = []
    for segment in segments:
        start = max(float(segment["start"]), min(x_lo, x_hi))
        end = min(float(segment["end"]), max(x_lo, x_hi))
        if end <= start:
            continue                      # segment lies outside the plotted range
        drawn.append(segment)
        ax.add_patch(plt.Rectangle(
            (start, 0.0), end - start, height,
            transform=transform, facecolor=segment["color"],
            edgecolor="none", clip_on=False, zorder=3,
        ))
    if show_legend and drawn:
        handles = [Patch(facecolor=s["color"], label=s["name"]) for s in drawn]
        ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.22),
                  ncol=4, fontsize=FONTSIZE * 0.5, frameon=False)
    return ax


def describe_domain(residue_number, segments=None):
    """Name the configured domain containing a real residue number."""
    segments = DOMAIN_SEGMENTS if segments is None else segments
    for segment in segments:
        if segment["start"] <= residue_number <= segment["end"]:
            return segment["name"]
    return "-"
