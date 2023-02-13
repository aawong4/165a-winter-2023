<<<<<<< Updated upstream
from lstore.table import Table, Record
from lstore.index import Index
=======
from lstore.basepage import BasePage
from lstore.components.Record import Record
>>>>>>> Stashed changes


class Query:
    """
    # Creates a Query object that can perform different queries on the specified table 
    Queries that fail must return False
    Queries that succeed should return the result or True
    Any query that crashes (due to exceptions) should return False
    """

    def __init__(self, table):
        self.table = table
        pass

    """
    # internal Method
    # Read a record with specified rid
    # Returns True upon succesful deletion
    # Return False if record doesn't exist or is locked due to 2PL
    """
<<<<<<< Updated upstream
    def delete(self, primary_key):
        pass
    
    
=======

    def delete(self, key):
        rid = self.table.index.locate(self.table.key, key)
        location = self.table.page_directory[rid[0]]

        bp = self.table.base_list[location[0]]
        bp.rid_to_zero(location[1])

        # rid = self.table.index.locate(self.table.key, key)
        # location = self.table.page_directory[rid[0]]
        # indirection_location = location
        # check_indirection = self.table.base_list[location[0]].get_indirection(location[1])
        #
        # self.table.rid_counter = self.table.rid_counter + 1
        #
        # base_data = self.table.base_list[location[0]].get_full_record(location[1])
        # base_data[1] = 0  # set rid 0
        # base_data[0] = rid[0]
        #
        # if len(self.table.tail_list) == 0:
        #     self.table.tail_list.append(BasePage(self.table.num_columns + 4, 0))
        #
        # elif self.table.tail_list[-1].is_full():
        #     bp_index = self.table.tail_list[-1].bp_index + 1
        #     self.table.tail_list.append(BasePage(self.table.num_columns + 4, bp_index))
        #
        # location = self.table.tail_list[-1].bp_insert(base_data)
        #
        # self.table.page_directory[self.table.rid_counter] = location
        # self.table.base_list[indirection_location[0]].physical_pages[0].update(self.table.rid_counter, indirection_location[1])

>>>>>>> Stashed changes
    """
    # Insert a record with specified columns
    # Return True upon succesful insertion
    # Returns False if insert fails for whatever reason
    """
<<<<<<< Updated upstream
    def insert(self, *columns):
        schema_encoding = '0' * self.table.num_columns
        pass
=======
>>>>>>> Stashed changes

    def insert(self, *columns):

        data = list(columns)
        self.table.rid_counter = self.table.rid_counter + 1
        meta_data = [0, self.table.rid_counter, 0, 0]
        meta_data_and_data = meta_data + data

        if len(self.table.base_list) == 0:
            self.table.base_list.append(BasePage(len(columns), 0))

        elif self.table.base_list[-1].is_full():
            bp_index = self.table.base_list[-1].bp_index + 1
            self.table.base_list.append(BasePage(len(columns), bp_index))

        location = self.table.base_list[-1].bp_insert(meta_data_and_data)

        self.table.page_directory[self.table.rid_counter] = location

        self.table.index.build_index(self.table.key, data[self.table.key], meta_data[1])

    """
    # Read matching record with specified search key
    # :param search_key: the value you want to search based on
    # :param search_key_index: the column index you want to search based on
    # :param projected_columns_index: what columns to return. array of 1 or 0 values.
    # Returns a list of Record objects upon success
    # Returns False if record locked by TPL
    # Assume that select will never be called on a key that doesn't exist
    """

    def select(self, key, key_index, query_columns):
        rid_list = self.table.index.locate(key_index, key)
        records = []

        for i in rid_list:
            location = self.table.page_directory[i]
            check_indirection = self.table.base_list[location[0]].get_indirection(location[1])
            if self.table.base_list[location[0]].read(location[1], 1) != 0:  # checking to see if there is a delete
                record = Record(0, 0, [None] * self.table.num_columns)

                if check_indirection == 0:
                    record.rid = self.table.base_list[location[0]].read(location[1], 1)
                    record.key = self.table.base_list[location[0]].read(location[1], self.table.key + 4)

                    for column_index, isUsed in enumerate(query_columns):
                        if isUsed == 1:
                            record.columns[column_index] = self.table.base_list[location[0]].read(location[1],
                                                                                                  column_index + 4)
                    records.append(record)


                else:

                    record.rid = self.table.base_list[location[0]].read(location[1], 1)
                    record.key = self.table.base_list[location[0]].read(location[1], self.table.key + 4)

                    temp = self.table.page_directory[check_indirection]

                    for column_index, isUsed in enumerate(query_columns):
                        if isUsed == 1:
                            record.columns[column_index] = self.table.tail_list[temp[0]].read(temp[1],
                                                                                              column_index + 4)
                    records.append(record)

        for idx in enumerate(query_columns):
            if query_columns[idx[0]] == 0:
                for i in records:
                    i.columns[idx[0]] = None

        return records

    """
    # Read matching record with specified search key
    # :param search_key: the value you want to search based on
    # :param search_key_index: the column index you want to search based on
    # :param projected_columns_index: what columns to return. array of 1 or 0 values.
    # :param relative_version: the relative version of the record you need to retreive.
    # Returns a list of Record objects upon success
    # Returns False if record locked by TPL
    # Assume that select will never be called on a key that doesn't exist
    """

    def select_version(self, search_key, search_key_index, projected_columns_index, relative_version):
        pass

    """
    # Update a record with specified key and columns
    # Returns True if update is succesful
    # Returns False if no records exist with given key or if the target record cannot be accessed due to 2PL locking
    """

    def update(self, key, *columns):
        rid = self.table.index.locate(self.table.key, key)
        location = self.table.page_directory[rid[0]]
        indirection_location = location
        check_indirection = self.table.base_list[location[0]].get_indirection(location[1])
        data = list(columns)
        self.table.rid_counter = self.table.rid_counter + 1

        if check_indirection == 0:
            base_data = self.table.base_list[location[0]].get_full_record(location[1])

            for idx, i in enumerate(data):
                if i is not None:
                    base_data[idx + 4] = i

            base_data[1] = self.table.rid_counter

            if len(self.table.tail_list) == 0:
                self.table.tail_list.append(BasePage(len(columns), 0))

            elif self.table.tail_list[-1].is_full():
                bp_index = self.table.tail_list[-1].bp_index + 1
                self.table.tail_list.append(BasePage(len(columns), bp_index))

            location = self.table.tail_list[-1].bp_insert(base_data)

        else:
            location = self.table.page_directory[check_indirection]

            tail_data = self.table.tail_list[location[0]].get_full_record(location[1])

            for idx, i in enumerate(data):
                if i is not None:
                    tail_data[idx + 4] = i

            tail_data[1] = self.table.rid_counter

            if len(self.table.tail_list) == 0:
                self.table.tail_list.append(BasePage(len(columns), 0))

            elif self.table.tail_list[-1].is_full():
                bp_index = self.table.tail_list[-1].bp_index + 1
                self.table.tail_list.append(BasePage(len(columns), bp_index))

            location = self.table.tail_list[-1].bp_insert(tail_data)

        self.table.page_directory[self.table.rid_counter] = location

        self.table.base_list[indirection_location[0]].physical_pages[0].update(self.table.rid_counter,
                                                                               indirection_location[1])

    """
    :param start_range: int         # Start of the key range to aggregate 
    :param end_range: int           # End of the key range to aggregate 
    :param aggregate_columns: int  # Index of desired column to aggregate
    # this function is only called on the primary key.
    # Returns the summation of the given range upon success
    # Returns False if no record exists in the given range
    """

    def sum(self, start_range, end_range, aggregate_column_index):
        sum_res = 0

        start_range = min(start_range, end_range)
        end_range = max(start_range, end_range)

        key_list = self.table.index.key_range(start_range, end_range, self.table.key)

        query_column = []

        for i in range(self.table.num_columns):
            if i == aggregate_column_index:
                query_column.append(1)
            else:
                query_column.append(0)

        for i in key_list:
            sum_res += self.select(i, self.table.key, query_column)[0].columns[aggregate_column_index]

        return sum_res

    """
    :param start_range: int         # Start of the key range to aggregate 
    :param end_range: int           # End of the key range to aggregate 
    :param aggregate_columns: int  # Index of desired column to aggregate
    :param relative_version: the relative version of the record you need to retreive.
    # this function is only called on the primary key.
    # Returns the summation of the given range upon success
    # Returns False if no record exists in the given range
    """

    def sum_version(self, start_range, end_range, aggregate_column_index, relative_version):
        pass

    """
    incremenets one column of the record
    this implementation should work if your select and update queries already work
    :param key: the primary of key of the record to increment
    :param column: the column to increment
    # Returns True is increment is successful
    # Returns False if no record matches key or if target record is locked by 2PL.
    """

    # def increment(self, key, column):
    #     r = self.select(key, self.table.key, [1] * self.table.num_columns)[0]
    #     if r is not False:
    #         updated_columns = [None] * self.table.num_columns
    #         updated_columns[column] = r[column] + 1
    #         u = self.update(key, *updated_columns)
    #         return u
    #     return False
