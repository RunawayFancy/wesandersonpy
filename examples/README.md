# Manufacturing-style plotting examples

These five scripts demonstrate how `wesandersonpy` palettes and Matplotlib colormaps can be used in publication-style, multi-layer figures. Every CSV under `examples/data/` is synthetic and non-experimental. The values were invented for software demonstrations, were not digitized from the visual references, and must not be used for scientific inference.

Each script defaults to its reviewed fixture directory relative to its own file. It validates the expected CSV schema, creates the requested output directory when needed, saves a deterministic figure at 180 DPI, closes the Matplotlib figure, and places a visible synthetic-data notice in the result. Source CSVs are never modified.

## Run the examples

Install the project and its example dependencies first from the repository root. Then run:

```console
python examples/diagram_sequence_time_domain.py --data-dir examples/data/diagram_sequence --output examples/figures/generated/diagram_sequence_time_domain.png
python examples/multiple_iterations_faded.py --input examples/data/multiple_iterations/iteration_populations.csv --output examples/figures/generated/multiple_iterations_faded.png
python examples/fidelity_multi_parameter.py --data-dir examples/data/fidelity_multi_parameter --output examples/figures/generated/fidelity_multi_parameter.png
python examples/scatter_with_simulation.py --data-dir examples/data/scatter_simulation --output examples/figures/generated/scatter_with_simulation.png
python examples/readout_calibration_rabi_subplots.py --data-dir examples/data/readout_calibration_rabi --output examples/figures/generated/readout_calibration_rabi_subplots.png
```

The defaults for `--input` or `--data-dir` and `--output` are the paths shown above, so the options may be omitted. The scripts accept alternate paths for adapting the plotting grammar, validate the expected schemas, and refuse to save over an input CSV. The bundled defaults are the reviewed synthetic fixtures; do not pass confidential or experimental data to these demonstration scripts.

First-pass renders remain under the ignored `examples/figures/generated/` directory. After the human maintainer confirms that a PNG is nonconfidential, uses only the synthetic fixtures, has no sensitive metadata, and renders correctly, copy or move that approved PNG one level up to `examples/figures/` for version control and README use. Do not promote an image before that review.

## Figure index

| Script | Plot grammar | Package color API |
|---|---|---|
| `diagram_sequence_time_domain.py` | Sequence schematic, time response, two population sweeps, inset, and level annotations | `get_palette("Zissou1")` |
| `multiple_iterations_faded.py` | Repeated marker traces with opacity showing chronology | `get_palette("Zissou1")` |
| `fidelity_multi_parameter.py` | Logarithmic five-series curves with marker and asymptote encodings | `get_colormap("Darjeeling1")` |
| `scatter_with_simulation.py` | Tall branch scatter panel and two compact probability strips | `get_palette("FantasticFox1")` |
| `readout_calibration_rabi_subplots.py` | Schematic, paired tone responses, IQ triptych, three population rows, and spin row | `get_palette(...)` and `get_colormap("GrandBudapest1")` |

The terms "fit," "experiment," "simulation," "fidelity," "population," and state labels appear only to preserve the requested plot grammar. They do not describe actual measurements, fitted models, physical simulations, or validated results.

## Human verification

Run the five commands above and report the Python version, installed `wesandersonpy` version, console output, and generated PNGs. Check that every image opens, contains the visible synthetic-data footer, and matches the intended layout. Only nonconfidential images reviewed and approved by the human maintainer should be committed or embedded in the root README.
