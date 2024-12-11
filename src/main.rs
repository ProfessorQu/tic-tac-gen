use std::{fs::File, io::Write};

use tictactoe::Player;
use tree::GameTree;

mod tictactoe;
mod tree;

fn main() {
    let mut gametree = GameTree::new();
    gametree.assert_correct();

    let collapsed = gametree.collapse(Player::O);
    collapsed.assert_correct();
    
    let code = collapsed.python_code();

    let mut file = File::create("main.py").unwrap();
    file.write_all(code.as_bytes()).unwrap();
}
