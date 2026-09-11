class MaxAbsolute:
    def __init__(self , lst):
        self.list = lst
        self._list = []
        self.res = []
        self._max = None
    @property
    def MaxAbs(self):
        for i in range(len(self.list)):
            self._list.append(abs(self.list[i]))
        self._max = max(self._list)
        return self._max
    @property
    def result(self):
        self.MaxAbs
        for j in self.list:
            self.res.append(j / self._max)
        return self.res

lst = [5 , -12 , 3 , -7 , 20 , -4]
ma = MaxAbsolute(lst)
print(ma.result)