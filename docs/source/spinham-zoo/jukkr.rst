.. _zoo_juKKR:

*****
juKKR
*****

========= ======================================================================
========= ======================================================================
Status    Verified
Links     `Web <https://jukkr.fz-juelich.de>`_
Languages Fortran
========= ======================================================================

Spin Hamiltonian
================ 

.. math::

    \mathcal{H}
    =
    \sum_{i}
    \mathbf{S}_{i}
    \cdot
    \boldsymbol{A}_{i}
    \cdot
    \mathbf{S}_{i}
    -
    \sum_{i,j}
    \mathbf{S}_{i}
    \cdot
    \boldsymbol{J}_{ij}
    \cdot
    \mathbf{S}_{j},

where the first term is a second-order onsite magnetic anisotropy and the second
term is the pairwise interaction between spins, that includes Heisenberg J,
Dzyaloshinskii-Moriya vector and 5 remaining symmetric anisotropic components.

Convention
==========

================= ===
================= ===
Spin normalized   yes
Multiple counting yes
================= ===
