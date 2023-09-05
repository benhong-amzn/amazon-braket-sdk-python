# <a name="algorithms">Quantum algorithms and protocols</a>

## <a name="canonical">Canonical</a>

  * [**Grover**](modules/Continue_Exploring/quantum_algorithms_and_protocols/canonical/Grover/Grover.ipynb)

    This tutorial provides a step-by-step walkthrough explaining Grover's quantum algorithm. We show how to build the corresponding quantum circuit with simple modular building blocks, by means of the Amazon Braket SDK. Specifically, we demonstrate how to build custom gates that are not part of the basic gate set provided by the SDK. A custom gate can used as a core quantum gate by registering it as a subroutine.

  * [**Quantum Fourier transform**](modules/Continue_Exploring/quantum_algorithms_and_protocols/canonical/Quantum_Fourier_Transform/Quantum_Fourier_Transform.ipynb)

    This tutorial provides a detailed implementation of the Quantum Fourier Transform (QFT) and the inverse QFT, using the Amazon Braket SDK. We provide two different implementations: with and without recursion. The QFT is an important subroutine to many quantum algorithms, most famously Shor's algorithm for factoring, and the quantum phase estimation (QPE) algorithm for estimating the eigenvalues of a unitary operator. The QFT can be performed efficiently on a quantum computer, using only O(n<sup>2</sup>) single-qubit Hadamard gates and two-qubit controlled phase shift gates, where 𝑛 is the number of qubits. We first review the basics of the quantum Fourier transform, and its relationship to the discrete (classical) Fourier transform. We then implement the QFT in code two ways: recursively and non-recursively. This notebook also showcases the Amazon Braket `circuit.subroutine` functionality, which allows one to define custom methods and add them to the Circuit class.

  * [**Quantum phase estimation**](modules/Continue_Exploring/quantum_algorithms_and_protocols/canonical/Quantum_Phase_Estimation/Quantum_Phase_Estimation.ipynb)

    This tutorial provides a detailed implementation of the Quantum Phase Estimation (QPE) algorithm, through the Amazon Braket SDK. The QPE algorithm is designed to estimate the eigenvalues of a unitary operator 𝑈; it is a very important subroutine to many quantum algorithms, most famously Shor's algorithm for factoring, and the HHL algorithm (named after the physicists Harrow, Hassidim and Lloyd) for solving linear systems of equations on a quantum computer. Moreover, eigenvalue problems can be found across many disciplines and application areas, including (for example) principal component analysis (PCA) as used in machine learning, or in the solution of differential equations as relevant across mathematics, physics, engineering and chemistry. We first review the basics of the QPE algorithm. We then implement the QPE algorithm in code using the Amazon Braket SDK, and we illustrate the application of the algorithm with simple examples. This notebook also showcases the Amazon Braket `circuit.subroutine` functionality, which allows you to use custom-built gates as if they were any other built-in gates. This tutorial is set up to run on the local simulator or the on-demand simulator. Changing between these devices requires changing only one line of code, as demonstrated below in cell.

  * [**Quantum amplitude amplification**](modules/Continue_Exploring/quantum_algorithms_and_protocols/canonical/Quantum_Amplitude_Amplification/Quantum_Amplitude_Amplification.ipynb)

    This tutorial provides a detailed discussion and implementation of the Quantum Amplitude Amplification (QAA) algorithm, using the Amazon Braket SDK. QAA is a routine in quantum computing which generalizes the idea behind Grover's famous search algorithm, with applications across many quantum algorithms. In short, QAA uses an iterative approach to systematically increase the probability of finding one or multiple target states in a given search space. In a quantum computer, QAA can be used to obtain a quadratic speedup over several classical algorithms.

  * [**Randomness generation**](modules/Continue_Exploring/quantum_algorithms_and_protocols/canonical/Randomness/Randomness_Generation.ipynb)

    This tutorial provides a detailed implementation of a quantum random number generation (QRNG). Random numbers are a ubiquitous resource in computation and cryptography. For example, in security, random numbers are crucial to creating keys for encryption. QRNGs, which make use of the inherent unpredictability in quantum physics, promise enhanced security compared to standard cryptographic pseudo-random number generators (CPRNGs) based on classical technologies. In the notebook, we program two separate quantum processor units (QPUs) from different suppliers in Amazon Braket to supply two streams of weakly random bits. We then show how to generate physically secure randomness from these two weak sources by means of classical post-processing based on randomness extractors.

  * [**Simon's algorithm**](modules/Continue_Exploring/quantum_algorithms_and_protocols/canonical/Simons_Algorithm/Simons_Algorithm.ipynb)

    This tutorial provides a detailed discussion and implementation of Simon's algorithm, which provided the first example of an exponential speedup over the best known classical algorithm by using a quantum computer to solve a particular problem. Originally published in 1994, Simon's algorithm was a precursor to Shor's well-known factoring algorithm, and it served as inspiration for many of the seminal works in quantum computation that followed.

  * [**Superdense coding**](modules/Continue_Exploring/quantum_algorithms_and_protocols/canonical/Superdense_coding/4_Superdense_coding.ipynb) 
  
    This tutorial constructs an implementation of the *superdense coding protocol*, by means of the Amazon Braket SDK. Superdense coding is a method of transmitting two classical bits by sending only one qubit. Starting with a pair of entanged qubits, the sender (*aka* Alice) applies a certain quantum gate to their qubit and sends the result to the receiver (*aka* Bob), who is then able to decode the full two-bit message.

## <a name="variational">Variational</a>

  * [**QAOA**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/QAOA/QAOA_braket.ipynb)

    This tutorial shows how to (approximately) solve binary combinatorial optimization problems, using the Quantum Approximate Optimization Algorithm (QAOA). The QAOA algorithm belongs to the class of _hybrid quantum algorithms_ (leveraging classical and quantum computers), which are widely believed to be the working horse for the current NISQ (noisy intermediate-scale quantum) era. In this NISQ era, QAOA is also an emerging approach for benchmarking quantum devices. It is a prime candidate for demonstrating a practical quantum speed-up on near-term NISQ device. To validate our approach, we benchmark our results with exact results as obtained from classical QUBO solvers.

  * [**VQE transverse Ising**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/VQE_Transverse_Ising/VQE_Transverse_Ising_Model.ipynb)

    This tutorial shows how to solve for the ground state of the Transverse Ising Model, which is arguably one of the most prominent, canonical quantum spin systems, using the variational quantum eigenvalue solver (VQE). The VQE algorithm belongs to the class of _hybrid quantum algorithms_ (leveraging classical andquantum computers), which are widely believed to be the working horse for the current NISQ (noisy intermediate-scale quantum) era. To validate our approach, we benchmark our results with exact results as obtained from a Jordan-Wigner transformation.

  * [**VQE chemistry**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/VQE_Chemistry/VQE_chemistry_braket.ipynb)

    This tutorial shows how to implement the Variational Quantum Eigensolver (VQE) algorithm in Amazon Braket SDK to compute the potential energy surface (PES) for the Hydrogen molecule. Specifically, we illustrate the following features of Amazon Braket SDK: `LocalSimulator` which allows one to simulate quantum circuits on their local machine; construction of the ansatz circuit for VQE in Braket SDK; and computing expectation values of the individual terms in the Hamiltonian in Braket SDK.

  * [**Amazon Braket Hybrid Jobs**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs)
  
    This folder contains examples that illustrate the use of Amazon Braket Hybrid Jobs (Braket Jobs for short).

      * [**When to use Braket Jobs**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/README_hybrid_jobs.md)

      * [**Getting started with Braket Jobs**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/0_Creating_your_first_Hybrid_Job/Creating_your_first_Hybrid_Job.ipynb)

        This notebook provides a demonstration of running a simple Braket Job. You will learn how to create a Braket Job using the Braket SDK or the Braket console, how to set the output S3 folder for a job, and how to retrieve results. You will also learn how to specify the Braket device to run your job on simulators or QPUs. Finally, you will learn how to use local mode to quickly debug your code.

      * [**Quantum machine learning in Braket Jobs**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs.ipynb)

        This notebook shows a typical quantum machine learning workflow using Braket Jobs. In the process, you will learn how to upload input data, how to set up hyperparameters for your job, and how to retrieve and plot metrics. Finally, you will see how to run multiple Braket Jobs in parallel with different sets of hyperparameters.

      * [**QAOA with Braket Jobs and PennyLane**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/2_Using_PennyLane_with_Braket_Jobs/Using_PennyLane_with_Braket_Jobs.ipynb)

        This notebook shows how to run the QAOA algorithm with PennyLane (similar to a [previous notebook](examples/pennylane/2_Graph_optimization_with_QAOA.ipynb)), but this time using Braket Jobs. In the process, you will learn how to select a container image that supports PennyLane, and how to use checkpoints to save and load training progress of a job.

      * [**Bring your own containers to Braket Jobs**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/3_Bring_your_own_container/bring_your_own_container.ipynb)

        This notebook demonstrates the use of the Bring-Your-Own-Container (BYOC) functionality of Braket Jobs. While Amazon Braket has pre-configured environments which support most use cases of Braket Jobs, BYOC enables you to define fully customizable environments using Docker containers. You will learn how to use BYOC, including preparing a Dockerfile, creating a private Amazon Elastic Container Registry (ECR), building the container, and submitting a Braket Job using the custom container.

      * [**Embedded simulators in Braket Jobs**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/4_Embedded_simulators_in_Braket_Jobs/Embedded_simulators_in_Braket_Jobs.ipynb)

        This notebook introduces embedded simulators in Braket Jobs. An embedded simulator is a local simulator that runs completely within a job instance, i.e., the compute resource that is running your algorithm script. In contrast, [on-demand simulators](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html#braket-simulator-sv1), such as SV1, DM1, or TN1, calculate the results of a quantum circuit on dedicated compute infrastructure on-demand by Amazon Braket. By using embedded simulators, we keep all computations in the same environment. This allows the optimization algorithm to access advanced features supported by the embedded simulator. Furthermore, with the [Bring Your Own Container (BYOC)](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-byoc.html) feature of Jobs, users may choose to use open source simulators or their own proprietary simulation tools.

      * [**Parallelize training for quantum machine learning**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/5_Parallelize_training_for_QML/Parallelize_training_for_QML.ipynb)

        This notebook shows how to use [SageMaker's distributed data parallel library](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel.html) in Braket Jobs to accelerate the training of your quantum model. We go through examples to show you how to parallelize trainings across multiple GPUs in an instance, and even multiple GPUs over multiple instances. 

      * [**Benchmarking QN-SPSA optimizer with Braket Jobs and embedded simulators**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/6_QNSPSA_optimizer_with_embedded_simulator/qnspsa_with_embedded_simulator.ipynb)

        This notebook demonstrates how to implement and benchmark the QN-SPSA optimizer, a novel quantum optimization algorithm proposed by Gacon et al. Following this example, we will show how you can use Amazon Braket Hybrid Jobs to iterate faster on variational algorithm research, discuss best practices, and help you scale up your simulations with embedded simulators.

      * [**Running notebooks as hybrid jobs with Amazon Braket**](modules/Continue_Exploring/quantum_algorithms_and_protocols/variational/hybrid_jobs/7_Running_notebooks_as_jobs/Running_notebooks_as_jobs.ipynb)

        This notebook shows how users can run notebooks on different quantum hardware with priority access by using Amazon Braket Hybrid Jobs.

## <a name="implementations">Algorithm implementation library</a>
  The Braket Algorithm Library Notebooks provide ready-to-run example notebooks of algorithm implementations.

  * [**Local setup instructions**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/README.md)

  * [**Bell's inequality**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Bells_Inequality.ipynb)
  
  * [**Bernstein-Vazirani algorithm**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Bernstein_Vazirani_Algorithm.ipynb)

  * [**CHSH inequality**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/CHSH_Inequality.ipynb)

  * [**Deutsch-Jozsa algorithm**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Deutsch_Jozsa_Algorithm.ipynb)

  * [**Grover's search algorithm**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Grovers_Search.ipynb)

  * [**Quantum approximate optimization algorithm (QAOA)**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Quantum_Approximate_Optimization_Algorithm.ipynb)

  * [**Quantum circuit born machine**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Quantum_Circuit_Born_Machine.ipynb)

  * [**Quantum Monte Carlo**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Quantum_Computing_Quantum_Monte_Carlo.ipynb)

  * [**Quantum Fourier transform**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Quantum_Fourier_Transform.ipynb)

  * [**Quantum phase estimation**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Quantum_Phase_Estimation_Algorithm.ipynb)

  * [**Quantum walk**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Quantum_Walk.ipynb)

  * [**Shor's algorithm**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Shors_Algorithm.ipynb)

  * [**Simon's algorithm**](modules/Continue_Exploring/quantum_algorithms_and_protocols/algorithm_implementations/Simons_Algorithm.ipynb)