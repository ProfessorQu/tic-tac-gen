use std::fmt::Display;

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Cell {
    Empty,
    O,
    X
}

impl Cell {
    pub fn opponent(&self) -> Self {
        match self {
            Cell::O => Cell::X,
            Cell::X => Cell::O,
            Cell::Empty => panic!("'Empty' has no opponent")
        }
    }
}

impl Display for Cell {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", Into::<&str>::into(*self))
    }
}

impl From<Cell> for &str {
    fn from(value: Cell) -> Self {
        match value {
            Cell::O => "O",
            Cell::X => "X",
            Cell::Empty => " "
        }
    }
}
