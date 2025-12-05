.. _zoo_vampire:

*******
Vampire
*******

========= ======================================================================
========= ======================================================================
Status    Draft
Links     `Docs <https://vampire.york.ac.uk/>`_
Languages C++
========= ======================================================================

Spin Hamiltonian
================ 


.. math::

    \mathcal{H}
    =
    -\mu_S
    \sum_i
    \mathbf{B} 
    \cdot
    \mathbf{S}_i
    -
    \sum_{i<j (?)}
    \mathbf{S}_i
    \cdot
    \mathbf{J}_{ij}
    \cdot
    \mathbf{S}_j
    +(?)
    \sum_{i<j(?)}
    \mathbf{B}_{ij}
    \left(
        \mathbf{S}_i
        \cdot
        \mathbf{S}_j
    \right)^2
    +
    (?)

where :math:`\mu_S` is (?), :math:`\mathbf{B}` is the external magnetic field,
:math:`\mathbf{J}_{ij}` is full exchange tensor, :math:`\mathbf{B}_{ij}` is 
biquadratic exchange parameter.


Convention
==========

================= ======
================= ======
Spin normalized   yes(?)
Multiple counting no(?)
================= ======

