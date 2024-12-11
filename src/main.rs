use tictactoe::Player;
use tree::GameTree;

mod tictactoe;
mod tree;

fn main() {
    let mut gametree = GameTree::new();
    gametree.assert_correct();

    let collapsed = gametree.collapse(Player::O);
    collapsed.assert_correct();
}
