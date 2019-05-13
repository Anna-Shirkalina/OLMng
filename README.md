# OLMng
"Next-generation" multi-compartment model of CA1 hippocampal O-LM interneurons
==============================================================================

Passive properties and Ih properties are all fitted from experimental data from
the same cells from which morphology data was derived. Thus, passive, Ih, and
morphological data are matched for each given model. Each model then represents
one cell. The remaining active conductances, however, are tuned to reproduce
firing characteristics as best as possible for the same cells. However, the
channel properties are derived from previous OLM (and non-OLM) cells and thus
are not experimentally constrained by recordings from the same cell. They can
thus be varied to explore parameter spaces or fit new experimental data. 

However, the passive and Ih properties (for the latter this includes Ih steady
state activation function, time dependency of activation and deactivation, and
reversal potential) should remain fixed as they have been determined directly
from recordings.

Specifying which cell and model
-------------------------------
In the init_model.hoc file there are three parameters to define the model:

cell - one of 1, 2, or 3, corresponding to the three reconstructed cells in the
    paper

paramtype - one of 1 (passive), 2 (passive + Ih), or 3 (passive + Ih + spiking
    currents)

modeltype - only used by the spiking model cells (1 and 2), corresponding to
    the five different spiking parameter sets to choose from (i.e. the top
    five models from the multi-objective optimization). To specify which 
    spiking model, set the "modelnum" parameter to any value between 1 and 5
    (in order from highest ranked to fifth-ranked).

Model invocation
----------------
Use nrngui or nrniv as follows:

    nrngui init_model.hoc

The parameters specified in the previous section can also be commented out and
provided during model invocation on the command-line using the -c switches for
nrngui or nrniv, e.g.,

    nrngui -c 'cell=1' -c 'paramtype=3' -c 'modelnum=1' init_model.hoc

(Spiking models only) run current-clamp protocols and plot the currentscapes
----------------------------------------------------------------------------
Use python and as follows:

    python init.py

Model parameters
----------------
Most parameters are found in either the sim_params.hoc file or in the 
per-cell parameter files within the "param_files" directory. The ones in
sim_params.hoc are particularly relevant for global aspects of operation
such as length of simulation, integration method, current clamp injection
parameters, etc. 

Experimental data
-----------------
Current-clamp traces under synaptic blocker wash-in conditions for cells 1 and
2 can be found in the respective CellX_exp_data/ directories. These traces are
needed for plotting currentscapes for the spiking models. The injected current
amplitude is included in the filename.
