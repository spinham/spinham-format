.. _mapping-5_elastic-energy:

**************
Elastic energy
**************

Elastic energy term involves two entities. Therefore, it can be expressed as a
:math:`\mathcal{H}_2` term.

.. math::

    \mathcal{H}_2
    =
    C_2
    \sum_{\substack{\mu_1, \mu_2,\\ \alpha_1, \alpha_2,\\ i_1, i_2}}
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}

The summary of the mapping for each code is given in the table below.


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
    *   - Renaming of indices
        - :math:`\alpha \rightarrow i_1`,
          :math:`\gamma \rightarrow i_2`
    *   - :math:`C_2`
        - :math:`\dfrac{1}{2}`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1,i_2}`
        - :math:`\dfrac{c^{i_1 i_2}}{N^2 N_C^2}`
    *   - :math:`X_{\mu_1, \alpha_1}^{i_1}`
        - :math:`\epsilon_{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`\epsilon_{i_2}`


.. note::

    -   :math:`i_1, i_2 = 1, \dots, 6`.
    -   :math:`N` is the number of sites in each cell and :math:`N_C` is the 
        number of cells in the system.
