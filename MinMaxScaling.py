class MinMaxScaling:
    def __init__(self , a = 0, b = 1):
        self.lower_bound = self._lower_bound(a , b)
        self.upper_bound = self._upper_bound(a , b)
        self.original_data = None
        self.transformed = None

    def _lower_bound(self , a , b):
        if a > b:
            raise ValueError("Lower_bounder could not be less then the upper bound!")
        return a

    def _upper_bound(self , a , b):
        if a > b:
            raise ValueError("Lower_bounder could not be less then the upper bound!")
        return b
    @property
    def _min(self):
        if self.original_data is None and len(self.original_data):
            print("No data to find minimum")
        return min(self.original_data)

    @property
    def _max(self):
        if self.original_data is None and len(self.original_data):
                    print("No data to find maximum")
        return max(self.original_data)

    def fit_transform(self , X):
        self.transformed = []
        self.original_data = X
        _min = self._min
        _max = self._max
        for sample in self.original_data:
             self.transformed.append((sample - _min) / (_max - _min) * (self.upper_bound - self.lower_bound) + self.lower_bound)
        return self.transformed

age = [30 , 35 , 60]
income = [40000 , 42000 , 60000]
mms = MinMaxScaling()
print(mms.fit_transform(age))
print(mms.fit_transform(income))