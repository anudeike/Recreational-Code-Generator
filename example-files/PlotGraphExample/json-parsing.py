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


def PlotGraph(obj):
    """
    Parses a PlotGraph Object
    :param obj:
    :return:
    """
    return None

class Generator():

    def __init__(self, path, target_name):
        self.config = self.openFile(path)
        self.pyFile = self.createFile(target_name)

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


# main function
def main():
    # get the dictionary
    config = openFile(path)

    # get the file we will be writing to
    pyFile = createFile("example")

    # for each element in the program
    for obj in config["program"]:
        # check if the imports is in there
        if "imports" in obj:
            # imports()
            print("found imports")

        # check if the PlotGraph is there.
        if "PlotGraph" in obj:
            # PlotGraph
            print("Found PlotGraph")





    return 0


if __name__ == "__main__":
    main()


