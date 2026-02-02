.. _mapping-4_elastic-energy:

**************
Elastic energy
**************

Elastic energy term involves two entities. Therefore, it can be
expressed via the term :math:`\mathcal{H}_2`.

.. math::

    \mathcal{H}_2
    =
    C_2
    \sum_{\substack{\mu_1, \mu_2,\\ \alpha_1, \alpha_2,\\ i_1, i_2}}
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}

The summary of the mapping for two terms is given in the tables below.


.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_mcphase`
    *   - :math:`\mathcal{H}`
        - .. math::
            \hat{H}
            =
            \dfrac{1}{2}
            \sum_{\alpha\gamma=1-6}
            c^{\alpha\gamma}
            \epsilon_{\alpha}
            \epsilon_{\gamma}
    *   - Indices renaming
        - :math:`\alpha \rightarrow i_1`,
          :math:`\gamma \rightarrow i_2`
    *   - :math:`C_2`
        - :math:`\dfrac{1}{2}`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1,i_2}`
        - :math:`c^{i_1 i_2}`
    *   - :math:`X_{\mu_1, \alpha_1}^{i_1}`
        - :math:`\epsilon_{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`\epsilon_{i_2}`


.. note::

    -   :math:`i_1, i_2 = 1, \dots, 6`.
    -   There is only one possible value for indices :math:`(\mu_1; \alpha_1)`
        or :math:`(\mu_2; \alpha_2)`, namely :math:`\_1`.
