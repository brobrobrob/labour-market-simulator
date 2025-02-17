import uuid

class BaseEmployee:
    def __init__(self,
                 name: str,
                 productivity: int
                 ):
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.productivity: int = productivity

    def __eq__(self, other):
        if isinstance(other, BaseEmployee):
            return self.id == other.id
        else: return False


    