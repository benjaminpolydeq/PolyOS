import random
from arsd.ars_core import ARSKernel

class ARSNode:
    def __init__(self, name):
        self.name = name
        self.kernel = ARSKernel()

    def step(self):
        context = random.randint(-5,5)
        return self.kernel.adapt(context)

class ARSNetwork:
    def __init__(self, num_nodes=5):
        self.nodes = [ARSNode(f"Node{i}") for i in range(num_nodes)]

    def simulate(self, steps=10):
        for s in range(steps):
            states = {node.name: node.step() for node in self.nodes}
            print(f"Step {s+1}: {states}")

if __name__ == "__main__":
    network = ARSNetwork()
    network.simulate()