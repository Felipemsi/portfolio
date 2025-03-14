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

After some iterations, the system configuration is statistically indenpendent from the original configuration and a sample of the equilibrium probability distribution, at this point we measure the system properties (energy, magnetization). 

 The <code>files.py</code> deals with outputs, like the measurements gathered through the simulation. 

 There is also an example of simulation in <code>example_simulation.py</code>.

<h2>Some Context on the Model</h2>
<p> <b> Ising Model </b> is a simple model where each atom has a magnetic moment (called <i>spin</i>) that interatics with its nearest-neighbours. This model is very important to study paramagnetic-ferromagnetic phase transition. </p>

<h2>Some Context on the Metropolis Algorithm</h2>

The <b>Metropolis</b> algorithm is a <i>Markov Chain Monte Carlo</i>(MCMC) method used mostly in statistical physics. Monte Carlo methods, in general, aim to obtain random samples for a probability distribution of interest, from those random samples statistical estimations can be made like for example the expected value.
