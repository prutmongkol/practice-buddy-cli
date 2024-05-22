import datetime


class MusicalPiece:
    def __init__(self, title: str, composer: str) -> None:
        self.title = title
        self.composer = composer
        
    def __repr__(self) -> str:
        return f"MusicalPiece({self.title}, {self.composer})"
    

class RepetoirePiece(MusicalPiece):
    def __init__(self, title: str, composer: str, retained=False, last_practice_date=None) -> None:
        super().__init__(title, composer)
        self._retained = retained
        self.last_practice_date = last_practice_date or datetime.date.today()

    def update_retained(self, retained=False) -> None:
        self._retained = retained
        self.last_practice_date = datetime.date.today()
        
    def __repr__(self) -> str:
        return f"RepetoirePiece({self.title}, {self.composer}, {self._retained}, {self.last_practice_date})"
