from abc import ABC, abstractmethod
from typing import Protocol
import pandas as pd

class Loader(ABC):
    @abstractmethod
    def load(self) -> pd.DataFrame:
        pass

class DataLoader(Loader):
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        return pd.read_csv(self.filepath)
    
class Pipeline:
    def __init__(self, loader: Loader):
        self.loader = loader

    def load(self):
        data = self.loader.load()
        return(data)
