.. _zoo_sunny:

*****
Sunny
*****

========= ======================================================================
========= ======================================================================
Status    Draft
Links     `Docs <https://sunnysuite.github.io/Sunny.jl/stable/>`_,
          `DOI <https://doi.org/10.48550/arXiv.2501.13095>`_,
          `Github <https://github.com/SunnySuite/Sunny.jl>`_
Languages Julia
========= ======================================================================

Spin Hamiltonian
================ 


Sunny Hamiltonians will commonly have the format:

.. math::

    \mathcal{H}
    =
    \mu_{B}\mathbf{B}
    \cdot
    \sum_{i}
    g_{i}\mathbf{S}_{i}
    +
    \sum_{i<j}
    \mathbf{S}_{j}
    J_{ij}
    \mathbf{S}_{j}
    +
    \sum_{i}\sum_{k,q}
    c_{i,k,q}
    \mathcal{O}_{k,q}
    (\mathbf{S}_{i}).

The first term is Zeeman coupling to an external field :math:`\mathbf{B}`. The
second term is a local bilinear exchange between dipoles. The third term is a
single-ion anisotropy, which can be an arbitrary polynomial of spin. For
example, this may be an arbitrary expansion in the Stevens operators 
:math:`\mathcal{O}_{k,q}(\mathbf{S})`. For details, see: 
`sunnysuite.github.io/Sunny.jl/stable/renormalization.html <https://sunnysuite.github.io/Sunny.jl/stable/renormalization.html>`_

Sunny also allows to "toggle on" long-range dipole-dipole interactions
with Ewald summation and arbitrary demagnetization tensor: 
`sunnysuite.github.io/Sunny.jl/stable/library.html#Sunny.enable_dipole_dipole! <https://sunnysuite.github.io/Sunny.jl/stable/library.html#Sunny.enable_dipole_dipole!>`_
It also allows for arbitrary coupling between pairs of sites :math:`(i,j)`
as higher-order polynomials in :math:`\mathbf{S}_{i}` and :math:`\mathbf{S}_{j}`
(e.g., scalar biquadratic, but more general pair couplings too):
`sunnysuite.github.io/Sunny.jl/stable/library.html#Sunny.set_pair_coupling! <https://sunnysuite.github.io/Sunny.jl/stable/library.html#Sunny.set_pair_coupling!>`_


Convention
==========

================= ======
================= ======
Spin normalized   no
Multiple counting no
================= ======

