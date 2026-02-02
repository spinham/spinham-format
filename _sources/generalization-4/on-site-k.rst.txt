.. _mapping-4_on-site-k:

**********************
On-site anisotropy (k)
**********************


Contributions to the term with :math:`k = 1` are discussed in
:ref:`mapping_zeeman`, with :math:`k = 2` in :ref:`mapping_on-site-k2`, 
with :math:`k = 4` in :ref:`mapping_on-site-k4`.

In this page we discuss the term with arbitrary :math:`k`.


Spirit
------

In :ref:`zoo_spirit`, the on-site anisotropy term is written as


.. math::
  \begin{alignedat}{1}
    \mathcal{H}_{\rm biaxial} & = \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} (1 - (\hat{K}_j^{(1)}\cdot\vec{n}_j)^2)^{n_1} \cdot (\hat{K}_j^{(2)}\cdot\vec{n}_j)^{n_2} \cdot ((\hat{K}_j^{(1)} \times \hat{K}_j^{(2)} ) \cdot\vec{n}_j)^{n_3} \\
                    & =                  \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} \cdot [\sin(\theta_j)]^{2n_1} \cdot [\cos(\varphi_j)\sin(\theta_j)]^{n_2} \cdot [\sin(\varphi_j)\sin(\theta_j)]^{n_3}                           \\
                    & =                  \sum_{j} \sum_{n_1,n_2,n_3} K_j^{(n_1, n_2, n_3)} \cdot [\sin(\theta_j)]^{2n_1 + n_2 + n_3} \cdot [\cos(\varphi_j)]^{n_2} \cdot [\sin(\varphi_j)]^{n_3},                                          \\
  \end{alignedat}
    

#TODO (mapping is possible, but the interpretation of the original Hamiltonian is unclear
at the moment)