# Module Decaration:
import pandas
#import matplotlib.pyplot                                   as plt
from IPython.display         import display
from sklearn.metrics         import accuracy_score         as acc
from sklearn.model_selection import train_test_split       as tts
from sklearn.model_selection import cross_val_score        as cvs
from sklearn.neighbors       import KNeighborsClassifier   as KNC
from sklearn.tree            import DecisionTreeClassifier as DTC
from sklearn.ensemble        import RandomForestClassifier as RFC


class Basic:
    def __init__(self, URL):
        self.data = pandas.read_csv(URL)
        self._initialize_()

    def _initialize_(self):
        self.setDataFrameStyle()
    
    def convertLabelsForm(self):
        label = {
            0: "Extremely Weak",
            1: "Weak",
            2: "Normal",
            3: "Overweight",
            4: "Obesity",
            5: "Extreme Obesity",
        }
        self.data.rename(
            columns = {"Index": "Label"},
            inplace = True
        )
        self.data["Label"] = self.data["Label"].map(label)
        converted = self.data
        return converted

    def setDataFrameStyle(self):
        stylesheet = (self.convertLabelsForm().head(10).style.hide(axis = "index")
                        .set_properties(**{
                            "background-color": "white",
                            "color"           : "black",
                            "border"          : "1px solid gray",
                            "text-align"      : "left",
                            "font-family"     : "'Sarasa Term SC Nerd', sans-serif"
                        })

        )
        display(stylesheet)
        

if __name__ == "__main__":
    URL = "https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv"
    task = Basic(URL)
