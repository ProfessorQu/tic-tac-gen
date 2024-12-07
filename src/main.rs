use std::io::{self, BufRead};

use tictactoe::Game;
use tree::Minimax;

mod tictactoe;
mod tree;

fn _play_game() {
    let mut game = Game::new();

    while game.board().result().is_none() {
        println!("{}", game.board_string());

        let stdin = io::stdin();
        let input = stdin.lock().lines().next().unwrap().unwrap();

        let player_move: usize = input.parse().unwrap();

        let x = player_move % 3;
        let y = player_move / 3;

        game.make_move(x, y);
    }

    println!("{}", game.board_string());
    println!("{} won!", game.board().result().unwrap());
}

fn main() {
    let mut minimax = Minimax::new();

    minimax.generate();

    minimax.print();
    
    let mut game = Game::new();

    while game.board().result().is_none() {
        println!("{}", game.board_string());

        let stdin = io::stdin();
        let input = stdin.lock().lines().next().unwrap().unwrap();

        let player_move: usize = input.parse().unwrap();

        let x = player_move % 3;
        let y = player_move / 3;

        game.make_move(x, y);
    }
}
