from Cols import Cols
import os.path

class Data:
    def __init__(self, source):
        self.cols = None
        self.rows = []
        self.error = False
        if (isinstance(source, str)):
            try:
                #open a csv file
                csv_file = open(source)

                #read the csv file
                csv_text = csv_file.read()

                #split the csv file into rows
                self.rows = csv_text.split("\n")

                #get the column names
                cols_names= self.rows[0].split(",")

                #construct new cols summary
                self.cols = Cols(cols_names)

                #close the file
                csv_file.close()
            except FileNotFoundError:
                self.error = True
                print("File", source, "does not exist")
                