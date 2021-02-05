import numpy as np


class Knapsack:
    def __init__(self, weight):
        self.items = []
        self.weight = weight
        self._items()

    def __len__(self):
        return len(self.items)

    def _items(self, newitem=None):
        self.items = [
            ("map", 9, 150),
            ("compass", 13, 35),
            ("water", 153, 200),
            ("sandwich", 50, 160),
            ("glucose", 15, 60),
            ("tin", 68, 45),
            ("banana", 27, 60),
            ("apple", 39, 40),
            ("cheese", 23, 30),
            ("beer", 52, 10),
            ("suntan cream", 11, 70),
            ("camera", 32, 30),
            ("T-shirt", 24, 15),
            ("trousers", 48, 10),
            ("umbrella", 73, 40),
            ("waterproof trousers", 42, 70),
            ("waterproof overclothes", 43, 75),
            ("note-case", 22, 80),
            ("sunglasses", 7, 20),
            ("towel", 18, 12),
            ("socks", 4, 50),
            ("book", 30, 10),
        ]
        if newitem:
            self.items.append(newitem)

    def getValue(self, zeroOrone):
        total_weight = 0
        total_value = 0
        for i in range(len(zeroOrone)):
            if len(zeroOrone) <= len(self.items):
                name, weight, value = self.items[i]
            else:
                print("Length is out of range")
                break
            if total_weight + weight < self.weight:
                total_weight += zeroOrone[i] * weight
                total_value += zeroOrone[i] * value
        return total_value

    def print(self, zeroOrone):
        total_weight = 0
        total_value_check = self.getValue(zeroOrone)
        for i in range(len(zeroOrone)):
            name, weight, value = self.items[i]
            if total_weight + weight < self.weight:
                total_weight += zeroOrone[i] * weight
                print(f"Name: {name}, Weight: {weight}, Value: {value}")
        print(f"Total weight: {total_weight}, Total_value: {total_value_check}")


if __name__ == '__main__':
    agent = Knapsack(400)
    randomlist = np.random.randint(2, size=len(agent))
    print(randomlist)
    agent.print(randomlist)
