.. _zoo_spirit:

******
Spirit
******

========= ======================================================================
========= ======================================================================
Status    Verified
Links     `Docs <https://spirit-code.github.io>`_,
          `DOI <https://doi.org/10.1103/PhysRevB.99.224414>`_,
          `Github <https://github.com/spirit-code/spirit>`_,
          `Zenodo <https://doi.org/10.5281/zenodo.7746551>`_ 
Languages C++/CUDA backend with C/Python API
========= ======================================================================



Spin Hamiltonian
================ 

.. math::
    \mathcal{H}
    =
    \mathcal{H}_{\rm Zeeman}
    +
    \mathcal{H}_{\rm pair}
    +
    \mathcal{H}_{\rm ddi}
    +
    \mathcal{H}_{\rm quad}
    +
    \mathcal{H}_{\rm ani}


Zeeman term
-----------

.. math::
   \mathcal{H}_{\rm Zeeman} = -\sum_i \mu_i \vec{B}\cdot \vec{n}_i

where :math:`\mu_i` is given in units of the Bohr magneton and :math:`\vec{B}` is given in Tesla.


Pair interactions
-----------------

Using Einstein notation for cartesian indices :math:`\alpha` and :math:`\beta`, the pair term is given as

.. math::
    \mathcal{H}_{\rm pair} = -\frac{1}{2}\sum_{i\neq j} J_{ij}^{\alpha\beta} n_i^\alpha n_j^\beta

It splits into the three typical distinctions

.. math::
  J_{ij}^{\alpha\beta}
  = \underbrace{\frac13 J_{ij}^{\gamma\gamma}}_{\text{Heisenberg}}
  + \underbrace{\frac12 (J_{ij}^{\alpha\beta} - J_{ij}^{\beta\alpha})}_{\text{DMI}}
  + \underbrace{\frac12 (J_{ij}^{\alpha\beta} + J_{ij}^{\beta\alpha}) - \frac13 J_{ij}^{\gamma\gamma}}_{\text{two-ion anisotropy}}

where the DMI term is given as a vector and the two-ion anisotropy in terms of 5 components.
Equivalently it can be written as

.. math::
    \mathcal{H}_{\rm pair}
    =
    -\frac{1}{2}\sum_{i\neq j} J_{ij} \vec{n}_i \cdot \vec{n}_j
    -\frac{1}{2}\sum_{i\neq j} \vec{D}_{ij} \cdot (\vec{n}_i \times \vec{n}_j)
    -\frac{1}{2}\sum_{i\neq j} \vec{n}_i \cdot K_{ij} \vec{n}_j

with the matrices :math:`K_{ij}` representing the two-site anisotropy being symmetric and traceless.

The actual definitions for the interaction use what we call pairs.
A pair identifies two atoms in the unit cell by a base index and a translation vector between two unit cells in integer units of the bravais vectors.
This allows minimal definitions for the typically periodic interactions we encounter.

DMI and Heisenberg terms can also be specified in terms of shells (nearest neighbor, next nearest neighbor, etc.), but this definition is converted internally to pairs.


Dipole-dipole interaction
-------------------------

The dipole-dipole interaction reads

.. math::
   \mathcal{H}_{\rm ddi} = \frac{1}{2}\frac{\mu_0}{4\pi} \sum_{i \neq j} \mu_i \mu_j \frac{(\vec{n}_i \cdot \hat{r}_{ij}) (\vec{n}_j\cdot\hat{r}_{ij}) - (\vec{n}_i \cdot \vec{n}_j)}{{r_{ij}}^3}

where :math:`\vec{r}_{ij} := \vec{r}_j - \vec{r}_i` is the distance vector between two sites, :math:`r_{ij}` is the distance between two sites or the norm of the distance vector and :math:`\hat{r}_{ij}` is the normalized distance vector between two sites :math:`i` and :math:`j`.
The distances are calculated in Å, :math:`\mu_i` is given in units of the Bohr magneton and the other units are chosen such that the result is given in meV like the other energies.


Quadruplet interaction
----------------------

.. math::
    \mathcal{H}_{\rm quad} = - \sum_{ijkl} K_{ijkl} (\vec{n}_i \cdot \vec{n}_j)(\vec{n}_k \cdot \vec{n}_l)


Anisotropy interactions
-----------------------

The anisotropy term :math:`\mathcal{H}_{\rm ani}` has three contributions: the uniaxial term, the cubic term and a general biaxial term.
The uniaxial anisotropy can be specified multiple times per site.

.. math::
   \mathcal{H}_{\rm uni} = \sum_j K_j (\hat{K}_j\cdot\vec{n}_j)^2

The cubic anisotropy is given by the expression

.. math::
  \mathcal{H}_{\rm cubic} = - \frac12 \sum_j K_j ([\vec{n}_j]_x^4 + [\vec{n}_j]_y^4 + [\vec{n}_j]_z^4)

This biaxial anisotropy allows specifying arbitrary polynomials in the components of the spin vector

.. math::
  \begin{alignedat}{1}
    \mathcal{H}_{\rm biaxial} & = \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} (1 - (\hat{K}_j^{(1)}\cdot\vec{n}_j)^2)^{n_1} \cdot (\hat{K}_j^{(2)}\cdot\vec{n}_j)^{n_2} \cdot ((\hat{K}_j^{(1)} \times \hat{K}_j^{(2)} ) \cdot\vec{n}_j)^{n_3} \\
                    & =                  \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} \cdot [\sin(\theta_j)]^{2n_1} \cdot [\cos(\varphi_j)\sin(\theta_j)]^{n_2} \cdot [\sin(\varphi_j)\sin(\theta_j)]^{n_3}                           \\
                    & =                  \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} \cdot [\sin(\theta_j)]^{2n_1 + n_2 + n_3} \cdot [\cos(\varphi_j)]^{n_2} \cdot [\sin(\varphi_j)]^{n_3},                                          \\
  \end{alignedat}

it contains the single axis uniaxial anisotropy as a special case, but both can be specified independently.


Additional notes
----------------

While the sums as written here are multiple counting the implementation in terms of pairs is not.
The indices in the sums :math:`i,j,k,l` in these definitions refer to individual sites, but we also recognize a definition of a unit cell that is then repeated periodically for the full system.


Convention
==========

================= ===
================= ===
Spin normalized   yes
Multiple counting yes
================= ===

