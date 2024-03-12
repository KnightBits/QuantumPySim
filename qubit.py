import numpy as np

class QuantumSimulator:
    def __init__(self, num_qubits=1, num_states=2):
        self.num_qubits = num_qubits
        self.num_states = num_states
        self.qubit_state = self.initialize_qubit()

    def initialize_qubit(self):
        state = np.zeros(2**self.num_qubits)
        state[0] = 1 / np.sqrt(2)  # Линейная комбинация |0⟩
        state[1] = 1 / np.sqrt(2)  # и |1⟩

        return state

    def apply_hadamard_gate(self, qubit_index):
        hadamard_matrix = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
        indices = np.arange(2**self.num_qubits)
        mask = (indices & (1 << qubit_index)) >> qubit_index  # Определение бита в qubit_index
        self.qubit_state = np.dot(np.diag([1, (-1)**mask]), np.dot(hadamard_matrix, self.qubit_state))

    def measure_qubit(self, qubit_index):
        probabilities = np.abs(self.qubit_state)**2

        outcome = np.random.choice(range(2**self.num_qubits), p=probabilities)
        self.qubit_state = np.zeros(2**self.num_qubits)
        self.qubit_state[outcome] = 1.0  # Проекция состояния на измеренное состояние

        return outcome

    def simulate(self, num_steps=100):
        results = []

        for _ in range(num_steps):
            for i in range(self.num_qubits):
                self.apply_hadamard_gate(i)
            measurement_result = self.measure_qubit(0)
            results.append(measurement_result)

        return results

    def get_qubit_state(self):
        return self.qubit_state

    def print_simulation_results(self, results):
        print("\nSimulation Results:")
        for i, measurement_result in enumerate(results):
            print(f"Step {i + 1}: Measurement outcome - {measurement_result}")

def main():
    try:
        num_qubits = int(input("Enter the number of qubits: "))
        num_steps = int(input("Enter the number of simulation steps: "))

        simulator = QuantumSimulator(num_qubits=num_qubits)

        print("Initial state of the qubit:", simulator.get_qubit_state())

        results = simulator.simulate(num_steps)

        simulator.print_simulation_results(results)

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
