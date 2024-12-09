use crate::tictactoe::{Board, Player};

use super::node::Node;

#[derive(Debug)]
pub struct GameTree {
    root: Node,
}

impl GameTree {
    pub fn new() -> Self {
        Self {
            root: Node::new(Board::empty(), Player::X),
        }
    }

    pub fn generate(&mut self) {
        self.root.generate();
    }

    pub fn assert_correct_boards(&self) {
        self.root.assert_correct_board(0);
    }
}
