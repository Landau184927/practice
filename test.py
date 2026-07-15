# Module Decaration:
import pandas
#import matplotlib.pyplot                                  as plt
from colorama                import Fore, init
from IPython.display         import display
from sklearn.metrics         import accuracy_score         as acc
from sklearn.model_selection import train_test_split       as tts
from sklearn.model_selection import cross_val_score        as cvs
from sklearn.neighbors       import KNeighborsClassifier   as KNC
from sklearn.tree            import DecisionTreeClassifier as DTC
from sklearn.ensemble        import RandomForestClassifier as RFC

class Color:
    Red    = Fore.RED
    Yellow = Fore.YELLOW
    Green  = Fore.GREEN
    Blue   = Fore.BLUE
    Reset  = Fore.RESET
R, Y, G, B, X = Color()

class Basic:
    def __init__(self, URL: str):
        init(autoreset = True, strip = False, convert = False)
        self.data = pandas.read_csv(URL)
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
        self.data["Label"] = self.data["Label"].map(label)
        conversion = self.data
        return conversion

    def setDataFrameStyles(self): # NOTE: Set the Output Data Frame Style
        conversion = self.convertLabelFormat()
        stylesheet = (conversion.head(10).style.hide(axis = "index"))
        # MESSAGE:
        print(f"The following shows a sample {G}(10 rows){X} of BMI data for 500 people:")
        print(f"Here, each label string has been replaced from original as follows:")
        print(f"{R}0{X}: {G}Extremely Weak")
        print(f"{R}1{X}: {G}Weak")
        print(f"{R}2{X}: {G}Normal")
        print(f"{R}3{X}: {G}Overweight")
        print(f"{R}4{X}: {G}Obesity")
        print(f"{R}5{X}: {G}Extreme Obesity")
        display(stylesheet)
        #TODO

    #def extractDataSummary(self): # NOTE: Extract Various Metadata from Data:


    
        
if __name__ == "__main__":
    URL = "https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv"
    task = Basic(URL)
