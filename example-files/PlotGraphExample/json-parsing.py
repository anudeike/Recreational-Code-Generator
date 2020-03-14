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
    return None

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
            tokens.append(imports(obj["imports"]))
            print("found imports")

        # check if the PlotGraph is there.
        if "PlotGraph" in obj:
            # PlotGraph()
            print("Found PlotGraph")

    print("Current File Output: ")
    print("".join(tokens))


if __name__ == "__main__":
    main()


