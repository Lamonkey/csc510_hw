class Row:
    def __init__(self, cells):
        self.cells = cells
        self.cooked = cells.copy()
        self.y_evaled = False