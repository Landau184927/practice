# region "Module Decaration"
import pandas, sys, argparse
#import matplotlib.pyplot                                  as plt
from colorama                import Fore, init
from IPython.display         import display
from sklearn.metrics         import accuracy_score         as acc
from sklearn.model_selection import train_test_split       as tts
from sklearn.model_selection import cross_val_score        as cvs
from sklearn.neighbors       import KNeighborsClassifier   as KNC
from sklearn.tree            import DecisionTreeClassifier as DTC
from sklearn.ensemble        import RandomForestClassifier as RFC
# endregion

# region "Utility Class"
class Utility:
    pass
# endregion

class Basic:
    def __init__(self):
        init(autoreset = True, strip = False, convert = False)
        self.data = pandas.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")
        self._initialize_()

    def _initialize_(self):
        self.setDataFrameStyles()

    def convertLabelFormat(self): # NOTE: Convert Numerical Labels to String Format:
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
        match self.switchA:
            case True:
                self.data["Label"] = self.data["Label"].map(label)
            case False:
                pass
        data = self.data
        return label, data

    def setDataFrameStyles(self): # NOTE: Set the Output Data Frame Style
        label, data = self.convertLabelFormat()
        stylesheets = (data.head(10).style.hide(axis = "index"))
        # MESSAGE:
        print(f"The following shows a sample {Fore.GREEN}(10 rows){Fore.RESET} of BMI data for 500 people.")
        print(f"Here, each label string has been replaced from original as follows:\n")
        for code, text in label.items():
            print(f"  {Fore.RED}{code}{Fore.RESET}: {text}")
        display(stylesheets)
        #TODO

    #def extractDataSummary(self): # NOTE: Extract Various Metadata from Data:

if __name__ == "__main__":
    task = Basic()

    