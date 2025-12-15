.. _zoo_magpie:

******
Magpie
******

========= ======================================================================
========= ======================================================================
Status    Verified
Links     `Github <https://github.com/ILLGrenoble/magpie>`_,
          `DOI <https://doi.org/10.5281/zenodo.16180814>`_,
          Paper in preparation,
          `Paper of predecessor software <https://doi.org/10.1016/j.softx.2023.101471>`_
Languages C++20, Python scripting interface
========= ======================================================================

Spin Hamiltonian
================ 

.. math::

    \mathcal{H}
    =
    \sum_i
    \mathbf{S}_i
    \cdot
    \mathbf{A}_i
    \cdot
    \mathbf{S}_i
    +
    \sum_{i \neq j}
    J_{ij}
    \,
    \mathbf{S}_i
    \cdot
    \mathbf{S}_j
    +
    \sum_{i \neq j}
    \mathbf{D}_{ij}
    \cdot
    \left(
    \mathbf{S}_i
    \times
    \mathbf{S}_j
    \right)
    +
    \mu_B H
    \sum_i
    g_i \mathbf{S}_i

where :math:`J_{ij}` is a Heisenberg interaction, :math:`\mathbf{D}_{ij}` is a
Dzyaloshinskii-Moryia interactions and :math:`\mathbf{A}_i` is a single-ion
anisotropy.

Convention
==========

================= ===
================= ===
Spin normalized   no
Multiple counting no
================= ===

