# Module Decaration:
import pandas
#import matplotlib.pyplot                                   as plt
from colorama                import Fore, Back, init
from IPython.display         import display
from sklearn.metrics         import accuracy_score         as acc
from sklearn.model_selection import train_test_split       as tts
from sklearn.model_selection import cross_val_score        as cvs
from sklearn.neighbors       import KNeighborsClassifier   as KNC
from sklearn.tree            import DecisionTreeClassifier as DTC
from sklearn.ensemble        import RandomForestClassifier as RFC

class Basic:
    def __init__(self, URL):
        init(autoreset = True)
        self.data = pandas.read_csv(URL)
        self._initialize_()

    def _initialize_(self):
        self.setDataFrameStyle()
    
    def convertLabelsForm(self): # Convert Numerical Labels to String Format:
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

    def setDataFrameStyle(self): # Set the Output Data Frame Style:
        stylesheet = (self.convertLabelsForm().head(10).style.hide(axis = "index")
                        #.set_properties(**{
                        #   "border"     : "1px solid gray",
                        #    "text-align" : "left",
                        #})
                        .set_table_styles([{
                            "selector"   : "th.col_heading.level0",
                            "props"      : [ ("text-align", "right") ]
                        }])
        )
        # (!) Change the Font
        print(Fore.GREEN + "Notice:", Fore.RESET + "The following shows a sample (10 rows) of BMI data for 500 people.")
        display(stylesheet)
        
if __name__ == "__main__":
    URL = "https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv"
    task = Basic(URL)
