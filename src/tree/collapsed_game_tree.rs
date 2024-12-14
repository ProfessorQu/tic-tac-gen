use crate::tictactoe::Player;

use super::{constants::MOVE_VAR_NAME, node::Node};

#[derive(Debug)]
pub struct CollapsedGameTree {
    root: Node,
    collapsed_player: Player,
}

impl CollapsedGameTree {
    pub fn new(root: Node, collapsed_player: Player) -> Self {
        Self {
            root,
            collapsed_player,
        }
    }

    pub fn assert_correct(&self) {
        self.root.assert_collapsed_correct(0, self.collapsed_player);
    }

    pub fn python_code(&self) -> String {
        self.root.python(0)
    }

    pub fn java_code(&self) -> String {
        let mut code = "import java.util.Scanner;\n".to_string();
        code += "class Main {\n";

        code += "\tpublic static void main(String[] args) {\n";

        code += "\t\tScanner scanner = new Scanner(System.in);\n";
        code += format!("\t\tint {MOVE_VAR_NAME};\n").as_str();

        code += self.root.java(2).as_str();

        code += "\t\tscanner.close();\n";
        code += "\t}\n";
        code += "}";

        code
    }
    
    pub fn c_code(&self) -> String {
        let mut code = "#include <stdio.h>\n".to_string();
        code += "int main() {\n";
        code += format!("\tint {MOVE_VAR_NAME};\n").as_str();

        code += self.root.c(1).as_str();

        code += "\treturn 0;\n";
        code += "}";

        code
    }

    pub fn rust_code(&self) -> String {
        let mut code = "use std::io::{stdout, stdin, Write};".to_string();
        code += "fn main() {\n";
        code += format!("\tlet mut {MOVE_VAR_NAME} = String::new();\n").as_str();

        code += self.root.rust(1).as_str();

        code += "}";

        code
    }
}
