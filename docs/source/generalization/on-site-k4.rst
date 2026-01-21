.. _mapping_on-site-k4:

**************************
On-site anisotropy (k = 4)
**************************

On-site anisotropy of the fourth order involves one magnetic site and four  
entities. Therefore, it can be expressed via the term :math:`\mathcal{H}_{4, 1}`.

- :math:`k = 4`
- :math:`l = 1`
- :math:`m_{4,1} = 1`

.. math::

    \mathcal{H}_{4,1}
    =
    C_{4, 1}
    \sum_{\mu_1, \alpha_1, i_1, i_2, i_3, i_4}
    V_{\mu_1; \alpha_1}^{i_1, i_2}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_2}
    X_{\mu_1; \alpha_1}^{i_3}
    X_{\mu_1; \alpha_1}^{i_4}
    
The summary of the mapping for each code is given in the table below.

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_spirit`
    *   - :math:`\mathcal{H}`
        - .. math::
            \mathcal{H}_{\rm cubic}
            =
            - \frac12 \sum_j K_j ([\vec{n}_j]_x^4 + [\vec{n}_j]_y^4 + [\vec{n}_j]_z^4)
    *   - Index renaming
        - :math:`j \rightarrow (\mu_1, \alpha_1)`
    *   - :math:`C_{4,1}`
        - :math:`- \frac12`
    *   - :math:`V_{\mu_1; \alpha_1}^{i_1, i_2, i_3, i_4}`
        - .. math::
            V_{\mu_1; \alpha_1}^{xxxx}
            =
            V_{\mu_1; \alpha_1}^{yyyy}
            =
            V_{\mu_1; \alpha_1}^{zzzz}
            =
            K_{\mu_1, \alpha_1}

          Other components are zero.
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`n_{\mu_1; \alpha_1}^{i_1}`
   