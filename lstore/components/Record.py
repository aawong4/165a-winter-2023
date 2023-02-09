
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

