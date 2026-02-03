.. _mapping-5_two-ion-crystal-field:

*********************
Two-ion crystal field
*********************

Two-ion crystal field involves two entities. Therefore, it can be expressed as a
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
        - :ref:`zoo_mcphase` (v1)
        - :ref:`zoo_mcphase` (v2)
    *   - :math:`\mathcal{H}`
        - .. math::
            \hat{\mathcal{H}}
            =
            -\dfrac{1}{2}
            \sum_{nn^{\prime}}
            \sum_{ll^{\prime}}
            \sum_{mm^{\prime}}
            K_{ll^{\prime}}^{mm^{\prime}}(nn^{\prime})
            \hat{O}_{lm}(\mathbf{J}^n)
            \hat{O}_{l^{\prime}m^{\prime}}(\mathbf{J}^{n^{\prime}})
        - .. math::
            \hat{\mathcal{H}}
            =
            -
            \dfrac{1}{2}
            \sum_{nn^{\prime}}
            \Biggl[
                \sum_{kk^{\prime}}
                \sum_{qq^{\prime}}
                \mathcal{K}_{kk^{\prime}}^{qq^{\prime}}(nn^{\prime})
                \hat{T}_{kq}^n
                \hat{T}_{k^{\prime}q^{\prime}}^{n^{\prime}}
            \Biggr]
    *   - Renaming of indices
        - :math:`(l,m) \rightarrow i_1`, :math:`(l^{\prime},m^{\prime}) \rightarrow i_2`,
          :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`n^{\prime} \rightarrow (\mu_2, \alpha_2)`
        - :math:`(k,q) \rightarrow i_1`, :math:`(k^{\prime},q^{\prime}) \rightarrow i_2`,
          :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`n^{\prime} \rightarrow (\mu_2, \alpha_2)`
    *   - :math:`C_2`
        - :math:`-\dfrac{1}{2}`
        - :math:`-\dfrac{1}{2}`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}`
        - :math:`K_{i_1, i_2}(\mu_1, \alpha_1; \mu_2, \alpha_2)`
        - :math:`\mathcal{K}_{i_1, i_2}(\mu_1, \alpha_1; \mu_2, \alpha_2)`
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`\hat{O}_{i_1}(\mathbf{J}^{\mu_1, \alpha_1})`
        - :math:`\hat{T}_{i_1}^{\mu_1, \alpha_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`\hat{O}_{i_2}(\mathbf{J}^{\mu_2, \alpha_2})`
        - :math:`\hat{T}_{i_2}^{\mu_2, \alpha_2}`

.. note::

    -   Pairs of indices :math:`(l,m)` (:math:`(l^{\prime},m^{\prime})`) or
        :math:`(k,q)` (:math:`(k^{\prime},q^{\prime})`) run over the finite set
        of the integer pairs. Therefore, they can be enumerated with a  
        single integer and mapped to the index :math:`i_1` (:math:`i_2`).
