.. _zoo_espins:

******
EspinS
******

========= ======================================================================
========= ======================================================================
Status    Draft
Links     `DOI <https://doi.org/10.1016/j.commatsci.2021.110947>`_,
          `Github <https://github.com/nafiserb/ESpinS>`_
Languages Fortran90, Python
========= ======================================================================

Spin Hamiltonian
================ 

.. math::

    \mathcal{H}
    =&
    \underbrace{\sum_{i}\Delta_i\,(\hat{z}_i\cdot\mathbf{S}_i)^2}_{\text{single-ion term}}
    +
    \underbrace{\sum_{i}\mathbf{B}\cdot\mathbf{S}_i}_{\text{magnetic field}}
    -\\&-
    \underbrace{\frac{1}{2}\sum_{i,j}J_{ij}\,\mathbf{S}_i\cdot\mathbf{S}_j}_{\text{exchange term}}
    +
    \underbrace{\frac{1}{2}\sum_{i,j}\mathbf{D}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)}_{\text{Dzyaloshinskii-Moriya term}}
    +\\&+
    \underbrace{\frac{1}{2}\sum_{i,j}B_{ij}\left(\mathbf{S}_i\cdot\mathbf{S}_j\right)^2}_{\text{bi-quadratic term}}

Convention
==========


================= ===
================= ===
Spin normalized   no
Multiple counting yes
================= ===
