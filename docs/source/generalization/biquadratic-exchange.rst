.. _mapping_biquadratic-exchange:

********************
Biquadratic exchange
********************

Bilinear exchange involves two sites and four entities (two entities per site).
Therefore, it can be expressed via the term :math:`\mathcal{H}_{4, 3}`.

- :math:`k = 4`
- :math:`l = 3`
- :math:`m_{4,3} = 2`

.. math::

    \mathcal{H}_{4,3}
    =
    C_{4, 3}
    \sum_{\substack{\mu_1, \mu_2,\\ \alpha_1, \alpha_2,\\ i_1, i_2, i_3, i_4}}
    V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}
    X_{\mu_1; \alpha_1}^{i_1}
    X_{\mu_1; \alpha_1}^{i_2}
    X_{\mu_2; \alpha_2}^{i_3}
    X_{\mu_2; \alpha_2}^{i_4}

The summary of the mapping for each code is given in the table below.

.. list-table::
    :header-rows: 1
    :stub-columns: 1

    *   - Code
        - :ref:`zoo_spinw`
        - :ref:`zoo_spirit`
    *   - :math:`\mathcal{H}`
        - .. math::
            \mathcal{H}
            =
            \sum_{i \neq j}
            B (\mathbf{S}_i \cdot \mathbf{S}_j)^2

        - .. math::
            \mathcal{H}_{\rm quad}
            =
            - \sum_{ij} K_{ij} (\vec{n}_i \cdot \vec{n}_j)^2
    *   - Indices renaming
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`j \rightarrow (\mu_2, \alpha_2)`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`j \rightarrow (\mu_2, \alpha_2)`
    *   - :math:`C_{4, 3}`
        - 1
        - -1
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2, i_3, i_4}`
        - :math:`B` if :math:`(i_1, i_2, i_3, i_4) \in \mathcal{K}` and 0 otherwise.
        - :math:`K_{\mu_1, \mu_2; \alpha_1, \alpha_2}` if :math:`(i_1, i_2, i_3, i_4) \in \mathcal{K}` and 0 otherwise.
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`S_{\mu_1; \alpha_1}^{i_1}`
        - :math:`n_{\mu_1; \alpha_1}^{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_3}`
        - :math:`S_{\mu_2; \alpha_2}^{i_3}`
        - :math:`n_{\mu_2; \alpha_2}^{i_3}`

.. note::

    -   :math:`\mathcal{K} = \{(x,x,x,x), (y,y,y,y), (z,z,z,z), (x,y,x,y), (x,z,x,z), (y,z,y,z), (y,x,y,x), (z,x,z,x), (z,y,z,y)\}`
    -   :ref:`zoo_spirit`

        Spirit includes more general Hamiltonian that is called "quadruplet interaction"

        .. math::

            \mathcal{H}_{\rm quad}
            =
            - \sum_{ijkl} K_{ijkl} (\vec{n}_i \cdot \vec{n}_j)(\vec{n}_k \cdot \vec{n}_l)

        in the case :math:`i = k` and :math:`j = l` (or, equivalently,
        :math:`i = l` and :math:`j = k`) this interaction describe a biquadratic
        exchange. Other cases are considered in the page 
        :ref:`mapping_quadruplet`. 
