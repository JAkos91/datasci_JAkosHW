import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

class experiment:
    
    def __init__(self, results, control, path, date):
        self.results = results
        self.control = control
        self.path = path
        self.date = date
        # self.results = self.normalize()
        self.now = datetime.now()
        self.date_time = self.now.strftime("%Y-%m-%d %H:%M:%S")
        self.path=f"{self.path}{self.date_time}.csv"
        
    def __len__(self):
        return len(self.results)
    
    def __repr__(self):
        return f"Experiment data: {self.results}"
    
    def normalize(self):
        return [x / self.control for x in self.results]

    def plot(self):
        return px.line(self.results)
    
    def da(self):
        self.experiment_df = { 'Results': self.results, 'Control': self.control, 'Date': self.date}
        self.df = pd.DataFrame(self.experiment_df) 
        self.df.to_csv(path_or_buf=self.path, index = False, header=True)
        print(self.df)
        print(self.path)