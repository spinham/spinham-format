.. _mapping-4_quadruplet:

**********************
Quadruplet interaction
**********************

In :ref:`zoo_spirit`, the quadruplet interaction term is written as

.. math::
    \mathcal{H}_{\rm quad}
    =
    - \sum_{ijkl} K_{ijkl} (\vec{n}_i \cdot \vec{n}_j)(\vec{n}_k \cdot \vec{n}_l)

First, notice, that :math:`i \ne j` and :math:`k \ne l`, otherwise the
Hamiltonian is constant. 

Second, a special case of this Hamiltonian have been discussed in one of the 
previous pages. This page includes it as a particular case:

- :math:`i = k` and :math:`j = l` (or equivalently :math:`i = l` and :math:`j = k`)

  This is a case of :ref:`mapping_biquadratic-exchange`.

In general the Hamiltonian maps to the :math:`\mathcal{H}_4`

.. math::
       
    \mathcal{H}_4
    =
    C_4
    \sum_{\substack{\mu_1, \mu_2, \mu_3, \mu_4, \\ \alpha_1, \alpha_2, \alpha_3, \alpha_4, \\ i_1, i_2, i_3, i_4}}
    V_{\mu_1, \mu_2, \mu_3, \mu_4; \alpha_1, \alpha_2, \alpha_3, \alpha_4}^{i_1, i_2, i_3, i_4}
    \cdot
    X_{\mu_1; \alpha_1}^{i_1}
    \cdot
    X_{\mu_2; \alpha_2}^{i_2}
    \cdot
    X_{\mu_3; \alpha_3}^{i_3}
    \cdot
    X_{\mu_4; \alpha_4}^{i_4}


By expanding the dot product, one gets

.. math::

    \mathcal{H}_{\rm quad}^{\rm case \, 2}
    =
    - \sum_{\substack{\mu_1, \mu_2, \mu_3, \mu_4,\\ \alpha_1, \alpha_2, \alpha_3, \alpha_4, \\ i_1, i_2, i_3, i_4}}
    K_{ijkl}^{i_1, i_2, i_3, i_4}
    n_{i}^{i_1}
    n_{j}^{i_2}
    n_{k}^{i_3}
    n_{l}^{i_4}

where the tensor :math:`K_{ijkl}^{i_1, i_2, i_3, i_4}` is defined as

.. math::

  K_{ijkl}  &= K_{ijkl}^{xxxx} = K_{ijkl}^{yyyy} = K_{ijkl}^{zzzz} \\
            &= K_{ijkl}^{xxyy} = K_{ijkl}^{xxzz} = K_{ijkl}^{yyzz} \\
            &= K_{ijkl}^{yyxx} = K_{ijkl}^{zzxx} = K_{ijkl}^{zzyy} \\

and all other components are zero. Then, one renames the indices as
:math:`i \rightarrow (\mu_1, \alpha_1)`, :math:`j \rightarrow (\mu_2, \alpha_2)`,
:math:`k \rightarrow (\mu_3, \alpha_3)`, :math:`l \rightarrow (\mu_4, \alpha_4)`
and correspondence becomes clear

.. math::

    C_4 &= -1 \\
    V_{\mu_1, \mu_2, \mu_3, \mu_4; \alpha_1, \alpha_2, \alpha_3, \alpha_4}^{i_1, i_2, i_3, i_4}
    &\leftrightarrow K_{ijkl}^{i_1, i_2, i_3, i_4}
    \\
    X_{\mu_1; \alpha_1}^{i_1} &\leftrightarrow n_{i}^{i_1} \\
    X_{\mu_2; \alpha_2}^{i_2} &\leftrightarrow n_{j}^{i_2} \\
    X_{\mu_3; \alpha_3}^{i_3} &\leftrightarrow n_{k}^{i_3} \\
    X_{\mu_4; \alpha_4}^{i_4} &\leftrightarrow n_{l}^{i_4} \\



    



  

