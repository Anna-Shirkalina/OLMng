# OLMng
"Next-generation" multi-compartment model of CA1 hippocampal O-LM interneurons
==============================================================================

Passive properties and Ih properties are all fitted from experimental data
from the same cells from which morphology data was derived. Thus, passive,
Ih, and morphological data are matched for each given model. Each model
then represents one cell. The remaining active conductances, however, are
tuned to reproduce firing characteristics as best as possible for the same
cells. However, the channel properties are derived from previous OLM (and
non-OLM) cells and thus are not experimentally constrained by recordings 
from the same cell. They can thus be varied to explore parameter spaces
or fit new experimental data. 

However, the passive and Ih properties (for the latter this includes Ih
steady state activation function, time dependency of activation and
deactivation, and reversal potential) should remain fixed as they have been
determined directly from recordings.


Model invocation
----------------
Use nrngui or nrniv and specify the cell ID as a command-line argument
as follows:

    nrngui -c 'cell=1' init_model.hoc


List of cells
-------------
The cells currently available are:

ID      Name
------------
1       Gormadoc


Model parameters
----------------
Most parameters are found in either the sim_params.hoc file or in the 
per-cell parameter files within the "param_files" directory. The ones in
sim_params.hoc are particularly relevant for global aspects of operation
such as length of simulation, integration method, current clamp injection
parameters, etc. 
