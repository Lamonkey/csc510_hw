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
                rows_text = csv_text.split("\n")

                #get the column names
                cols_names= rows_text[0].split(",")

                #construct new cols summary
                self.cols = Cols(cols_names)

                #add the rows
                for r in range(1, len(rows_text)):
                    self.add(rows_text[r].split(","))

                #close the file
                csv_file.close()
            except FileNotFoundError:
                self.error = True
                print("File", source, "does not exist")
                
    def add(self, xs):
        
        '''
        Add a new row to the data
         - xs: The new "row" to be added to data
        Returns: None
        '''
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

    def stats(self, places=2, showCols=None, fun=None):
        '''
        Retrives the stats of specified columns based on a given function
         - places: The number of places to round a numerical answer to
         - showCols: The columns to retrieve the stats for
         - fun: The function (either mid or div) to use when getting stats
        Retrurns: A dictionary mapping the column name to the stats output
        '''
        # If showCols was not passed as a parameter then initialize it to the y columns
        showCols = self.cols.y_columns if showCols == None else showCols
        # If a function string name was not given then default it to mid
        fun = 'mid' if fun == None else fun
        # Initialize the dictionary mapping column name to stats output
        t = {}
        # For each column we want stats of
        for col in showCols:
            # Get the output of the function based on the parameter fun
            v = col.mid() if fun == 'mid' else col.div()
            try: # If v is a numerical answer then we can round it to the number of places
                v = round(v, places)
            except: # Otherwise do nothing
                v = v
            t[col.name] = v # Create the mapping
        return t

