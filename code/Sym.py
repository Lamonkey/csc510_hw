class Sym:
    def __init__(self, column_at, given_name):
        self.n = 0
        self.col_at = column_at if column_at != None else 0
        self.name = given_name if given_name != None else ''
        self.data = []