import requests
import pandas as pd
import numpy as np

class MusicExtract:
    
    def __init__(self, csv_path):
        self.csv = csv_path

    def queries(self):
        self.data = pd.read_csv(self.csv)
        return data

    def response(self):
        data = self.queries()
        return data.head(5)
