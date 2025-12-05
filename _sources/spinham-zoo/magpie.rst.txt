.. _zoo_magpie:

******
Magpie
******

========= ======================================================================
========= ======================================================================
Status    Draft
Links     `Github <https://github.com/ILLGrenoble/magpie>`_
Languages C++20
========= ======================================================================

Spin Hamiltonian
================ 

.. math::

    \mathcal{H}
    =
    (?)
    \sum_i
    \mathbf{S}_i
    \cdot
    \mathbf{A}_i
    \cdot
    \mathbf{S}_i
    -
    \sum_{i \neq j}
    J_{ij}
    \,
    \mathbf{S}_i
    \cdot
    \mathbf{S}_j
    +(?)
    \sum_{i \neq j}
    \mathbf{D}_{ij}
    \cdot
    \left(
    \mathbf{S}_i
    \times
    \mathbf{S}_j
    \right)

where :math:`J_{ij}` is a Heisenberg interaction, :math:`\mathbf{D}_{ij}` is a
Dzyaloshinskii-Moryia interactions and :math:`\mathbf{A}_i` is a single-ion
anisotropy.

Convention
==========

================= ===
================= ===
Spin normalized   ?
Multiple counting ?
================= ===

