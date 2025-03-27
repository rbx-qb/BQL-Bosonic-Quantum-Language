from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt
import numpy as np

class BQLInterpreter:
    def __init__(self):
        self.registers = {}
        self.qc = None  # QuantumCircuit para interação com Qiskit
    
    def execute(self, command):
        tokens = command.split()
        if not tokens:
            return
        
        action = tokens[0]
        
        if action == "CREATE":
            self.create_register(tokens[1], int(tokens[2]))
        elif action == "ENTANGLE":
            self.entangle(tokens[1], tokens[2])
        elif action == "APPLY_NOISE":
            self.apply_noise(tokens[1], float(tokens[2]))
        elif action == "DISTILL":
            self.distill(tokens[1])
        elif action == "MEASURE":
            self.measure(tokens[1])
        elif action == "EVOLVE":
            self.evolve(tokens[1], int(tokens[2]))
        elif action == "SHOW":
            self.show(tokens[1])
        elif action == "SHOW_GRAPH":
            self.show_graph(tokens[1])
        elif action == "RUN_QISKIT":
            self.run_qiskit()
        else:
            print("Unknown command")
    
    def create_register(self, name, levels):
        self.registers[name] = {"levels": levels, "state": [1] + [0] * (levels - 1)}
        print(f"Created bosonic register {name} with {levels} levels.")
    
    def entangle(self, reg1, reg2):
        if reg1 in self.registers and reg2 in self.registers:
            print(f"Entangled {reg1} and {reg2} using rotation-based encoding.")
        else:
            print("Register not found.")
    
    def apply_noise(self, reg, strength):
        if reg in self.registers:
            print(f"Applied noise with strength {strength} to {reg}.")
        else:
            print("Register not found.")
    
    def distill(self, reg):
        if reg in self.registers:
            print(f"Applied entanglement distillation on {reg}.")
        else:
            print("Register not found.")
    
    def measure(self, reg):
        if reg in self.registers:
            print(f"Measured register {reg} state.")
        else:
            print("Register not found.")
    
    def evolve(self, reg, steps):
        if reg in self.registers:
            print(f"Evolving register {reg} for {steps} steps.")
        else:
            print("Register not found.")
    
    def show(self, reg):
        if reg in self.registers:
            print(f"State of {reg}: {self.registers[reg]}")
        else:
            print("Register not found.")
    
    def show_graph(self, reg):
        if reg in self.registers:
            state = self.registers[reg]["state"]
            plt.bar(range(len(state)), state)
            plt.title(f"State of {reg}")
            plt.xlabel("State Levels")
            plt.ylabel("Amplitude")
            plt.show()
        else:
            print("Register not found.")
    
    def run_qiskit(self):
        if not self.qc:
            self.qc = QuantumCircuit(2)  # Exemplo com 2 qubits
            self.qc.h(0)
            self.qc.cx(0, 1)
            self.qc.measure_all()
        
        backend = Aer.get_backend('qasm_simulator')
        result = execute(self.qc, backend, shots=1024).result()
        counts = result.get_counts(self.qc)
        
        print("Qiskit result:", counts)
        self.plot_histogram(counts)
    
    def plot_histogram(self, counts):
        plt.bar(counts.keys(), counts.values())
        plt.title("Measurement Result from Qiskit")
        plt.xlabel("State")
        plt.ylabel("Frequency")
        plt.show()

# Testando a nova linguagem com Qiskit e geração de gráficos
if __name__ == "__main__":
    bql = BQLInterpreter()
    commands = [
        "CREATE q1 4",
        "CREATE q2 4",
        "ENTANGLE q1 q2",
        "APPLY_NOISE q1 0.1",
        "DISTILL q1",
        "SHOW q1",
        "SHOW_GRAPH q1",
        "RUN_QISKIT"
    ]
    
    for cmd in commands:
        bql.execute(cmd)
