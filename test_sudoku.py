from sudoku import Sudoku
import pytest

@pytest.fixture
def sudoku():
    sudoku=Sudoku()
    return sudoku

@pytest.fixture
def possible_sudoku(sudoku):
    sudoku.set_board([
        [0, 8, 0, 0, 2, 0, 5, 6, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 9, 0, 4, 0, 8],
        [0, 0, 7, 8, 0, 0, 0, 0, 3],
        [0, 9, 0, 0, 1, 0, 0, 5, 0],
        [2, 0, 4, 0, 0, 0, 8, 0, 0],
        [0, 6, 0, 0, 8, 5, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 1, 0, 0]
    ])
    return sudoku

@pytest.fixture
def impossible_sudoku(sudoku):
    sudoku.set_board([
        [0, 7, 0, 0, 0, 6, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 4, 1],
        [0, 0, 8, 0, 0, 9, 0, 5, 0],
        [0, 9, 0, 0, 0, 9, 0, 5, 0],
        [0, 0, 3, 0, 0, 0, 8, 0, 0],
        [4, 0, 0, 8, 0, 0, 0, 1, 0],
        [0, 8, 0, 3, 0, 0, 9, 0, 0],
        [1, 6, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 5, 0, 0, 0, 8, 0]
    ])
    return sudoku

@pytest.fixture
def solved_sudoku(sudoku):
    sudoku.set_board([
        [4, 8, 3, 7, 2, 9, 5, 6, 1],
        [5, 2, 9, 1, 4, 6, 3, 8, 7],
        [7, 1, 6, 5, 3, 8, 2, 4, 9],
        [1, 5, 2, 6, 9, 3, 4, 7, 8],
        [6, 4, 7, 8, 5, 2, 9, 1, 3],
        [3, 9, 8, 4, 1, 7, 6, 5, 2],
        [2, 7, 4, 9, 6, 1, 8, 3, 5],
        [9, 6, 1, 3, 8, 5, 7, 2, 4],
        [8, 3, 5, 2, 7, 4, 1, 9, 6]
    ])
    return sudoku

@pytest.fixture
def badly_solved_sudoku(sudoku):
    sudoku.set_board([
        [4, 8, 3, 7, 2, 9, 5, 6, 1],
        [5, 2, 9, 1, 4, 6, 3, 8, 7],
        [7, 1, 6, 5, 3, 8, 2, 4, 9],
        [1, 5, 2, 6, 9, 3, 4, 7, 8],
        [6, 4, 7, 8, 4, 2, 9, 1, 3],
        [3, 9, 8, 4, 1, 7, 6, 5, 2],
        [2, 7, 4, 9, 6, 1, 8, 3, 5],
        [9, 6, 1, 3, 8, 5, 7, 2, 4],
        [8, 3, 5, 2, 7, 4, 1, 9, 6]
    ])
    return sudoku

def test_solve_positive(possible_sudoku):
    assert possible_sudoku.solve() == True

def test_solve_impossible(impossible_sudoku):
    assert impossible_sudoku.solve() == False

def test_set_board_with_0(sudoku):
    from numpy import array, array_equal
    sudoku.set_board([
        [0, 8, 0, 0, 2, 0, 5, 6, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 9, 0, 4, 0, 8],
        [0, 0, 7, 8, 0, 0, 0, 0, 3],
        [0, 9, 0, 0, 1, 0, 0, 5, 0],
        [2, 0, 4, 0, 0, 0, 8, 0, 0],
        [0, 6, 0, 0, 8, 5, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 1, 0, 0]
    ])
    assert array_equal(sudoku.board, array(
        [[[1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 7],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 8],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 5,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
    ))

def test_set_board_with_None(sudoku):
    from numpy import array, array_equal
    sudoku.set_board([
        [None, 8, None, None, 2, None, 5, 6, None],
        [None, None, None, 1, None, None, None, None, 7],
        [None, None, None, None, None, None, None, None, None],
        [None, 5, None, None, 9, None, 4, None, 8],
        [None, None, 7, 8, None, None, None, None, 3],
        [None, 9, None, None, 1, None, None, 5, None],
        [2, None, 4, None, None, None, 8, None, None],
        [None, 6, None, None, 8, 5, None, None, None],
        [None, None, None, 2, None, None, 1, None, None]
    ])
    assert array_equal(sudoku.board, array(
        [[[1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 7],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 8],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 5,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2,
          [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
    ))

def test_str(solved_sudoku):
    assert str(solved_sudoku)==\
    """4 8 3 7 2 9 5 6 1 
5 2 9 1 4 6 3 8 7 
7 1 6 5 3 8 2 4 9 
1 5 2 6 9 3 4 7 8 
6 4 7 8 5 2 9 1 3 
3 9 8 4 1 7 6 5 2 
2 7 4 9 6 1 8 3 5 
9 6 1 3 8 5 7 2 4 
8 3 5 2 7 4 1 9 6 """

def test_get_progress(possible_sudoku):
    assert possible_sudoku.get_progress()==(29,24)

def test_validate_board_positive(solved_sudoku):
    assert solved_sudoku.validate_board() == True

def test_validate_board_negative(badly_solved_sudoku):
    assert badly_solved_sudoku.validate_board() == False

def test_validate_cell_new_val_positive(possible_sudoku):
    assert possible_sudoku.validate_cell_new_val(0,0,4) == True

def test_validate_cell_new_val_negative(possible_sudoku):
    assert possible_sudoku.validate_cell_new_val(0,0,8) == False
