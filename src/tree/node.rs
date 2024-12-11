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
        let mut node = Self {
            board,
            turn,
            value: 0.0,
            children: HashMap::new(),
        };

        node.generate();
        node
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

        let mut best_value = match self.turn {
            Player::X => f32::MIN,
            Player::O => f32::MAX,
        };

        for (x, y) in possible_moves {
            let mut child_board = self.board.clone();
            child_board.set(x, y, self.turn.cell());

            let child = Node::new(child_board, self.turn.opponent());
            best_value = match self.turn {
                Player::O => f32::min(best_value, child.value),
                Player::X => f32::max(best_value, child.value),
            };
            total_children_value += child.value;

            self.children.insert((x, y), Box::new(child));
        }

        self.value = best_value;

        if best_value.abs() < 0.5 {
            self.value = total_children_value / total_children;
        }

        self.value *= 0.99;
    }

    pub fn collapse(&mut self, player: Player) {
        for child in self.children.values_mut() {
            child.collapse(player);
        }

        if self.board.result().is_some() || self.turn != player {
            return;
        }

        let mut best_move = None;
        let mut best_value = match player {
            Player::X => f32::MIN,
            Player::O => f32::MAX,
        };

        for child in self.children.values() {
            match self.turn {
                Player::X => {
                    if child.value > best_value {
                        best_value = child.value;
                        best_move = Some(child.clone());
                    }
                }
                Player::O => {
                    if child.value < best_value {
                        best_value = child.value;
                        best_move = Some(child.clone());
                    }
                }
            }
        }

        if let Some(best_move) = best_move {
            *self = *best_move;
        }
    }

    fn create_info_string(
        &self,
        num_xs: usize,
        num_os: usize,
        turn_num: usize,
        collapsed_player: Player,
    ) -> String {
        let boards: String = self
            .children
            .iter()
            .map(|((_x, _y), child)| {
                child.board.board_string() + "\nVALUE: " + child.value.to_string().as_str()
            })
            .collect::<Vec<String>>()
            .join("\n===========================\n");

        format!(
            "{} X's {} O's turn_num of {} and value {} player: {:?}, board:\n{}\nchildren boards:\n{}",
            num_xs,
            num_os,
            turn_num,
            self.value,
            collapsed_player,
            self.board.board_string(),
            boards
        )
    }

    pub fn python(&self, depth: usize) -> String {
        let spaces = "    ".repeat(depth);
        let mut code = format!("{spaces}print({:?})\n", self.board.board_string());

        if let Some(result) = self.board.result() {
            code += format!("{spaces}print(\"result: {}\")\n", result).as_str();
            return code;
        }

        code += format!("{spaces}move = input(\"move: \")\n").as_str();

        let mut first = true;
        for ((x, y), child) in &self.children {
            let el = if first { "" } else { "el" };
            code += format!("{spaces}{}if move == \"{}\":\n", el, x + y * 3 + 1).as_str();
            code += child.python(depth + 1).as_str();

            first = false;
        }

        code
    }

    pub fn assert_collapsed_correct(&self, turn_num: usize, collapsed_player: Player) {
        let num_xs = self.board.count_xs();
        let num_os = self.board.count_os();

        let info_string = self.create_info_string(num_xs, num_os, turn_num, collapsed_player);

        match self.board.result() {
            Some(GameResult::XWon) => {
                assert!(collapsed_player == Player::X, "{}", info_string);
                assert!(num_xs == turn_num + 1, "{}", info_string);
                assert!(num_os == turn_num, "{}", info_string);
            }
            Some(GameResult::Draw) => {
                assert!(num_os == 4, "{}", info_string);
                assert!(num_xs == 5, "{}", info_string);
            }
            Some(GameResult::OWon) => {
                assert!(collapsed_player == Player::O, "{}", info_string);
                assert!(num_xs == turn_num, "{}", info_string);
                assert!(num_os == turn_num, "{}", info_string);
            }
            None => match collapsed_player {
                Player::O => {
                    assert!(num_xs == turn_num, "{}", info_string);
                    assert!(num_os == turn_num, "{}", info_string);
                }
                Player::X => {
                    assert!(num_xs == turn_num + 1, "{}", info_string);
                    assert!(num_os == turn_num, "{}", info_string);
                }
            },
        }

        if self.turn == collapsed_player {
            assert!(self.board.result().is_some(), "{}", info_string)
        }

        for child in self.children.values() {
            child.assert_collapsed_correct(turn_num + 1, collapsed_player);
        }
    }

    pub fn assert_correct(&self, turn_num: usize) {
        let num_xs = self.board.count_xs();
        let num_os = self.board.count_os();

        let info_string = self.create_info_string(num_xs, num_os, turn_num, Player::X);

        assert!(num_xs == turn_num, "{}", info_string);
        if self.turn == Player::X {
            assert!(num_os == turn_num, "{}", info_string);
            for child in self.children.values() {
                child.assert_correct(turn_num + 1);
            }
        } else {
            assert!(num_os + 1 == turn_num, "{}", info_string);
            for child in self.children.values() {
                child.assert_correct(turn_num);
            }
        }
    }
}
