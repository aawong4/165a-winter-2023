from lstore.index import Index
<<<<<<< Updated upstream
from time import time
=======
>>>>>>> Stashed changes

INDIRECTION_COLUMN = 0
RID_COLUMN = 1
TIMESTAMP_COLUMN = 2
SCHEMA_ENCODING_COLUMN = 3


<<<<<<< Updated upstream
class Record:

    def __init__(self, rid, key, columns):
        self.rid = rid
        self.key = key
        self.columns = columns

=======
>>>>>>> Stashed changes
class Table:

    """
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
    def __init__(self, name, num_columns, key):
        self.name = name
        self.key = key
        self.num_columns = num_columns
        self.page_directory = {}
        self.index = Index(self)
<<<<<<< Updated upstream
=======
        self.rid_counter = 0
        self.base_list = []
        self.tail_list = []
>>>>>>> Stashed changes
        pass

    def __merge(self):
        print("merge is happening")
        pass
 
