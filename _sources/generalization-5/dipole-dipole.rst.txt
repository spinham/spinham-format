.. _mapping-5_dipole-dipole:

**********************************
Magnetic dipole-dipole interaction
**********************************

Magnetic dipole-dipole interaction involves two entities. Therefore, it can be
expressed as a :math:`\mathcal{H}_2` term.


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
        - :ref:`zoo_mcphase`
        - :ref:`zoo_spirit`
        - :ref:`zoo_sunny`
    *   - :math:`\mathcal{H}`
        - .. math::

            \mathcal{H}
            =
            -
            \dfrac{1}{2}
            \sum_{n\ne n^{\prime},\alpha\beta=1,2,3}
            \dfrac{\mu_0\mu_B^2 g_n g_{n^{\prime}}}{2\pi}
            \Biggl(
                3\dfrac{(R_{n^{\prime}}^{\alpha} - R_{n}^{\alpha})(R_{n^{\prime}}^{\beta} - R_{n}^{\beta})}{|\mathbf{R}_{n^{\prime}} - \mathbf{R}_{n}|^5}
                -
                \dfrac{\delta_{\alpha\beta}}{|\mathbf{R}_{n^{\prime}} - \mathbf{R}_{n}|^3}
            \Biggr)
            \hat{J}_{\alpha}^n
            \hat{J}_{\beta}^{n^{\prime}}
        - .. math::
            \mathcal{H}
            =
            \frac{1}{2}\frac{\mu_0}{4\pi}
            \sum_{i \neq j} \mu_i \mu_j \frac{(\vec{n}_i \cdot \hat{r}_{ij}) (\vec{n}_j\cdot\hat{r}_{ij}) - (\vec{n}_i \cdot \vec{n}_j)}{{r_{ij}}^3}
        - .. math::
            \mathcal{H}
            =
            -\dfrac{\mu_0}{4\pi}
            \sum_{ij}
            \dfrac{
            3(\mu_i \cdot \hat{r}_{ij}) (\mu_j \cdot \hat{r}_{ij}) - \mu_i \cdot \mu_j
            }{r^3_{ij}}
    *   - Renaming of indices
        - :math:`n \rightarrow (\mu_1, \alpha_1)`, :math:`n^{\prime} \rightarrow (\mu_2, \alpha_2)`, :math:`\alpha \rightarrow i_1`, :math:`\beta \rightarrow i_2`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`j \rightarrow (\mu_2, \alpha_2)`
        - :math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`j \rightarrow (\mu_2, \alpha_2)`
    *   - :math:`C_2`
        - :math:`-\dfrac{1}{2}`
        - :math:`\dfrac{1}{2}`
        - :math:`-1`
    *   - :math:`V_{\mu_1, \mu_2; \alpha_1, \alpha_2}^{i_1, i_2}`
        - .. math::
            \dfrac{\mu_0\mu_B^2 g_{\mu_1, \alpha_1} g_{\mu_2, \alpha_2}}{2\pi}
            \Biggl(
                3\dfrac{(R_{\mu_2, \alpha_2}^{i_1} - R_{\mu_1, \alpha_1}^{i_1})(R_{\mu_2, \alpha_2}^{i_2} - R_{\mu_1, \alpha_1}^{i_2})}{|\mathbf{R}_{\mu_2, \alpha_2} - \mathbf{R}_{\mu_1, \alpha_1}|^5}
                -
                \dfrac{\delta_{i_1, i_2}}{|\mathbf{R}_{\mu_2, \alpha_2} - \mathbf{R}_{\mu_1, \alpha_1}|^3}
            \Biggr)
        - .. math::
            \frac{\mu_0}{4\pi}\mu_{\mu_1, \alpha_1} \mu_{\mu_2, \alpha_2}
            \frac{
            \hat{r}_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_1}
            \hat{r}_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_2}
            - \delta_{i_1, i_2}
            }
            {r_{\mu_1, \alpha_1; \mu_2, \alpha_2}^3}
        - .. math::
            \dfrac{\mu_0}{4\pi}
            \frac{
            3\hat{r}_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_1}
            \hat{r}_{\mu_1, \alpha_1; \mu_2, \alpha_2}^{i_2}
            - \delta_{i_1, i_2}
            }
            {r_{\mu_1, \alpha_1; \mu_2, \alpha_2}^3}
    *   - :math:`X_{\mu_1; \alpha_1}^{i_1}`
        - :math:`\hat{J}_{i_1}^{\mu_1; \alpha_1}`
        - :math:`n_{\mu_1, \alpha_1}^{i_1}`
        - :math:`\mu_{\mu_1, \alpha_1}^{i_1}`
    *   - :math:`X_{\mu_2; \alpha_2}^{i_2}`
        - :math:`\hat{J}_{i_2}^{\mu_2; \alpha_2}`
        - :math:`n_{\mu_2, \alpha_2}^{i_2}`
        - :math:`\mu_{\mu_2, \alpha_2}^{i_2}`      
