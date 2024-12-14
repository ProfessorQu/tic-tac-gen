import java.util.Scanner;
class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int move;
		System.out.println(" | | \n------\n | | \n------\n | | ");
		move = scanner.nextInt();
		if (move == 6) {
			System.out.println(" | | \n------\n |O|X\n------\n | | ");
			move = scanner.nextInt();
			if (move == 8) {
				System.out.println(" | | \n------\n |O|X\n------\n |X|O");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X| |O\n------\n |O|X\n------\n |X|O");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("X| |O\n------\nO|O|X\n------\nX|X|O");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("X| |O\n------\nX|O|X\n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("X|X|O\n------\n |O|X\n------\nO|X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 7) {
					System.out.println("O| | \n------\n |O|X\n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("O|X| \n------\n |O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\n |O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| | \n------\nX|O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 9) {
				System.out.println(" | |O\n------\n |O|X\n------\n | |X");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println(" | |O\n------\n |O|X\n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |O\n------\n |O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" | |O\n------\n |O|X\n------\nX|O|X");
					move = scanner.nextInt();
					if (move == 1) {
						System.out.println("X|O|O\n------\n |O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println(" |O|O\n------\nX|O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 4) {
					System.out.println(" | |O\n------\nX|O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 4) {
				System.out.println("O| | \n------\nX|O|X\n------\n | | ");
				move = scanner.nextInt();
				if (move == 9) {
					System.out.println("O| |O\n------\nX|O|X\n------\n | |X");
					move = scanner.nextInt();
					if (move == 2) {
						System.out.println("O|X|O\n------\nX|O|X\n------\nO| |X");
						System.out.println("result: O Won");
					}
					else if (move == 7) {
						System.out.println("O|O|O\n------\nX|O|X\n------\nX| |X");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("O|O|O\n------\nX|O|X\n------\n |X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 7) {
					System.out.println("O| | \n------\nX|O|X\n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("O|X| \n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("O| | \n------\nX|O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 1) {
				System.out.println("X|O| \n------\n |O|X\n------\n | | ");
				move = scanner.nextInt();
				if (move == 9) {
					System.out.println("X|O| \n------\n |O|X\n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("X|O| \n------\nX|O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X|O| \n------\n |O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X|O| \n------\n |O|X\n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("X|O|X\n------\n |O|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("X|O|X\n------\nX|O|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("X|O|O\n------\nX|O|X\n------\nO|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("X|O|O\n------\n |O|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 3) {
					System.out.println("X|O|X\n------\n |O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 3) {
				System.out.println(" | |X\n------\n |O|X\n------\n | |O");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X|O|X\n------\n |O|X\n------\n | |O");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("X|O|X\n------\n |O|X\n------\nX|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("X|O|X\n------\nO|O|X\n------\n |X|O");
						move = scanner.nextInt();
						if (move == 7) {
							System.out.println("X|O|X\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("X|O|X\n------\nX|O|X\n------\n |O|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 4) {
					System.out.println("O| |X\n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("O|X|X\n------\n |O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("O| |X\n------\n |O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O| |X\n------\n |O|X\n------\nX| |O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 7) {
				System.out.println(" | | \n------\n |O|X\n------\nX|O| ");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println("O|X| \n------\n |O|X\n------\nX|O| ");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("O|X|X\n------\n |O|X\n------\nX|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("O|X| \n------\nX|O|X\n------\nX|O|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 3) {
					System.out.println(" |O|X\n------\n |O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|O| \n------\n |O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" |O| \n------\n |O|X\n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" |O| \n------\nX|O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 2) {
				System.out.println(" |X|O\n------\n |O|X\n------\n | | ");
				move = scanner.nextInt();
				if (move == 4) {
					System.out.println(" |X|O\n------\nX|O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O|X|O\n------\n |O|X\n------\nX| | ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 8) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println("O|X|O\n------\nX|O|X\n------\nX| |O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|X|O\n------\n |O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO|X| ");
					System.out.println("result: O Won");
				}
			}
		}
		else if (move == 1) {
			System.out.println("X| | \n------\n |O| \n------\n | | ");
			move = scanner.nextInt();
			if (move == 8) {
				System.out.println("X| | \n------\nO|O| \n------\n |X| ");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println("X| |O\n------\nO|O|X\n------\n |X| ");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("X| |O\n------\nO|O|X\n------\nX|X|O");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nO|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("X| |O\n------\nO|O|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 7) {
					System.out.println("X| | \n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("X|X| \n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X| | \n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("X| |X\n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 9) {
				System.out.println("X| | \n------\nO|O| \n------\n | |X");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("X| |X\n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X| | \n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X| | \n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("X|X| \n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("X| |O\n------\nO|O|X\n------\n | |X");
					move = scanner.nextInt();
					if (move == 8) {
						System.out.println("X| |O\n------\nO|O|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 7) {
						System.out.println("X| |O\n------\nO|O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nO| |X");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 6) {
				System.out.println("X|O| \n------\n |O|X\n------\n | | ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("X|O|X\n------\n |O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X|O| \n------\n |O|X\n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("X|O| \n------\nX|O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X|O| \n------\n |O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X|O| \n------\n |O|X\n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("X|O|X\n------\n |O|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("X|O|X\n------\nX|O|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("X|O|O\n------\nX|O|X\n------\nO|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("X|O|O\n------\n |O|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 2) {
				System.out.println("X|X|O\n------\n |O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println("X|X|O\n------\n |O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("X|X|O\n------\nX|O| \n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X|X|O\n------\nO|O| \n------\nX| | ");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nX|O| ");
						move = scanner.nextInt();
						if (move == 9) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 8) {
						System.out.println("X|X|O\n------\nO|O|O\n------\nX|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("X|X|O\n------\nO|O|O\n------\nX| |X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 6) {
					System.out.println("X|X|O\n------\n |O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X|X|O\n------\n |O| \n------\nO| |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 4) {
				System.out.println("X| | \n------\nX|O| \n------\nO| | ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("X|O|X\n------\nX|O| \n------\nO| | ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("X|O|X\n------\nX|O| \n------\nO|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("X|O|X\n------\nX|O|O\n------\nO|X| ");
						move = scanner.nextInt();
						if (move == 9) {
							System.out.println("X|O|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println("X|O|X\n------\nX|O|X\n------\nO|O| ");
						System.out.println("result: O Won");
					}
				}
				else if (move == 6) {
					System.out.println("X| |O\n------\nX|O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("X|X|O\n------\nX|O| \n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X| |O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X| |O\n------\nX|O| \n------\nO| |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 7) {
				System.out.println("X| | \n------\nO|O| \n------\nX| | ");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println("X|O| \n------\nO|O|X\n------\nX| | ");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("X|O|X\n------\nO|O|X\n------\nX|O| ");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("X|O| \n------\nO|O|X\n------\nX|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 9) {
						System.out.println("X|O| \n------\nO|O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 8) {
					System.out.println("X| | \n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("X| |X\n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X| | \n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("X|X| \n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 3) {
				System.out.println("X|O|X\n------\n |O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println("X|O|X\n------\n |O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X|O|X\n------\n |O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X|O|X\n------\n |O|O\n------\n |X| ");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("X|O|X\n------\nO|O|O\n------\nX|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("X|O|X\n------\nO|O|O\n------\n |X|X");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println("X|O|X\n------\nX|O|O\n------\nO|X| ");
						move = scanner.nextInt();
						if (move == 9) {
							System.out.println("X|O|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 4) {
					System.out.println("X|O|X\n------\nX|O| \n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X|O|X\n------\n |O| \n------\nX|O| ");
					System.out.println("result: O Won");
				}
			}
		}
		else if (move == 7) {
			System.out.println(" | | \n------\n |O| \n------\nX| | ");
			move = scanner.nextInt();
			if (move == 2) {
				System.out.println(" |X| \n------\nO|O| \n------\nX| | ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println(" |X|X\n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |X| \n------\nO|O|X\n------\nX| |O");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("O|X|X\n------\nO|O|X\n------\nX| |O");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nX| |O");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 8) {
						System.out.println("O|X| \n------\nO|O|X\n------\nX|X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println(" |X| \n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" |X| \n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|X| \n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 4) {
				System.out.println("O| | \n------\nX|O| \n------\nX| | ");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println("O|X| \n------\nX|O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("O| | \n------\nX|O|X\n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O| | \n------\nX|O| \n------\nX|O|X");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("O|O|X\n------\nX|O| \n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X| \n------\nX|O|O\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println("O|O| \n------\nX|O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 8) {
					System.out.println("O| | \n------\nX|O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\nX|O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 3) {
				System.out.println(" | |X\n------\n |O|O\n------\nX| | ");
				move = scanner.nextInt();
				if (move == 9) {
					System.out.println(" | |X\n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|X\n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" | |X\n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |X\n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| |X\n------\nX|O|O\n------\nX| | ");
					move = scanner.nextInt();
					if (move == 2) {
						System.out.println("O|X|X\n------\nX|O|O\n------\nX| |O");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("O| |X\n------\nX|O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O| |X\n------\nX|O|O\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
				}
			}
			else if (move == 1) {
				System.out.println("X| | \n------\nO|O| \n------\nX| | ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("X| |X\n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("X|X| \n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("X| | \n------\nO|O|X\n------\nX|O| ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("X|O| \n------\nO|O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nX|O| ");
						move = scanner.nextInt();
						if (move == 9) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println("X|O|X\n------\nO|O|X\n------\nX|O| ");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println("X| | \n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X| | \n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 6) {
				System.out.println(" | | \n------\n |O|X\n------\nX|O| ");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println("O|X| \n------\n |O|X\n------\nX|O| ");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("O|X| \n------\nX|O|X\n------\nX|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("O|X|X\n------\n |O|X\n------\nX|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 1) {
					System.out.println("X|O| \n------\n |O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" |O| \n------\nX|O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println(" |O|X\n------\n |O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" |O| \n------\n |O|X\n------\nX|O|X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 8) {
				System.out.println(" | | \n------\n |O| \n------\nX|X|O");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println("O| | \n------\n |O|X\n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| | \n------\nX|O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\n |O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| | \n------\nO|O| \n------\nX|X|O");
					move = scanner.nextInt();
					if (move == 2) {
						System.out.println("X|X| \n------\nO|O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("X| |X\n------\nO|O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("X|O| \n------\nO|O|X\n------\nX|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 2) {
					System.out.println("O|X| \n------\n |O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 9) {
				System.out.println(" | | \n------\n |O| \n------\nX|O|X");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println(" |O|X\n------\n |O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|O| \n------\n |O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |O| \n------\n |O|X\n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" |O| \n------\nX|O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X| \n------\nO|O| \n------\nX|O|X");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println(" |X|O\n------\nO|O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|X| \n------\nO|O|O\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println(" |X|X\n------\nO|O|O\n------\nX|O|X");
						System.out.println("result: O Won");
					}
				}
			}
		}
		else if (move == 5) {
			System.out.println(" | | \n------\n |X| \n------\nO| | ");
			move = scanner.nextInt();
			if (move == 2) {
				System.out.println(" |X| \n------\n |X| \n------\nO|O| ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println(" |X|X\n------\n |X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O|X| \n------\n |X| \n------\nO|O|X");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("O|X| \n------\nX|X|O\n------\nO|O|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|X|X\n------\nX|X|O\n------\nO|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println("O|X|X\n------\nO|X| \n------\nO|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("O|X| \n------\nO|X|X\n------\nO|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 4) {
					System.out.println(" |X| \n------\nX|X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |X| \n------\n |X|X\n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|X| \n------\n |X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 1) {
				System.out.println("X| | \n------\n |X| \n------\nO| |O");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println("X|X| \n------\n |X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X|O| \n------\n |X| \n------\nO|X|O");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("X|O| \n------\nO|X|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nO|X|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println("X|O|X\n------\n |X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("X|O| \n------\nX|X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 4) {
					System.out.println("X| | \n------\nX|X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("X| |X\n------\n |X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("X| | \n------\n |X|X\n------\nO|O|O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 3) {
				System.out.println(" | |X\n------\n |X| \n------\nO| |O");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println(" |X|X\n------\n |X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |X\n------\n |X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" | |X\n------\nX|X| \n------\nO|O|O");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" |O|X\n------\n |X| \n------\nO|X|O");
					move = scanner.nextInt();
					if (move == 1) {
						System.out.println("X|O|X\n------\n |X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println(" |O|X\n------\nO|X|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|O|X\n------\nO|X|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println(" |O|X\n------\nX|X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 6) {
					System.out.println(" | |X\n------\n |X|X\n------\nO|O|O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 9) {
				System.out.println("O| | \n------\n |X| \n------\nO| |X");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println("O| | \n------\nO|X| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("O| | \n------\nO|X|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("O|X| \n------\nO|X| \n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| | \n------\nX|X|O\n------\nO| |X");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("O| |X\n------\nX|X|O\n------\nO|O|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|X|O\n------\nO|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println("O|X| \n------\nX|X|O\n------\nO|O|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|X|X\n------\nX|X|O\n------\nO|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 8) {
						System.out.println("O|O| \n------\nX|X|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|O|X\n------\nX|X|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\nO|X| \n------\nO| |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 8) {
				System.out.println(" |O| \n------\n |X| \n------\nO|X| ");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X|O| \n------\n |X| \n------\nO|X|O");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("X|O| \n------\nX|X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println("X|O| \n------\nO|X|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nO|X|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println("X|O|X\n------\n |X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 4) {
					System.out.println(" |O| \n------\nX|X|O\n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("O|O| \n------\nX|X|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|O|X\n------\nX|X|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|O| \n------\nX|X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println(" |O|X\n------\nX|X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 6) {
					System.out.println(" |O| \n------\nO|X|X\n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("O|O|X\n------\nO|X|X\n------\nO|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X|O| \n------\nO|X|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nO|X|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 9) {
						System.out.println("O|O| \n------\nO|X|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println("O|O| \n------\n |X| \n------\nO|X|X");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("O|O|X\n------\nO|X| \n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("O|O| \n------\nO|X|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println("O|O|O\n------\nX|X| \n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 3) {
					System.out.println("O|O|X\n------\n |X| \n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("O|O|X\n------\nX|X|O\n------\nO|X| ");
						move = scanner.nextInt();
						if (move == 9) {
							System.out.println("O|O|X\n------\nX|X|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println("O|O|X\n------\nO|X|X\n------\nO|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O|O|X\n------\nO|X| \n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 6) {
				System.out.println(" | | \n------\nO|X|X\n------\nO| | ");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X| | \n------\nO|X|X\n------\nO| |O");
					move = scanner.nextInt();
					if (move == 2) {
						System.out.println("X|X| \n------\nO|X|X\n------\nO|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("X|O| \n------\nO|X|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nO|X|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println("X| |X\n------\nO|X|X\n------\nO|O|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println("O| | \n------\nO|X|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\nO|X|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("O|X| \n------\nO|X|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("O| | \n------\nO|X|X\n------\nO|X| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 4) {
				System.out.println(" | | \n------\nX|X|O\n------\nO| | ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println(" | |X\n------\nX|X|O\n------\nO|O| ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("O| |X\n------\nX|X|O\n------\nO|O|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|X|O\n------\nO|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println(" |X|X\n------\nX|X|O\n------\nO|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X| |X\n------\nX|X|O\n------\nO|O|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println("O| | \n------\nX|X|O\n------\nO| |X");
					move = scanner.nextInt();
					if (move == 2) {
						System.out.println("O|X| \n------\nX|X|O\n------\nO|O|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|X|X\n------\nX|X|O\n------\nO|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println("O|O|X\n------\nX|X|O\n------\nO| |X");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("O|O|X\n------\nX|X|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 8) {
						System.out.println("O|O| \n------\nX|X|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|O|X\n------\nX|X|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 8) {
					System.out.println(" |O| \n------\nX|X|O\n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println(" |O|X\n------\nX|X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|O| \n------\nX|X|O\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("X|O|X\n------\nX|X|O\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 9) {
						System.out.println("O|O| \n------\nX|X|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|O|X\n------\nX|X|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 1) {
					System.out.println("X| | \n------\nX|X|O\n------\nO| |O");
					move = scanner.nextInt();
					if (move == 8) {
						System.out.println("X| |O\n------\nX|X|O\n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("X| |X\n------\nX|X|O\n------\nO|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("X|X|O\n------\nX|X|O\n------\nO| |O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 2) {
					System.out.println(" |X| \n------\nX|X|O\n------\nO|O| ");
					move = scanner.nextInt();
					if (move == 1) {
						System.out.println("X|X| \n------\nX|X|O\n------\nO|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println(" |X|X\n------\nX|X|O\n------\nO|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O|X| \n------\nX|X|O\n------\nO|O|X");
						move = scanner.nextInt();
						if (move == 3) {
							System.out.println("O|X|X\n------\nX|X|O\n------\nO|O|X");
							System.out.println("result: Draw");
						}
					}
				}
			}
		}
		else if (move == 8) {
			System.out.println(" | | \n------\n |O| \n------\n |X| ");
			move = scanner.nextInt();
			if (move == 9) {
				System.out.println(" | | \n------\n |O| \n------\nO|X|X");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X| |O\n------\n |O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" | |O\n------\nX|O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" | |O\n------\n |O|X\n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|O\n------\n |O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println(" | |X\n------\n |O|O\n------\nO|X|X");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println(" |O|X\n------\nX|O|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|O|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println(" |X|X\n------\nO|O|O\n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X| |X\n------\nO|O|O\n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 4) {
				System.out.println(" | | \n------\nX|O| \n------\nO|X| ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("O| |X\n------\nX|O| \n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("O| |X\n------\nX|O|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println("O| |X\n------\nX|O|X\n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X|X\n------\nX|O| \n------\nO|X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 6) {
					System.out.println(" | |O\n------\nX|O|X\n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" | |O\n------\nX|O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 2) {
				System.out.println(" |X|O\n------\n |O| \n------\n |X| ");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X|X|O\n------\n |O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |X|O\n------\n |O| \n------\nX|X|O");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X|X|O\n------\n |O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println("O|X|O\n------\nX|O| \n------\nX|X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 6) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" |X|O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" |X|O\n------\n |O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 6) {
				System.out.println(" | | \n------\n |O|X\n------\n |X|O");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println("O|X| \n------\n |O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| | \n------\nX|O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\n |O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O| | \n------\n |O|X\n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| | \n------\n |O|X\n------\nO|X|O");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("X| |O\n------\nX|O|X\n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("X|X|O\n------\n |O|X\n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("X|O|X\n------\n |O|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("X|O|X\n------\nX|O|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
				}
			}
			else if (move == 1) {
				System.out.println("X| | \n------\nO|O| \n------\n |X| ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("X| |X\n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X| | \n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X| | \n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("X| |O\n------\nO|O|X\n------\n |X| ");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("X| |O\n------\nO|O|X\n------\nX|X|O");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 9) {
						System.out.println("X| |O\n------\nO|O|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nO|X| ");
						System.out.println("result: O Won");
					}
				}
				else if (move == 2) {
					System.out.println("X|X| \n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 7) {
				System.out.println(" | | \n------\n |O| \n------\nX|X|O");
				move = scanner.nextInt();
				if (move == 4) {
					System.out.println("O| | \n------\nX|O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("O| | \n------\n |O|X\n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\n |O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| | \n------\nO|O| \n------\nX|X|O");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("X| |X\n------\nO|O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("X| |O\n------\nO|O|X\n------\nX|X|O");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println("X|X| \n------\nO|O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 2) {
					System.out.println("O|X| \n------\n |O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 3) {
				System.out.println(" | |X\n------\n |O|O\n------\n |X| ");
				move = scanner.nextInt();
				if (move == 7) {
					System.out.println(" | |X\n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|X\n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| |X\n------\nX|O|O\n------\n |X| ");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("O| |X\n------\nX|O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O| |X\n------\nX|O|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println("O|X|X\n------\nX|O|O\n------\n |X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println(" | |X\n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |X\n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
			}
		}
		else if (move == 9) {
			System.out.println(" | | \n------\n |O| \n------\n | |X");
			move = scanner.nextInt();
			if (move == 7) {
				System.out.println(" | | \n------\n |O| \n------\nX|O|X");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X|O| \n------\n |O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |O| \n------\n |O|X\n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X| \n------\nO|O| \n------\nX|O|X");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println(" |X|O\n------\nO|O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|X| \n------\nO|O|O\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println(" |X|X\n------\nO|O|O\n------\nX|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 4) {
					System.out.println(" |O| \n------\nX|O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println(" |O|X\n------\n |O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 4) {
				System.out.println(" | | \n------\nX|O| \n------\n |O|X");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println(" |O|X\n------\nX|O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|O\n------\nX|O| \n------\n |O|X");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("O|X|O\n------\nX|O| \n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 6) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|X|O\n------\nX|O| \n------\nO|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println(" |X|O\n------\nX|O|X\n------\nO|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 1) {
					System.out.println("X|O| \n------\nX|O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |O| \n------\nX|O|X\n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |O| \n------\nX|O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 2) {
				System.out.println(" |X| \n------\n |O|O\n------\n | |X");
				move = scanner.nextInt();
				if (move == 4) {
					System.out.println(" |X| \n------\nX|O|O\n------\nO| |X");
					move = scanner.nextInt();
					if (move == 8) {
						System.out.println(" |X|O\n------\nX|O|O\n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("O|X|X\n------\nX|O|O\n------\nO| |X");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|X|O\n------\nX|O|O\n------\nO| |X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 8) {
					System.out.println(" |X| \n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|X| \n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |X| \n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println(" |X|X\n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 1) {
				System.out.println("X| | \n------\n |O| \n------\n |O|X");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("X|O|X\n------\n |O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X|O| \n------\n |O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("X|O| \n------\nX|O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("X|O| \n------\n |O|X\n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("X|X|O\n------\n |O| \n------\n |O|X");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("X|X|O\n------\n |O|X\n------\nO|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 7) {
						System.out.println("X|X|O\n------\nO|O| \n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 6) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("X|X|O\n------\nX|O| \n------\nO|O|X");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 3) {
				System.out.println(" | |X\n------\n |O|O\n------\n | |X");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X| |X\n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" | |X\n------\nX|O|O\n------\n |O|X");
					move = scanner.nextInt();
					if (move == 1) {
						System.out.println("X|O|X\n------\nX|O|O\n------\n |O|X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X|X\n------\nX|O|O\n------\n |O|X");
						move = scanner.nextInt();
						if (move == 7) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 7) {
						System.out.println(" |O|X\n------\nX|O|O\n------\nX|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 7) {
					System.out.println(" | |X\n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" | |X\n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|X\n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 8) {
				System.out.println(" | | \n------\n |O| \n------\nO|X|X");
				move = scanner.nextInt();
				if (move == 4) {
					System.out.println(" | |O\n------\nX|O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" | |O\n------\n |O|X\n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println(" | |X\n------\n |O|O\n------\nO|X|X");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("O| |X\n------\nX|O|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 2) {
						System.out.println(" |X|X\n------\nO|O|O\n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X| |X\n------\nO|O|O\n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 2) {
					System.out.println(" |X|O\n------\n |O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |O\n------\n |O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 6) {
				System.out.println(" | |O\n------\n |O|X\n------\n | |X");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println(" | |O\n------\n |O|X\n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |O\n------\n |O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" | |O\n------\n |O|X\n------\nX|O|X");
					move = scanner.nextInt();
					if (move == 1) {
						System.out.println("X|O|O\n------\n |O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println(" |O|O\n------\nX|O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 4) {
					System.out.println(" | |O\n------\nX|O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
			}
		}
		else if (move == 4) {
			System.out.println(" | | \n------\nX|O| \n------\n | | ");
			move = scanner.nextInt();
			if (move == 1) {
				System.out.println("X| | \n------\nX|O| \n------\nO| | ");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println("X| |O\n------\nX|O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("X|X|O\n------\nX|O| \n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X| |O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X| |O\n------\nX|O| \n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("X|O|X\n------\nX|O| \n------\nO| | ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("X|O|X\n------\nX|O| \n------\nO|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("X|O|X\n------\nX|O|X\n------\nO|O| ");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("X|O|X\n------\nX|O|O\n------\nO|X| ");
						move = scanner.nextInt();
						if (move == 9) {
							System.out.println("X|O|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
				}
			}
			else if (move == 3) {
				System.out.println(" |O|X\n------\nX|O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println(" |O|X\n------\nX|O| \n------\n |X|O");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("O|O|X\n------\nX|O| \n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("O|O|X\n------\nX|O|X\n------\n |X|O");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X|O|X\n------\nX|O| \n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 6) {
							System.out.println("X|O|X\n------\nX|O|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 9) {
					System.out.println(" |O|X\n------\nX|O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |O|X\n------\nX|O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|O|X\n------\nX|O| \n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |O|X\n------\nX|O| \n------\nX|O| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 8) {
				System.out.println(" | | \n------\nX|O| \n------\nO|X| ");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println(" |X|O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" | |O\n------\nX|O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\nX|O| \n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 2) {
						System.out.println("O|X|X\n------\nX|O| \n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O| |X\n------\nX|O|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println("O| |X\n------\nX|O|X\n------\nO|X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 6) {
					System.out.println(" | |O\n------\nX|O|X\n------\nO|X| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 7) {
				System.out.println("O| | \n------\nX|O| \n------\nX| | ");
				move = scanner.nextInt();
				if (move == 3) {
					System.out.println("O| |X\n------\nX|O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println("O|X| \n------\nX|O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("O| | \n------\nX|O|X\n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("O| | \n------\nX|O| \n------\nX|X|O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O| | \n------\nX|O| \n------\nX|O|X");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("O|O| \n------\nX|O|X\n------\nX|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X|O\n------\nX|O| \n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 6) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 3) {
						System.out.println("O|O|X\n------\nX|O| \n------\nX|O|X");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 2) {
				System.out.println("O|X| \n------\nX|O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println("O|X| \n------\nX|O| \n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O|X| \n------\nX|O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O|X|X\n------\nX|O| \n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("O|X| \n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O|X| \n------\nX|O| \n------\nO| |X");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("O|X|O\n------\nX|O|X\n------\nO| |X");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("O|X|X\n------\nX|O|O\n------\nO| |X");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 8) {
						System.out.println("O|X|O\n------\nX|O| \n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 6) {
				System.out.println("O| | \n------\nX|O|X\n------\n | | ");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println("O|X| \n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O| |O\n------\nX|O|X\n------\n | |X");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("O|O|O\n------\nX|O|X\n------\nX| |X");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X|O\n------\nX|O|X\n------\nO| |X");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("O| |O\n------\nX|O|X\n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 3) {
					System.out.println("O| |X\n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("O| | \n------\nX|O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O| | \n------\nX|O|X\n------\nX| |O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 9) {
				System.out.println(" | | \n------\nX|O| \n------\n |O|X");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X|O| \n------\nX|O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |O| \n------\nX|O|X\n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|O\n------\nX|O| \n------\n |O|X");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println(" |X|O\n------\nX|O|X\n------\nO|O|X");
						System.out.println("result: O Won");
					}
					else if (move == 7) {
						System.out.println("O|X|O\n------\nX|O| \n------\nX|O|X");
						move = scanner.nextInt();
						if (move == 6) {
							System.out.println("O|X|O\n------\nX|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|X|O\n------\nX|O| \n------\nO|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 3) {
					System.out.println(" |O|X\n------\nX|O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |O| \n------\nX|O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
			}
		}
		else if (move == 3) {
			System.out.println(" | |X\n------\n |O| \n------\n | | ");
			move = scanner.nextInt();
			if (move == 6) {
				System.out.println(" | |X\n------\n |O|X\n------\n | |O");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X|O|X\n------\n |O|X\n------\n | |O");
					move = scanner.nextInt();
					if (move == 8) {
						System.out.println("X|O|X\n------\n |O|X\n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 4) {
							System.out.println("X|O|X\n------\nX|O|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 7) {
						System.out.println("X|O|X\n------\n |O|X\n------\nX|O|O");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println("X|O|X\n------\nX|O|X\n------\n |O|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 2) {
					System.out.println("O|X|X\n------\n |O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("O| |X\n------\n |O|X\n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| |X\n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O| |X\n------\n |O|X\n------\nX| |O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 9) {
				System.out.println(" | |X\n------\n |O|O\n------\n | |X");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println(" | |X\n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |X\n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" |O|X\n------\nX|O|O\n------\n | |X");
					move = scanner.nextInt();
					if (move == 8) {
						System.out.println(" |O|X\n------\nX|O|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 1) {
							System.out.println("X|O|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|O|X\n------\nX|O|O\n------\n |O|X");
						System.out.println("result: O Won");
					}
					else if (move == 7) {
						System.out.println(" |O|X\n------\nX|O|O\n------\nX|O|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 7) {
					System.out.println(" | |X\n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 2) {
					System.out.println(" |X|X\n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 2) {
				System.out.println("O|X|X\n------\n |O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println("O|X|X\n------\n |O| \n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O|X|X\n------\n |O|O\n------\n | |X");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("O|X|X\n------\nO|O|O\n------\nX| |X");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("O|X|X\n------\nO|O|O\n------\n |X|X");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println("O|X|X\n------\nX|O|O\n------\n |O|X");
						move = scanner.nextInt();
						if (move == 7) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 6) {
					System.out.println("O|X|X\n------\n |O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O|X|X\n------\nX|O| \n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O|X|X\n------\n |O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 4) {
				System.out.println(" |O|X\n------\nX|O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 9) {
					System.out.println(" |O|X\n------\nX|O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" |O|X\n------\nX|O| \n------\n |X|O");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("O|O|X\n------\nX|O| \n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("O|O|X\n------\nX|O|X\n------\n |X|O");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X|O|X\n------\nX|O| \n------\nO|X|O");
						move = scanner.nextInt();
						if (move == 6) {
							System.out.println("X|O|X\n------\nX|O|X\n------\nO|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 1) {
					System.out.println("X|O|X\n------\nX|O| \n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |O|X\n------\nX|O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |O|X\n------\nX|O| \n------\nX|O| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 1) {
				System.out.println("X|O|X\n------\n |O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println("X|O|X\n------\nO|O| \n------\n |X| ");
					move = scanner.nextInt();
					if (move == 7) {
						System.out.println("X|O|X\n------\nO|O|O\n------\nX|X| ");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("X|O|X\n------\nO|O|O\n------\n |X|X");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("X|O|X\n------\nO|O|X\n------\n |X|O");
						move = scanner.nextInt();
						if (move == 7) {
							System.out.println("X|O|X\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
				}
				else if (move == 4) {
					System.out.println("X|O|X\n------\nX|O| \n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X|O|X\n------\n |O| \n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("X|O|X\n------\n |O|X\n------\n |O| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X|O|X\n------\n |O| \n------\n |O|X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 7) {
				System.out.println(" |O|X\n------\n |O| \n------\nX| | ");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println(" |O|X\n------\n |O|X\n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" |O|X\n------\n |O| \n------\nX|O|X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|O|X\n------\n |O| \n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" |O|X\n------\nX|O| \n------\nX|O| ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" |O|X\n------\n |O| \n------\nX|X|O");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("O|O|X\n------\nX|O| \n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 6) {
						System.out.println("O|O|X\n------\n |O|X\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 1) {
						System.out.println("X|O|X\n------\nO|O| \n------\nX|X|O");
						move = scanner.nextInt();
						if (move == 6) {
							System.out.println("X|O|X\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
				}
			}
			else if (move == 8) {
				System.out.println(" | |X\n------\n |O|O\n------\n |X| ");
				move = scanner.nextInt();
				if (move == 2) {
					System.out.println(" |X|X\n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X| |X\n------\nO|O|O\n------\n |X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" | |X\n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" | |X\n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O| |X\n------\nX|O|O\n------\n |X| ");
					move = scanner.nextInt();
					if (move == 9) {
						System.out.println("O| |X\n------\nX|O|O\n------\nO|X|X");
						move = scanner.nextInt();
						if (move == 2) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 7) {
						System.out.println("O| |X\n------\nX|O|O\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 2) {
						System.out.println("O|X|X\n------\nX|O|O\n------\n |X|O");
						System.out.println("result: O Won");
					}
				}
			}
		}
		else if (move == 2) {
			System.out.println(" |X| \n------\n |O| \n------\n | | ");
			move = scanner.nextInt();
			if (move == 7) {
				System.out.println(" |X| \n------\nO|O| \n------\nX| | ");
				move = scanner.nextInt();
				if (move == 9) {
					System.out.println(" |X| \n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|X| \n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" |X| \n------\nO|O|O\n------\nX|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println(" |X|X\n------\nO|O|O\n------\nX| | ");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println(" |X| \n------\nO|O|X\n------\nX| |O");
					move = scanner.nextInt();
					if (move == 1) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nX| |O");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 8) {
						System.out.println("O|X| \n------\nO|O|X\n------\nX|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("O|X|X\n------\nO|O|X\n------\nX| |O");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 1) {
				System.out.println("X|X|O\n------\n |O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 4) {
					System.out.println("X|X|O\n------\nX|O| \n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("X|X|O\n------\n |O| \n------\nO| |X");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println("X|X|O\n------\n |O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("X|X|O\n------\n |O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("X|X|O\n------\nO|O| \n------\nX| | ");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nX|O| ");
						move = scanner.nextInt();
						if (move == 9) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 9) {
						System.out.println("X|X|O\n------\nO|O|O\n------\nX| |X");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("X|X|O\n------\nO|O|O\n------\nX|X| ");
						System.out.println("result: O Won");
					}
				}
			}
			else if (move == 6) {
				System.out.println(" |X|O\n------\n |O|X\n------\n | | ");
				move = scanner.nextInt();
				if (move == 1) {
					System.out.println("X|X|O\n------\n |O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 8) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println(" |X|O\n------\nX|O|X\n------\nO| | ");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |X|O\n------\n |O|X\n------\nX| |O");
					move = scanner.nextInt();
					if (move == 1) {
						System.out.println("X|X|O\n------\nO|O|X\n------\nX| |O");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("X|X|O\n------\nO|O|X\n------\nX|X|O");
							System.out.println("result: Draw");
						}
					}
					else if (move == 4) {
						System.out.println("O|X|O\n------\nX|O|X\n------\nX| |O");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("O|X|O\n------\n |O|X\n------\nX|X|O");
						System.out.println("result: O Won");
					}
				}
				else if (move == 9) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO| |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 8) {
				System.out.println(" |X| \n------\n |O| \n------\nO|X| ");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println(" |X|O\n------\n |O|X\n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println(" |X|O\n------\n |O| \n------\nO|X|X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O|X|X\n------\n |O| \n------\nO|X| ");
					move = scanner.nextInt();
					if (move == 6) {
						System.out.println("O|X|X\n------\n |O|X\n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 4) {
						System.out.println("O|X|X\n------\nX|O| \n------\nO|X|O");
						System.out.println("result: O Won");
					}
					else if (move == 9) {
						System.out.println("O|X|X\n------\nO|O| \n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 4) {
					System.out.println(" |X|O\n------\nX|O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|X|O\n------\n |O| \n------\nO|X| ");
					System.out.println("result: O Won");
				}
			}
			else if (move == 3) {
				System.out.println("O|X|X\n------\n |O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 6) {
					System.out.println("O|X|X\n------\n |O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O|X|X\n------\n |O|O\n------\n | |X");
					move = scanner.nextInt();
					if (move == 4) {
						System.out.println("O|X|X\n------\nX|O|O\n------\n |O|X");
						move = scanner.nextInt();
						if (move == 7) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nX|O|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 7) {
						System.out.println("O|X|X\n------\nO|O|O\n------\nX| |X");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("O|X|X\n------\nO|O|O\n------\n |X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 8) {
					System.out.println("O|X|X\n------\n |O| \n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 4) {
					System.out.println("O|X|X\n------\nX|O| \n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println("O|X|X\n------\n |O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
			}
			else if (move == 9) {
				System.out.println(" |X| \n------\n |O|O\n------\n | |X");
				move = scanner.nextInt();
				if (move == 4) {
					System.out.println(" |X| \n------\nX|O|O\n------\nO| |X");
					move = scanner.nextInt();
					if (move == 8) {
						System.out.println(" |X|O\n------\nX|O|O\n------\nO|X|X");
						System.out.println("result: O Won");
					}
					else if (move == 3) {
						System.out.println("O|X|X\n------\nX|O|O\n------\nO| |X");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 1) {
						System.out.println("X|X|O\n------\nX|O|O\n------\nO| |X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 8) {
					System.out.println(" |X| \n------\nO|O|O\n------\n |X|X");
					System.out.println("result: O Won");
				}
				else if (move == 7) {
					System.out.println(" |X| \n------\nO|O|O\n------\nX| |X");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println(" |X|X\n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
				else if (move == 1) {
					System.out.println("X|X| \n------\nO|O|O\n------\n | |X");
					System.out.println("result: O Won");
				}
			}
			else if (move == 4) {
				System.out.println("O|X| \n------\nX|O| \n------\n | | ");
				move = scanner.nextInt();
				if (move == 8) {
					System.out.println("O|X| \n------\nX|O| \n------\n |X|O");
					System.out.println("result: O Won");
				}
				else if (move == 3) {
					System.out.println("O|X|X\n------\nX|O| \n------\n | |O");
					System.out.println("result: O Won");
				}
				else if (move == 9) {
					System.out.println("O|X| \n------\nX|O| \n------\nO| |X");
					move = scanner.nextInt();
					if (move == 3) {
						System.out.println("O|X|X\n------\nX|O|O\n------\nO| |X");
						move = scanner.nextInt();
						if (move == 8) {
							System.out.println("O|X|X\n------\nX|O|O\n------\nO|X|X");
							System.out.println("result: Draw");
						}
					}
					else if (move == 6) {
						System.out.println("O|X|O\n------\nX|O|X\n------\nO| |X");
						System.out.println("result: O Won");
					}
					else if (move == 8) {
						System.out.println("O|X|O\n------\nX|O| \n------\nO|X|X");
						System.out.println("result: O Won");
					}
				}
				else if (move == 7) {
					System.out.println("O|X| \n------\nX|O| \n------\nX| |O");
					System.out.println("result: O Won");
				}
				else if (move == 6) {
					System.out.println("O|X| \n------\nX|O|X\n------\n | |O");
					System.out.println("result: O Won");
				}
			}
		}
		scanner.close();
	}
}