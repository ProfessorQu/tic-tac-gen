use super::{cell::Cell, game_result::GameResult};

#[derive(Clone, Debug)]
pub struct Board {
    board: [[Cell; 3]; 3],
}

impl Board {
    pub fn empty() -> Self {
        Self {
            board: [[Cell::Empty; 3]; 3],
        }
    }

    pub fn get(&self, x: usize, y: usize) -> Cell {
        self.board[x][y]
    }

    pub fn set(&mut self, x: usize, y: usize, cell: Cell) {
        if self.board[x][y] == Cell::Empty {
            self.board[x][y] = cell;
        }
    }

    pub fn result(&self) -> Option<GameResult> {
        for i in 0..3usize {
            // Check rows
            if self.get(i, 0) == self.get(i, 1)
                && self.get(i, 1) == self.get(i, 2)
                && self.get(i, 0) != Cell::Empty
            {
                return Some(self.get(i, 0).into());
            }

            // Check columns
            if self.get(0, i) == self.get(1, i)
                && self.get(1, i) == self.get(2, i)
                && self.get(0, i) != Cell::Empty
            {
                return Some(self.get(0, i).into());
            }
        }

        // Check top-left to bottom-right diagonal
        if self.get(0, 0) == self.get(1, 1)
            && self.get(1, 1) == self.get(2, 2)
            && self.get(0, 0) != Cell::Empty
        {
            return Some(self.get(0, 0).into());
        }

        // Check bottom-left to top-right diagonal
        if self.get(0, 2) == self.get(1, 1)
            && self.get(1, 1) == self.get(2, 0)
            && self.get(0, 2) != Cell::Empty
        {
            return Some(self.get(0, 2).into());
        }

        // Check if the game still has empty spaces
        for x in 0..3 {
            for y in 0..3 {
                if self.get(x, y) == Cell::Empty {
                    return None;
                }
            }
        }

        Some(GameResult::Draw)
    }

    pub fn count_xs(&self) -> usize {
        let mut num_xs = 0;
        for x in 0..3 {
            for y in 0..3 {
                if self.get(x, y) == Cell::X {
                    num_xs += 1;
                }
            }
        }

        num_xs
    }

    pub fn count_os(&self) -> usize {
        let mut num_os = 0;
        for x in 0..3 {
            for y in 0..3 {
                if self.get(x, y) == Cell::O {
                    num_os += 1;
                }
            }
        }

        num_os
    }

    pub fn possible_moves(&self) -> Vec<(usize, usize)> {
        let mut moves = vec![];
        for x in 0..3 {
            for y in 0..3 {
                if self.get(x, y) == Cell::Empty {
                    moves.push((x, y));
                }
            }
        }

        moves
    }

    pub fn board_string(&self) -> String {
        let mut board_string = String::new();

        for y in 0..3 {
            for x in 0..3 {
                board_string += self.get(x, y).into();
                if x < 2 {
                    board_string += "|";
                }
            }

            if y < 2 {
                board_string += "\n------\n";
            }
        }

        board_string
    }
}
