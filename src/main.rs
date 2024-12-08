use tree::Minimax;

mod tictactoe;
mod tree;

fn main() {
    let mut minimax = Minimax::new();

    minimax.generate();
    minimax.collapse(tictactoe::Cell::O);

    // println!("{:?}", minimax);
    // minimax.print();

    minimax.to_python("main.py");
}
