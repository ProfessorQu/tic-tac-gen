use std::{fs::File, io::Write};

use clap::{arg, Parser, ValueEnum};
use tictactoe::Player;
use tree::GameTree;

mod tictactoe;
mod tree;

#[derive(ValueEnum, Clone)]
enum PlayerArg {
    X,
    O,
}

#[derive(ValueEnum, Clone)]
enum LanguageArg {
    Python,
}

#[derive(Parser)]
struct Args {
    /// What name to give the new file
    #[arg(short, long)]
    filename: String,

    /// Which player should be the opponent
    #[arg(short, long, default_value = "o")]
    player: PlayerArg,

    /// What language should the code be generated in
    #[arg(short, long, default_value = "python")]
    language: LanguageArg,
}

fn main() {
    let args = Args::parse();

    let player = match args.player {
        PlayerArg::O => Player::O,
        PlayerArg::X => Player::X,
    };

    let gametree = GameTree::new();
    gametree.assert_correct();

    let collapsed = gametree.collapse(player);
    collapsed.assert_correct();

    let code = match args.language {
        LanguageArg::Python => collapsed.python_code(),
    };

    let mut file = File::create(args.filename).unwrap();
    file.write_all(code.as_bytes()).unwrap();
}
