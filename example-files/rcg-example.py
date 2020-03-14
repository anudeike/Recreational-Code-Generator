import numpy as np
import matplotlib.pyplot as plt


"""
This is a simple function plotting code:

it plots the equation that you put into it.

the idea is that another code will generate this template code (with specified values and what not)

"""


# PlotGraph type
class PlotGraph():
    """
    //create a plot graph class, name -> is the name of the object when it is called in main
    // this is how you will comment - duh
    // must have a main (can call it a struct, comp, or pattern idk yet -- lol this is too fancy)

    Main :
        PlotGraphPatternName.call(); // this will call all of the "running function" in this case - plot the stuff to the screen


    PlotGraph <PlotGraphPatternName> :
        start = 0; //mandatory
        stop = 100; //mandatory
        samples = 100;
        expression = "this will be a string that is parsable can should be used to create a math expression"
        title = ' this is an optional string '; // will have a default value
        graphColor = 'will have a default value'

    Can Use JSON representation to parse information

    " program " : { // can have an array here of different things
        "PlotGraph": {
            "name": string,
            "start": number,
            "stop": number,
            "samples" = 100,
            "expression" = string,
            "title" = name(optional),
            "graphColor" = "red" (optional)
        }
    }

    for something like this


    """
    def __init__(self, start, stop, num_samples, title="example"):
        self.function = ""
        self.title = title
        self.X = np.linspace(start, stop, num_samples) # create the X values
        self.Y = []

    def f(self):
        # should return an array with a function applied
        self.Y = [self.compute(x) for x in self.X]

    def compute(self, x):
        """
        Computes the Y values of the function.
        :return:
        """
        return np.sin(x)# this function will be arbitrary

    def plot(self, scatter=False, color='b'):
        plt.figure(1)
        plt.title(self.title)

        # plots the values
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

    # these are the functions that you need to run to fully use the class
    graph = PlotGraph(0, 100, 100)
    graph.call()


if __name__ == "__main__":
    main()