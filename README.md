# QuantumPySim

QuantumPySim is a simple quantum simulator library for Python.

## Installation

You can install QuantumPySim using `pip`:

```bash
pip install quantum_pysim
```

## Usage

```python
from quantum_simulator import QuantumSimulator

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
```

## Documentation

### QuantumSimulator Class

#### `__init__(num_qubits=1, num_states=2)`

Initialize the QuantumSimulator with the specified number of qubits and states.

#### `simulate(num_steps=100)`

Run the quantum simulation for the specified number of steps.

#### `get_qubit_state()`

Get the current state of the qubit.

#### `print_simulation_results(results)`

Print the results of the quantum simulation.

### Example

Check the provided `main_script.py` for an example of using the QuantumPySim library.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
