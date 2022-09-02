class Sym:
    def __init__(self, column_at, given_name):
        self.n = 0
        self.col_at = column_at
        self.name = given_name
        self.data = []
        #TODO: Add W, or weight