# Page class: Page has 4096 bytes, each record is 8 bytes
# Total: 512 records per page

class Page:

    def __init__(self):
        self.num_records = 0
        self.data = bytearray(4096)

    # Returns if the page has space for a new record
    def has_capacity(self):
        return self.num_records < 512
        
    # Writes value to next available record
    def write(self, value):
        write_offset = self.num_records * 8
        self.data[write_offset : write_offset + 8] = value.to_bytes(8, 'big')
        self.num_records += 1

    # Returns data of page
    def read(self):
        return self.data

# Modified by Kenny Sun @ 2/11/2023
class BasePage:
    def __init__(self, column_num):
        self.num = column_num
        self.columns = []
        for i in range(column_num + 4):
            self.columns.append(Page())



class TailPage:
    def __init__(self, column_num):
        self.num = column_num
        self.columns = []
        row_num = 0
        for i in range(column_num + 4):
            self.columns.append(Page())



class Page_Range:
    def __init__(self, column_num):
        self.column_num = column_num
        self.base_page_list = [BasePage(column_num)]
        self.tail_page_list = [TailPage(column_num)]
    # INDIRECTION_COLUMN = 0
    # RID_COLUMN = 1
    # TIMESTAMP_COLUMN = 2
    # SCHEMA_ENCODING_COLUMN = 3
    def append(self, columns):
        if not self.tail_page_list[-1].columns[0].has_capacity():
            self.tail_page_list.append(TailPage(self.column_num))
        else:
            for i in range(len(columns)):
                self.tail_page_list[-1].columns[i].write(columns[i])
    pass
