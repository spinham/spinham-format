.. _zoo:

*******************
Zoo of Hamiltonians
******************* 

The status of each page is either "Verified" or "Draft". "Verified" means that
the page content have been verified by the developer of the respective tool.

Convention of the spin Hamiltonian is defined by their form (constants before
the sums) and two properties:

*   Whether spin vectors are normalised or not.

    * ``yes``: :math:`\vert \mathbf{S}_i \vert = 1`
    * ``no``: :math:`\vert \mathbf{S}_i \vert = S_i`

*   Whether multiple counting is implied in the sums or not.

    * ``yes``: both :math:`i \rightarrow j` and :math:`j \rightarrow i` are
      included.
    * ``no``: only one direction is included.

For multiple counting the example is given for 2-sites terms of the Hamiltonian,
the same concept is generalizable for terms that involve more than 2 sites.

  
.. toctree::
    :maxdepth: 1

    espins
    grogu
    jukkr
    magnopy
    magpie
    mcphase
    questaal
    spinw
    spirit
    sunny
    tb2j
    uppasd
    vampire

