import lstore.config


# Page class: Page has 4096 bytes, each record is 8 bytes
# Total: 512 records per page
class Physical_Page:

    def __init__(self):
        self.num_records = 0
        self.data = bytearray(lstore.config.BYTES_PER_PAGE)

    # Returns if the page has space for a new record
    def has_capacity(self):
        return self.num_records < lstore.config.BYTES_PER_PAGE / lstore.config.BYTES_PER_ENTRY

    # Writes to the entry indicated by the offset
    def write(self, offset, value):
        next_entry = offset * lstore.config.BYTES_PER_ENTRY
        self.data[next_entry: next_entry + lstore.config.BYTES_PER_ENTRY] = value.to_bytes(
            lstore.config.BYTES_PER_ENTRY, 'big')
        self.num_records += 1

    # Returns data of page
    def read(self, offset):
        row_number = self.data[
                     offset * lstore.config.BYTES_PER_ENTRY: offset * lstore.config.BYTES_PER_ENTRY + lstore.config.BYTES_PER_ENTRY]
        return int.from_bytes(row_number)

    # Reset the number of valid records to 0
    # NOTE: this does not clear the actual data in the entries
    def clean(self):
        self.num_records = 0
