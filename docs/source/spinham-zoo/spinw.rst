.. _zoo_spinw:

*****
SpinW
*****

========= ======================================================================
========= ======================================================================
Status    Draft
Links     `Docs <https://spinw.org/>`_,
          `DOI <https://doi.org/10.1088/0953-8984/27/16/166002>`_,
          `Github <https://github.com/SpinW>`_
Languages Matlab, Python, Rust
========= ======================================================================

Spin Hamiltonian
================ 

.. math::
    \mathcal{H}
    =
    \mu_B H
    \sum_i
     g_i \mathbf{S}_i
    +
    \sum_i
    \mathbf{S}_i A_i \mathbf{S}_i
    +
    \sum_{i,j}
    \mathbf{S}_i J_{ij} \mathbf{S}_j
    +
    \sum_{i,j}
    B (\mathbf{S}_i \cdot \mathbf{S}_j)^2

where first term is a Zeeman interaction, second is a single-ion anisotropy,
third is a bilinear interaction and fourth is a biquadratic interaction.

Convention
==========

================= ===
================= ===
Spin normalized   ?
Multiple counting yes
================= ===

