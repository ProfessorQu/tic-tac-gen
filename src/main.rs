use tree::Minimax;

mod tictactoe;
mod tree;

// fn _play_game() {
//     let stdin = io::stdin();
//     let input = stdin.lock().lines().next().unwrap().unwrap();

//     let player_move: usize = input.parse().unwrap();

//     let x = player_move % 3;
//     let y = player_move / 3;
// }

fn main() {
    let mut minimax = Minimax::new();

    minimax.generate();
    minimax.collapse(tictactoe::Cell::O);

    // println!("{:?}", minimax);
    minimax.print();

    minimax.to_python("main.py");
}
