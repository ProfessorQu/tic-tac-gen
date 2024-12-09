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
