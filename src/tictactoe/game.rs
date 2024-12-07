use super::{board::Board, cell::Cell};

pub struct Game {
    board: Board,
    turn: Cell,
}

impl Game {
    pub fn new() -> Self {
        Self {
            board: Board::empty(),
            turn: Cell::X,
        }
    }

    pub fn make_move(&mut self, x: usize, y: usize) {
        self.board.set(x, y, self.turn);
        self.turn = match self.turn {
            Cell::X => Cell::O,
            Cell::O => Cell::X,
            Cell::Empty => panic!("Player's turn cannot be Empty!"),
        }
    }

    pub fn board(&self) -> Board {
        self.board.clone()
    }

    pub fn board_string(&self) -> String {
        self.board.board_string()
    }
}
