.. _mapping_magneto-elastic:

***************************
Magneto-elastic interaction
***************************

Magneto-elastic interaction involves either two sites and two entities
or one site and one entity. Therefore, it can be expressed via the terms
:math:`\mathcal{H}_{2, 2}` and :math:`\mathcal{H}_{1, 1}`.

- :math:`k = 2`
- :math:`l = 2`
- :math:`m_{2,2} = 2`

.. math::

    \mathcal{H}_{2,2}
    =
    C_{2, 2}
    \sum_{\substack{\mu_1, \mu_2,\\ \alpha_1, \alpha_2,\\ i_1, i_2}}
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}

- :math:`k = 1`
- :math:`l = 1`
- :math:`m_{1,1} = 1`

.. math::

    \mathcal{H}_{1,1}
    =
    C_{1, 1}
    \sum_{\substack{\mu_1,\\ \alpha_1,\\ i_1}}
    V_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_1}

The summary of the mapping for two terms is given in the tables below.

.. _mapping_magneto-elastic-1-1:

Magneto-elastic interaction (1, 1)
==================================

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
    *   - Indices renaming
        - :math:`n \rightarrow (\mu_1; \alpha_1)`,
          :math:`(l,m) \rightarrow i_1`
    *   - :math:`C_{1, 1}`
        - :math:`-1`
    *   - :math:`V_{\mu_1; \alpha_1}^{i_1}`
        - :math:`\sum_{\alpha=1,\dots,6}G^{\alpha, i_1}_{\text{cfph}}(\mu_1,\alpha_1)\epsilon_{\alpha}`
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`O_{i_1}(\hat{\mathbf{J}}^{\mu_1, \alpha_1})`

.. _mapping_magneto-elastic-2-2:

Magneto-elastic interaction (2, 2)
==================================

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
    *   - Indices renaming
        - :math:`n \rightarrow (\mu_1; \alpha_1)`,
          :math:`n^{\prime} \rightarrow (\mu_2; \alpha_2)`,
          :math:`\alpha \rightarrow i_1`,
          :math:`(l,m) \rightarrow i_2`
    *   - :math:`C_{2, 2}`
        - :math:`-1`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}`
        - :math:`\Gamma^{i_1, i_2}(\mu_1, \alpha_1, \mu_2, \alpha_2)` 
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`\hat{u}_{\mu_1, \alpha_1}^{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`O_{i_2}(\hat{\mathbf{J}}^{\mu_2, \alpha_2})`

.. note::

    -   Pair of indices :math:`(l,m)` run over the finite set of the sets of two
        integers. Therefore, they can be enumerated with a single integer and
        mapped to the index :math:`i_1` (:math:`i_2`).
    -   In the case of :math:`(2, 2)`, index :math:`i_1 = x, y, z`, while index 
        :math:`i_2` runs over all pairs of integers :math:`(l,m)` of the 
        original Hamiltonian.