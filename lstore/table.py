from lstore.index import Index
from time import time
from lstore.components.Record import Record
from components.Record import Record
import components
from page import Page_Range

INDIRECTION_COLUMN = 0
RID_COLUMN = 1
TIMESTAMP_COLUMN = 2
SCHEMA_ENCODING_COLUMN = 3



class Table:
    """
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """

    def __init__(self, name, num_columns, key, base_page, tail_page):
        self.name = name
        self.key = key
        self.num_columns = num_columns
        self.page_directory = {}
        self.page_range_list = [Page_Range(num_columns)]
        self.index = Index(self)
        self.rid_counter = 0
        pass

    def __merge(self):
        print("merge is happening")
        pass
