# <a name="simulations">Quantum simulations</a>

  * [**Noise simulations**](modules/Continue_Exploring/quantum_sims/noise_simulations)

    This notebook collection provides a detailed overview of noise simulation on Amazon Braket. You will learn how to define noise channels, apply noise to new or existing circuits, and run those circuits on the Amazon Braket noise simulators. We also introduce noise models on Amazon Braket, along with details on how to create noise models containing different types of noise and instructions for how to apply the noise to a circuit. We show how to construct a noise model from device calibration data for real quantum processing units (QPUs) and also compare the measurement outcomes of circuits run on a noisy simulator with the same circuits run on QPUs to show that simulating circuits with noise models more closely mimics QPUs.

  * [**Testing the tensor network simulator with local and non-local random quantum circuits**](modules/Continue_Exploring/quantum_sims/TN1_demo_local_vs_non-local_random_circuits.ipynb)

    This notebook explores a class of random quantum circuits known as Hayden-Preskill circuits using the tensor network simulator backend in Amazon Braket. The goal is to understand the degree to which the tensor network simulator is capable of detecting a hidden local structure in a quantum circuit, while simultaneously building experience with the Amazon Braket service and SDK. We find that the TN1 tensor network simulator can efficiently simulate local random quantum circuits, even when the local structure is obfuscated by permuting the qubit indices. Conversely, when running genuinely non-local versions of the quantum circuits, the simulator's performance is significantly degraded.

  * [**Using the 'AdjointGradient' result type on Amazon Braket**](modules/Continue_Exploring/quantum_sims/Using_The_Adjoint_Gradient_Result_Type.ipynb)

    This notebook introduces the `AdjointGradient` result type, discusses what a gradient is and how to compute one on a quantum circuit, explains how they can be used to accelerate your workflows, and shows an example of gradients in action on a hybrid quantum algorithm.

  * [**Using the Amazon Braket tensor network simulator TN1**](modules/Continue_Exploring/quantum_sims/Using_the_tensor_network_simulator_TN1.ipynb)

    This notebook introduces the Amazon Braket on-demand tensor network simulator, TN1. You will learn about how TN1 works, how to use it, and which problems are best suited to run on TN1.