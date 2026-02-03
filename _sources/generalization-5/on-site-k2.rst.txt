.. _mapping-5_on-site-k2:

**************************
On-site anisotropy (k = 2)
**************************

On-site anisotropy can involve arbitrary amount of entities. A case of 
two entities is discussed in this page. Therefore, it can be expressed as a
:math:`\mathcal{H}_2` term.

.. math::

    \mathcal{H}_2
    =
    C_2
    \sum_{\substack{\mu_1, \mu_2, \\ \alpha_1, \alpha_2, \\ i_1, i_2}}
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}
    
The summary of the mapping for each code is given in the table below.

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_grogu`
        - :ref:`zoo_jukkr`, :ref:`zoo_magpie`, :ref:`zoo_spinw`
        - :ref:`zoo_spirit`
        - :ref:`zoo_tb2j`
    *   - :math:`\mathcal{H}`
        - .. math::
            \mathcal{H}
            =
            \sum_{i}
            \boldsymbol{e}_{i}
            \cdot
            \boldsymbol{K}_{i}
            \cdot
            \boldsymbol{e}_{i}
        - .. math::
            \mathcal{H}
            =
            \sum_{i}
            \mathbf{S}_{i}
            \cdot
            \boldsymbol{A}_{i}
            \cdot
            \mathbf{S}_{i}
        - .. math::
            \mathcal{H}_{\rm uni}
            =
            \sum_j K_j (\hat{K}_j\cdot\vec{n}_j)^2
        - .. math::
            \mathcal{H}
            =
            -
            \sum_{i}
            \mathbf{S}_{i}
            \cdot
            \boldsymbol{A}_{i}
            \cdot
            \mathbf{S}_{i}
    *   - Index renaming
        - :math:`i \rightarrow (\mu_1, \alpha_1)`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`
        - :math:`j \rightarrow (\mu_1, \alpha_1)`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`
    *   - :math:`C_2`
        - :math:`1`
        - :math:`1`
        - :math:`1`
        - :math:`-1`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}`
        - :math:`K_{\mu_1; \alpha_1}^{i_1, i_2}\delta_{\mu_1,\mu_2}\delta_{\alpha_1,\alpha_2}`
        - :math:`A_{\mu_1; \alpha_1}^{i_1, i_2}\delta_{\mu_1,\mu_2}\delta_{\alpha_1,\alpha_2}`
        - .. math::
            K_j^{i_1, i_2}
            =
            \delta_{\mu_1,\mu_2}\delta_{\alpha_1,\alpha_2}
            \begin{pmatrix}
                K_j \left(\hat{K}_{j}^{x}\right)^2 & K_j \hat{K}_{j}^{x} \hat{K}_{j}^{y} & K_j \hat{K}_{j}^{x} \hat{K}_{j}^{z} \\
                K_j \hat{K}_{j}^{x} \hat{K}_{j}^{y} & K_j \left(\hat{K}_{j}^{y}\right)^2 & K_j \hat{K}_{j}^{y} \hat{K}_{j}^{z} \\
                K_j \hat{K}_{j}^{x} \hat{K}_{j}^{z} & K_j \hat{K}_{j}^{y} \hat{K}_{j}^{z} & K_j \left(\hat{K}_{j}^{z}\right)^2
            \end{pmatrix} 
        - :math:`A_{\mu_1; \alpha_1}^{i_1, i_2}\delta_{\mu_1,\mu_2}\delta_{\alpha_1,\alpha_2}`
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`e_{\mu_1; \alpha_1}^{i_1}`
        - :math:`S_{\mu_1; \alpha_1}^{i_1}`
        - :math:`n_{\mu_1; \alpha_1}^{i_1}`
        - :math:`S_{\mu_1; \alpha_1}^{i_1}` 
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`e_{\mu_2; \alpha_2}^{i_2}`
        - :math:`S_{\mu_2; \alpha_2}^{i_2}`
        - :math:`n_{\mu_2; \alpha_2}^{i_2}`
        - :math:`S_{\mu_2; \alpha_2}^{i_2}` 
        