.. _mapping-5_on-site-k:

**********************
On-site anisotropy (k)
**********************


Contributions to the term with :math:`k = 2` are discussed in
:ref:`mapping_on-site-k2`, with :math:`k = 4` in :ref:`mapping_on-site-k4`.

In this page the term with arbitrary :math:`k` is discussed.

In :ref:`zoo_spirit`, the on-site anisotropy term is written as


.. math::
  \begin{alignedat}{1}
    \mathcal{H}_{\rm biaxial} & = \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} (1 - (\hat{K}_j^{(1)}\cdot\vec{n}_j)^2)^{n_1} \cdot (\hat{K}_j^{(2)}\cdot\vec{n}_j)^{n_2} \cdot ((\hat{K}_j^{(1)} \times \hat{K}_j^{(2)} ) \cdot\vec{n}_j)^{n_3} \\
                    & =                  \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} \cdot [\sin(\theta_j)]^{2n_1} \cdot [\cos(\varphi_j)\sin(\theta_j)]^{n_2} \cdot [\sin(\varphi_j)\sin(\theta_j)]^{n_3}                           \\
                    & =                  \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} \cdot [\sin(\theta_j)]^{2n_1 + n_2 + n_3} \cdot [\cos(\varphi_j)]^{n_2} \cdot [\sin(\varphi_j)]^{n_3},                                          \\
  \end{alignedat}

This term can be mapped to the general form in different ways.

Strategy #1
===========

This strategy maps the term to the :math:`\mathcal{H}_3` term of the general
form.

.. math::

  \mathcal{H}_3 
  =
  C_3
  \sum_{\mu_1, \mu_2, \mu_3, \alpha_1, \alpha_2, \alpha_3, i_1, i_2, i_3}
  V_{\mu_1, \mu_2, \mu_3; \alpha_1, \alpha_2, \alpha_3}^{i_1, i_2, i_3}
  X_{\mu_1, \alpha_1}^{i_1}
  X_{\mu_2, \alpha_2}^{i_2}
  X_{\mu_3, \alpha_3}^{i_3}

First rename the index :math:`j \rightarrow (\mu, \alpha)`, then define three 
entities 

.. math::
  X_{\mu, \alpha}^{i_1}
  &=
  (1 - (\hat{K}_{\mu, \alpha}^{(1)}\cdot\vec{n}_{\mu, \alpha})^2)^{i_1}
  \\
  X_{\mu, \alpha}^{i_2}
  &=
  (\hat{K}_{\mu, \alpha}^{(2)}\cdot\vec{n}_{\mu, \alpha})^{i_2}
  \\
  X_{\mu, \alpha}^{i_3}
  &=
  ((\hat{K}_{\mu, \alpha}^{(1)} \times \hat{K}_{\mu, \alpha}^{(2)} ) \cdot\vec{n}_{\mu, \alpha})^{i_3}

where component indices :math:`i_1, i_2, i_3` assume the same integer values as
:math:`n_1, n_2, n_3` respectively. Then the interaction parameter can be 
defined as

.. math::

  V_{\mu_1, \mu_2, \mu_3; \alpha_1, \alpha_2, \alpha_3}^{i_1, i_2, i_3}
  =
  \delta_{\mu_1, \mu_2}
  \delta_{\mu_1, \mu_3}
  \delta_{\alpha_1, \alpha_2}
  \delta_{\alpha_1, \alpha_3}
  K_{\mu_1, \alpha_1}^{(i_1, i_2, i_3)}