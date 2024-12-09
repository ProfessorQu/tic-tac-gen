use crate::tictactoe::{Board, Player};

use super::{node::Node, CollapsedGameTree};

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

    pub fn collapse(&mut self) -> CollapsedGameTree {
        let collapsed_player = Player::O;
        let mut new_root = self.root.clone();
        new_root.collapse(collapsed_player);

        CollapsedGameTree::new(new_root, collapsed_player)
    }

    pub fn assert_correct(&self) {
        self.root.assert_correct(0);
    }
}