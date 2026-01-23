.. _generalization:

*************************
Attempt at generalization
*************************


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

    where :math:`i` runs from :math:`1` to :math:`n`. In the simpliest case those
    are Cartesian components (:math:`i = x, y, z`). However, in some cases those
    can have different meaning.

-   Each entity has a well defined position in the real space.

    .. math::

        X_{\mu; \alpha}

    As each entity is associated with a site, its position is simply the
    position of tha site.

-   Two entities that are associated with two distinct sites commute.

    .. math::

        [X_{\mu_1; \alpha_1}^{i_1}, X_{\mu_2; \alpha_2}^{i_2}] = 0

    if :math:`(\mu_1; \alpha_1) \neq (\mu_2; \alpha_2)`.

In the following whether the indices :math:`(\mu_1; \alpha_1)` and
:math:`(\mu_2; \alpha_2)` are written within the same context it is implied that
they indicate distinct sites:
:math:`(\mu_1; \alpha_1) \neq (\mu_2; \alpha_2)`.


Interaction parameters
======================

Then, an interaction between sites is described by the interaction parameters.
Label such an interaction parameter with the capital letter :math:`V`. Each
interaction parameter connects one or more entities, whilst those entities are
associates with one or more sites. As with entities, the interpretation of the 
parameter :math:`V` depends on the term of the Hamiltonian, which it enters.
However, there are two common properties


-   Each interaction parameter has as many independent dimensions as the number of
    components of the entities that it connects. For example, an interaction
    parameter

    .. math::

        V^{i_1, i_2, \ldots, i_k}

    connects :math:`k` entities.

-   Each interaction parameter depends on as many pairs of position indices
    (cell index and site index) as the number of unique sites that it connects.
    For example, an interaction parameter

    .. math::

        V_{\mu_1, \mu_2, \ldots, \mu_m; \alpha_1, \alpha_2, \ldots, \alpha_m}

    connects :math:`m` unique sites.

.. note::

    Amount of entities and the amount of unique sites can be different. For
    example, an interaction parameter can connect two entities
    :math:`X_{\mu_1; \alpha_1}^{i_1}` and :math:`X_{\mu_1; \alpha_1}^{i_2}` is
    denoted as

    .. math::

        V_{\mu_1; \alpha_1}^{i_1, i_2}

    While an interaction parameter that connects two entities
    :math:`X_{\mu_1; \alpha_1}^{i_1}` and :math:`X_{\mu_2; \alpha_2}^{i_2}` is
    denoted as  

    .. math::

        V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}

Terms of the Hamiltonian
========================

The Hamiltonian itself is constructed with the following properties in mind

- Terms of the Hamiltonian can involve an arbitrary amount of entities.
- Terms of the Hamiltonian can involve an arbitrary amount of unique sites.
- Each combination of components of the entities can have a unique
  interaction parameter associated with it.


Consider an arbitrary term of the Hamiltonian. Let it involve :math:`m` distinct
sites

.. math::

    (\mu_1; \alpha_1), (\mu_2; \alpha_2), \ldots, (\mu_m; \alpha_m)

and :math:`k` entities. Then the interaction parameter for such term is denoted
as

.. math::

    V_{\mu_1, \ldots, \mu_m; \alpha_1, \ldots, \alpha_m}^{i_1, \ldots, i_k}

Now, the first question is - What are the restrictions on the values of :math:`k`
and :math:`m`? The answer is 

-   :math:`k \ge m`.

    As every entity is associated with exactly one site.

-   :math:`k \ne 0` and :math:`m \ne 0`. 

    If the Hamiltonian includes a term that is independent of the entities or 
    does not involve any sites, then such a term either describes the
    environment and not the system or is a constant energy term that can be
    ignored.

With those rules in mind one can sketch a table (cross means that the term is
not possible/considered) for one possible classification of the Hamiltonian's
terms.


.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - :math:`m = 1`
      - :math:`m = 2`
      - :math:`m = 3`
      - :math:`m = 4`
      - :math:`\ldots`
    * - :math:`k = 1`
      - 
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 2`
      - 
      - 
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 3`
      - 
      -
      - 
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 4`
      - 
      -
      - 
      - 
      - :math:`\times`
    * - :math:`\ldots`
      - 
      - 
      - 
      - 
      - 

Unfortunately, one can not simply classify the terms of the Hamiltonian by the
pair :math:`(k, m)`. First counter-example occurs when :math:`k = 4`. Imagine 
two terms that both involve :math:`k = 4` entities and :math:`m = 2` sites 

.. math::

    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_2}
    X_{\mu_2; \alpha_2}^{i_3}
    X_{\mu_2; \alpha_2}^{i_4}
    \qquad
    \text{and}
    \qquad
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_2}
    X_{\mu_1; \alpha_1}^{i_3}
    X_{\mu_2; \alpha_2}^{i_4}

Those two terms are distinct and can not be express one through another.
Therefore, the label :math:`(k, m)` is not sufficient to uniquely identify a
term of the Hamiltonian.

.. hint::

    On the other, hand the terms 

    .. math::

        &V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
        X_{\mu_1; \alpha_1}^{i_1}
        X_{\mu_1; \alpha_1}^{i_2}
        X_{\mu_1; \alpha_1}^{i_3}
        X_{\mu_2; \alpha_2}^{i_4}
        \\

        &V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
        X_{\mu_1; \alpha_1}^{i_1}
        X_{\mu_1; \alpha_1}^{i_2}
        X_{\mu_2; \alpha_2}^{i_3}
        X_{\mu_1; \alpha_1}^{i_4}
        \\

        &V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
        X_{\mu_1; \alpha_1}^{i_1}
        X_{\mu_2; \alpha_2}^{i_2}
        X_{\mu_1; \alpha_1}^{i_3}
        X_{\mu_1; \alpha_1}^{i_4}
        \\

        &V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
        X_{\mu_2; \alpha_2}^{i_1}
        X_{\mu_1; \alpha_1}^{i_2}
        X_{\mu_1; \alpha_1}^{i_3}
        X_{\mu_1; \alpha_1}^{i_4}
        \\

    are equivalent, as two entities associated with two distinct sites commute
    (therefore, all of those four terms can be expressed through the first one
    by re-ordering of the entities and renaming of the indices).

Now the questions are 

- How many distinct terms of the Hamiltonian exist for each :math:`k`?
- How those can be labeled?

To answer those, define a set of numbers :math:`\{n_1, n_2, \ldots, n_m\}`,
where each number :math:`n_j` indicates how many entities are associated with
the site :math:`(\mu_j; \alpha_j)`. As the total amount of entities is :math:`k`,
one gets

.. math::

    \sum_j n_j = k

Then, the first question can be re-formulated as 

- How many integer partitions of an integer :math:`k` exist (see
  |Integer-partition|_)?

The answer is a partition function, that is labeled as :math:`p(k)`. Here are
its values for a few first values of :math:`k`


.. list-table:: 
    :header-rows: 0
    :stub-columns: 1

    * - :math:`k`
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - :math:`\ldots`
    * - :math:`p(k)`
      - 1
      - 2
      - 3
      - 5
      - 7
      - 11
      - :math:`\ldots`

Therefore, the terms of the Hamiltonian can be uniquely labeled by a pair
:math:`(k, l)`, where :math:`k` is the amount of entities and :math:`l` is 
an index of a particular integer partition of the number :math:`k` (with
:math:`l = 1, \ldots, p(k)`). For each such pair define a number :math:`m_{k,l}`,
which indicates how many unique sites are involved in the term :math:`(k, l)`.

.. hint::

    To be exact, pick the ordering on the partitions of an integer :math:`k` to
    be an descending order of sets of integers that specified a partition, while
    each set is ordered in a descending order. Here is an example of such
    ordering



    -   :math:`k = 1`

        ========= =========
        Partition :math:`l`
        ========= =========
        1         1
        ========= =========

    -   :math:`k = 2`

        ========= =========
        Partition :math:`l`
        ========= =========
        2         1
        1 + 1     2
        ========= =========

    -   :math:`k = 3`

        ========= =========
        Partition :math:`l`
        ========= =========
        3         1
        2 + 1     2
        1 + 1 + 1 3
        ========= =========

    -   :math:`k = 4`        

        ============= ========= 
        Partition     :math:`l`
        ============= =========
        4             1
        3 + 1         2
        2 + 2         3
        2 + 1 + 1     4
        1 + 1 + 1 + 1 5
        ============= =========

Redesign a classification table by using the labels :math:`(k, l)` 
(instead of :math:`(k, m)`). As entries of the table put the amount of distinct
sites :math:`m_{k,l}` that are involved in the term.


.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - :math:`l = 1`
      - :math:`l = 2`
      - :math:`l = 3`
      - :math:`l = 4`
      - :math:`l = 5`
      - :math:`\ldots`
    * - :math:`k = 1`
      - 1
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 2`
      - 1
      - 2
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 3`
      - 1
      - 2
      - 3 
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 4`
      - 1
      - 2
      - 2
      - 3
      - 4
      - :math:`\times`
    * - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`

or the repetition numbers :math:`\{n_{l, 1}, \ldots, n_{l, m_{k,l}}\}`


.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - :math:`l = 1`
      - :math:`l = 2`
      - :math:`l = 3`
      - :math:`l = 4`
      - :math:`l = 5`
      - :math:`\ldots`
    * - :math:`k = 1`
      - 1
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 2`
      - 2
      - 1, 1
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 3`
      - 3
      - 2, 1
      - 1, 1, 1 
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 4`
      - 4
      - 3, 1
      - 2, 2
      - 2, 1, 1
      - 1, 1, 1, 1
      - :math:`\times`
    * - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`


The Hamiltonian
===============

Finally, everything is ready to write the Hamiltonian.

The Hamiltonian is a sum over :math:`k` and over :math:`l` 

.. math::

    \mathcal{H}
    =
    \sum_{k=1}^{\infty}
    \sum_{l=1}^{p(k)}
    \mathcal{H}_{k, l}

Before introducing the general form of :math:`\mathcal{H}_{k, l}`, consider a
few examples. 

.. hint::
    The constants of the form :math:`C_{k, l}` are introduced to account for
    different conventions (see :issue:`2`).


k = 1
-----

One case is possible.

-   :math:`l = 1`: :math:`m_{1,1} = 1`, :math:`n_1 = 1`

    .. math::
        
        \mathcal{H}_{1, 1}
        =
        C_{1, 1}
        \sum_{\substack{\mu_1, \\ \alpha_1, \\ i_1}}
        V_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}


k = 2
-----

Two cases are possible.

-   :math:`l = 1`: :math:`m_{2,1} = 1`, :math:`n_1 = 2`

    .. math::
         
        \mathcal{H}_{2, 1}
        =
        C_{2, 1}
        \sum_{\substack{\mu_1, \\ \alpha_1, \\ i_1, i_2}}
        V_{\mu_1; \alpha_1}^{i_1, i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}

-   :math:`l = 2`: :math:`m_{2,2} = 2`, :math:`n_1 = 1`, :math:`n_2 = 1`

    .. math::
       
        \mathcal{H}_{2, 2}
        =
        C_{2, 2}
        \sum_{\substack{\mu_1, \mu_2, \\ \alpha_1, \alpha_2, \\ i_1, i_2}}
        V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_2; \alpha_2}^{i_2}

k = 3
-----

Three cases are possible.

-   :math:`l = 1`: :math:`m_{3,1} = 1`, :math:`n_1 = 3`


    .. math::
         
        \mathcal{H}_{3, 1}
        =
        C_{3, 1}
        \sum_{\substack{\mu_1, \\ \alpha_1, \\ i_1, i_2, i_3}}
        V_{\mu_1; \alpha_1}^{i_1, i_2, i_3}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_1; \alpha_1}^{i_2}
        \cdot
        X_{\mu_1; \alpha_1}^{i_3}  

-   :math:`l = 2`: :math:`m_{3,2} = 2`, :math:`n_1 = 2`, :math:`n_2 = 1`

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

-   :math:`l = 3`: :math:`m_{3,3} = 3`, :math:`n_1 = 1`, :math:`n_2 = 1`, :math:`n_3 = 1`

    .. math::
       
        \mathcal{H}_{3, 3}
        =
        C_{3, 3}
        \sum_{\substack{\mu_1, \mu_2, \mu_3, \\ \alpha_1, \alpha_2, \alpha_3, \\ i_1, i_2, i_3}}
        V_{\mu_1, \mu_2, \mu_3; \alpha_1, \alpha_2, \alpha_3}^{i_1, i_2, i_3}
        \cdot
        X_{\mu_1; \alpha_1}^{i_1}
        \cdot
        X_{\mu_2; \alpha_2}^{i_2}
        \cdot
        X_{\mu_3; \alpha_3}^{i_3}


k = 4
-----

Five cases are possible.

-   :math:`l = 1`: :math:`m_{4,1} = 1`, :math:`n_1 = 4`

    .. math::
         
        \mathcal{H}_{4, 1}
        =
        C_{4, 1}
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

-   :math:`l = 2`: :math:`m_{4,2} = 2`, :math:`n_1 = 3`, :math:`n_2 = 1`

    .. math::
         
        \mathcal{H}_{4, 2}
        =
        C_{4, 2}
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

-   :math:`l = 3`: :math:`m_{4,3} = 2`, :math:`n_1 = 2`, :math:`n_2 = 2`

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

-   :math:`l = 4`: :math:`m_{4,4} = 3`, :math:`n_1 = 2`, :math:`n_2 = 1`, :math:`n_3 = 1`

    .. math::
    
        \mathcal{H}_{4, 4}
        =
        C_{4, 4}
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

-   :math:`l = 5`: :math:`m_{4,5} = 4`, :math:`n_1 = 1`, :math:`n_2 = 1`, :math:`n_3 = 1`, :math:`n_4 = 1`

    .. math::
       
        \mathcal{H}_{4, 5}
        =
        C_{4, 5}
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

Arbitrary k
-----------

Generalizing the examples above, one can write the general form of
:math:`\mathcal{H}_{k, l}` as

.. math::

    \mathcal{H}_{k, l}
    =
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
:math:`k` and :math:`m_{k,l}` is the amount of different sites involved in the
term that corresponds to the integer partition :math:`l` of the number
:math:`k`.

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

The terms of the Hamiltonian, that are discussed above, can be classified as
follows


.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - :math:`l = 1`
      - :math:`l = 2`
      - :math:`l = 3`
      - :math:`l = 4`
      - :math:`l = 5`
      - :math:`\ldots`
    * - :math:`k = 1`
      - :ref:`mapping_crystal-field`,
        :ref:`mapping_crystal-field_ambiguity`,
        :ref:`mapping_magneto-elastic-1-1`,
        :ref:`mapping_zeeman`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 2`
      - :ref:`mapping_crystal-field_ambiguity`, 
        :ref:`mapping_on-site-k2`
      - :ref:`mapping_bilinear-exchange`, 
        :ref:`mapping_dipole-dipole`,  
        :ref:`mapping_exchange_striction`, 
        :ref:`mapping_two-ion-crystal-field`, 
        :ref:`mapping_two-ion-crystal-field_ambiguity`,
        :ref:`mapping_magneto-elastic-2-2`,
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 3`
      - :ref:`mapping_crystal-field_ambiguity`
      - :ref:`mapping_two-ion-crystal-field_ambiguity`
      - 3 
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 4`
      - :ref:`mapping_crystal-field_ambiguity`, 
        :ref:`mapping_on-site-k4`
      - :ref:`mapping_two-ion-crystal-field_ambiguity`
      - :ref:`mapping_biquadratic-exchange`
      - :ref:`mapping_quadruplet-case-1`
      - :ref:`mapping_quadruplet-case-2`
      - :math:`\times`
    * - :math:`\ldots`
      - :ref:`mapping_crystal-field_ambiguity`
      - :ref:`mapping_two-ion-crystal-field_ambiguity`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`

The table below gives an idea of which terms are implemented in each code 
(:math:`^*` indicates that the entry is due to the ambiguity of crystal 
field parameterization, see :ref:`mapping_crystal-field_ambiguity` and
:ref:`mapping_two-ion-crystal-field_ambiguity`)


.. list-table:: 
    :header-rows: 1
    :stub-columns: 1
    :widths: 10 18 18 18 18 18 10

    * - 
      - :math:`l = 1`
      - :math:`l = 2`
      - :math:`l = 3`
      - :math:`l = 4`
      - :math:`l = 5`
      - :math:`\ldots`
    * - :math:`k = 1`
      - :ref:`zoo_magnopy`,
        :ref:`zoo_magpie`,
        :ref:`zoo_mcphase`,
        :ref:`zoo_spinw`
        :ref:`zoo_spirit`
        :ref:`zoo_sunny`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 2`
      - :ref:`zoo_grogu`, :ref:`zoo_jukkr`, :ref:`zoo_magnopy`, :ref:`zoo_magpie`, :ref:`zoo_mcphase`:math:`^*`, :ref:`zoo_spinw`, :ref:`zoo_spirit`, :ref:`zoo_sunny`:math:`^*`, :ref:`zoo_tb2j`
      - :ref:`zoo_grogu`, :ref:`zoo_jukkr`, :ref:`zoo_magnopy`, :ref:`zoo_magpie`, :ref:`zoo_mcphase`, :ref:`zoo_spinw`, :ref:`zoo_spirit`, :ref:`zoo_sunny`, :ref:`zoo_tb2j`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 3`
      - :ref:`zoo_magnopy`, 
        :ref:`zoo_mcphase`:math:`^*`, 
        :ref:`zoo_sunny`:math:`^*`
      - :ref:`zoo_magnopy`, 
        :ref:`zoo_mcphase`:math:`^*`
      - :ref:`zoo_magnopy`
      - :math:`\times`
      - :math:`\times`
      - :math:`\times`
    * - :math:`k = 4`
      - :ref:`zoo_magnopy`, 
        :ref:`zoo_mcphase`:math:`^*`, 
        :ref:`zoo_spirit`, 
        :ref:`zoo_sunny`:math:`^*`
      - :ref:`zoo_magnopy`, 
        :ref:`zoo_mcphase`:math:`^*`
      - :ref:`zoo_magnopy`, 
        :ref:`zoo_spinw`, 
        :ref:`zoo_spirit`
      - :ref:`zoo_magnopy`, 
        :ref:`zoo_spirit`
      - :ref:`zoo_magnopy`, 
        :ref:`zoo_spirit`
      - :math:`\times`
    * - :math:`\ldots`
      - :ref:`zoo_mcphase`:math:`^*`, :ref:`zoo_sunny`:math:`^*`
      - :ref:`zoo_mcphase`:math:`^*`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
      - :math:`\ldots`
