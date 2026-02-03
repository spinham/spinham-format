.. _generalization-5:

******************************
Attempt at generalization (#5)
******************************


(Crystal) structure
===================

A Hamiltonian is defined in the real space on a (periodic) structure, for 
example crystal, lattice, molecule, ion, etc. A natural first step is to
formally describe such structure.

First, imagine an arbitrary periodic lattice in :math:`d` dimensions, defined
by the :math:`d` lattice vectors
:math:`\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_d`. Label the cells of
such lattice with the subscript indices :math:`\mu` (or :math:`\mu_1`,
:math:`\mu_2`, and so on if more than one cell index is required). Then,
the sum of the form 

.. math::

    \sum_{\mu_1, \mu_2} \ldots

implies the summation of its argument over all cells of the lattice twice. In
other words, index :math:`\mu_1` runs over all cells of the lattice and for each
value of :math:`\mu_1`, index :math:`\mu_2` also runs over all cells of the
lattice as well.

Second, assume that there are :math:`N` (magnetic) sites in each cell of the
lattice and label each site in the cell with an index :math:`\alpha`
(or :math:`\alpha_1`, :math:`\alpha_2`, and so on if more than one site index is
required).

Then, the position of an arbitrary site in such structure is given by the
radius vector

.. math::

    \mathbf{r}_{\mu; \alpha} = \mathbf{r}_{\mu} + \mathbf{r}_{\alpha}

Finally, the (Cartesian) components are denoted with the superscript indices
:math:`i` (or :math:`i_1`, :math:`i_2`, and so on if more than one component
index is required).

.. math::

    r_{\mu; \alpha}^{i} = r_{\mu}^{i} + r_{\alpha}^{i}

for :math:`i = 1, \ldots, d` (or :math:`i = x, y, z` if :math:`d = 3`).

.. note::

    Component indices can denote generic components of the vector. In this
    section a special case of the Cartesian components is discussed.

    In the next sections the component indices are not limited to Cartesian
    components.

(Magnetic) sites
================

Once the structure is defined, one is ready to discuss the variables that 
act on the system or operators/parameters of the system. For the sake of the 
generality call such object an "entity" and label it with the capital letter
:math:`X`. An interpretation of such entity depends on the context of the
particular term of the Hamiltonian that it enters. For example, it can denote a
spin vector, a spin operator, an angular momentum operator, a Stevens operator,
a Wybourne operator, an external magnetic field and so on.


Among all possible interpretations there are a few common properties of such 
entities.

-   Each entity has :math:`n` components, which is denoted as

    .. math::

        X^{i}

    where :math:`i` runs from :math:`1` to :math:`n`. In the simplest case those
    are Cartesian components (:math:`i = x, y, z`). However, the component
    indices can have other meaning as well.

-   Each entity is associated with exactly one site of the structure, which is
    denoted as

    .. math::

        X_{\mu; \alpha}

.. hint::

    One site can have multiple entities associated with it. Think about an 
    on-site anisotropy as an example.


Interaction parameters
======================

After the structure is defined and populated with individual entities, the next
step is to think about interaction between such entities.

Assume that an interaction parameter connects one or more entities and label it
with the capital letter :math:`V`. As with entities, the interpretation of the
parameter :math:`V` depends on the term of the Hamiltonian, which it enters.
However, there are a few common properties


-   Each interaction parameter has as many independent dimensions as the number
    of the entities that it connects.

-   Each interaction parameter depends on as many pairs of position indices as
    the number of entities it connects. 
    
    
For instance, an interaction parameter

.. math::

    V_{\mu_1, \mu_2, \ldots, \mu_m; \alpha_1, \alpha_2, \ldots, \alpha_k}^{i_1, i_2, \ldots, i_k}


connects :math:`k` entities :math:`X^{i_1}_{\mu_1; \alpha_1}`, ...,
:math:`X^{i_k}_{\mu_k; \alpha_k}`.

.. hint::

    Size of each index :math:`i_1`, ..., :math:`i_k` can be different.

Terms of the Hamiltonian
========================

Before arriving at the general form of the Hamiltonian, consider an arbitrary
term of the Hamiltonian. Let it involve :math:`k` sites (distinct or not)

.. math::

    (\mu_1; \alpha_1), (\mu_2; \alpha_2), \ldots, (\mu_m; \alpha_m)

Each site has an entity associated with it

.. math::
    X_{\mu_1; \alpha_1}^{i_1},
    X_{\mu_2; \alpha_2}^{i_2},
    \ldots,
    X_{\mu_k; \alpha_k}^{i_k}

and the interaction parameter is labeled as

.. math::

    V_{\mu_1, \ldots, \mu_k; \alpha_1, \ldots, \alpha_k}^{i_1, \ldots, i_k}

Then the term of the Hamiltonian that involves those entities is written as

.. math::

    \mathcal{H}_k
    =
    C_k
    \sum_{\substack{\mu_1, \ldots, \mu_k, \\ \alpha_1, \ldots, \alpha_k, \\ i_1, \ldots, i_k}}
    V_{\mu_1, \ldots, \mu_k; \alpha_1, \ldots, \alpha_k}^{i_1, \ldots, i_k}
    \cdot
    X_{\mu_1; \alpha_1}^{i_1}
    \cdot
    X_{\mu_2; \alpha_2}^{i_2}
    \cdot
    \ldots
    \cdot
    X_{\mu_k; \alpha_k}^{i_k}

  
.. note::
    - The constants of the form :math:`C_{k}` are introduced to account for
      different conventions (see :issue:`2`).
    - Any combination of entity's components can have an scalar individual
      parameter associated with it. Those scalar parameters are collected into
      an tensor of the interaction parameter :math:`V_{\mu_1, \ldots, \mu_k;
      \alpha_1, \ldots, \alpha_k}^{i_1, \ldots, i_k}`.

The Hamiltonian can include multiple terms of the same form, with distinct
physical interpretation.
    
The Hamiltonian
===============

Finally, the Hamiltonian is simply written as a sum of all possible terms

.. math::

    \mathcal{H}
    =
    \sum_{k=1}^{\infty}
    \mathcal{H}_k
    =
    \sum_{k=1}^{\infty}
    C_k
    \sum_{\substack{\mu_1, \ldots, \mu_k, \\ \alpha_1, \ldots, \alpha_k, \\ i_1, \ldots, i_k}}
    V_{\mu_1, \ldots, \mu_k; \alpha_1, \ldots, \alpha_k}^{i_1, \ldots, i_k}
    \cdot
    X_{\mu_1; \alpha_1}^{i_1}
    \cdot
    X_{\mu_2; \alpha_2}^{i_2}
    \cdot
    \ldots
    \cdot
    X_{\mu_k; \alpha_k}^{i_k}

.. note::

    The restrictions on the summation over the lattice and site indices are left 
    undefined and considered to be a separate problem (see :issue:`2`). The
    purpose of the general form is to provide a structure for writing down
    the parameter in a file. Said that, the general form implies three things

    - The cell (lattice vectors :math:`\mathbf{a}_1, \ldots, \mathbf{a}_d`) and 
      a set of sites in the cell (positions & labels) are defined file-vide. 
    
    - The set of values for the cell and site indices (:math:`\mu_1, \ldots,
      \mu_k, \alpha_1, \ldots, \alpha_k`) are defined for each individual
      parameter (for each tensor, *not* for each type of tensor).

    - The value of the constant :math:`C_k`, interpretation of each entity
      (position-wise), size of each component index are defined for a group 
      of parameters (for example, parameters of the bilinear exchange, or 
      parameters of the Zeeman term, etc.).


Mapping to the general form
===========================

The pages below discuss the mapping the terms present in the :ref:`"zoo" <zoo>`
to the general form of the Hamiltonian.

.. toctree::
    :maxdepth: 1

    bilinear-exchange
    biquadratic-exchange
    crystal-field
    dipole-dipole
    elastic-energy
    exchange-striction
    magneto-elastic
    on-site-k2
    on-site-k4
    quadruplet-interaction
    two-ion-crystal-field
    zeeman

.. toctree::
    :maxdepth: 1

    on-site-k
