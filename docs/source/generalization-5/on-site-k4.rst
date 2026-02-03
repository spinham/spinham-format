.. _mapping-5_on-site-k4:

**************************
On-site anisotropy (k = 4)
**************************

On-site anisotropy can involve arbitrary amount of entities. A case of 
four entities is discussed in this page. Therefore, it can be expressed as a
:math:`\mathcal{H}_4` term.

.. math::

    \mathcal{H}_4
    =
    C_4
    \sum_{\substack{\mu_1, \mu_2, \mu_3, \mu_4, \\ \alpha_1, \alpha_2, \alpha_3, \alpha_4, \\ i_1, i_2, i_3, i_4}}
    V_{\mu_1, \mu_2, \mu_3, \mu_4; \alpha_1, \alpha_2, \alpha_3, \alpha_4}^{i_1, i_2, i_3, i_4}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_2; \alpha_2}^{i_2}
    X_{\mu_3; \alpha_3}^{i_3}
    X_{\mu_4; \alpha_4}^{i_4}
    
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
    *   - :math:`C_4`
        - :math:`- \frac12`
    *   - :math:`V_{\mu_1, \mu_2, \mu_3, \mu_4; \alpha_1, \alpha_2, \alpha_3, \alpha_4}^{i_1, i_2, i_3, i_4}`
        - .. math::
            V_{...}^{xxxx}
            =
            V_{...}^{yyyy}
            =
            V_{...}^{zzzz}
            =
            K_{\mu_1, \alpha_1}
            \delta_{\mu_1,\mu_2}\delta_{\mu_1,\mu_3}\delta_{\mu_1,\mu_4}
            \delta_{\alpha_1,\alpha_2}\delta_{\alpha_1,\alpha_3}\delta_{\alpha_1,\alpha_4}

          Other components are zero.
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`n_{\mu_1; \alpha_1}^{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`n_{\mu_2; \alpha_2}^{i_2}`
    *   - :math:`X_{\mu_3; \alpha_3}^{i_3}`
        - :math:`n_{\mu_3; \alpha_3}^{i_3}`
    *   - :math:`X_{\mu_4; \alpha_4}^{i_4}`
        - :math:`n_{\mu_4; \alpha_4}^{i_4}`
   