
import numpy as np
import matplotlib.pyplot as plt


class PlotGraph():
	def __init__(self, start, stop, num_samples, title="Quadratic Graph"): 
		self.function = ""
		self.title = title
		self.X = np.linspace(start, stop, num_samples)
		self.Y = []

	def f(self):
		self.Y = [self.compute(x) for x in self.X]

	def compute(self, x):
		return np.sin(x)

	def plot(self, scatter=False, color='red'):
		plt.figure(1)
		plt.title(self.title)
		if scatter:
			plt.scatter(self.X, self.Y, c=color)
			return
		plt.plot(self.X, self.Y, c=color)

	def show(self):
		plt.show()

	def call(self):
		self.f()
		self.plot()
		self.show()

def main():
	Quadratic = PlotGraph(0, 100, 100)
	Quadratic.call()

if __name__ == "__main__":
	main()