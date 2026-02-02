.. _generalization-4:

******************************
Attempt at generalization (#4)
******************************


(Crystal) structure
===================

A Hamiltonian is defined on a real-space structure (i. e. crystal, lattice,
molecule, ion, etc.). A natural first step is to formally describe such
structure.

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
angular momentum operator, a Stevens operator, a Wybourne operator, an external 
magnetic field and so on.

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

"Extra" variables
=================

Some terms of the Hamiltonian contain special variables, that may not depend on
the site indices. For example, strain tensor in :ref:`zoo_mcphase` or an external
effect, as a magnetic flux density. Such variables 

Those terms include variables, that are expected to be described as entities, 
but are either associated with a crystal as a whole or are uniform for all sites.
Therefore, the association with a particular site is not natural for such 
variables. To account for such variables introduce a special value for 
the indices :math:`(\mu, \alpha)`, for example :math:`(\mu, \alpha) \in \{\_1, \_2, \_3, \dots\}`.

.. note::

    The form of the values — "_<integer>" — is a suggestion. The actual label
    can be decided during the design stage for the details of the format.

Then, such variables can be formally written as entities as well. The indication
of how those terms shall be interpreted shall be designed as a detail of the
format. The importance for the generalized algebraic form is the possibility of
having a special index value.

.. note::

    Consider a Zeeman term (let :math:`g\mu_B = 1`)
    :math:`\sum_{\mu, \alpha, i} B^{i} S_{\mu; \alpha}^{i}`. A spin operator/vector
    is an entity, that have a clear association with a site
    :math:`X^{i}_{\mu; \alpha} \equiv S^i_{\mu; \alpha}`. However, the magnetic
    flux density :math:`B^{i}` is typically uniform for all sites and therefore
    does not have a clear association with a particular site. Using a concept of
    special values for the site indices, one can write
    :math:`X^i_{\_1} \equiv B^i`. Then the Zeeman term can be written as

    .. math::

        \sum_{\mu_1, \alpha_1, \mu_2, \alpha_2, i}
        X^i_{\mu_1, \alpha_1} \cdot X^{i}_{\mu_2; \alpha_2}


    In such a sum one understands that the file would include only blocks with 
    :math:`(\mu_1, \alpha_1) = \_1`, but the algebraic form is written in 
    such a way that :math:`X^i_{\_1}` and :math:`X^{i}_{\mu; \alpha}` are
    treated on equal footing.
    
In the following, the meaning of the word "sites" is extended with such special
value of its indices.

Interaction parameters
======================

Then, an interaction between sites is described by the interaction parameters.
Label such an interaction parameter with the capital letter :math:`V`. Each
interaction parameter connects one or more entities. As with entities, the
interpretation of the parameter :math:`V` depends on the term of the
Hamiltonian, which it enters. However, there are two common properties


-   Each interaction parameter has as many independent dimensions as the number of
    components of the entities that it connects. For example, an interaction
    parameter

    .. math::

        V^{i_1, i_2, \ldots, i_k}

    connects :math:`k` entities.

-   Each interaction parameter depends on as many pairs of position indices 
    and/or labels as the number of entities it connects.

    .. math::

        V_{\mu_1, \mu_2, \ldots, \mu_m; \alpha_1, \alpha_2, \ldots, \alpha_k}

Terms of the Hamiltonian
========================

The Hamiltonian itself is constructed with the following properties in mind

- Terms of the Hamiltonian can involve an arbitrary amount of entities.
- Each combination of components of the entities can have a unique
  interaction parameter associated with it.


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

Then, the interaction parameter that connects those entities is labeled as

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
