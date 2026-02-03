.. _mapping-5_crystal-field:

*************
Crystal field
*************

Crystal field terms involves either one entity. Therefore, it can be expressed
as a :math:`\mathcal{H}_1` term.

.. math::

    \mathcal{H}_1
    =
    C_1
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
    *   - Renaming of indices
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`(l,m) \rightarrow i_1`
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`(l,m) \rightarrow i_1`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`(k,q) \rightarrow i_1`
    *   - :math:`C_1`
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

    -   Pairs of indices :math:`(l, m)` or :math:`(k, q)` run over the finite
        set of the integer pairs. Therefore, they can be enumerated with a
        single integer and mapped to the index :math:`i_1`.
       