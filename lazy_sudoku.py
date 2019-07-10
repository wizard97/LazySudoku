import copy
import sys

class SudokuError(Exception):
  pass


class Tile(object):
  def __init__(self, position, val=None):
    self.pos = position
    self.val = None
    if isinstance(val, int):
      self.val = val
      self.possible = {val}
    elif val is None:
      self.possible = {i for i in range(1, 10)}
    else:
      self.possible = val

  def value(self):
    return self.val

  def position(self):
    return self.pos

  def possibles(self):
    return self.possible

  def setValue(self, val):
    self.val = val
    self.possible = {val}

  def setNot(self, val):
    ret = val in self.possible
    self.possible.discard(val)
    if len(self.possible) == 0:
      raise SudokuError("No possible value for tile in {}".format(self.pos))
    if self.known() and ret:
      self.val = list(self.possible)[0]
    return ret

  def known(self):
    return len(self.possible) == 1

  def __repr__(self):
    return str(self.possible)


def make_board(board):
  blines = board.split()
  bd = []

  for i,l in enumerate(blines):
    ls = l.strip()
    assert len(ls) == 9
    line = [Tile((i,j), int(c) if c.isdigit() else None) for j,c in enumerate(ls)]
    bd.append(line)
  return bd


def str_board(b):
  conv = lambda c: str(c.value()) if c.known() else ' '
  return '\n'.join(['|'.join(map(conv, l)) for l in b])


def flatten(bd):
  flat = []
  for l in bd:
    flat.extend(l)
  return flat

def solve(bd):
  work = set(filter(lambda t: t.known(), flatten(bd)))
  def tile_apply(tile, val):
    if tile.setNot(val) and tile not in work:
      work.add(tile)
  board_flat = flatten(bd)

  while len(work) > 0:
    t = work.pop()
    x, y = t.position()
    if t.known(): # Apply constraints to sourondings
      # same row
      tiles = bd[x][:]
      # Same col
      tiles += board_flat[y::9]
      # Same square
      row = 3*(x // 3)
      col = 3*(y //3)
      tiles += [bd[j][i] for i in range(col, col+3) for j in range(row, row+3)]
      for tile in tiles:
        if tile is not t:
          tile_apply(tile, t.value())
  # If the board is not solved, make a guess and recurse
  unknown = [t for t in board_flat if not t.known()]
  # Check if we solved it!
  if len(unknown) == 0:
    return bd
  # Otherwise pick a tile to guess on and recurse
  tile_guess = min(unknown, key= lambda t : len(t.possibles()))
  for guess in tile_guess.possibles():
    # Deep copy the board so we can recover
    tmp = copy.deepcopy(bd)
    try:
      gx, gy = tile_guess.position()
      tmp[gx][gy].setValue(guess)
      return solve(tmp)
    except SudokuError as e:
      pass # Earlier incorrect tile assignment, recover
  raise SudokuError('Unsolvable board')


def main():
  if len(sys.argv) != 2:
    print("Usage: '{} <board.txt>'".format(sys.argv[0]))
    return
  with open(sys.argv[1]) as fd:
    board_txt = fd.read()
    board = make_board(board_txt)
    print("INPUT BOARD:")
    print(str_board(board))
    solved = solve(board)
    print("\nSOLVED BOARD:")
    print(str_board(solved))


if __name__ == "__main__":
  main()
