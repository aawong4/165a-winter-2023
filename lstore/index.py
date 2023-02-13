"""
A data strucutre holding indices for various columns of a table. Key column should be indexd by default, other columns can be indexed through this object. Indices are usually B-Trees, but other data structures can be used as well.
"""


class Index:

    def __init__(self, table):
        self.indices = [None] * table.num_columns
        pass

    """
    # returns the location of all records with the given value on column "column"
    """

    def locate(self, column, value):
<<<<<<< Updated upstream
        pass
=======
        result = []
        if value in self.indices[column]:
            result.append(self.indices[column][value])
        return result
>>>>>>> Stashed changes

    """
    # Returns the RIDs of all records with values in column "column" between "begin" and "end"
    """

    def locate_range(self, begin, end, column):
<<<<<<< Updated upstream
        pass
=======
        result = []
        for i in self.indices[column]:
            if begin <= i[0] <= end:
                result.append(i[1])
        return result
>>>>>>> Stashed changes

    def key_range(self, begin, end, column):
        result = []
        for i in self.indices[column]:
            if begin <= i <= end:
                result.append(i)
        return result

    def build_index(self, column, key, rid):
        if self.indices[column] is None:
            self.indices[column] = {}
        self.indices[column][key] = rid

    """
    # optional: Create index on specific column
    """

    def create_index(self, column_number):
        pass

    """
    # optional: Drop index of specific column
    """

    def drop_index(self, column_number):
        pass
