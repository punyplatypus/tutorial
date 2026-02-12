class FileLoader:
    def load(self):
        print("Loading from file")

class APILoader:
    def load(self):
        print("Loading from API")

class DataPipeline:
    def __init__(self, loader):
        self.loader = loader

    def run(self):
        self.loader.load()

a = DataPipeline(FileLoader())
b = DataPipeline(APILoader())
#a.run()
#b.run()

class Pipeline:
    def __init__(self, loader: Loader):
        self.loader = loader

    def run(self):
        print(self.loader.load())

a = Pipeline(FileLoader())  
a.run()