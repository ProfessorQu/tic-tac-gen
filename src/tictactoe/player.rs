use super::Cell;

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum Player {
    X,
    O,
}

impl Player {
    pub fn opponent(&self) -> Self {
        match self {
            Player::O => Player::X,
            Player::X => Player::O,
        }
    }

    pub fn cell(&self) -> Cell {
        match self {
            Player::O => Cell::O,
            Player::X => Cell::X,
        }
    }
}
