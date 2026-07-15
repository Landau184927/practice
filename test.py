# Module Decaration:
import pandas
import matplotlib.pyplot                                   as plt
from sklearn.metrics         import accuracy_score         as acc
from sklearn.model_selection import train_test_split       as tts
from sklearn.model_selection import cross_val_score        as cvs
from sklearn.neighbors       import KNeighborsClassifier   as KNC
from sklearn.tree            import DecisionTreeClassifier as DTC
from sklearn.ensemble        import RandomForestClassifier as RFC


class Basic:
    def __init__(self, URL):
        self.data = pandas.read_csv(URL, index_col = 'Index')
        self._initialize_()

    def _initialize_(self):
        self.extractDataFile()

    def extractDataFile(self):
        self.data
        

if __name__ == "__main__":
    URL = "https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv"
    task = Basic(URL)
