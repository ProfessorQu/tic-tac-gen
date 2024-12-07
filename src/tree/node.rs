use std::collections::HashMap;

use crate::tictactoe::{Board, Cell};

#[derive(Debug, Clone)]
pub struct Node {
    board: Board,
    turn: Cell,
    winner: Option<Cell>,
    moves: HashMap<(usize, usize), Box<Node>>,
}

impl Node {
    pub fn new(board: Board, turn: Cell) -> Self {
        Self {
            board,
            turn,
            winner: None,
            moves: HashMap::new(),
        }
    }

    pub fn generate(&mut self) {
        if let Some(result) = self.board.result() {
            self.winner = Some(result);
            return;
        }

        for x in 0..3 {
            for y in 0..3 {
                if self.board.get(x, y) == Cell::Empty {
                    let mut new_board = self.board.clone();
                    new_board.set(x, y, self.turn);

                    let mut new_cell = Node::new(new_board, self.turn.opponent());
                    new_cell.generate();

                    if self.set_winner(&new_cell) {
                        break;
                    }

                    self.moves.insert((x, y), Box::new(new_cell));
                }
            }
        }
    }

    pub fn collapse(&mut self, player: Cell) {
        if self.board.result().is_some() {
            return;
        }

        let mut best_node = None;

        if self.turn == player {
            for node in self.moves.values() {
                if let Some(node_winner) = node.winner {
                    if node_winner == player {
                        best_node = Some(node);
                        break;
                    } else if node_winner == Cell::Empty && best_node.is_none() {
                        best_node = Some(node);
                    }
                }
            }

            if let Some(best_node) = best_node {
                self.board = best_node.board.clone();
                self.turn = best_node.turn;
                self.winner = best_node.winner;
                self.moves = best_node.moves.clone();

                self.collapse(player);
            }
        } else {
            for node in self.moves.values_mut() {
                node.collapse(player);
            }
        }
    }

    pub fn code(&self, depth: usize) -> String {
        let mut spaces = String::new();
        for _ in 0..depth {
            spaces += "    ";
        }

        if self.board.result().is_some() {
            return "".to_string();
        }

        let mut code = String::new();

        code += format!("{spaces}a = input('move: ')").as_str();

        let mut first = true;

        for ((x, y), node) in &self.moves {
            code += format!(
                "
{spaces}{}if a == '{}':
{spaces}    print({:?})
{}",
                if !first { "el" } else { "" },
                x + y * 3,
                node.board.board_string(),
                node.code(depth + 1)
            )
            .as_str();

            first = false;
        }

        code += format!(
            "
{spaces}else:
{spaces}    print('INVALID MOVE')"
        )
        .as_str();

        code
    }

    fn set_winner(&mut self, other: &Node) -> bool {
        let other_winner = other.winner.expect("Previous nodes should have winners");

        if let Some(own_winner) = self.winner {
            if other_winner == self.turn {
                self.winner = Some(other_winner);
                return true;
            } else if other_winner == Cell::Empty && own_winner == self.turn.opponent() {
                self.winner = Some(other_winner)
            }
        } else {
            self.winner = other.winner;
        }

        false
    }
}
