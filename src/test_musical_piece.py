import unittest
import datetime

from musical_piece import MusicalPiece, RepetoirePiece


class TestMusicalPiece(unittest.TestCase):
    def test_repr(self):
        title = "Romance"
        composer = "Anonymous"
        piece = MusicalPiece(title, composer)
        self.assertEqual(
            repr(piece),
            f"MusicalPiece({title}, {composer})"
        )
        

class TestRepetoirePiece(unittest.TestCase):
    def test_repr(self):
        title = "Romance"
        composer = "Anonymous"
        retained = True
        piece = RepetoirePiece(title, composer, retained)
        self.assertEqual(
            repr(piece),
            f"RepetoirePiece({title}, {composer}, {retained}, {datetime.date.today()})"
        )
    
    
if __name__ == "__main__":
    unittest.main()
