use std::collections::HashMap;

use crate::tictactoe::{Board, Cell};

#[derive(Debug)]
pub struct Node {
    board: Board,
    turn: Cell,
    pub winner: Option<Cell>,
    moves: HashMap<(usize, usize), Box<Node>>,
}

impl Node {
    pub fn new(board: Board, turn: Cell) -> Self {
        Self {
            board,
            turn,
            winner: None,
            moves: HashMap::new()
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

                    self.set_winner(&new_cell);

                    self.moves.insert((x, y), Box::new(new_cell));
                }
            }
        }
    }

    fn set_winner(&mut self, other: &Node) {
        let other_winner = other.winner.expect("Previous nodes should have winners");

        if let Some(own_winner) = self.winner {
            if other_winner == Cell::Empty && own_winner == self.turn.opponent() {
                self.winner = Some(other_winner)
            } if other_winner == self.turn {
                self.winner = Some(other_winner);
            }
        } else {
            self.winner = other.winner;
        }
    }
}
