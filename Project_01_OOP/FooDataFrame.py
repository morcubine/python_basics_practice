from wsgiref import headers

from ColumnClass import Column

class FooDataFrame:

    def __init__(self, filepath):

        with open(filepath, 'r') as f:
            header = f.readline().strip().split(',')
            # print(header)
            body = f.readlines()

            col_names = []
            col_types = []

            for pair in header:
                pair = pair.split(':')
                name = pair[0]
                dtype = pair[1]
                col_names.append(name)
                col_types.append(dtype)

            # print(col_names)
            # print(col_types)

            col_values = {}

            for name in col_names:
                col_values[name] = []

            # print(col_values)

            for row in body:
                row = row.strip().split(',')
                _id, name, age, department, salary, city = row
                # print(_id, name, department, salary, city)
                col_values['id'].append(_id)
                col_values['name'].append(name)
                col_values['age'].append(age)
                col_values['department'].append(department)
                col_values['salary'].append(salary)
                col_values['city'].append(city)

            # print(col_values)
        
        self._size = 0
        self._shape = (0, 0)
        self._column_names = []
        self._columns = {}

    def get_shape(self):
        return self._shape
    def get_size(self):
        return self._size
    def get_column_names(self):
        return self._column_names

    def get_column(self, column_name):
        if column_name not in self._columns:
            raise KeyError(f"{column_name} doesn't exist")
        return self._columns[column_name]

    def add_column(self, name, dtype, values):
        if name in self._columns:
            raise ValueError(f'{name} already exists in DataFrame')

        if len(values) != self._size:
            raise ValueError(f"{values} doesn't match current size {self._size}")

        col = Column(name, dtype, values)

        self._columns[name] = col
        self._column_names.append(name)
        self._shape = (self._size, len(self._column_names))



if __name__ == '__main__':
    df = FooDataFrame('data.csv')