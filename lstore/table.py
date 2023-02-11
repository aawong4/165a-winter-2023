from lstore.index import Index
import time
from lstore.page import Physical_Page
import lstore.config

class Record:
    def __init__(self, rid, key, columns):
        self.rid = rid
        self.key = key
        self.columns = columns


# Classes for conceptual pages, includes physical pages for each column in the table
# Can be used as either base or tail page as well
# Extra physical pages for rid, indirection, schema encoding, timestamp
class Conceptual_Page:
    def __init__(self, num_columns):
        self.pages = []
        for i in range(num_columns + 5):
            self.pages.append(Physical_Page())
        self.num_records = 0

    # Function to insert record into base page, uses num_records to determine next row
    def insert(self, offset, record):
        if self.is_full():
            return
        self.pages[lstore.config.INDIRECTION_COLUMN].write(self.num_records, 0)
        self.pages[lstore.config.RID_COLUMN].write(self.num_records, record.rid)
        self.pages[lstore.config.SCHEMA_ENCODING_COLUMN].write(self.num_records, 0)
        self.pages[lstore.config.PRIMARY_KEY_COLUMN].write(self.num_records, record.key)
        for column in range(len(record.columns)):
            self.pages[column + 4].write(self.num_records, record.columns[column])
        self.num_records += 1
        return (self, offset)

    # Function to read record based on row_number
    def read(self, offset):
        columns = []
        for column in range(4, len(self.pages)):
            columns.append(self.pages[column].read(offset))
        return columns
    
    # Function to delete record based on row_number
    # NOTE: does not delete the data in the record, only sets the RID to -1
    def delete(self, offset):
        self.pages[lstore.config.RID_COLUMN].write(offset, lstore.config.DELETED_RECORD_RID)

    # Function to check if page is full of records
    def is_full(self):
        return self.num_records == 512

# Class for a Page Range
# Properly manages insertions into next available base record and allocating tail pages as needed
class Page_Range:
    def __init__(self, num_columns):
        # Initialize base pages of page range
        self.base_pages = []
        for i in range(lstore.config.BASE_PAGE_PER_PAGE_RANGE):
            self.base_pages.append(Conceptual_Page(num_columns))

        # Initialize tail pages of page range
        self.tail_pages = []
        self.tail_pages.append(Conceptual_Page(num_columns))

        # Track number of base and tail records
        self.num_base_records = 0
        self.num_tail_records = 0
        self.num_columns = num_columns

    def insert(self, record):
        if self.base_pages_full():
            return
        base_page_number = int(self.num_base_records // lstore.config.RECORDS_PER_PAGE)
        offset = self.num_base_records % lstore.config.RECORDS_PER_PAGE
        self.num_base_records += 1
        return self.base_pages[base_page_number].insert(offset, record)
    
    def update(self, record):
        if(self.num_tail_records > lstore.config.RECORDS_PER_PAGE * len(self.tail_pages)):
            self.tail_pages.append(Conceptual_Page(self.num_columns))
            self.current_tail_page += 1
        tail_page_number = int(self.num_tail_records // lstore.config.RECORDS_PER_PAGE)
        offset = self.num_tail_records % lstore.config.RECORDS_PER_PAGE
        return self.tail_pages[tail_page_number].insert(offset, record)
        
    def read(self, page_number, base_or_tail, offset):
        if base_or_tail == 0:
            return self.base_pages[page_number].read(offset)
        return self.tail_pages[page_number].read(offset)

    def base_pages_full(self):
        return self.num_base_records >= lstore.config.BASE_PAGE_PER_PAGE_RANGE * lstore.config.RECORDS_PER_PAGE

class Table:

    """
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
    def __init__(self, name, num_columns, key):
        self.num_records = 0
        self.name = name
        self.key = key
        self.num_columns = num_columns
        self.page_directory = dict()
        self.index = Index(self)
        self.page_ranges = []
        self.page_ranges.append(Page_Range(num_columns))
        self.current_page_range = 0
        pass

    def insert(self, record):
        if self.page_ranges[self.current_page_range].base_pages_full():
            self.page_ranges.append(Page_Range(self.num_columns))
            self.current_page_range += 1
        self.page_directory[self.num_records] = self.page_ranges[self.current_page_range].insert(record)
        self.num_records += 1
        pass


    def __merge(self):
        print("merge is happening")
        pass

