<h1 align="center">
<img src="logo-GABI.png" width="300">
</h1><br>

# gABi: graphical Automated Bayesian inference 
Python package to perform Bayesian causal discovery on data, based on probabilistic graphical models.

This package has the following dependencies:

 - decorator 
 - itertools (built-in)
 - matplotlib ( built-in
 - networkx (version  > 2.6)
 - joblib 
 - os
 - pandas
 - pypickle
 - scipy
 - statsmodels
 - tqdm
 - wget
 - pyarrow
 - Apache arrow
 - pybind11
 - dask
 - mpi4py

## Release 0.0
At the moment the gABI package provides the parallel version of the following structure learning
algorithms:

- PC-stable
- kernel-PC

The algorithms depends on dask and MPI for the parallelization, and can be launched on CPUs and GPUs
