.. _zoo_grogu:

*****
GROGU
*****

========= ======================================================================
========= ======================================================================
Status    Verified
Links     `Docs <https://grogupy.readthedocs.io/en/stable/>`_,
          `DOI <https://doi.org/10.1103/PhysRevB.108.214418>`_,
          `Zenodo <https://zenodo.org/records/17459345>`_
Languages Python
========= ======================================================================

Spin Hamiltonian
================ 

.. math::

    \mathcal{H}
    =
    \frac{1}{2}
    \sum_{i\neq j}
    \boldsymbol{e}_{i}
    \cdot
    \boldsymbol{J}_{ij}
    \cdot
    \boldsymbol{e}_{j}
    + 
    \sum_{i}
    \boldsymbol{e}_{i}
    \cdot
    \boldsymbol{K}_{i}
    \cdot
    \boldsymbol{e}_{i}, 

where :math:`\boldsymbol{e}_{i} = 1 / (\hbar S_i) \boldsymbol{S}_{i}` is a unit
vector of the angular momentum vector and :math:`\boldsymbol{J}_{ij}`, and
:math:`\boldsymbol{K}_{i}` are the exchange and on-site anisotropy tensors
respectively.

Convention
==========


================= ===
================= ===
Spin normalized   yes
Multiple counting yes
================= ===
