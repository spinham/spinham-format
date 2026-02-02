.. _mapping-4_exchange_striction:

******************
Exchange striction
******************

Exchange striction involves three entities. Therefore, it can be expressed via the term
:math:`\mathcal{H}_3`.

.. math::

    \mathcal{H}_3
    =
    C_3
    \sum_{\substack{\mu_1, \mu_2, \mu_3\\ \alpha_1, \alpha_2, \alpha_3\\ i_1, i_2, i_3}}
    V_{\mu_1, \mu_2, \mu_3; \alpha_1, \alpha_2, \alpha_3}^{i_1, i_2, i_3}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}
    X_{\mu_3; \alpha_3}^{i_3}
    
The summary of the mapping for each code is given in the table below.

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_mcphase`
    *   - :math:`\mathcal{H}`
        - .. math::
            \hat{\mathcal{H}}
            =
            -
            \dfrac{1}{2}
            \sum_{\substack{nn^{\prime},\alpha\beta\alpha^{\prime}\gamma=1,2,3\\\beta^{\prime}=1-6}}
            \Biggl(
                \dfrac{\partial \mathcal{J}_{\alpha\beta}}{\partial \epsilon_{\beta^{\prime}}}
                +
                \dfrac{\partial \mathcal{J}_{\alpha\beta}}{\partial R_{nn^{\prime}}^{\alpha^{\prime}}}
                \dfrac{\partial \epsilon_{\alpha^{\prime}\gamma} R_{nn^{\prime}}^{\gamma}}{\partial \epsilon_{\beta^{\prime}}}
            \Biggr)
            \epsilon_{\beta^{\prime}}
            \hat{\mathcal{I}}_{\alpha}^n
            \hat{\mathcal{I}}_{\beta}^{n^{\prime}}
    *   - Indices renaming
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, 
          :math:`n^{\prime} \rightarrow (\mu_2, \alpha_2)`, 
          :math:`\beta^{\prime} \rightarrow i_1`,
          :math:`\alpha \rightarrow i_2`,
          :math:`\beta \rightarrow i_3`
    *   - :math:`C_3`
        - :math:`-\dfrac{1}{2}`
    *   - :math:`V_{\mu_1, \mu_2, \mu_3; \alpha_1, \alpha_2, \alpha_3}^{i_1, i_2, i_3}`
        - .. math::
            \sum_{\alpha^{\prime}\gamma=1,2,3}
            \Biggl(
                \dfrac{\partial \mathcal{J}_{i_2,i_3}}{\partial \epsilon_{i_1}}
                +
                \dfrac{\partial \mathcal{J}_{i_2,i_3}}{\partial R_{\mu_1,\mu_2;\alpha_1,\alpha_2}^{\alpha^{\prime}}}
                \dfrac{\partial \epsilon_{\alpha^{\prime}\gamma} R_{\mu_1,\mu_2;\alpha_1,\alpha_2}^{\gamma}}{\partial \epsilon_{i_1}}
            \Biggr)
    *   - :math:`X_{\mu_1, \alpha_1}^{i_1}`
        - :math:`\epsilon_{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`\hat{\mathcal{I}}_{i_2}^{\mu_2,\alpha_2}`
    *   - :math:`X_{\mu_3; \alpha_3}^{i_3}`
        - :math:`\hat{\mathcal{I}}_{i_3}^{\mu_3,\alpha_3}`

.. note::

    Indices :math:`(\mu_1, \alpha_1)` have only one possible value, 
    :math:`(\mu_1, \alpha_1) = \_1`. 