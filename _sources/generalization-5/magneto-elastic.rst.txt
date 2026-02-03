.. _mapping-5_magneto-elastic:

***************************
Magneto-elastic interaction
***************************

Magneto-elastic interaction involves two entities. Therefore, it can be
expressed as a :math:`\mathcal{H}_2` term.

.. math::

    \mathcal{H}_2
    =
    C_2
    \sum_{\substack{\mu_1, \mu_2,\\ \alpha_1, \alpha_2,\\ i_1, i_2}}
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}

The summary of the mapping for each code is given in the tables below.

.. _mapping-5_magneto-elastic-1:

Magneto-elastic interaction (1)
===============================


.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_mcphase`
    *   - :math:`\mathcal{H}`
        - .. math::

            \hat{\mathcal{H}}_{ME1}
            =
            -
            \sum_n
            \sum_{\alpha=1,\dots,6, lm}
            G^{\alpha,l,m}_{\text{cfph}}(n)
            \epsilon_{\alpha}
            O_{lm}(\hat{\mathbf{J}}^n)
    *   - Renaming of indices
        - :math:`n \rightarrow (\mu_1; \alpha_1)`,
          :math:`\alpha \rightarrow i_1`,
          :math:`(l,m) \rightarrow i_2`
    *   - :math:`C_2`
        - :math:`-1`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1,i_2}`
        - :math:`G^{i_1, i_2}_{\text{cfph}}(\mu_2,\alpha_2)\delta_{\mu_1, \mu_2}\delta_{\alpha_1, \alpha_2}`
    *   - :math:`X_{\mu_1, \alpha_1}^{i_1}`
        - :math:`\epsilon_{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`O_{i_2}(\hat{\mathbf{J}}^{\mu_2, \alpha_2})`


.. note::

    -   Pair of indices :math:`(l,m)` run over the finite set of the integer
        pairs. Therefore, they can be enumerated with a single integer and
        mapped to the index :math:`i_2`.
    -   Index :math:`i_1 = 1, \dots, 6`, while index :math:`i_2` runs over all
        pairs of integers :math:`(l,m)` of the original Hamiltonian.

.. _mapping-5_magneto-elastic-2:

Magneto-elastic interaction (2)
===============================

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_mcphase`
    *   - :math:`\mathcal{H}`
        - .. math::
            \hat{\mathcal{H}}_{ME2}
            =
            -
            \sum_{\substack{n<n^{\prime},lm,\\\alpha=1,2,3}}
            \Gamma^{\alpha,l,m}(nn^{\prime})
            \hat{u}_n^{\alpha}
            O_{lm}(\hat{\mathbf{J}}^{n^{\prime}})
    *   - Renaming of indices
        - :math:`n \rightarrow (\mu_1; \alpha_1)`,
          :math:`n^{\prime} \rightarrow (\mu_2; \alpha_2)`,
          :math:`\alpha \rightarrow i_1`,
          :math:`(l,m) \rightarrow i_2`
    *   - :math:`C_2`
        - :math:`-1`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}`
        - :math:`\Gamma^{i_1, i_2}(\mu_1, \alpha_1, \mu_2, \alpha_2)` 
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`\hat{u}_{\mu_1, \alpha_1}^{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`O_{i_2}(\hat{\mathbf{J}}^{\mu_2, \alpha_2})`

.. note::

    -   Pair of indices :math:`(l,m)` run over the finite set of the integer
        pairs. Therefore, they can be enumerated with a single integer and
        mapped to the index :math:`i_2`.
    -   Index :math:`i_1 = x, y, z`, while index :math:`i_2` runs over all pairs
        of integers :math:`(l,m)` of the original Hamiltonian.