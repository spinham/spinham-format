.. _generalization:

*************************
Attempt at generalization
*************************


Structure
=========

First let us describe a real-space structure on which the Hamiltonian is
defined.

Imagine an arbitrary periodic lattice in d-dimensions, defined by the 
lattice vectors :math:`\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_d`. Let us
label unit cells of such lattice with the subscript indices :math:`\mu` (or
:math:`\mu_1`, :math:`\mu_2`, and so on if we need more that one unit cell
index). In such way, the sum of the form 

.. math::

    \sum_{\mu_1, \mu_2} \ldots

indicate that its argument is summed over all unit cell of the lattice twice,
i. e. :math:`\mu_1` runs over all unit cells of the lattice and for each value
of :math:`\mu_1`, index :math:`\mu_2` also runs over all unit cells of the
lattice.

Then, let us assume that there are :math:`N` magnetic sites in each unit cell, 
which we label with the subscript indices :math:`\alpha` (or :math:`\alpha_1`,
:math:`\alpha_2`, and so on if we need more that one magnetic site index).

Then the position of the magnetic site in such structure is defined by the 
radius vector

.. math::

    \mathbf{r}_{\mu; \alpha} = \mathbf{r}_{\mu} + \mathbf{r}_{\alpha}

Finally, let us always denote cartesian components (or other component with more
complex meaning) with the superscript indices :math:`i` (or :math:`i_1`,
:math:`i_2`, and so on if we need more that one component index). Then the
formula above can be rewritten as

.. math::

    r_{\mu; \alpha}^{i} = r_{\mu}^{i} + r_{\alpha}^{i}

for :math:`i = 1, \ldots, d` (or :math:`i = x, y, z` if :math:`d = 3`).


Magnetic sites
==============

There is an entity associated with each magnetic site. Let us denote such an
entity with the letter :math:`X`. The interpretation of the letter :math:`X`
depends on the term of the Hamiltonian (i. e. it can be a spin vector, spin
operator, angular momentum operator, Stevens operator, Wybourne operator, etc.). 
For now, we assume that this entity has :math:`d` cartesian components (or 
amount of other components with more complex meaning). Therefore, we denote it

.. math::

    X_{\mu; \alpha}^{i}

where index :math:`\mu` indicates the unit cell, index :math:`\alpha` indicates
magnetic site within the unit cell and index :math:`i` indicates the (cartesian)
component of the entity.

One general assumption is made about the entities: if :math:`(\mu_1; \alpha_1) \neq
(\mu_2; \alpha_2)`, then entities :math:`X_{\mu_1; \alpha_1}^{i_1}` and
:math:`X_{\mu_2; \alpha_2}^{i_2}` commute. This assumption seems to be fulfilled
for all possible interpretations of the entity :math:`X`, that we consider.

Interaction parameters
======================

Interaction parameters connect one or more entities. We note an interaction
parameter as :math:`V`. An interaction parameter has as many component indices
as the number of entities that it connects. Interaction parameter depend on as
many unit cell and magnetic site indices as the number of unique sites that it
connects.

For example, the interaction parameter that connects two entities
:math:`X_{\mu_1; \alpha_1}^{i_1}` and :math:`X_{\mu_2; \alpha_2}^{i_2}` is
denoted as

.. math::

    V_{\mu_1, \mu_2; \alpha_1, \alpha_2; \alpha_2}^{i_1, i_2}

and an interaction parameter that connects two entities
:math:`X_{\mu_1; \alpha_1}^{i_1}` and :math:`X_{\mu_1; \alpha_1}^{i_2}` is
denoted as

.. math::

    V_{\mu_1; \alpha_1}^{i_1, i_2}


.. note::

    Due to the translational invariance of the underlying lattice, the 
    interaction parameter would actually depend on :math:`\mu_2 - \mu_1` in the 
    first example and would not depend on :math:`\mu_1` in the second example.

    Formally, this symmetry can be encoded by defining the relative unit cell index
    as :math:`\nu_i = \mu_i - \mu_1` and updating the notation as

    .. math::

        \sum_{\mu_1, \mu_2}
        &\rightarrow
        \sum_{\mu_1, \nu_2}
        \\
        X_{\mu_1; \alpha_1}^{i_1}
        &\rightarrow
        X_{\mu_1; \alpha_1}^{i_1}
        \\
        X_{\mu_2; \alpha_2}^{i_2}
        &\rightarrow
        X_{\mu_1 + \nu_2; \alpha_2}^{i_2}
        \\
        V_{\mu_1, \mu_2; \alpha_1, \alpha_2; \alpha_2}^{i_1, i_2}
        &\rightarrow
        V_{\nu_2; \alpha_1, \alpha_2}^{i_1, i_2}
        \\
        V_{\mu_1; \alpha_1}^{i_1, i_2}
        &\rightarrow
        V_{\alpha_1}^{i_1, i_2}

    However, for the sake of clarity we would not do that here.

Terms of the Hamiltonian
========================

To systematize the terms of the Hamiltonian, one can map them to a 
2D-grid, where first axis indicates the number of different magnetic sites that
are involved in the term (:math:`n_{sites} \equiv m`), and the second axis
indicates the number of entities that are multiplied together in the term
(:math:`n_{entities} \equiv k`).

Before drawing such a table, let us deduce a couple of simplification rules.

- :math:`n_{entities}` cannot be bigger than :math:`n_{sites}`.

  As every entity is associated with a magnetic site.

- :math:`n_{entities} = 0` is not considered in the Hamiltonian. 

  Part of the Hamiltonian that does not depend on the entities do not describe
  the physical effect that is encoded in the entities. In other words, it is a
  constant energy term, that can be ignored.

- :math:`n_{sites} = 0` is not considered in the Hamiltonian.

  The term that does not involve any magnetic sites do not describe the physical
  system that we consider. In other words, it is a constant energy term, that
  can be ignored.

With those rules in mind one can sketch the table, without any terms filled in
(cross means that the term is not possible/considered)


.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - :math:`n_{sites} = 0`
      - :math:`n_{sites} = 1`
      - :math:`n_{sites} = 2`
      - :math:`n_{sites} = 3`
      - :math:`n_{sites} = 4`
      - :math:`\ldots`
    * - :math:`n_{entities} = 0`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 1`
      - :math:`\times`
      - 
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 2`
      - :math:`\times`
      - 
      - 
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 3`
      - :math:`\times`
      - 
      -
      - 
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 4`
      - :math:`\times`
      - 
      -
      - 
      - 
      - :math:`\times`
    * - :math:`\ldots`
      - :math:`\times`
      - 
      - 
      - 
      - 
      - 

The table will be filled later, first let us sketch the generic term of the
Hamiltonian.

General term of the Hamiltonian
===============================

Now everything is ready to sketch the generic term of the Hamiltonian. 

Let the term involve :math:`n_{sites} \equiv m` different magnetic sites

.. math::

    (\mu_1; \alpha_1), (\mu_2; \alpha_2), \ldots, (\mu_m; \alpha_m)

and :math:`n_{entities} \equiv k` entities (:math:`k \geq m`). Then the
interaction parameter that connects those entities is

.. math::

    V_{\mu_1, \ldots, \mu_m; \alpha_1, \ldots, \alpha_m}^{i_1, \ldots, i_k}

Before we introduce the general form of the Hamiltonian, let us give a few
examples for different values of :math:`k`.

k = 1
-----

There is one case.

-   :math:`m = 1`, the term can be written as

    .. math::
        
        \mathcal{H}_{1, 1}
        =
        C_{1, 1}
        \sum_{\substack{\mu_1, \\ \alpha_1, \\ i_1}}
        V_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}

The constant :math:`C_{1, 1}` accounts for different conventions (see
:issue:`2`).


k = 2
-----

There are two cases.

-   :math:`m = 2`: :math:`n_1 = 1`, :math:`n_2 = 1`

    .. math::
       
        \mathcal{H}_{2, 1}
        =
        C_{2, 1}
        \sum_{\substack{\mu_1, \mu_2, \\ \alpha_1, \alpha_2, \\ i_1, i_2}}
        V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_2; \alpha_2}^{i_2}

-   :math:`m = 1`: :math:`n_1 = 2`

    .. math::
         
        \mathcal{H}_{2, 2}
        =
        C_{2, 2}
        \sum_{\substack{\mu_1, \\ \alpha_1, \\ i_1, i_2}}
        V_{\mu_1; \alpha_1}^{i_1, i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}

k = 3
-----

There are three cases.

-   :math:`m = 3`: :math:`n_1 = 1`, :math:`n_2 = 1`, :math:`n_3 = 1`

    .. math::
       
        \mathcal{H}_{3, 1}
        =
        C_{3, 1}
        \sum_{\substack{\mu_1, \mu_2, \mu_3, \\ \alpha_1, \alpha_2, \alpha_3, \\ i_1, i_2, i_3}}
        V_{\mu_1, \mu_2, \mu_3; \alpha_1, \alpha_2, \alpha_3}^{i_1, i_2, i_3}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_2; \alpha_2}^{i_2}
        \cdot
        X_{\mu_3; \alpha_3}^{i_3}

-   :math:`m = 2`: :math:`n_1 = 2`, :math:`n_2 = 1` (or :math:`n_1 = 1`, :math:`n_2 = 2`)

    .. math::
    
        \mathcal{H}_{3, 2}
        =
        C_{3, 2}
        \sum_{\substack{\mu_1, \mu_2, \\ \alpha_1, \alpha_2, \\ i_1, i_2, i_3}}
        V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_2; \alpha_2}^{i_2}
        \cdot
        X_{\mu_2; \alpha_2}^{i_3}

-   :math:`m = 1`: :math:`n_1 = 3`


    .. math::
         
        \mathcal{H}_{3, 3}
        =
        C_{3, 3}
        \sum_{\substack{\mu_1, \\ \alpha_1, \\ i_1, i_2, i_3}}
        V_{\mu_1; \alpha_1}^{i_1, i_2, i_3}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_3}  


k = 4
-----

There are five (not four!) cases.

-   :math:`m = 4`: :math:`n_1 = 1`, :math:`n_2 = 1`, :math:`n_3 = 1`, :math:`n_4 = 1`

    .. math::
       
        \mathcal{H}_{4, 1}
        =
        C_{4, 1}
        \sum_{\substack{\mu_1, \mu_2, \mu_3, \mu_4, \\ \alpha_1, \alpha_2, \alpha_3, \alpha_4, \\ i_1, i_2, i_3, i_4}}
        V_{\mu_1, \mu_2, \mu_3, \mu_4; \alpha_1, \alpha_2, \alpha_3, \alpha_4}^{i_1, i_2, i_3, i_4}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_2; \alpha_2}^{i_2}
        \cdot
        X_{\mu_3; \alpha_3}^{i_3}
        \cdot
        X_{\mu_4; \alpha_4}^{i_4}

-   :math:`m = 3`: :math:`n_1 = 2`, :math:`n_2 = 1`, :math:`n_3 = 1` (and permutations)

    .. math::
    
        \mathcal{H}_{4, 2}
        =
        C_{4, 2}
        \sum_{\substack{\mu_1, \mu_2, \mu_3, \\ \alpha_1, \alpha_2, \alpha_3, \\ i_1, i_2, i_3, i_4}}
        V_{\mu_1, \mu_2, \mu_3; \alpha_1, \alpha_2, \alpha_3}^{i_1, i_2, i_3, i_4}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}
        \cdot
        X_{\mu_2; \alpha_2}^{i_3}
        \cdot
        X_{\mu_3; \alpha_3}^{i_4}

-   :math:`m = 2`: :math:`n_1 = 2`, :math:`n_2 = 2`

    .. math::
         
        \mathcal{H}_{4, 3}
        =
        C_{4, 3}
        \sum_{\substack{\mu_1, \mu_2, \\ \alpha_1, \alpha_2, \\ i_1, i_2, i_3, i_4}}
        V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}
        \cdot
        X_{\mu_2; \alpha_2}^{i_3}
        \cdot
        X_{\mu_2; \alpha_2}^{i_4}

-   :math:`m = 2`: :math:`n_1 = 3`, :math:`n_2 = 1` (and permutations)

    .. math::
         
        \mathcal{H}_{4, 4}
        =
        C_{4, 4}
        \sum_{\substack{\mu_1, \mu_2, \\ \alpha_1, \alpha_2, \\ i_1, i_2, i_3, i_4}}
        V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_3}
        \cdot
        X_{\mu_2; \alpha_2}^{i_4}

-   :math:`m = 1`: :math:`n_1 = 4`

    .. math::
         
        \mathcal{H}_{4, 5}
        =
        C_{4, 5}
        \sum_{\substack{\mu_1, \\ \alpha_1, \\ i_1, i_2, i_3, i_4}}
        V_{\mu_1; \alpha_1}^{i_1, i_2, i_3, i_4}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_3}
        \cdot
        X_{\mu_1; \alpha_1}^{i_4}

General case
------------


As one can see, the number of cases behaves as a
number of integer partitions of :math:`k` (see |Integer-partition|_), which we
denote as :math:`p(k)`. This fact can be explained as follows.

The number of entities :math:`k` have to be larger or equal than the number of
sites :math:`m`. Let us define a set of numbers :math:`\{n_1, n_2, \ldots, n_m\}`,
where each number :math:`n_j` indicates how many entities are associated with
site :math:`(\mu_j; \alpha_j)`. Then the following conditions have to be fulfilled

.. math::

    \sum_j n_j = k

integer partition function counts the amount of sets
:math:`\{n_1, n_2, \ldots, n_m\}` that satisfy the condition above.



Therefore, in the general form the pre-factors can be
written as

.. math::

    C_{k, l}
    
where  :math:`l = 1, \ldots, p(k)`. Finally, the Hamiltonian can be written as

.. math::

    \mathcal{H}
    =
    \sum_{k=1}^{\infty}
    \sum_{l=1}^{p(k)}
    C_{k, l}
    \sum_{\substack{\mu_1, \ldots, \mu_{m_{k,l}}, \\ \alpha_1, \ldots, \alpha_{m_{k,l}}, \\ i_1, \ldots, i_k}}
    V_{\mu_1, \ldots, \mu_{m_{k,l}}; \alpha_1, \ldots, \alpha_{m_{k,l}}}^{i_1, \ldots, i_k}
    \cdot
    \Biggl(
        X_{\mu_1; \alpha_1}^{i_1}
    \cdot
    \ldots
    \cdot
        X_{\mu_1; \alpha_1}^{i_{n_{l,1}}}
    \Biggr)
    \cdot
    \ldots
    \cdot
    \Biggl(
        X_{\mu_{m_{k,l}}; \alpha_{m_{k,l}}}^{i_{k - n_{l,m_{k,l}} + 1}}
    \cdot
    \ldots
    \cdot
        X_{\mu_{m_{k,l}}; \alpha_{m_{k,l}}}^{i_k}
    \Biggr)

where :math:`n_{l, j}` indicates how many entities are associated with site
:math:`(\mu_j; \alpha_j)` in the integer partition :math:`l` of the number
:math:`k` and :math:`m_{k,l}` is the amount of different magnetic sites
involved in the term that corresponds to the integer partition :math:`l` of
the number :math:`k`.

Mapping to the general form
===========================

Finally, lets consider the terms of the Hamiltonian that are present in the
:ref:`"zoo" <zoo>` and map each one of them to the general form above.

.. toctree::
    :maxdepth: 1

    zeeman
    on-site-k2
    on-site-k4
    on-site-k
    dipole-dipole
    bilinear-exchange
    exchange-striction
    biquadratic-exchange
    quadruplet-interaction
    crystal-field
    two-ion-crystal-field

After those exercises in mapping one can fill the table by placing the type of
interactions in it


.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - :math:`n_{sites} = 0`
      - :math:`n_{sites} = 1`
      - :math:`n_{sites} = 2`
      - :math:`n_{sites} = 3`
      - :math:`n_{sites} = 4`
      - :math:`\ldots`
    * - :math:`n_{entities} = 0`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 1`
      - :math:`\times`
      - :ref:`mapping_zeeman`, :ref:`mapping_on-site-k`, :ref:`mapping_crystal-field`, :ref:`mapping_crystal-field_ambiguity`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 2`
      - :math:`\times`
      - :ref:`mapping_on-site-k2`, :ref:`mapping_on-site-k`, :ref:`mapping_crystal-field_ambiguity`
      - :ref:`mapping_bilinear-exchange`, :ref:`mapping_dipole-dipole`, :ref:`mapping_exchange_striction`, :ref:`mapping_two-ion-crystal-field`, :ref:`mapping_two-ion-crystal-field_ambiguity`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 3`
      - :math:`\times`
      - :ref:`mapping_on-site-k`, :ref:`mapping_crystal-field_ambiguity`
      - :ref:`mapping_two-ion-crystal-field_ambiguity`
      - 
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 4`
      - :math:`\times`
      - :ref:`mapping_on-site-k4`, :ref:`mapping_on-site-k`, :ref:`mapping_crystal-field_ambiguity`
      - :ref:`mapping_biquadratic-exchange`, :ref:`mapping_two-ion-crystal-field_ambiguity`
      - :ref:`mapping_quadruplet-case-1`
      - :ref:`mapping_quadruplet-case-2`
      - :math:`\times`
    * - :math:`\ldots`
      - :math:`\times`
      - :ref:`mapping_on-site-k`, :ref:`mapping_crystal-field_ambiguity`
      - :ref:`mapping_two-ion-crystal-field_ambiguity`
      - 
      -
      -


or by placing the code names in the cells where the code has some term
implemented (:math:`^*` means that the entry is due to the ambiguity o
f crystal 
field parameterization, see :ref:`mapping_crystal-field_ambiguity` and
:ref:`mapping_two-ion-crystal-field_ambiguity`)



.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - :math:`n_{sites} = 0`
      - :math:`n_{sites} = 1`
      - :math:`n_{sites} = 2`
      - :math:`n_{sites} = 3`
      - :math:`n_{sites} = 4`
      - :math:`\ldots`
    * - :math:`n_{entities} = 0`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 1`
      - :math:`\times`
      - :ref:`zoo_magnopy`, :ref:`zoo_magpie`, :ref:`zoo_mcphase`, :ref:`zoo_spinw`, :ref:`zoo_spirit`, :ref:`zoo_sunny`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 2`
      - :math:`\times`
      - :ref:`zoo_grogu`, :ref:`zoo_jukkr`, :ref:`zoo_magnopy`, :ref:`zoo_magpie`, :ref:`zoo_mcphase`:math:`^*`, :ref:`zoo_spinw`, :ref:`zoo_spirit`, :ref:`zoo_sunny`:math:`^*`, :ref:`zoo_tb2j`
      - :ref:`zoo_grogu`, :ref:`zoo_jukkr`, :ref:`zoo_magnopy`, :ref:`zoo_magpie`, :ref:`zoo_mcphase`, :ref:`zoo_spinw`, :ref:`zoo_spirit`, :ref:`zoo_sunny`, :ref:`zoo_tb2j`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 3`
      - :math:`\times`
      - :ref:`zoo_magnopy`, :ref:`zoo_mcphase`:math:`^*`, :ref:`zoo_spirit`, :ref:`zoo_sunny`:math:`^*`
      - :ref:`zoo_magnopy`
      - :ref:`zoo_magnopy`
      - :math:`\times`
      - :math:`\times`
    * - :math:`n_{entities} = 4`
      - :math:`\times`
      - :ref:`zoo_magnopy`, :ref:`zoo_mcphase`:math:`^*`, :ref:`zoo_spirit`, :ref:`zoo_sunny`:math:`^*`
      - :ref:`zoo_magnopy`, :ref:`zoo_spinw`, :ref:`zoo_spirit`
      - :ref:`zoo_magnopy`, :ref:`zoo_spirit`
      - :ref:`zoo_magnopy`, :ref:`zoo_spirit`
      - :math:`\times`
    * - :math:`\ldots`
      - :math:`\times`
      - :ref:`zoo_magnopy`, :ref:`zoo_mcphase`:math:`^*`, :ref:`zoo_spirit`, :ref:`zoo_sunny`:math:`^*`
      - :ref:`zoo_magnopy`
      - :ref:`zoo_magnopy`
      - :ref:`zoo_magnopy`
      - :ref:`zoo_magnopy`








