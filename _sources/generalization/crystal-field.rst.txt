.. _mapping_crystal-field:

*************
Crystal field
*************

Crystal field terms involve one site and either one or :math:`k` entities
(depending on the mapping procedure choice). Consider case with one entity as a
preferred mapping scheme. Then, it can be expressed via the term
:math:`\mathcal{H}_{1, 1}`.

- :math:`k = 1`
- :math:`l = 1`
- :math:`m_{1,1} = 1`

.. math::

    \mathcal{H}_{1,1}
    =
    C_{1, 1}
    \sum_{\mu_1, \alpha_1, i_1}
    V_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_1}

The summary of the mapping for each code is given in the table below.

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_mcphase` (v1)
        - :ref:`zoo_mcphase` (v2)
        - :ref:`zoo_sunny`
    *   - :math:`\mathcal{H}`
        - .. math::
            \hat{\mathcal{H}}
            =
            \sum_n
            \sum_{lm}
            B_l^m
            \hat{O}_{lm}(\mathbf{J}^n)
        - .. math::
            \hat{\mathcal{H}}
            =  
            \sum_n
            \sum_{lm}
            L_l^m(n)
            \hat{T}_{lm}^{n}
        - .. math::
            \mathcal{H}
            =
            \sum_{i}\sum_{k,q}
            c_{i,k,q}
            \mathcal{O}_{k,q}
            (\mathbf{S}_{i})
    *   - Indices renaming
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`(l,m) \rightarrow i_1`
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`(l,m) \rightarrow i_1`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`(k,q) \rightarrow i_1`
    *   - :math:`C_{4, 3}`
        - 1
        - 1
        - 1
    *   - :math:`V_{\mu_1; \alpha_1}^{i_1}`
        - :math:`B^{i_1}`
        - :math:`L^{i_1}(\mu_1, \alpha_1)`
        - :math:`c_{\mu_1, \alpha_1, i_1}`
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`\hat{O}_{i_1}(\mathbf{J}^{\mu_1, \alpha_1})`
        - :math:`\hat{T}_{i_1}^{\mu_1, \alpha_1}`
        - :math:`\mathcal{O}_{i_1}(\mathbf{S}_{\mu_1, \alpha_1})`

.. note::

    -   Pairs of indices :math:`(l,m)` or :math:`(k,q)` run over the finite set
        of the sets of two integers. Therefore, they can be enumerated with a  
        single integer and mapped to the index :math:`i_1`.
       
.. _mapping_crystal-field_ambiguity:

Crystal field (ambiguity)
-------------------------

Alternatively, the crystal field term can be mapped to the terms with one site
and various amount of entities if one is to express the Stevens operators
via the angular momentum/spin operators.

Here is an example that illustrate it. Consider the term (in McPhase's notation)


.. math::

    \mathcal{H}
    =
    B_2^0 \hat{O}_{2}^0(\mathbf{J}^n)

One can express the Stevens operators through angular momentum operator as

.. math::

    \mathcal{H}
    =
    B_2^0
    \Bigl(
        3 (\hat{J}_z^n)^2 - J(J+1)
    \Bigr)  
    =
    E_{const}
    +
    3B_2^0
    \hat{J}_z^n \hat{J}_z^n

By renaming indices as :math:`n \rightarrow (\mu_1, \alpha_1)` one can express
the non-constant part as

.. math::

    \mathcal{H}
    =
    C_{2,1}
    \sum_{\mu_1, \alpha_1, i_1, i_2}
    V_{\mu_1; \alpha_1}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_1}

where 

.. math::

    C_{2,1} &= 1
    \\
    V_{\mu_1; \alpha_1} &= 
    \begin{pmatrix}
        0 & 0 & 0 \\
        0 & 0 & 0 \\
        0 & 0 & 3B_2^0
    \end{pmatrix}
    \\
    X_{\mu_1; \alpha_1}^{i} &= \hat{J}_{i_1}^{\mu_1, \alpha_1}



