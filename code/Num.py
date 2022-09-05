class Num:
    def __init__(self, column_at, given_name):
        self.n = 0
        self.low = max
        self.high = min
        self.col_at = column_at if column_at != None else 0
        self.name = given_name if given_name != None else ''
        self.is_sorted = False
        self.data = []
        self.w = -1 if given_name != None and given_name[-1] == '-' else 1
