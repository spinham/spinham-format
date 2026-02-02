.. _generalization-3:

******************************
Attempt at generalization (#3)
******************************


Structure
=========

Any Hamiltonian is defined on a real-space structure (i. e. crystal, lattice,
molecule, ion, etc.). A natural first step is to formally describe such structure.

First, imagine an arbitrary periodic lattice in d-dimensions, defined by the
:math:`d` lattice vectors :math:`\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_d`.
Label the cells of such lattice with the subscript indices :math:`\mu` (or 
:math:`\mu_1`, :math:`\mu_2`, and so on if more than one cell index is
required). In such way, the sum of the form 

.. math::

    \sum_{\mu_1, \mu_2} \ldots

indicates that its argument is summed over all cells of the lattice twice. In
other words, index :math:`\mu_1` runs over all cells of the lattice and for each
value of :math:`\mu_1`, index :math:`\mu_2` also runs over all cells of the
lattice.

Second, assume that there are :math:`N` (magnetic) sites in each cell of the
lattice. Label each site in the lattice with an index :math:`\alpha`
(or :math:`\alpha_1`, :math:`\alpha_2`, and so on if more than one site index is
required).

With the definitions from above, the position of an arbitrary site in such
structure is defined by the radius vector

.. math::

    \mathbf{r}_{\mu; \alpha} = \mathbf{r}_{\mu} + \mathbf{r}_{\alpha}

Finally, the cartesian components are denoted with the superscript indices
:math:`i` (or :math:`i_1`, :math:`i_2`, and so on if more than one Cartesian
component index is required).

.. math::

    r_{\mu; \alpha}^{i} = r_{\mu}^{i} + r_{\alpha}^{i}

for :math:`i = 1, \ldots, d` (or :math:`i = x, y, z` if :math:`d = 3`).

In the following one shall keep in mind the usual 3D space (:math:`d = 3`).


(Magnetic) sites
================

Once the structure is defined, imagine that each site has an "entity" associated
with it. Label such an entity with the capital letter :math:`X`. The 
interpretation of the letter :math:`X` depends on the term of the Hamiltonian,
which it enters. For example, it can be a spin vector, a spin operator, an
angular momentum operator, a Stevens operator, a Wybourne operator and so on.

Common for all interpretations of the entity :math:`X` are the following properties

-   Each entity have :math:`n` components.

    .. math::

        X^{i}

    where :math:`i` runs from :math:`1` to :math:`n`. In the simplest case those
    are Cartesian components (:math:`i = x, y, z`). However, in some cases those
    can have different meaning.

-   Each entity has a well defined position in the real space.

    .. math::

        X_{\mu; \alpha}

    As each entity is associated with a site, its position is simply the
    position of tha site.

Other entities
==============

In addition to the entities associated with the magnetic sites, introduce a
separate type of entity that have no dependency on the site indices (for example,
external magnetic field or strain tensor). Label such an entity with the capital
letter :math:`Y`. 

Common for all interpretations of the entity :math:`Y` are the following properties

-   Each entity have :math:`m` components.

    .. math::

        Y^{j}

    where :math:`j` runs from :math:`1` to :math:`m`. In the simplest case those
    are Cartesian components (:math:`j = x, y, z`). However, in some cases those
    can have different meaning.

-   Each entity has a **label** (no an index). The meaning of that label depends
    on the interpretation of the entity :math:`Y`. The purpose of that label is
    to distinguish between multiple entities of the same type. An integer 
    number is a good choice for such label.

    .. math::

        Y_1

.. note::

    Key difference between entities of type :math:`X` and :math:`Y` is that 
    a summation over the site indices for entities of type :math:`X` is assumed,
    while no summation over the labels for entities of type :math:`Y` is allowed.


Interaction parameters
======================

Then, an interaction between sites is described by the interaction parameters.
Label such an interaction parameter with the capital letter :math:`V`. Each
interaction parameter connects one or more entities of arbitrary type. As with
entities, the interpretation of the parameter :math:`V` depends on the term of
the Hamiltonian, which it enters. However, there are two common properties


-   Each interaction parameter has as many independent dimensions as the number of
    components of the entities that it connects. For example, an interaction
    parameter

    .. math::

        V^{j_1, j_2, \ldots, j_l, i_1, i_2, \ldots, i_k}

    connects :math:`l` entities of the type :math:`Y` and :math:`k` entities of
    the type :math:`X`.

-   Each interaction parameter depends on as many pairs of position indices 
    and/or labels as the number of entities it connects.

    .. math::

        V_{1, 2, \ldots, l; \mu_1, \mu_2, \ldots, \mu_m; \alpha_1, \alpha_2, \ldots, \alpha_k}

    connects :math:`l` sites of the type :math:`Y` and :math:`k` sites of the type
    :math:`X`.


Terms of the Hamiltonian
========================

The Hamiltonian itself is constructed with the following properties in mind

- Terms of the Hamiltonian can involve an arbitrary amount of entities.
- Each combination of components of the entities can have a unique
  interaction parameter associated with it.
- Entities of the type :math:`Y` are always written to the left of the entities
  of the type :math:`X` in each term of the Hamiltonian.


Consider an arbitrary term of the Hamiltonian. Let it involve :math:`k` sites
(distinct or not)

.. math::

    (\mu_1; \alpha_1), (\mu_2; \alpha_2), \ldots, (\mu_m; \alpha_m)

Each site has an entity associated with it

.. math::
    X_{\mu_1; \alpha_1}^{i_1},
    X_{\mu_2; \alpha_2}^{i_2},
    \ldots,
    X_{\mu_k; \alpha_k}^{i_k}

In addition, let it involve :math:`l` entities of the type :math:`Y`

.. math::
    Y_{1}^{j_1},
    Y_{2}^{j_2},
    \ldots,
    Y_{l}^{j_l}

Then, the interaction parameter that connects those entities is labeled as

.. math::

    V_{1, 2, \ldots, l; \mu_1, \ldots, \mu_k; \alpha_1, \ldots, \alpha_k}^{j_1, \ldots, j_l, i_1, \ldots, i_k}

and the term of the Hamiltonian that involves those entities is written as

.. math::

    \mathcal{H}_k
    =
    C_{l, k}
    \sum_{\substack{\mu_1, \ldots, \mu_k, \\ \alpha_1, \ldots, \alpha_k, \\ j_1, \ldots, j_l, \\i_1, \ldots, i_k}}
    V_{1, 2, \ldots, l; \mu_1, \ldots, \mu_k; \alpha_1, \ldots, \alpha_k}^{j_1, \ldots, j_l, i_1, \ldots, i_k}
    \cdot
    Y_{1}^{j_1}
    \cdot
    \ldots
    \cdot
    Y_{l}^{j_l}
    \cdot
    X_{\mu_1; \alpha_1}^{i_1}
    \cdot
    \ldots
    \cdot
    X_{\mu_k; \alpha_k}^{i_k}

  
.. hint::
    The constants of the form :math:`C_{k}` are introduced to account for
    different conventions (see :issue:`2`).

The Hamiltonian can include multiple terms of the same form, with distinct
physical origin.
    


The Hamiltonian
===============

Finally, everything is ready to write the Hamiltonian, which simply a sum over
all possible terms of the form from above

.. math::

    \mathcal{H}
    =
    \sum_{l=1}^{\infty}
    \sum_{k=1}^{\infty}
    \mathcal{H}_{l, k}
    =
    C_{l, k}
    \sum_{\substack{\mu_1, \ldots, \mu_k, \\ \alpha_1, \ldots, \alpha_k, \\ j_1, \ldots, j_l, \\i_1, \ldots, i_k}}
    V_{1, 2, \ldots, l; \mu_1, \ldots, \mu_k; \alpha_1, \ldots, \alpha_k}^{j_1, \ldots, j_l, i_1, \ldots, i_k}
    \cdot
    Y_{1}^{j_1}
    \cdot
    \ldots
    \cdot
    Y_{l}^{j_l}
    \cdot
    X_{\mu_1; \alpha_1}^{i_1}
    \cdot
    \ldots
    \cdot
    X_{\mu_k; \alpha_k}^{i_k}

.. note::

    By convention, the entities of the type :math:`Y` are always written to the
    left of the entities of the type :math:`X` in each term of the Hamiltonian.
    Moreover, the labels and component indices of the entities of the type
    :math:`Y` are always written to the left of the position indices and
    component indices of the entities of the type :math:`X` in the interaction
    parameters.


Mapping to the general form
===========================

Now, consider the terms of the Hamiltonian that are present in the
:ref:`"zoo" <zoo>` and map each one of them to the general form above.

The pages below discuss the mapping of each term in detail.

.. toctree::
    :maxdepth: 1

    bilinear-exchange
    biquadratic-exchange
    crystal-field
    dipole-dipole
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

Below is the table that classifies the terms in the matrix of :math:`(l, k)`.



.. list-table:: 
    :header-rows: 1
    :stub-columns: 1
    :widths: 10 45 35 10

    *   - 
        - :math:`l = 0`
        - :math:`l = 1`
        - :math:`\ldots`
    *   - :math:`k = 0`
        - 
        - 
        - 
    *   - :math:`k = 1`
        - :ref:`mapping-3_crystal-field`
        - :ref:`mapping-3_magneto-elastic-1`,
          :ref:`mapping-3_zeeman`
        - :math:`\ldots`
    *   - :math:`k = 2`
        - :ref:`mapping-3_bilinear-exchange`,
          :ref:`mapping-3_dipole-dipole`,
          :ref:`mapping-3_magneto-elastic-2`,
          :ref:`mapping-3_on-site-k2`,
          :ref:`mapping-3_two-ion-crystal-field`
        - :ref:`mapping-3_exchange_striction`
        - :math:`\ldots`
    *   - :math:`k = 3`
        -
        -
        - :math:`\ldots`
    *   - :math:`k = 4`
        - :ref:`mapping-3_biquadratic-exchange`,
          :ref:`mapping-3_on-site-k4`,
          :ref:`mapping-3_quadruplet`
        -
        - :math:`\ldots`
    *   - :math:`\ldots`
        - :math:`\ldots`
        - :math:`\ldots`
        - :math:`\ldots`
