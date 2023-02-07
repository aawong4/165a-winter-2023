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
