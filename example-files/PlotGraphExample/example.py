
import numpy as np
import matplotlib.pyplot as plt
class Quadratic():
	def __init__(self, start, stop, num_samples, title="Quadratic Graph"): 
		self.function = ""
		self.title = title
		self.X = np.linspace(start, stop, num_samples)
		self.Y = []

	def f(self):
		self.Y = [self.compute(x) for x in self.X]