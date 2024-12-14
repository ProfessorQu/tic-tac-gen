use std::io::{stdout, stdin, Write};fn main() {
	let mut player_move = String::new();
	println!(" | | \n------\n | | \n------\n | | ");
	stdout().flush().expect("Failed to flush stdout");
	player_move.clear();
	stdin().read_line(&mut player_move).expect("Failed to read line");
	if player_move.trim() == "2" {
		println!(" |X| \n------\n |O| \n------\n | | ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "6" {
			println!(" |X|O\n------\n |O|X\n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "9" {
				println!(" |X|O\n------\n |O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O|X|O\n------\n |O|X\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "9" {
					println!("O|X|O\n------\n |O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "4" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "8" {
					println!("O|X|O\n------\n |O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!("O|X|O\n------\nX|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!(" |X|O\n------\n |O|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|X|O\n------\n |O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" |X|O\n------\nX|O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!("O|X| \n------\nX|O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!("O|X| \n------\nX|O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O|X|X\n------\nX|O| \n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O|X| \n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O|X|O\n------\nX|O| \n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("O|X|O\n------\nX|O| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("O|X|O\n------\nX|O| \n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "6" {
					println!("O|X|O\n------\nX|O|X\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "7" {
				println!("O|X| \n------\nX|O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "7" {
			println!(" |X| \n------\nO|O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!(" |X| \n------\nO|O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|X|O\n------\nO|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("X|X|O\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "8" {
					println!("O|X| \n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("O|X|X\n------\nO|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "9" {
				println!(" |X| \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|X| \n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!(" |X|X\n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" |X| \n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "3" {
			println!("O|X|X\n------\n |O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("O|X|X\n------\nX|O| \n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O|X|X\n------\n |O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O|X|X\n------\n |O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O|X|X\n------\n |O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "7" {
					println!("O|X|X\n------\nO|O|O\n------\nX| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("O|X|X\n------\nO|O|O\n------\n |X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!("O|X|X\n------\nX|O|O\n------\n |O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "7" {
						println!("O|X|X\n------\nX|O|O\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "8" {
				println!("O|X|X\n------\n |O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "9" {
			println!(" |X| \n------\n |O|O\n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!(" |X| \n------\nX|O|O\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!(" |X|O\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X|X|O\n------\nX|O|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("O|X|X\n------\nX|O|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("O|X|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "7" {
				println!(" |X| \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|X| \n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!(" |X|X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" |X| \n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "1" {
			println!("X|X|O\n------\n |O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!("X|X|O\n------\n |O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("X|X|O\n------\nX|O| \n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("X|X|O\n------\nO|O| \n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "9" {
					println!("X|X|O\n------\nO|O|O\n------\nX| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("X|X|O\n------\nO|O|X\n------\nX|O| ");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "9" {
						println!("X|X|O\n------\nO|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "8" {
					println!("X|X|O\n------\nO|O|O\n------\nX|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "6" {
				println!("X|X|O\n------\n |O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X|X|O\n------\n |O| \n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "8" {
			println!("O|X| \n------\n |O| \n------\n |X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("O|X| \n------\nX|O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O|X| \n------\n |O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O|X| \n------\n |O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("O|X|X\n------\nO|O| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("O|X| \n------\nO|O|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!("O|X|O\n------\nX|O| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "3" {
				println!("O|X|X\n------\n |O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O|X| \n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
	}
	else if player_move.trim() == "7" {
		println!(" | | \n------\n |O| \n------\nX| | ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "6" {
			println!(" | | \n------\n |O|X\n------\nX|O| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "9" {
				println!(" |O| \n------\n |O|X\n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O| \n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("O|X|X\n------\n |O|X\n------\nX|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O|X|O\n------\n |O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "4" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("O|X| \n------\nX|O|X\n------\nX|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "3" {
				println!(" |O|X\n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" |O| \n------\nX|O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "9" {
			println!(" | | \n------\n |O| \n------\nX|O|X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!(" |O| \n------\nX|O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X| \n------\nO|O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!(" |X|X\n------\nO|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!(" |X|O\n------\nO|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|X|O\n------\nO|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "1" {
					println!("X|X| \n------\nO|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "1" {
				println!("X|O| \n------\n |O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" |O| \n------\n |O|X\n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!(" |O|X\n------\n |O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!("O| | \n------\nX|O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!("O| |X\n------\nX|O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\nX|O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O| | \n------\nX|O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("O| | \n------\nX|O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O| | \n------\nX|O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("O|O|X\n------\nX|O| \n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("O|O| \n------\nX|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!("O|X| \n------\nX|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|X|X\n------\nX|O|O\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
		}
		else if player_move.trim() == "1" {
			println!("X| | \n------\nO|O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!("X| |X\n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("X|O| \n------\nO|O|X\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("X|O|X\n------\nO|O|X\n------\nX|O| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("X|O| \n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "9" {
					println!("X|O| \n------\nO|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!("X| | \n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X| | \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("X|X| \n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "8" {
			println!(" | | \n------\n |O| \n------\nX|X|O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "2" {
				println!("O|X| \n------\n |O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("O| | \n------\nX|O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\n |O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O| | \n------\n |O|X\n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| | \n------\nO|O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!("X|X| \n------\nO|O|O\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("X| |X\n------\nO|O|O\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("X|O| \n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
		}
		else if player_move.trim() == "2" {
			println!(" |X| \n------\nO|O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!(" |X|X\n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" |X| \n------\nO|O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|X|O\n------\nO|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("X|X|O\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "8" {
					println!("O|X| \n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("O|X|X\n------\nO|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!(" |X| \n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" |X| \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|X| \n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "3" {
			println!(" | |X\n------\nO|O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!(" | |X\n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |X\n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|X\n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" | |X\n------\nO|O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("O| |X\n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X|O|X\n------\nO|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("O|X|X\n------\nO|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "9" {
				println!(" | |X\n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
	}
	else if player_move.trim() == "6" {
		println!(" | | \n------\n |O|X\n------\n | | ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "9" {
			println!(" | |O\n------\n |O|X\n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!(" | |O\n------\nX|O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" | |O\n------\n |O|X\n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" | |O\n------\n |O|X\n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "4" {
					println!(" |O|O\n------\nX|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!(" |X|O\n------\nO|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|X|O\n------\nO|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "1" {
					println!("X|O|O\n------\n |O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "2" {
				println!(" |X|O\n------\n |O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |O\n------\n |O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "2" {
			println!(" |X|O\n------\n |O|X\n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "1" {
				println!("X|X|O\n------\n |O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" |X|O\n------\nX|O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O|X|O\n------\n |O|X\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "4" {
					println!("O|X|O\n------\nX|O|X\n------\nX| |O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("O|X|O\n------\n |O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O|X|O\n------\n |O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "4" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "8" {
				println!(" |X|O\n------\n |O|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" |X|O\n------\n |O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "8" {
			println!(" | | \n------\n |O|X\n------\n |X|O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "7" {
				println!("O| | \n------\n |O|X\n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("O| | \n------\nX|O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| | \n------\n |O|X\n------\nO|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!("X|X|O\n------\n |O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("X|O|X\n------\n |O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "4" {
						println!("X|O|X\n------\nX|O|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("X| |O\n------\nX|O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "3" {
			println!(" | |X\n------\n |O|X\n------\n | |O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!("O| |X\n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O|X\n------\n |O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "4" {
					println!("X|O|X\n------\nX|O|X\n------\n |O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("X|O|X\n------\n |O|X\n------\nX|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("X|O|X\n------\nO|O|X\n------\n |X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "7" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "2" {
				println!("O|X|X\n------\n |O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("O| |X\n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O| |X\n------\n |O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "1" {
			println!("X|O| \n------\n |O|X\n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("X|O| \n------\nX|O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("X|O|X\n------\n |O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X|O| \n------\n |O|X\n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X|O| \n------\n |O|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "9" {
					println!("X|O|O\n------\n |O|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!("X|O|O\n------\nX|O|X\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("X|O|X\n------\n |O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "4" {
						println!("X|O|X\n------\nX|O|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "7" {
				println!("X|O| \n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!("O| | \n------\nX|O|X\n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "9" {
				println!("O| |O\n------\nX|O|X\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!("O|X|O\n------\nX|O|X\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("O|O|O\n------\nX|O|X\n------\n |X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("O|O|O\n------\nX|O|X\n------\nX| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!("O| | \n------\nX|O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O| | \n------\nX|O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "7" {
			println!(" | | \n------\n |O|X\n------\nX|O| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!(" |O| \n------\nX|O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("O|X|X\n------\n |O|X\n------\nX|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O|X|O\n------\n |O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "4" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("O|X| \n------\nX|O|X\n------\nX|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "3" {
				println!(" |O|X\n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O| \n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" |O| \n------\n |O|X\n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
	}
	else if player_move.trim() == "1" {
		println!("X| | \n------\n |O| \n------\n | | ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "7" {
			println!("X| | \n------\nO|O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!("X|O| \n------\nO|O|X\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("X|O| \n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "9" {
					println!("X|O| \n------\nO|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("X|O|X\n------\nO|O|X\n------\nX|O| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!("X| | \n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X| | \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("X| |X\n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("X|X| \n------\nO|O|O\n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "8" {
			println!("X| | \n------\nO|O| \n------\n |X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "7" {
				println!("X| | \n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("X|X| \n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("X| |O\n------\nO|O|X\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "9" {
					println!("X| |O\n------\nO|O|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("X| |O\n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("X|X|O\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("X|X|O\n------\nO|O|X\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "3" {
				println!("X| |X\n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X| | \n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "3" {
			println!("X|O|X\n------\n |O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!("X|O|X\n------\nO|O| \n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("X|O|X\n------\nO|O|X\n------\n |X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "7" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "9" {
					println!("X|O|X\n------\nO|O|O\n------\n |X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("X|O|X\n------\nO|O|O\n------\nX|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "6" {
				println!("X|O|X\n------\n |O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X|O|X\n------\n |O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("X|O|X\n------\nX|O| \n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("X|O|X\n------\n |O| \n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "2" {
			println!("X|X|O\n------\n |O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("X|X|O\n------\nX|O| \n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("X|X|O\n------\nO|O| \n------\nX| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("X|X|O\n------\nO|O|O\n------\nX|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("X|X|O\n------\nO|O|X\n------\nX|O| ");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "9" {
						println!("X|X|O\n------\nO|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "9" {
					println!("X|X|O\n------\nO|O|O\n------\nX| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "6" {
				println!("X|X|O\n------\n |O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X|X|O\n------\n |O| \n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X|X|O\n------\n |O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!("X| | \n------\nX|O| \n------\nO| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "2" {
				println!("X|X|O\n------\nX|O| \n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("X| |O\n------\nX|O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("X|O|X\n------\nX|O| \n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("X|O|X\n------\nX|O|O\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "9" {
						println!("X|O|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "6" {
					println!("X|O|X\n------\nX|O|X\n------\nO|O| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("X|O|X\n------\nX|O| \n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!("X| |O\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X| |O\n------\nX|O| \n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "6" {
			println!("X|O| \n------\n |O|X\n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!("X|O|X\n------\n |O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X|O| \n------\n |O|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "9" {
					println!("X|O|O\n------\n |O|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("X|O|X\n------\n |O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "4" {
						println!("X|O|X\n------\nX|O|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("X|O|O\n------\nX|O|X\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "4" {
				println!("X|O| \n------\nX|O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X|O| \n------\n |O|X\n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("X|O| \n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "9" {
			println!("X| | \n------\n |O|O\n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "7" {
				println!("X| | \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("X| | \n------\nX|O|O\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("X|O|X\n------\nX|O|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("X|O|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("X|X|O\n------\nX|O|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("X| |O\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "3" {
				println!("X| |X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X| | \n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("X|X| \n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
	}
	else if player_move.trim() == "3" {
		println!(" | |X\n------\n |O| \n------\n | | ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "2" {
			println!("O|X|X\n------\n |O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!("O|X|X\n------\n |O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("O|X|X\n------\nX|O| \n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O|X|X\n------\n |O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "4" {
					println!("O|X|X\n------\nX|O|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("O|X|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "8" {
					println!("O|X|X\n------\nO|O|O\n------\n |X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("O|X|X\n------\nO|O|O\n------\nX| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "7" {
				println!("O|X|X\n------\n |O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("O|X|X\n------\n |O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "9" {
			println!(" | |X\n------\n |O|O\n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "7" {
				println!(" | |X\n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" | |X\n------\nX|O|O\n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|O|X\n------\nX|O|O\n------\n |O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!(" |O|X\n------\nX|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!("O|X|X\n------\nX|O|O\n------\n |O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "7" {
						println!("O|X|X\n------\nX|O|O\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "1" {
				println!("X| |X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" | |X\n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "1" {
			println!("X|O|X\n------\n |O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("X|O|X\n------\nX|O| \n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("X|O|X\n------\n |O| \n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X|O|X\n------\n |O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X|O|X\n------\n |O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "9" {
					println!("X|O|X\n------\nO|O|O\n------\n |X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!("X|O|X\n------\nX|O|O\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "9" {
						println!("X|O|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "7" {
					println!("X|O|X\n------\nO|O|O\n------\nX|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "6" {
				println!("X|O|X\n------\n |O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!(" |O|X\n------\nX|O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "7" {
				println!(" |O|X\n------\nX|O| \n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" |O|X\n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" |O|X\n------\nX|O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|O|X\n------\nX|O| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nX|O|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "7" {
					println!("O|O|X\n------\nX|O| \n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("O|O|X\n------\nX|O|X\n------\n |X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "1" {
				println!("X|O|X\n------\nX|O| \n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" |O|X\n------\nX|O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "8" {
			println!(" | |X\n------\n |O|O\n------\n |X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "2" {
				println!(" |X|X\n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" | |X\n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("O| |X\n------\nX|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!("O|X|X\n------\nX|O|O\n------\n |X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O| |X\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("O|X|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "7" {
					println!("O| |X\n------\nX|O|O\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "7" {
				println!(" | |X\n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |X\n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "7" {
			println!(" |O|X\n------\n |O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "9" {
				println!(" |O|X\n------\n |O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" |O|X\n------\n |O|X\n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O|X\n------\n |O| \n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" |O|X\n------\n |O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("O|O|X\n------\n |O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X|O|X\n------\nO|O| \n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("O|O|X\n------\nX|O| \n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "4" {
				println!(" |O|X\n------\nX|O| \n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "6" {
			println!(" | |X\n------\n |O|X\n------\n | |O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("O| |X\n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O| |X\n------\n |O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O|X\n------\n |O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("X|O|X\n------\nO|O|X\n------\n |X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "7" {
						println!("X|O|X\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("X|O|X\n------\nX|O|X\n------\n |O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("X|O|X\n------\n |O|X\n------\nX|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!("O| |X\n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X|X\n------\n |O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
	}
	else if player_move.trim() == "9" {
		println!(" | | \n------\n |O| \n------\n | |X");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "8" {
			println!(" | | \n------\n |O| \n------\nO|X|X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!(" | |X\n------\n |O|O\n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "4" {
					println!(" |O|X\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|O|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "1" {
					println!("X| |X\n------\nO|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!(" |X|X\n------\nO|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "6" {
				println!(" | |O\n------\n |O|X\n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" | |O\n------\nX|O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |O\n------\n |O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|O\n------\n |O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "7" {
			println!(" | | \n------\n |O| \n------\nX|O|X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!(" |O| \n------\nX|O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O| \n------\n |O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" |O| \n------\n |O|X\n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!(" |O|X\n------\n |O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X| \n------\n |O|O\n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!(" |X|X\n------\nO|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X|X| \n------\nO|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!("O|X| \n------\nX|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|X|X\n------\nX|O|O\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
		}
		else if player_move.trim() == "2" {
			println!(" |X| \n------\n |O|O\n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!(" |X|X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" |X| \n------\nX|O|O\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|X|O\n------\nX|O|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!(" |X|O\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("O|X|X\n------\nX|O|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("O|X|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "1" {
				println!("X|X| \n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" |X| \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" |X| \n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!(" | | \n------\nX|O| \n------\n |O|X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "2" {
				println!(" |X|O\n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!(" |X|O\n------\nX|O|X\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("O|X|O\n------\nX|O| \n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "1" {
					println!("X|X|O\n------\nX|O| \n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "6" {
				println!(" |O| \n------\nX|O|X\n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!(" |O|X\n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O| \n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" |O| \n------\nX|O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "3" {
			println!(" | |X\n------\n |O|O\n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "2" {
				println!(" |X|X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" | |X\n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" | |X\n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" |O|X\n------\nX|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!(" |O|X\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|O|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "1" {
					println!("X|O|X\n------\nX|O|O\n------\n |O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!(" |O|X\n------\nX|O|O\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
		}
		else if player_move.trim() == "6" {
			println!(" | |O\n------\n |O|X\n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!(" | |O\n------\nX|O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" | |O\n------\n |O|X\n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|O|O\n------\n |O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!(" |X|O\n------\nO|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|X|O\n------\nO|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!(" |O|O\n------\nX|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "8" {
				println!(" | |O\n------\n |O|X\n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|O\n------\n |O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |O\n------\n |O|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "1" {
			println!("X| | \n------\nO|O| \n------\n | |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "7" {
				println!("X| | \n------\nO|O|O\n------\nX| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("X| |O\n------\nO|O|X\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "7" {
					println!("X| |O\n------\nO|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("X|X|O\n------\nO|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "8" {
					println!("X| |O\n------\nO|O|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!("X|X|O\n------\nO|O|X\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "3" {
				println!("X| |X\n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("X|X| \n------\nO|O|O\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X| | \n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
	}
	else if player_move.trim() == "4" {
		println!(" | | \n------\nX|O| \n------\n | | ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "6" {
			println!("O| | \n------\nX|O|X\n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!("O| | \n------\nX|O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O| | \n------\nX|O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O| |O\n------\nX|O|X\n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "7" {
					println!("O|O|O\n------\nX|O|X\n------\nX| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("O| |O\n------\nX|O|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!("O|X|O\n------\nX|O|X\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "9" {
			println!(" | | \n------\nX|O| \n------\n |O|X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "1" {
				println!("X|O| \n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" |O| \n------\nX|O|X\n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" |O| \n------\nX|O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!(" |O|X\n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|O\n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|X|O\n------\nX|O| \n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("O|X|O\n------\nX|O| \n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "6" {
					println!(" |X|O\n------\nX|O|X\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
		}
		else if player_move.trim() == "2" {
			println!("O|X| \n------\nX|O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!("O|X| \n------\nX|O|X\n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!("O|X| \n------\nX|O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O|X|X\n------\nX|O| \n------\n | |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("O|X| \n------\nX|O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O|X|O\n------\nX|O| \n------\n | |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "7" {
					println!("O|X|O\n------\nX|O| \n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "6" {
					println!("O|X|O\n------\nX|O|X\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("O|X|O\n------\nX|O| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
		}
		else if player_move.trim() == "8" {
			println!(" | | \n------\nX|O| \n------\nO|X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "2" {
				println!(" |X|O\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" | |O\n------\nX|O|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |O\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!(" | |X\n------\nX|O| \n------\nO|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("O| |X\n------\nX|O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X|O|X\n------\nX|O| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nX|O|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("O|X|X\n------\nX|O| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "9" {
				println!(" | |O\n------\nX|O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "3" {
			println!(" |O|X\n------\nX|O| \n------\n | | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!(" |O|X\n------\nX|O|X\n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" |O|X\n------\nX|O| \n------\nX|O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|O|X\n------\nX|O| \n------\n |O| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" |O|X\n------\nX|O| \n------\n |O|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" |O|X\n------\nX|O| \n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|O|X\n------\nX|O| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nX|O|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "7" {
					println!("O|O|X\n------\nX|O| \n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("O|O|X\n------\nX|O|X\n------\n |X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
		}
		else if player_move.trim() == "1" {
			println!("X| | \n------\nX|O| \n------\nO| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "2" {
				println!("X|X|O\n------\nX|O| \n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X| |O\n------\nX|O| \n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("X| |O\n------\nX|O|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X| |O\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("X|O|X\n------\nX|O| \n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("X|O|X\n------\nX|O|X\n------\nO|O| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("X|O|X\n------\nX|O| \n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("X|O|X\n------\nX|O|O\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "9" {
						println!("X|O|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
		}
		else if player_move.trim() == "7" {
			println!("O| | \n------\nX|O| \n------\nX| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!("O| | \n------\nX|O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\nX|O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\nX|O| \n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O| | \n------\nX|O|X\n------\nX| |O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O| | \n------\nX|O| \n------\nX|O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("O|O| \n------\nX|O|X\n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!("O|X|O\n------\nX|O| \n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("O|X|O\n------\nX|O|X\n------\nX|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "3" {
					println!("O|O|X\n------\nX|O| \n------\nX|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
		}
	}
	else if player_move.trim() == "5" {
		println!(" | | \n------\n |X| \n------\nO| | ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "9" {
			println!("O| | \n------\n |X| \n------\nO| |X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "8" {
				println!("O| | \n------\nO|X| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\nO|X| \n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O| | \n------\nO|X|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\nO|X| \n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("O| | \n------\nX|X|O\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("O|O| \n------\nX|X|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|O|X\n------\nX|X|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("O|X| \n------\nX|X|O\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|X|X\n------\nX|X|O\n------\nO|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "3" {
					println!("O|O|X\n------\nX|X|O\n------\nO| |X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "8" {
						println!("O|O|X\n------\nX|X|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
		}
		else if player_move.trim() == "3" {
			println!(" | |X\n------\n |X| \n------\nO| |O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!(" | |X\n------\n |X|X\n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" | |X\n------\nX|X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|X\n------\n |X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!(" |O|X\n------\n |X| \n------\nO|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!(" |O|X\n------\nO|X|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "1" {
					println!("X|O|X\n------\nO|X| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!(" |O|X\n------\nX|X|O\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|O|X\n------\nX|X|O\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "1" {
				println!("X| |X\n------\n |X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "1" {
			println!("X| | \n------\n |X| \n------\nO| |O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("X| | \n------\nX|X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("X|X| \n------\n |X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("X|O| \n------\n |X| \n------\nO|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("X|O| \n------\nO|X|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("X|O| \n------\nX|X|O\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nX|X|O\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "3" {
					println!("X|O|X\n------\nO|X| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "3" {
				println!("X| |X\n------\n |X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("X| | \n------\n |X|X\n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "2" {
			println!(" |X| \n------\n |X| \n------\nO|O| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!(" |X|X\n------\n |X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" |X| \n------\n |X|X\n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|X| \n------\n |X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!(" |X| \n------\nX|X| \n------\nO|O|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("O|X| \n------\n |X| \n------\nO|O|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "4" {
					println!("O|X| \n------\nX|X|O\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|X|X\n------\nX|X|O\n------\nO|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "6" {
					println!("O|X| \n------\nO|X|X\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("O|X|X\n------\nO|X| \n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
		}
		else if player_move.trim() == "6" {
			println!(" | | \n------\nO|X|X\n------\nO| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "9" {
				println!("O| | \n------\nO|X|X\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| | \n------\nO|X|X\n------\nO| |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!("X|X| \n------\nO|X|X\n------\nO|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("X| |X\n------\nO|X|X\n------\nO|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "8" {
					println!("X|O| \n------\nO|X|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\nO|X|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "8" {
				println!("O| | \n------\nO|X|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\nO|X|X\n------\nO| | ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!(" | | \n------\nX|X|O\n------\nO| | ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "1" {
				println!("X| | \n------\nX|X|O\n------\nO| |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!("X| |O\n------\nX|X|O\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!("X|X|O\n------\nX|X|O\n------\nO| |O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!("X| |X\n------\nX|X|O\n------\nO|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "3" {
				println!(" | |X\n------\nX|X|O\n------\nO| |O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "8" {
					println!(" |O|X\n------\nX|X|O\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|O|X\n------\nX|X|O\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "1" {
					println!("X| |X\n------\nX|X|O\n------\nO|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!(" |X|X\n------\nX|X|O\n------\nO|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "2" {
				println!(" |X| \n------\nX|X|O\n------\nO|O| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|X| \n------\nX|X|O\n------\nO|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "3" {
					println!(" |X|X\n------\nX|X|O\n------\nO|O|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O|X| \n------\nX|X|O\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|X|X\n------\nX|X|O\n------\nO|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "9" {
				println!("O| | \n------\nX|X|O\n------\nO| |X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("O| |X\n------\nX|X|O\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("O|X|X\n------\nX|X|O\n------\nO|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("O|X| \n------\nX|X|O\n------\nO|O|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|X|X\n------\nX|X|O\n------\nO|O|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "8" {
					println!("O|O| \n------\nX|X|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|O|X\n------\nX|X|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "8" {
				println!(" |O| \n------\nX|X|O\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|O| \n------\nX|X|O\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nX|X|O\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "3" {
					println!("O|O|X\n------\nX|X|O\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "9" {
						println!("O|O|X\n------\nX|X|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "9" {
					println!("O|O| \n------\nX|X|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|O|X\n------\nX|X|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
		}
		else if player_move.trim() == "8" {
			println!(" |O| \n------\n |X| \n------\nO|X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!(" |O| \n------\nO|X|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("O|O|X\n------\nO|X|X\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O|O| \n------\nO|X|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X|O| \n------\nO|X|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "1" {
				println!("X|O| \n------\n |X| \n------\nO|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("X|O| \n------\nO|X|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "3" {
					println!("X|O|X\n------\nO|X| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("X|O| \n------\nX|X|O\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nX|X|O\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "9" {
				println!("O|O| \n------\n |X| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("O|O|X\n------\nO|X| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!("O|O|O\n------\nX|X| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("O|O| \n------\nO|X|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "4" {
				println!(" |O| \n------\nX|X|O\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "1" {
					println!("X|O| \n------\nX|X|O\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("X|O|X\n------\nX|X|O\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "9" {
					println!("O|O| \n------\nX|X|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "3" {
						println!("O|O|X\n------\nX|X|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "3" {
					println!("O|O|X\n------\nX|X|O\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "9" {
						println!("O|O|X\n------\nX|X|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "3" {
				println!(" |O|X\n------\nO|X| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "6" {
					println!("O|O|X\n------\nO|X|X\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X|O|X\n------\nO|X| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "6" {
						println!("X|O|X\n------\nO|X|X\n------\nO|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "9" {
					println!("O|O|X\n------\nO|X| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
		}
	}
	else if player_move.trim() == "8" {
		println!(" | | \n------\n |O| \n------\n |X| ");
		stdout().flush().expect("Failed to flush stdout");
		player_move.clear();
		stdin().read_line(&mut player_move).expect("Failed to read line");
		if player_move.trim() == "6" {
			println!(" | | \n------\n |O|X\n------\n |X|O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "1" {
				println!("X| |O\n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!("X|X|O\n------\n |O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "7" {
					println!("X| |O\n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("X|X|O\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "4" {
					println!("X| |O\n------\nX|O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "7" {
				println!("O| | \n------\n |O|X\n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "4" {
				println!("O| | \n------\nX|O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\n |O|X\n------\n |X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "9" {
			println!(" | | \n------\n |O| \n------\nO|X|X");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!(" | |X\n------\n |O|O\n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!(" |X|X\n------\nO|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "1" {
					println!("X| |X\n------\nO|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "4" {
					println!(" |O|X\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "1" {
						println!("X|O|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "4" {
				println!(" | |O\n------\nX|O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|O\n------\n |O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| |O\n------\n |O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" | |O\n------\n |O|X\n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "7" {
			println!(" | | \n------\n |O| \n------\nX|X|O");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("O| | \n------\nX|O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X| | \n------\nO|O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "3" {
					println!("X| |X\n------\nO|O|O\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("X| |O\n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("X|X|O\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("X|X| \n------\nO|O|O\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "2" {
				println!("O|X| \n------\n |O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O| |X\n------\n |O| \n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("O| | \n------\n |O|X\n------\nX|X|O");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "4" {
			println!(" | | \n------\nX|O| \n------\nO|X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!("O| |X\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "2" {
					println!("O|X|X\n------\nX|O| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("O| |X\n------\nX|O|X\n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O| |X\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("O|X|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "1" {
				println!("X| |O\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|O\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!(" | |O\n------\nX|O|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" | |O\n------\nX|O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "1" {
			println!("X| | \n------\nO|O| \n------\n |X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "3" {
				println!("X| |X\n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!("X|X| \n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!("X| | \n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "6" {
				println!("X| |O\n------\nO|O|X\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "7" {
					println!("X| |O\n------\nO|O|X\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("X|X|O\n------\nO|O|X\n------\nX|X|O");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
				else if player_move.trim() == "2" {
					println!("X|X|O\n------\nO|O|X\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("X| |O\n------\nO|O|X\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "7" {
				println!("X| | \n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "2" {
			println!(" |X| \n------\n |O| \n------\nO|X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "6" {
				println!(" |X|O\n------\n |O|X\n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "3" {
				println!("O|X|X\n------\n |O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "4" {
					println!("O|X|X\n------\nX|O| \n------\nO|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "6" {
					println!("O|X|X\n------\nO|O|X\n------\nO|X| ");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O|X|X\n------\nO|O| \n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
			}
			else if player_move.trim() == "4" {
				println!(" |X|O\n------\nX|O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "1" {
				println!("X|X|O\n------\n |O| \n------\nO|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" |X|O\n------\n |O| \n------\nO|X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
		else if player_move.trim() == "3" {
			println!(" | |X\n------\n |O|O\n------\n |X| ");
			stdout().flush().expect("Failed to flush stdout");
			player_move.clear();
			stdin().read_line(&mut player_move).expect("Failed to read line");
			if player_move.trim() == "4" {
				println!("O| |X\n------\nX|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				player_move.clear();
				stdin().read_line(&mut player_move).expect("Failed to read line");
				if player_move.trim() == "7" {
					println!("O| |X\n------\nX|O|O\n------\nX|X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "2" {
					println!("O|X|X\n------\nX|O|O\n------\n |X|O");
					stdout().flush().expect("Failed to flush stdout");
					println!("result: O Won");
				}
				else if player_move.trim() == "9" {
					println!("O| |X\n------\nX|O|O\n------\nO|X|X");
					stdout().flush().expect("Failed to flush stdout");
					player_move.clear();
					stdin().read_line(&mut player_move).expect("Failed to read line");
					if player_move.trim() == "2" {
						println!("O|X|X\n------\nX|O|O\n------\nO|X|X");
						stdout().flush().expect("Failed to flush stdout");
						println!("result: Draw");
					}
				}
			}
			else if player_move.trim() == "1" {
				println!("X| |X\n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "2" {
				println!(" |X|X\n------\nO|O|O\n------\n |X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "9" {
				println!(" | |X\n------\nO|O|O\n------\n |X|X");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
			else if player_move.trim() == "7" {
				println!(" | |X\n------\nO|O|O\n------\nX|X| ");
				stdout().flush().expect("Failed to flush stdout");
				println!("result: O Won");
			}
		}
	}
}