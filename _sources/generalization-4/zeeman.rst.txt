.. _mapping-4_zeeman:

******************
Zeeman interaction
******************

Zeeman interaction involves two entities. Therefore, it can be
expressed via the term :math:`\mathcal{H}_2`.


.. math::

    \mathcal{H}_2
    =
    C_2
    \sum_{\mu_1, \mu_2; \alpha_1, \alpha_2; i_1, i_2}
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2} 
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}
    
The summary of the mapping for each code is given in the table below.

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_magpie`, :ref:`zoo_spinw`
        - :ref:`zoo_mcphase` (v1)
        - :ref:`zoo_mcphase` (v2)
        - :ref:`zoo_spirit`
        - :ref:`zoo_sunny`
    *   - :math:`\mathcal{H}`
        - .. math::
            \mathcal{H}
            =
            \mu_B
            \mathbf{H}
            \sum_{i}
            g_i
            \mathbf{S}_i
        - .. math::
            \hat{\mathcal{H}}_{Z-J}
            =
            -
            \sum_{n, \alpha=1,2,3}
            g_n
            \mu_B
            \hat{J}^{n}_{\alpha}
            H_{\alpha}
        - .. math::
            \hat{\mathcal{H}}_{Z-LS}
            =
            -
            \sum_{n, \alpha=1,2,3}
            \mu_B
            \Bigl(
                2 \hat{S}^n_{\alpha} + \hat{L}^n_{\alpha}
            \Bigr)
            H_{\alpha}
        - .. math::
            \mathcal{H}_{\rm Zeeman}
            =
            -\sum_i \mu_i \vec{B}\cdot \vec{n}_i
        - .. math::
            \mathcal{H}
            =
            \mu_B
            \mathbf{B}
            \sum_{i}
            g_i
            \mathbf{S}_i
    *   - Indices renaming
        - :math:`i \rightarrow (\mu_2, \alpha_2)`, :math:`i_1, i_2 = x, y, z`
        - :math:`n \rightarrow (\mu_2, \alpha_2)`, :math:`\alpha \rightarrow i_1` and :math:`\alpha \rightarrow i_2`
        - :math:`n \rightarrow (\mu_2, \alpha_2)`, :math:`\alpha \rightarrow i_1` and :math:`\alpha \rightarrow i_2`
        - :math:`i \rightarrow (\mu_2, \alpha_2)`, :math:`i_1, i_2 = x, y, z`
        - :math:`i \rightarrow (\mu_2, \alpha_2)`, :math:`i_1, i_2 = x, y, z`
    *   - :math:`C_2`
        - 1
        - -1
        - -1
        - -1
        - 1
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}`
        - :math:`\mu_B g_{\mu_2, \alpha_2} \delta_{i_1, i_2}`
        - :math:`g_{\mu_2, \alpha_2} \mu_B \delta_{i_1, i_2}`
        - :math:`\mu_B \delta_{i_1, i_2}`
        - :math:`\mu_{\mu_2, \alpha_2} \delta_{i_1, i_2}`
        - :math:`\mu_B g_{\mu_2, \alpha_2} \delta_{i_1, i_2}`
    *   - :math:`X_{\mu_1, \alpha_1}^{i_1}`
        - :math:`H^{i_1}`
        - :math:`H^{i_1}`
        - :math:`H^{i_1}`
        - :math:`B^{i_1}`
        - :math:`B^{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`S_{\mu_2, \alpha_2}^{i_2}`
        - :math:`\hat{J}^{\mu_2, \alpha_2}_{i_2}`
        - :math:`2 \hat{S}^{\mu_2, \alpha_2}_{i_2} + \hat{L}^{\mu_2, \alpha_2}_{i_2}`
        - :math:`n_{\mu_2, \alpha_2}^{i_2}`
        - :math:`S_{\mu_2, \alpha_2}^{i_2}`
        
