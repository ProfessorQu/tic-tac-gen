use std::fmt::Display;

use super::Cell;

pub enum GameResult {
    XWon,
    OWon,
    Draw,
}

impl From<Cell> for GameResult {
    fn from(value: Cell) -> Self {
        match value {
            Cell::Empty => GameResult::Draw,
            Cell::X => GameResult::XWon,
            Cell::O => GameResult::OWon,
        }
    }
}

impl Display for GameResult {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            GameResult::Draw => f.write_str("Draw"),
            GameResult::XWon => f.write_str("X Won"),
            GameResult::OWon => f.write_str("O Won"),
        }
    }
}
