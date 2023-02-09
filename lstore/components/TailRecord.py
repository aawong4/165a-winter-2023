from lstore.components.Record import Record


class TailRecord(Record):
    """
    @author Maintain by ShangqiCai
    """

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
