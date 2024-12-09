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

    pub fn collapse(&mut self, player: Player) {
        if self.board.result().is_some() {
            return;
        } else if self.turn != player {
            for child in self.children.values_mut() {
                child.collapse(player);
            }

            return;
        }

        for child in self.children.values_mut() {
            child.collapse(player);
        }

        let mut best_move = self
            .children
            .values()
            .next()
            .expect("Should have children")
            .clone();
        let mut best_value = match player {
            Player::X => f32::MIN,
            Player::O => f32::MAX,
        };

        for child in self.children.values() {
            match self.turn {
                Player::X => {
                    if child.value > best_value {
                        best_value = child.value;
                        best_move = child.clone();
                    }
                }
                Player::O => {
                    if child.value < best_value {
                        best_value = child.value;
                        best_move = child.clone();
                    }
                }
            }
        }

        self.children = best_move.children;
        self.board = best_move.board;
        self.turn = best_move.turn;
        self.value = best_move.value;
    }

    fn create_info_string(
        &self,
        num_xs: usize,
        num_os: usize,
        turn_num: usize,
    ) -> String {
        let boards: String = self
            .children
            .iter()
            .map(|((_x, _y), child)| child.board.board_string())
            .collect::<Vec<String>>()
            .join("\n===========================\n");

        format!("{} X's {} O's turn_num of {} and value {}, board:\n{}\nchildren boards:\n{}", num_xs, num_os, turn_num, self.value, self.board.board_string(), boards)
    }

    pub fn assert_collapsed_correct(&self, turn_num: usize, collapsed_player: Player) {
        let num_xs = self.board.count_xs();
        let num_os = self.board.count_os();

        assert!(
            num_xs == turn_num,
            "{}",
            self.create_info_string(num_xs, num_os, turn_num)
        );

        match self.board.result() {
            Some(GameResult::XWon) | Some(GameResult::Draw) => {
                assert!(
                    num_os + 1 == turn_num,
                    "{}",
                    self.create_info_string(num_xs, num_os, turn_num)
                )
            }
            Some(GameResult::OWon) | None => {
                assert!(
                    num_os == turn_num,
                    "{}",
                    self.create_info_string(num_xs, num_os, turn_num)
                )
            }
        }

        if self.turn == collapsed_player {
            assert!(
                self.board.result().is_some(),
                "{}",
                self.create_info_string(num_xs, num_os, turn_num)
            )
        }

        for child in self.children.values() {
            child.assert_collapsed_correct(turn_num + 1, collapsed_player);
        }
    }

    pub fn assert_correct(&self, turn_num: usize) {
        let num_xs = self.board.count_xs();
        let num_os = self.board.count_os();

        assert!(
            num_xs == turn_num,
            "{}",
            self.create_info_string(num_xs, num_os, turn_num)
        );
        if self.turn == Player::X {
            assert!(
                num_os == turn_num,
                "{}",
                self.create_info_string(num_xs, num_os, turn_num)
            );
            for child in self.children.values() {
                child.assert_correct(turn_num + 1);
            }
        } else {
            assert!(
                num_os + 1 == turn_num,
                "{}",
                self.create_info_string(num_xs, num_os, turn_num)
            );
            for child in self.children.values() {
                child.assert_correct(turn_num);
            }
        }
    }
}
