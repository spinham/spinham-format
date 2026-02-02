.. _mapping-4_bilinear-exchange:

*****************
Bilinear exchange
*****************

Bilinear exchange involves two entities. Therefore, it can be
expressed via the term :math:`\mathcal{H}_2`.

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
        - :ref:`zoo_grogu`
        - :ref:`zoo_jukkr`, :ref:`zoo_tb2j`
        - :ref:`zoo_magpie`
        - :ref:`zoo_mcphase`
        - :ref:`zoo_spinw`
        - :ref:`zoo_spirit`
        - :ref:`zoo_sunny`
    *   - :math:`\mathcal{H}`
        - .. math::
            \frac{1}{2}
            \sum_{i\neq j}
            \boldsymbol{e}_{i}
            \cdot
            \boldsymbol{J}_{ij}
            \cdot
            \boldsymbol{e}_{j}
        - .. math::
            -
            \sum_{i\ne j}
            \mathbf{S}_{i}
            \cdot
            \boldsymbol{J}_{ij}
            \cdot
            \mathbf{S}_{j}
        - .. math::
            \sum_{i \neq j}
            J_{ij}
            \,
            \mathbf{S}_i
            \cdot
            \mathbf{S}_j
            +
            \sum_{i \neq j}
            \mathbf{D}_{ij}
            \cdot
            \left(
            \mathbf{S}_i
            \times
            \mathbf{S}_j
            \right)
        - .. math::
            -
            \dfrac{1}{2}
            \sum_{nn^{\prime}, \alpha\beta}
            \mathcal{J}_{\alpha\beta}(\mathbf{R}_{n^{\prime}} - \mathbf{R}_{n})
            \hat{\mathcal{I}}_{\alpha}^n
            \hat{\mathcal{I}}_{\beta}^{n^{\prime}}
        - .. math::
            \sum_{i \neq j}
            \mathbf{S}_i J_{ij} \mathbf{S}_j
        - .. math::
            -\frac{1}{2}
            \sum_{i\neq j}
            J_{ij}^{\alpha\beta}
            n_i^\alpha
            n_j^\beta
        - .. math::
            \sum_{i<j}
            \mathbf{S}_{j}
            J_{ij}
            \mathbf{S}_{j}
    *   - Indices renaming
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, 
          :math:`j \rightarrow (\mu_2, \alpha_2)`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, 
          :math:`j \rightarrow (\mu_2, \alpha_2)`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, 
          :math:`j \rightarrow (\mu_2, \alpha_2)`
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, 
          :math:`n^{\prime} \rightarrow (\mu_2, \alpha_2)`,
          :math:`\alpha \rightarrow i_1`,
          :math:`\beta \rightarrow i_2`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, 
          :math:`j \rightarrow (\mu_2, \alpha_2)`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, 
          :math:`j \rightarrow (\mu_2, \alpha_2)`,
          :math:`\alpha \rightarrow i_1`,
          :math:`\beta \rightarrow i_2`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, 
          :math:`j \rightarrow (\mu_2, \alpha_2)`
    *   - :math:`C_2`
        - :math:`\dfrac{1}{2}`
        - :math:`-1`
        - :math:`1`
        - :math:`-\dfrac{1}{2}`
        - :math:`1`
        - :math:`-\dfrac{1}{2}`
        - :math:`1`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}`
        - :math:`J_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_1, i_2}`
        - :math:`J_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_1, i_2}`
        - :math:`J_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_1, i_2}
          +
          \sum_{i_3}
          D_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_3}
          e_{i_1, i_2, i_3}`
        - :math:`\mathcal{J}^{i_1,i_2}(\mathbf{R}_{\mu_2, \alpha_2} - \mathbf{R}_{\mu_1, \alpha_1})`
        - :math:`J_{\mu _1, \alpha_1; \mu_2, \alpha_2}^{i_1, i_2}`
        - :math:`J_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_1, i_2}`
        - :math:`J_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_1, i_2}`
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`e_{\mu_1, \alpha_1}^{i_1}`
        - :math:`S_{\mu_1, \alpha_1}^{i_1}`
        - :math:`S_{\mu_1, \alpha_1}^{i_1}`
        - :math:`\hat{\mathcal{I}}^{\mu_1; \alpha_1}_{i_1}`
        - :math:`S_{\mu_1, \alpha_1}^{i_1}`
        - :math:`n_{\mu_1, \alpha_1}^{i_1}`
        - :math:`S_{\mu_1, \alpha_1}^{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`e_{\mu_2, \alpha_2}^{i_2}`
        - :math:`S_{\mu_2, \alpha_2}^{i_2}`
        - :math:`S_{\mu_2, \alpha_2}^{i_2}`
        - :math:`\hat{\mathcal{I}}^{\mu_2; \alpha_2}_{i_2}`
        - :math:`S_{\mu_2, \alpha_2}^{i_2}`
        - :math:`n_{\mu_2, \alpha_2}^{i_2}`
        - :math:`S_{\mu_2, \alpha_2}^{i_2}`

.. note::

    -   :ref:`zoo_magpie`

        :math:`e_{i_2, i_3, i_1}` is the Levi-Civita symbol.
    
    -   :ref:`zoo_mcphase`
  
        Indices :math:`i_1, i_2` run either over three or six components, as the 
        operators :math:`\hat{\mathcal{I}}_{\alpha}^n` are interpreted either as 

        .. math::

            \begin{pmatrix}
                \hat{\mathcal{I}}_1^n \\
                \hat{\mathcal{I}}_2^n \\
                \hat{\mathcal{I}}_3^n
            \end{pmatrix}
            =
            \begin{pmatrix}
                \hat{J}_x^n \\
                \hat{J}_y^n \\
                \hat{J}_z^n
            \end{pmatrix}

        or

        .. math::

            \begin{pmatrix}
                \hat{\mathcal{I}}_1^n \\
                \hat{\mathcal{I}}_2^n \\
                \hat{\mathcal{I}}_3^n \\
                \hat{\mathcal{I}}_4^n \\
                \hat{\mathcal{I}}_5^n \\
                \hat{\mathcal{I}}_6^n
            \end{pmatrix}
            =
            \begin{pmatrix}
                \hat{S}_x^n \\
                \hat{S}_y^n \\
                \hat{S}_z^n \\
                \hat{L}_x^n \\
                \hat{L}_y^n \\
                \hat{L}_z^n
            \end{pmatrix}
