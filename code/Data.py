from code.Cols import Cols
from code.Row import Row
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
                
    def add(self, xs):
        # If this is the first row added then initialize cols
        if self.cols == None:
            self.cols = Cols(xs)
        else:
            # Initialize row variable to be none
            row = None
            try:
                # If xs is a Row object then append it to self.rows and set row equal to it
                xs.cells
                self.rows.append(xs)
                row = xs
            except:
                # If xs is not a Row object then initialize a new Row object and set row equal to it
                self.rows.append(Row(xs))
                row = Row(xs)
            # For each x column
            for col in self.cols.x_columns:
                col.add(row.cells[col.col_at])
            # For each y column
            for col in self.cols.y_columns:
                col.add(row.cells[col.col_at])