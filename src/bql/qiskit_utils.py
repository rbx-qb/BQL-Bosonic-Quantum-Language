from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt

def create_entangled_pair():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()

    simulator = Aer.get_backend('aer_simulator')
    result = execute(qc, simulator).result()
    return result.get_counts()

def plot_results(counts):
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("State")
    plt.ylabel("Count")
    plt.title("Quantum Entanglement Measurement")
    plt.show()

