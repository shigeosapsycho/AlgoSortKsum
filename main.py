import random
from typing import List
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import itertools
from math import comb

class main:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.nums = []
        self.target = 0
        self.k = 0
        self.indices = []
        self.tries = 0
        self.start_time = None
        self.total_combinations = 0
        self.successful_combinations_count = 0
        self.expected_tries = 0
        self.rarity_percentage = 0

    def kSum(self, nums: List[int], target: int, k: int):
        self.nums = nums
        self.target = target
        self.k = k
        self.tries = 0
        self.start_time = time.time()
        self.indices = random.sample(range(len(nums)), k)
        print(f"Expected number of tries: {self.expected_tries:.2f}")
        print(f"Rarity percentage: {self.rarity_percentage:.6f}%")
        ani = FuncAnimation(self.fig, self.update, frames=range(1000), repeat=False)
        plt.show()

    def update(self, frame):
        self.ax.clear()
        self.indices = random.sample(range(len(self.nums)), self.k)
        self.tries += 1

        colors = ['lightblue'] * len(self.nums)
        for idx in self.indices:
            colors[idx] = 'red'

        self.ax.bar(range(len(self.nums)), self.nums, color=colors)

        current_sum = sum(self.nums[idx] for idx in self.indices)
        trying_values = ' + '.join(str(self.nums[idx]) for idx in self.indices)
        self.ax.set_title(f'Target: {self.target}, Trying: {trying_values}\nExpected tries: {self.expected_tries:.2f}, Rarity: {self.rarity_percentage:.6f}%')

        if current_sum == self.target:
            elapsed_time = time.time() - self.start_time
            indices_str = ', '.join(str(idx) for idx in self.indices)
            self.ax.set_title(f'Found indices: {indices_str} in {self.tries} tries\nExpected tries: {self.expected_tries:.2f}, Rarity: {self.rarity_percentage:.6f}%')
            print(f"Found indices: {indices_str} in {self.tries} tries and {elapsed_time:.2f} seconds")
            print(f"Expected number of tries: {self.expected_tries:.2f}")
            print(f"Rarity percentage: {self.rarity_percentage:.6f}%")
            plt.pause(5)
            plt.close()
        else:
            random.shuffle(self.nums)

    def get_integer_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    def out_of_target_range(self, nums, target, k):
        import itertools
        from math import comb
        while True:
            possible_sums = {sum(comb) for comb in itertools.combinations(nums, k)}
            total_combinations = comb(len(nums), k)
            successful_combinations_count = sum(1 for comb in itertools.combinations(nums, k) if sum(comb) == target)
            if target in possible_sums:
                self.total_combinations = total_combinations
                self.successful_combinations_count = successful_combinations_count
                probability = successful_combinations_count / total_combinations
                self.expected_tries = 1 / probability
                self.rarity_percentage = probability * 100
                return nums
            print("The given range does not contain a valid k-sum solution for the target. Please enter the ranges again.")
            range1 = self.get_integer_input("What would you like the first range to be? \n")
            range2 = self.get_integer_input("What would you like the second range to be? \n") + 1
            nums = list(range(range1, range2))
            random.shuffle(nums)

bogo = main()

range1 = bogo.get_integer_input("What would you like the first range to be? \n")
range2 = bogo.get_integer_input("What would you like the second range to be? \n") + 1
target = bogo.get_integer_input("What is your target sum? \n") 
k = bogo.get_integer_input("How many numbers would you like to sum (e.g., 2 for two-sum)? \n")

nums = list(range(range1, range2))
random.shuffle(nums)

nums = bogo.out_of_target_range(nums, target, k)

bogo.kSum(nums, target, k)
