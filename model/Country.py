from dataclasses import dataclass

@dataclass
class Country:
    CCode: int
    StateAbb: str
    StateNme: str

    def __eq__(self, other):
        return self.StateAbb == other.StateAbb
    def __hash__(self):
        return hash(self.StateAbb)
    def __str__(self):
        return f"{self.StateAbb} - {self.StateNme}"
    def __lt__(self, other):
        """
        permette il confronto tra due oggetti country
        viene usato da .sort()
        """
        return self.StateNme.lower() < other.StateNme.lower()
