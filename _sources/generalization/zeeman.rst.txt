.. _mapping_zeeman:

******************
Zeeman interaction
******************

Zeeman interaction involves two magnetic sites and two entities. Therefore, it
can be expressed via the term :math:`\mathcal{H}_{1, 1}`.

- :math:`k = 1`
- :math:`l = 1`
- :math:`m_{1,1} = 1`


.. math::

    \mathcal{H}_{1,1}
    =
    C_{1, 1}
    \sum_{\mu_1; \alpha_1; i_1}
    V_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_1}
    
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
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`i_1 = x, y, z`
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`\alpha \rightarrow i_1`
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`\alpha \rightarrow i_1`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`i_1 = x, y, z`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`i_1 = x, y, z`
    *   - :math:`C_{1, 1}`
        - 1
        - -1
        - -1
        - -1
        - 1
    *   - :math:`V_{\mu_1; \alpha_1}^{i_1}`
        - :math:`\mu_B g_{\mu_1, \alpha_1} H^{i_1}`
        - :math:`g_{\mu_1, \alpha_1} \mu_B H_{i_1}`
        - :math:`\mu_B H_{i_1}`
        - :math:`\mu_{\mu_1, \alpha_1} B^{i_1}`
        - :math:`\mu_B g_{\mu_1, \alpha_1} B^{i_1}`
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`S_{\mu_1, \alpha_1}^{i_1}`
        - :math:`\hat{J}^{\mu_1, \alpha_1}_{i_1}`
        - :math:`2 \hat{S}^{\mu_1, \alpha_1}_{i_1} + \hat{L}^{\mu_1, \alpha_1}_{i_1}`
        - :math:`n_{\mu_1, \alpha_1}^{i_1}`
        - :math:`S_{\mu_1, \alpha_1}^{i_1}`
        
