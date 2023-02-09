from lstore.index import Index
from time import time

INDIRECTION_COLUMN = 0
RID_COLUMN = 1
TIMESTAMP_COLUMN = 2
SCHEMA_ENCODING_COLUMN = 3

# begin of Maintain
class Record:
    """
    @author Maintain by ShangqiCai
    """

    def __init__(self, rid: int, key: int, columns: list):
        self.rid = rid
        self.key = key
        self.columns = columns

        """
     need to initialize the size of record
     when create a record in correspond table
     ________table________
     | c1 | c2 | c3 | c4 |
     |Key |Data|Data|Data| (Record)
     |Key |Data|Data|Data|
     |Key |Data|Data|Data|
     |Key |Data|Data|Data|
    """


# THE KEY OF RECORD SHOULD NOT BE CHANGED!


class TailRecord(Record):
    """
    when the update is happen, the new TailRecord should append to the tailPage
    last TailRecord, it should first get the last TailRecord update_id, and set
    this id to new TailRecord :param previous_pointer. After that, the new TailRecord
    should have its own update_id prepare.
    
    When it can not fetch the last TailRecord update_id, it means this tail record 
    is the first one append to tailPage, Set the :param previous_pointer to None 
    or something?
    """

    def __init__(self, rid: int, key: int, columns: list, previous_pointer: int):
        super().__init__(rid, key, columns)
        # this should point to the previous TailRecord
        self.previous_pointer = previous_pointer
        # the generated update id
        self.update_id = None

    # return the update_id
    def getUpdateId(self) -> int:
        return self.update_id

    def setUpdateId(self, update_id: int) -> None:
        self.update_id = update_id

    """
    :raise None if not found
    """

    def getPreviousPointer(self) -> int | None:
        if self.previous_pointer:
            return self.previous_pointer
        else:
            return None


# end of Maintain

class Table:
    """
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """

    def __init__(self, name, num_columns, key):
        self.name = name
        self.key = key
        self.num_columns = num_columns
        self.page_directory = {}
        self.index = Index(self)
        pass

    def __merge(self):
        print("merge is happening")
        pass
