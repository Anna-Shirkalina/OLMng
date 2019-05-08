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

Specifying which model
----------------------
In the respective init_modelXX.hoc file change the "cell" parameter on line 2
to one of "1", "2", or "3", corresponding to the Cell from the accompanying
paper. For the spiking model cells (1 and 2), there are currently five
different models to choose from (i.e. the top five models from the
multi-objective optimization). To specify which model, set the "modelnum"
parameter on line 3 to any value between 1 and 5 (in order from highest ranked
to fifth-ranked).

Model invocation
----------------
Use nrngui or nrniv as follows:

PASSIVE MODEL:

    nrngui -c init_model_passive.hoc

PASSIVE MODEL + Ih:

    nrngui -c init_model_Ih.hoc

PASSIVE MODEL + Ih + SPIKING CURRENTS:

    nrngui -c init_model.hoc

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
