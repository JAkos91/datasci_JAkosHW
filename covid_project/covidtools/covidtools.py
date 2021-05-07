import pandas as pd
import numpy as np
import plotly.express as px
import datetime

class CovidData:
      
    def __init__(self, results, control, name):
        self.results = results
        self.control = control
        self.name = name
        
        self.results = self.normalize()
        
    def __repr__(self):
        return f"Covid data: {self.results}"
    
    def __len__(self):
        return len(self.results)
    
    def __add__(self, other):
        return [x + other for x in self.results]
    
    def normalize(self):
        return [x / self.control for x in self.results]

    def plot(self):
        return px.line(self.results)
     

        
    @classmethod
    def changeType(cls, datatype):
        cls.datatype =datatype
    
class Literature:
    
    def first():
        pass

class Image:
    
    pass