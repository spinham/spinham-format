.. _mapping_on-site-k2:

**************************
On-site anisotropy (k = 2)
**************************

On-site anisotropy of the second order involves one magnetic site and two
entities. Therefore, it can be expressed via the term :math:`\mathcal{H}_{2, 1}`.

- :math:`k = 2`
- :math:`l = 1`
- :math:`m_{2,1} = 1`

.. math::

    \mathcal{H}_{2,1}
    =
    C_{2, 1}
    \sum_{\substack{\mu_1, \\ \alpha_1,\\ i_1, i_2}}
    V_{\mu_1; \alpha_1}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_2}
    
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
    *   - :math:`C_{2,1}`
        - :math:`1`
        - :math:`1`
        - :math:`1`
        - :math:`-1`
    *   - :math:`V_{\mu_1; \alpha_1}^{i_1, i_2}`
        - :math:`K_{\mu_1; \alpha_1}^{i_1, i_2}`
        - :math:`A_{\mu_1; \alpha_1}^{i_1, i_2}`
        - .. math::
            K_j^{i_1, i_2}
            =
            \begin{pmatrix}
                K_j \left(\hat{K}_{j}^{x}\right)^2 & K_j \hat{K}_{j}^{x} \hat{K}_{j}^{y} & K_j \hat{K}_{j}^{x} \hat{K}_{j}^{z} \\
                K_j \hat{K}_{j}^{x} \hat{K}_{j}^{y} & K_j \left(\hat{K}_{j}^{y}\right)^2 & K_j \hat{K}_{j}^{y} \hat{K}_{j}^{z} \\
                K_j \hat{K}_{j}^{x} \hat{K}_{j}^{z} & K_j \hat{K}_{j}^{y} \hat{K}_{j}^{z} & K_j \left(\hat{K}_{j}^{z}\right)^2
            \end{pmatrix} 
        - :math:`A_{\mu_1; \alpha_1}^{i_1, i_2}`
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`e_{\mu_1; \alpha_1}^{i_1}`
        - :math:`S_{\mu_1; \alpha_1}^{i_1}`
        - :math:`n_{\mu_1; \alpha_1}^{i_1}`
        - :math:`S_{\mu_1; \alpha_1}^{i_1}` 
        