<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
class Page:

    def __init__(self):
        self.num_records = 0
        self.data = bytearray(4096)

<<<<<<< Updated upstream
    def has_capacity(self):
        pass

    def write(self, value):
=======
    def write(self, value):
        if self.has_space is False:
            print("Page is full.")
            return

        byte_value = value.to_bytes(8, byteorder='big')
        i = self.num_records * 8

        self.data[i:i+8] = byte_value
>>>>>>> Stashed changes
        self.num_records += 1
        pass

<<<<<<< Updated upstream
=======
    def update(self, value, index):

        byte_value = value.to_bytes(8, byteorder='big')
        i = index * 8
        self.data[i:i + 8] = byte_value

    def read(self, index):
        if index >= self.num_records:
            print("ERROR: Index out of range.")
            return

        i = index * 8
        return int.from_bytes(self.data[i:i+8], byteorder='big')

    def delete(self, index):
        if index >= self.num_records:
            print("ERROR: Index out of range.")
            return

        byte_value = (0).to_bytes(8, byteorder='big')
        i = index * 8

        self.data[i:i+8] = byte_value

    def has_space(self):
        return self.num_records < 512
>>>>>>> Stashed changes
