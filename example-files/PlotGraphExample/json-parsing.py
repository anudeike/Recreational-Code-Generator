import json

path = r"C:\Users\Ikechukwu Anude\Documents\recreational-code-generator\example-files\PlotGraphExample\example.json"
"""
// this is the correct notation for json
{
	"program": {
		"PlotGraph": {
			"name": "Quadratic",
			"start": 0,
			"stop": 100,
			"samples": 100,
			"expression": "x^2",
			"title": "Quadratic Graph",
			"graphColor": "red"
		}
	}
}
"""


# opens the file -> returns a dict from the json
def openFile(path):
    with open(path) as f:
        config = json.load(f)

    return config

# create file to write
def createFile(fileName):
    f = open(fileName + ".py", "w+")

    return f



# not going to use just yet - make script first
class Generator():

    def __init__(self, path, target_name):
        self.config = self.openFile(path)
        self.pyFile = self.createFile(target_name)
        self.tokens = []  # holds the tokens

    def openFile(self, path):
        """
        Opens a JSON file
        :param path: the file path of the JSON File
        :return: the json object as a dict
        """
        with open(path) as f:
            return json.load(f)

    def createFile(self, fileName):
        """
        Generates the empty file that will be filled
        :param fileName: the name of the file
        :return: a writable file object
        """

        with open(fileName, "w+") as f:
            return f

def PlotGraph(obj):
    """
    Parses a PlotGraph Object
    :param obj:
    :return:
    """

    generated_text = "\n\n\nclass {}():".format(obj["name"])

    # get the parameters needed from the object
    expression = obj["expression"]
    title = obj["name"] + " Graph"
    graphColor = "b"
    scatter = False

    # optional parameters
    if obj["title"]:
        title = obj["title"] # should be written more concisely in python 3.8

    if obj["graphColor"]:
        graphColor = obj["graphColor"] # should be written more concisely in python 3.8

    if obj["scatter"]:
        scatter = obj["scatter"] # should be written more concisely in python 3.8

    # CONSTRUCTOR
    # def __init__(self, start, stop, num_samples, title="example"):
    generated_text += "\n\tdef __init__(self, start, stop, num_samples, title=\"{}\"): ".format(title)
    generated_text += "\n\t\tself.function = \"\""
    generated_text += "\n\t\tself.title = title"
    generated_text += "\n\t\tself.X = np.linspace(start, stop, num_samples)"
    generated_text += "\n\t\tself.Y = []"

    # f()
    generated_text += "\n\n\tdef f(self):"
    generated_text += "\n\t\tself.Y = [self.compute(x) for x in self.X]"

    # compute()
    generated_text += "\n\n\tdef compute(self, x):"
    generated_text += "\n\t\treturn np.sin(x)"

    # plot()
    generated_text += "\n\n\tdef plot(self, scatter=False, color='{}'):".format(graphColor)
    generated_text += "\n\t\tplt.figure(1)\n\t\tplt.title(self.title)"
    generated_text += "\n\t\tif scatter:"
    generated_text += "\n\t\t\tplt.scatter(self.X, self.Y, c=color)\n\t\t\treturn"
    generated_text += "\n\t\tplt.plot(self.X, self.Y, c=color)"

    # show()
    generated_text += "\n\n\tdef show(self):"
    generated_text += "\n\t\tplt.show()"

    # call()
    generated_text += "\n\n\tdef call(self):"
    generated_text += "\n\t\tself.f()"
    generated_text += "\n\t\tself.plot()"
    generated_text += "\n\t\tself.show()"

    #print(generated_text)
    return generated_text

def imports(obj):
    """
    Handles the imports obj -> generates a string that contains the list of imports needed
    :param obj:
    :return:
    """
    generated_text = ""

    for lib in obj:
        if lib == "numpy":
            generated_text += "\nimport numpy as np"

        if lib == "pyplot":
            generated_text += "\nimport matplotlib.pyplot as plt"


    return generated_text


# main function
def main():

    # get the dictionary
    config = openFile(path)

    # tokens -> generated from the stuff this is
    tokens = []

    # get the file we will be writing to
    pyFile = createFile("example")

    # for each element in the program
    for obj in config["program"]:
        # check if the imports is in there
        if "imports" in obj:

            # handle the imports and then append the result to the token list
            import_token = imports(obj["imports"])
            tokens.append(import_token)

            print("found imports")

        # check if the PlotGraph is there.
        if "PlotGraph" in obj:
            PlotGraph_token = PlotGraph(obj["PlotGraph"])
            tokens.append(PlotGraph_token)

    print("\nCurrent File Output: ")
    print("".join(tokens))

    # write to a file
    pyFile.write("".join(tokens))


if __name__ == "__main__":
    main()


