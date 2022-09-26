class Row:
    """Represents a row of data, containing cells."""
    def __init__(self, cells):
        self.cells = cells
        #copy by value instead of reference
        self.cooked = cells.copy()
        self.y_evaled = False
    
