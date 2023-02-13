from lstore.page import *
from lstore.components.Record import Record


class BasePage:
    def __init__(self, num_of_pages, bp_index):
        self.bp_index = bp_index
        self.physical_pages = []
        for i in range(num_of_pages+4):
            self.physical_pages.append(Page())

    def bp_insert(self, *columns):
        columns = columns[0]

        for idx, i in enumerate(columns):
            self.physical_pages[idx].write(i)

        return [self.bp_index, self.physical_pages[-1].num_records - 1]

    def rid_to_zero(self, index):
        self.physical_pages[1].delete(index)

    def get_indirection(self, index):
        return self.physical_pages[0].read(index)

    def read(self, index, column):
        return self.physical_pages[column].read(index)

    def get_full_record(self, index):
        columns = []
        for i in range(len(self.physical_pages)):
            columns.append(self.read(index, i))
        return columns

    def record(self, index, key_index): 
        record = Record(self.read(index, 1), self.read(index, 4 + key_index), [])
        columns = []
        for i in range(4, len(self.physical_pages)):
            columns.append(self.read(index, i))
        
        record.columns = columns
        return record

    def is_full(self):
        return self.space_left() == 0

    def space_left(self):
        return 512 - self.physical_pages[3].num_records
