use crate::tictactoe::Player;

use super::node::Node;

#[derive(Debug)]
pub struct CollapsedGameTree {
    root: Node,
    collapsed_player: Player
}

impl CollapsedGameTree {
    pub fn new(root: Node, collapsed_player: Player) -> Self {
        Self {
            root,
            collapsed_player
        }
    }

    pub fn assert_correct(&self) {
        self.root.assert_collapsed_correct(0, self.collapsed_player);
    }
}
