<h1> Ising Model using Metropolis Algorithm </h1>
<h2> Implementation</h2>

<p>This implementation has 3 file:</p>

<ul>
  <li><code>lattice.py</code></li>
  <li><code>metropolis_algorithm.py</code></li>
  <li><code>files.py</code></li>
</ul> 

 
 <code>lattice.py</code> defines the <code>Lattice()</code> class, which is the object that will be update through the simulation. The lattice is a numpy array representing the spin lattice at each site, and has properties like temperature, external magnetic field, energy, magnetization, etc. The class has also methods like <code>measure()</code> that compute the energy and magnetization of the lattice. 

<code>metropolis_algorithm.py</code> implements the metropolis algorithm, in which a random site of the lattice is choose, then the spin in this site is flipped with a probability:


$$ \text{prob} = 1, \quad \text{if the energy does not increase} $$
$$ \text{prob} = e^{-\beta \Delta E}, \quad \text{if the energy increases}  \quad \ $$


 The <code>files.py</code> deals with outputs, like the measurements gathered through the simulation. 

 There is also an example of simulation in <code>example_simulation.py</code>.

<h2>Some Context on the Model</h2>
<p> Ferromagnetism is a phase of matter in which the material has a permanent magnetization. <b> Ising Model </b> is a simple model where each atom has a magnetic moment (called <i>spin</i>) that interatics with its nearest-neighbours. </p>

<h2>Some Context on the Metropolis Algorithm</h2>

