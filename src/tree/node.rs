use std::collections::HashMap;

use crate::tictactoe::{Board, GameResult, Player};

#[derive(Debug, Clone)]
pub struct Node {
    board: Board,
    turn: Player,
    value: f32,
    children: HashMap<(usize, usize), Box<Node>>,
}

impl Node {
    pub fn new(board: Board, turn: Player) -> Self {
        Self {
            board,
            turn,
            value: 0.0,
            children: HashMap::new(),
        }
    }

    pub fn generate(&mut self) {
        if let Some(result) = self.board.result() {
            match result {
                GameResult::Draw => self.value = 0.0,
                GameResult::XWon => self.value = 1.0,
                GameResult::OWon => self.value = -1.0,
            }

            return;
        }

        let possible_moves = self.board.possible_moves();

        let mut total_children_value = 0.0;
        let total_children = possible_moves.len() as f32;

        for (x, y) in possible_moves {
            let mut child_board = self.board.clone();
            child_board.set(x, y, self.turn.cell());

            let mut child = Node::new(child_board, self.turn.opponent());
            child.generate();

            total_children_value += child.value;

            self.children.insert((x, y), Box::new(child));
        }

        self.value = total_children_value / total_children;
    }

    pub fn assert_correct_board(&self, turn_num: usize) {
        let num_xs = self.board.count_xs();
        let num_os = self.board.count_os();

        assert!(num_xs == turn_num);
        if self.turn == Player::X {
            assert!(num_os == turn_num);
            for child in self.children.values() {
                child.assert_correct_board(turn_num + 1);
            }
        } else {
            assert!(num_os + 1 == turn_num);
            for child in self.children.values() {
                child.assert_correct_board(turn_num);
            }
        }
    }
}
