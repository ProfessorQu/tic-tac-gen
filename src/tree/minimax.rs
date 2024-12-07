use crate::tictactoe::{Board, Cell};

use super::node::Node;

#[derive(Debug)]
pub struct Minimax {
    root: Node
}

impl Minimax {
    pub fn new() -> Self {
        Self {
            root: Node::new(Board::empty(), Cell::X)
        }
    }

    pub fn generate(&mut self) {
        self.root.generate();
    }

    pub fn print(&self) {
        println!("{:?}", self.root.winner);
    }
}
