.. _zoo_tb2j:

*****
TB2J
*****

========= ======================================================================
========= ======================================================================
Status    Verified
Links     `Docs <https://tb2j.readthedocs.io/en/latest/>`_,
          `DOI <https://doi.org/10.1016/j.cpc.2021.107938>`_,
          `Github <https://github.com/mailhexu/TB2J>`_
Languages Python
========= ======================================================================

Spin Hamiltonian
================ 


TB2J calculates parameters for the following bilinear spin Hamiltonian:

.. math::
    \mathcal{H}
    =
    -\sum_{i \neq j}
    \mathbf{S}_i
    \cdot
    \mathcal{J}_{ij}
    \cdot
    \mathbf{S}_j
    -
    \sum_i
    \mathbf{S}_i
    \cdot A_i
    \cdot \mathbf{S}_i

where :math:`\mathbf{S}_i` is a classical spin vector at magnetic site :math:`i`
**normalized to 1**; :math:`\mathcal{J}_{ij}` is a 3x3 exchange tensor, that can
be decomposed into physical components

1.   **Isotropic Heisenberg Exchange**

     .. math::
        H_{\text{iso}}
        =
        -\sum_{i \neq j}
        J_{ij}
        (\mathbf{S}_i \cdot \mathbf{S}_j)
   
2.   **Dzyaloshinskii-Moriya Interaction**

     .. math::
        H_{\text{DM}}
        =
        -\sum_{i \neq j}
        \mathbf{D}_{ij}
        \cdot
        (\mathbf{S}_i \times \mathbf{S}_j)
   
3.   **Symmetric Anisotropic Exchange**

     .. math::
        H_{\text{sym-ani}}
        =
        -\sum_{i \neq j}
        \mathbf{S}_i
        \cdot
        \mathcal{J}^{\text{ANI}}_{ij}
        \cdot
        \mathbf{S}_j

     where :math:`\mathcal{J}^{\text{ANI}}_{ij}` is the traceless symmetric part
     of :math:`\mathcal{J}_{ij}`.


Convention
==========

================= ===
================= ===
Spin normalized   yes
Multiple counting yes
================= ===

