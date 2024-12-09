use tree::GameTree;

mod tictactoe;
mod tree;

fn main() {
    let mut gametree = GameTree::new();

    gametree.generate();
    gametree.assert_correct();

    let collapsed = gametree.collapse();
    collapsed.assert_correct();
}
