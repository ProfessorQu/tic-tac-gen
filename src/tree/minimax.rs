use std::{fs::File, io::Write};

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

    pub fn collapse(&mut self, player: Cell) {
        self.root.collapse(player);
    }

    pub fn print(&self) {
        // self.root.print();
    }

    pub fn to_python(&self, filename: &str) {
        // let mut code = format!("print({:?})", self.root.board_string());
        let mut code = self.root.code(0);
        code += "\n";
        code = code.replace("\n\n", "\n");

        let mut file = File::create(filename).expect("Failed to create file");
        file.write_all(code.as_bytes()).expect("Failed to write to file");
    }
}
