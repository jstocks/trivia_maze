import unittest
from gameboard import GameBoard


def set_up():
    gameboard = GameBoard(4, 4)
    gameboard.place_entrance_exit()
    gameboard.update_border_paths()
    return gameboard


class GameBoardTests(unittest.TestCase):
    """
    Tests for GameBoard class
    """

    def test_traverse_exit_blocked(self):
        # block exit
        gameboard = set_up()
        gameboard.cell_at(3, 3).remove_path(gameboard.cell_at(3, 2), "N")
        gameboard.cell_at(3, 3).remove_path(gameboard.cell_at(2, 3), "W")
        self.assertEqual(False, gameboard.traverse(0, 0), "Error: Unknown Bug in Traverse method")

    def test_traverse_entrance_blocked(self):
        # block entrance
        gameboard = set_up()
        (x, y) = (0, 0)
        gameboard.cell_at(0, 0).remove_path(gameboard.cell_at(x, y + 1), "S")
        gameboard.cell_at(0, 0).remove_path(gameboard.cell_at(x + 1, y), "E")
        self.assertEqual(False, gameboard.traverse(0, 0), "Error: Unknown Bug in Traverse method")

    def test_traverse_path_blocked(self):
        gameboard = set_up()
        gameboard.cell_at(2, 2).remove_path(gameboard.cell_at(2, 1), "N")
        gameboard.cell_at(2, 2).remove_path(gameboard.cell_at(1, 2), "W")
        gameboard.cell_at(3, 2).remove_path(gameboard.cell_at(3, 1), "N")
        gameboard.cell_at(2, 3).remove_path(gameboard.cell_at(1, 3), "W")
        self.assertEqual(False, gameboard.traverse(0, 0), "Error: Unknown Bug in Traverse method")


if __name__ == '__main__':
    unittest.main()