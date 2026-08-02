class Column:

    def __init__(self, name, dtype, values):

        # --- Step 1: type checks ---
        
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(dtype, str):
            raise TypeError('dtype must be a string')
        if not isinstance(values, list):
            raise TypeError('values must be a list')

        # --- Step 2: value checks ---

        if dtype not in ('str', 'int'):
            raise ValueError(f'dtype must be a "str" or an "int", got {dtype!r}')

        # check every value matches the declared dtype

        if dtype == 'int':
            for v in values:
                if not isinstance(v, int):
                    raise ValueError(f'dtype must be an "int", got {v!r}')

        if dtype == 'str':
            for v in values:
                if not isinstance(v, str):
                    raise ValueError(f'dtype must be an "str", got {v!r}')


        self._name = name
        self._dtype = dtype
        self._values = values
        self._length = len(self._values)


    def get_name(self):
        return self._name

    def get_dtype(self):
        return self._dtype

    def get_values(self):
        return self._values

    def get_length(self):
        return self._length


    def get_element(self, index):    
                                    
        if not isinstance(index, int):
            raise IndexError(f'index must be an "integer", got {index!r}')
        if index < 0 or index >= self._length:
            raise IndexError(f'Index {index} out of range for column of length {self._length}')
        return self._values[index]


    def sum(self):
        if self._dtype != 'int':
            raise TypeError('sum() only works on "int" columns')
        return sum(self._values)

    def mean(self):
        if self._dtype != 'int':
            raise TypeError('mean() only works on "int" columns')
        if self._length == 0:
            raise ValueError('mean() cannot be computed on an empty column')
        return sum(self._values) / self._length

    def count(self):
        return self._length

    def min(self):
        return min(self._values)

    def max(self):
        return max(self._values)

    def unique(self):
        unique_values = []
        for v in self._values:
            if v not in unique_values:
                unique_values.append(v)
        return unique_values



    def __str__(self):
        return f'{self._name}, {self._dtype}, {self._values}'


col = Column('age', 'int', [25, 30, 35])
# print(col.get_name())
# print(col.get_dtype())
# print(col.get_values())
# print(col.get_length())
# print(col.sum())    
# print(col.mean())   
print(col)
