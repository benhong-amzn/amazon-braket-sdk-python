# <a name="hardware">Quantum hardware</a>

  * [**Allocating qubits on QPU devices**](modules/Continue_Exploring/quantum_hardware/Allocating_Qubits_on_QPU_Devices.ipynb)

    This tutorial explains how you can use the Amazon Braket SDK to allocate the qubit selection for your circuits manually, when running on QPUs.

  * [**Analog Hamiltonian simulation**](modules/Continue_Exploring/quantum_hardware/analog_hamiltonian_simulation)

    This tutorial series provides a step-by-step walkthrough explaining analog Hamiltonian simulations (AHS) and how to run AHS programs on local simulators and Rydberg-based QPUs via Amazon Braket. AHS is a quantum computing paradigm different from gate-based computing. AHS uses a well-controlled quantum system and tunes its parameters to mimic the dynamics of another quantum system, the one we aim to study. In the gate-based quantum computation, the program is a quantum circuit consisting of a series of quantum gates, each of which acts only a small subset of qubits. In contrast, an AHS program is a sequence of time-dependent Hamiltonians that govern the quantum dynamics of all qubits; during AHS, the effect of the evolution under a Hamiltonian can be understood as a unitary acting simultaneously on all qubits.

  * [**Compilation**](modules/Continue_Exploring/quantum_hardware/compilation)

    This notebook collection shows how to run your circuits on Braket devices exactly as defined without any modification during the compilation process, a feature known as verbatim compilation. Usually, when you run a circuit on a QPU, behind the scenes, Amazon Braket will do a series of compilation steps to optimize your circuit and map the abstract circuit to the physical qubits on the QPU. However, in many situations, such as for error mitigation or benchmarking experiments, researchers require full control of the qubits and the gates that are being applied, thereby motivating the use of verbatim compilation.
    
    OpenQASM, a popular human-readable and hardware-agnostic quantum circuit description language currently supported as an *Intermediate Representation* (IR) on Amazon Braket, is also introduced. The associated tutorials show how to submit OpenQASM tasks to various devices on Braket and introduce some OpenQASM features available on Braket. In addition, verbatim compilation can be performed with OpenQASM by specifying a verbatim pragma around a box of code.

  * [**Error mitigation**](modules/Continue_Exploring/quantum_hardware/error_mitigation)

    This tutorial shows how to get started with using IonQ's Aria QPU on Amazon Braket. You’ll learn how Aria's two built-in error mitigation techniques work, how to switch between them, and the performance difference you can expect to see with and without these techniques for toy problems. 

  * [**Pulse control**](modules/Continue_Exploring/quantum_hardware/pulse_control/)

    This tutorial series explains how to use pulse control on various QPUs in Amazon Braket. Pulses are the analog signals that control the qubits in a quantum computer. With certain devices on Amazon Braket, you can access the pulse control feature to submit circuits using pulses.