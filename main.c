#include <stdio.h>
int main() {
	int move;
	printf(" | | \n------\n | | \n------\n | | ");
	scanf("%d", move);
	if (move == 2) {
		printf(" |X| \n------\n |O| \n------\n | | ");
		scanf("%d", move);
		if (move == 7) {
			printf(" |X| \n------\nO|O| \n------\nX| | ");
			scanf("%d", move);
			if (move == 9) {
				printf(" |X| \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" |X|X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|X| \n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" |X| \n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf(" |X| \n------\nO|O|X\n------\nX| |O");
				scanf("%d", move);
				if (move == 1) {
					printf("X|X|O\n------\nO|O|X\n------\nX| |O");
					scanf("%d", move);
					if (move == 8) {
						printf("X|X|O\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 3) {
					printf("O|X|X\n------\nO|O|X\n------\nX| |O");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O|X| \n------\nO|O|X\n------\nX|X|O");
					printf("result: O Won");
				}
			}
		}
		else if (move == 3) {
			printf("O|X|X\n------\n |O| \n------\n | | ");
			scanf("%d", move);
			if (move == 6) {
				printf("O|X|X\n------\n |O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("O|X|X\n------\n |O| \n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("O|X|X\n------\n |O|O\n------\n | |X");
				scanf("%d", move);
				if (move == 4) {
					printf("O|X|X\n------\nX|O|O\n------\nO| |X");
					scanf("%d", move);
					if (move == 8) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 7) {
					printf("O|X|X\n------\nO|O|O\n------\nX| |X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O|X|X\n------\nO|O|O\n------\n |X|X");
					printf("result: O Won");
				}
			}
			else if (move == 7) {
				printf("O|X|X\n------\n |O| \n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("O|X|X\n------\nX|O| \n------\n | |O");
				printf("result: O Won");
			}
		}
		else if (move == 1) {
			printf("X|X|O\n------\n |O| \n------\n | | ");
			scanf("%d", move);
			if (move == 4) {
				printf("X|X|O\n------\nX|O| \n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X|X|O\n------\n |O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X|X|O\n------\nO|O| \n------\nX| | ");
				scanf("%d", move);
				if (move == 8) {
					printf("X|X|O\n------\nO|O|O\n------\nX|X| ");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("X|X|O\n------\nO|O|O\n------\nX| |X");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("X|X|O\n------\nO|O|X\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("X|X|O\n------\nO|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 6) {
				printf("X|X|O\n------\n |O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("X|X|O\n------\n |O| \n------\nO| |X");
				printf("result: O Won");
			}
		}
		else if (move == 4) {
			printf("O|X| \n------\nX|O| \n------\n | | ");
			scanf("%d", move);
			if (move == 3) {
				printf("O|X|X\n------\nX|O| \n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("O|X| \n------\nX|O| \n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O|X| \n------\nX|O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("O|X|O\n------\nX|O| \n------\n | |X");
				scanf("%d", move);
				if (move == 7) {
					printf("O|X|O\n------\nX|O| \n------\nX|O|X");
					scanf("%d", move);
					if (move == 6) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 8) {
					printf("O|X|O\n------\nX|O| \n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("O|X|O\n------\nX|O|X\n------\nO| |X");
					printf("result: O Won");
				}
			}
			else if (move == 8) {
				printf("O|X| \n------\nX|O| \n------\n |X|O");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf(" |X|O\n------\n |O|X\n------\n | | ");
			scanf("%d", move);
			if (move == 1) {
				printf("X|X|O\n------\n |O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |X|O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" |X|O\n------\n |O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("O|X|O\n------\n |O|X\n------\nX| | ");
				scanf("%d", move);
				if (move == 9) {
					printf("O|X|O\n------\n |O|X\n------\nX|O|X");
					scanf("%d", move);
					if (move == 4) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 4) {
					printf("O|X|O\n------\nX|O|X\n------\nX| |O");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O|X|O\n------\n |O|X\n------\nX|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf(" |X|O\n------\n |O|X\n------\nO| |X");
				printf("result: O Won");
			}
		}
		else if (move == 9) {
			printf(" |X| \n------\n |O|O\n------\n | |X");
			scanf("%d", move);
			if (move == 7) {
				printf(" |X| \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |X| \n------\nX|O|O\n------\nO| |X");
				scanf("%d", move);
				if (move == 1) {
					printf("X|X|O\n------\nX|O|O\n------\nO| |X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf(" |X|O\n------\nX|O|O\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 3) {
					printf("O|X|X\n------\nX|O|O\n------\nO| |X");
					scanf("%d", move);
					if (move == 8) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 8) {
				printf(" |X| \n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|X| \n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" |X|X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
		}
		else if (move == 8) {
			printf(" |X| \n------\n |O| \n------\nO|X| ");
			scanf("%d", move);
			if (move == 6) {
				printf(" |X|O\n------\n |O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |X|O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|X|O\n------\n |O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O|X|X\n------\n |O| \n------\nO|X| ");
				scanf("%d", move);
				if (move == 9) {
					printf("O|X|X\n------\nO|O| \n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("O|X|X\n------\nX|O| \n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("O|X|X\n------\n |O|X\n------\nO|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf(" |X|O\n------\n |O| \n------\nO|X|X");
				printf("result: O Won");
			}
		}
	}
	else if (move == 9) {
		printf(" | | \n------\n |O| \n------\n | |X");
		scanf("%d", move);
		if (move == 8) {
			printf(" | | \n------\n |O| \n------\nO|X|X");
			scanf("%d", move);
			if (move == 6) {
				printf(" | |O\n------\n |O|X\n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|O\n------\n |O| \n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" | |X\n------\n |O|O\n------\nO|X|X");
				scanf("%d", move);
				if (move == 2) {
					printf(" |X|X\n------\nO|O|O\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("O| |X\n------\nX|O|O\n------\nO|X|X");
					scanf("%d", move);
					if (move == 2) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 1) {
					printf("X| |X\n------\nO|O|O\n------\nO|X|X");
					printf("result: O Won");
				}
			}
			else if (move == 4) {
				printf(" | |O\n------\nX|O| \n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\n |O| \n------\nO|X|X");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf(" | |O\n------\n |O|X\n------\n | |X");
			scanf("%d", move);
			if (move == 7) {
				printf(" | |O\n------\n |O|X\n------\nX|O|X");
				scanf("%d", move);
				if (move == 2) {
					printf(" |X|O\n------\nO|O|X\n------\nX|O|X");
					scanf("%d", move);
					if (move == 1) {
						printf("X|X|O\n------\nO|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 4) {
					printf(" |O|O\n------\nX|O|X\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X|O|O\n------\n |O|X\n------\nX|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 2) {
				printf(" |X|O\n------\n |O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" | |O\n------\n |O|X\n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\n |O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" | |O\n------\nX|O|X\n------\nO| |X");
				printf("result: O Won");
			}
		}
		else if (move == 3) {
			printf(" | |X\n------\n |O|O\n------\n | |X");
			scanf("%d", move);
			if (move == 8) {
				printf(" | |X\n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" | |X\n------\nX|O|O\n------\n |O|X");
				scanf("%d", move);
				if (move == 2) {
					printf("O|X|X\n------\nX|O|O\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|X\n------\nX|O|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 1) {
					printf("X|O|X\n------\nX|O|O\n------\n |O|X");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf(" |O|X\n------\nX|O|O\n------\nX|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 1) {
				printf("X| |X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" | |X\n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
		}
		else if (move == 2) {
			printf(" |X| \n------\n |O|O\n------\n | |X");
			scanf("%d", move);
			if (move == 1) {
				printf("X|X| \n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" |X| \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |X| \n------\nX|O|O\n------\nO| |X");
				scanf("%d", move);
				if (move == 3) {
					printf("O|X|X\n------\nX|O|O\n------\nO| |X");
					scanf("%d", move);
					if (move == 8) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 1) {
					printf("X|X|O\n------\nX|O|O\n------\nO| |X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf(" |X|O\n------\nX|O|O\n------\nO|X|X");
					printf("result: O Won");
				}
			}
			else if (move == 3) {
				printf(" |X|X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" |X| \n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
		}
		else if (move == 4) {
			printf(" | | \n------\nX|O| \n------\n |O|X");
			scanf("%d", move);
			if (move == 2) {
				printf(" |X|O\n------\nX|O| \n------\n |O|X");
				scanf("%d", move);
				if (move == 1) {
					printf("X|X|O\n------\nX|O| \n------\nO|O|X");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf("O|X|O\n------\nX|O| \n------\nX|O|X");
					scanf("%d", move);
					if (move == 6) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf(" |X|O\n------\nX|O|X\n------\nO|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 1) {
				printf("X|O| \n------\nX|O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf(" |O| \n------\nX|O|X\n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" |O|X\n------\nX|O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" |O| \n------\nX|O| \n------\nX|O|X");
				printf("result: O Won");
			}
		}
		else if (move == 1) {
			printf("X| | \n------\n |O|O\n------\n | |X");
			scanf("%d", move);
			if (move == 4) {
				printf("X| | \n------\nX|O|O\n------\nO| |X");
				scanf("%d", move);
				if (move == 2) {
					printf("X|X|O\n------\nX|O|O\n------\nO| |X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("X| |O\n------\nX|O|O\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 3) {
					printf("X|O|X\n------\nX|O|O\n------\nO| |X");
					scanf("%d", move);
					if (move == 8) {
						printf("X|O|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 3) {
				printf("X| |X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("X|X| \n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X| | \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X| | \n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
		}
		else if (move == 7) {
			printf(" | | \n------\n |O| \n------\nX|O|X");
			scanf("%d", move);
			if (move == 2) {
				printf(" |X| \n------\n |O|O\n------\nX|O|X");
				scanf("%d", move);
				if (move == 4) {
					printf("O|X| \n------\nX|O|O\n------\nX|O|X");
					scanf("%d", move);
					if (move == 3) {
						printf("O|X|X\n------\nX|O|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 1) {
					printf("X|X| \n------\nO|O|O\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 3) {
					printf(" |X|X\n------\nO|O|O\n------\nX|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 6) {
				printf(" |O| \n------\n |O|X\n------\nX|O|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|O| \n------\n |O| \n------\nX|O|X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |O| \n------\nX|O| \n------\nX|O|X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" |O|X\n------\n |O| \n------\nX|O|X");
				printf("result: O Won");
			}
		}
	}
	else if (move == 1) {
		printf("X| | \n------\n |O| \n------\n | | ");
		scanf("%d", move);
		if (move == 2) {
			printf("X|X|O\n------\n |O| \n------\n | | ");
			scanf("%d", move);
			if (move == 4) {
				printf("X|X|O\n------\nX|O| \n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X|X|O\n------\n |O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X|X|O\n------\nO|O| \n------\nX| | ");
				scanf("%d", move);
				if (move == 9) {
					printf("X|X|O\n------\nO|O|O\n------\nX| |X");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("X|X|O\n------\nO|O|X\n------\nX| |O");
					scanf("%d", move);
					if (move == 8) {
						printf("X|X|O\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 8) {
					printf("X|X|O\n------\nO|O|O\n------\nX|X| ");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf("X|X|O\n------\n |O| \n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("X|X|O\n------\n |O|X\n------\nO| | ");
				printf("result: O Won");
			}
		}
		else if (move == 3) {
			printf("X|O|X\n------\n |O| \n------\n | | ");
			scanf("%d", move);
			if (move == 6) {
				printf("X|O|X\n------\n |O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("X|O|X\n------\nX|O| \n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X|O|X\n------\n |O| \n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("X|O|X\n------\n |O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X|O|X\n------\n |O|O\n------\n |X| ");
				scanf("%d", move);
				if (move == 9) {
					printf("X|O|X\n------\nO|O|O\n------\n |X|X");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("X|O|X\n------\nX|O|O\n------\nO|X| ");
					scanf("%d", move);
					if (move == 9) {
						printf("X|O|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 7) {
					printf("X|O|X\n------\nO|O|O\n------\nX|X| ");
					printf("result: O Won");
				}
			}
		}
		else if (move == 7) {
			printf("X| | \n------\nO|O| \n------\nX| | ");
			scanf("%d", move);
			if (move == 2) {
				printf("X|X| \n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("X| | \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X| | \n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("X| |X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("X| | \n------\nO|O|X\n------\nX|O| ");
				scanf("%d", move);
				if (move == 3) {
					printf("X|O|X\n------\nO|O|X\n------\nX|O| ");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("X|O| \n------\nO|O|X\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("X|X|O\n------\nO|O|X\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("X|X|O\n------\nO|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
		}
		else if (move == 8) {
			printf("X| | \n------\nO|O| \n------\n |X| ");
			scanf("%d", move);
			if (move == 9) {
				printf("X| | \n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X| | \n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("X|X| \n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("X| |X\n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("X| |O\n------\nO|O|X\n------\n |X| ");
				scanf("%d", move);
				if (move == 9) {
					printf("X| |O\n------\nO|O|X\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("X|X|O\n------\nO|O|X\n------\nO|X| ");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf("X| |O\n------\nO|O|X\n------\nX|X|O");
					scanf("%d", move);
					if (move == 2) {
						printf("X|X|O\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
			}
		}
		else if (move == 9) {
			printf("X| | \n------\nO|O| \n------\n | |X");
			scanf("%d", move);
			if (move == 8) {
				printf("X| | \n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X| | \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("X| |X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("X| |O\n------\nO|O|X\n------\n | |X");
				scanf("%d", move);
				if (move == 2) {
					printf("X|X|O\n------\nO|O|X\n------\nO| |X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("X| |O\n------\nO|O|X\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf("X| |O\n------\nO|O|X\n------\nX|O|X");
					scanf("%d", move);
					if (move == 2) {
						printf("X|X|O\n------\nO|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 2) {
				printf("X|X| \n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
		}
		else if (move == 4) {
			printf("X| | \n------\nX|O| \n------\nO| | ");
			scanf("%d", move);
			if (move == 2) {
				printf("X|X|O\n------\nX|O| \n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("X| |O\n------\nX|O| \n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("X|O|X\n------\nX|O| \n------\nO| | ");
				scanf("%d", move);
				if (move == 6) {
					printf("X|O|X\n------\nX|O|X\n------\nO|O| ");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("X|O|X\n------\nX|O| \n------\nO|O|X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("X|O|X\n------\nX|O| \n------\nO|X|O");
					scanf("%d", move);
					if (move == 6) {
						printf("X|O|X\n------\nX|O|X\n------\nO|X|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 6) {
				printf("X| |O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X| |O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf("X|O| \n------\n |O|X\n------\n | | ");
			scanf("%d", move);
			if (move == 4) {
				printf("X|O| \n------\nX|O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X|O| \n------\n |O|X\n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X|O| \n------\n |O|X\n------\nO|X| ");
				scanf("%d", move);
				if (move == 3) {
					printf("X|O|X\n------\n |O|X\n------\nO|X|O");
					scanf("%d", move);
					if (move == 4) {
						printf("X|O|X\n------\nX|O|X\n------\nO|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 9) {
					printf("X|O|O\n------\n |O|X\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("X|O|O\n------\nX|O|X\n------\nO|X| ");
					printf("result: O Won");
				}
			}
			else if (move == 3) {
				printf("X|O|X\n------\n |O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("X|O| \n------\n |O|X\n------\n |O|X");
				printf("result: O Won");
			}
		}
	}
	else if (move == 6) {
		printf(" | | \n------\n |O|X\n------\n | | ");
		scanf("%d", move);
		if (move == 4) {
			printf(" | | \n------\nX|O|X\n------\nO| | ");
			scanf("%d", move);
			if (move == 8) {
				printf(" | |O\n------\nX|O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" | |X\n------\nX|O|X\n------\nO| |O");
				scanf("%d", move);
				if (move == 1) {
					printf("X| |X\n------\nX|O|X\n------\nO|O|O");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf(" |X|X\n------\nX|O|X\n------\nO|O|O");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O| |X\n------\nX|O|X\n------\nO|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf(" | |O\n------\nX|O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
		}
		else if (move == 2) {
			printf(" |X|O\n------\n |O|X\n------\n | | ");
			scanf("%d", move);
			if (move == 8) {
				printf(" |X|O\n------\n |O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|X|O\n------\n |O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" |X|O\n------\n |O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("O|X|O\n------\n |O|X\n------\nX| | ");
				scanf("%d", move);
				if (move == 8) {
					printf("O|X|O\n------\n |O|X\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("O|X|O\n------\nX|O|X\n------\nX| |O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O|X|O\n------\n |O|X\n------\nX|O|X");
					scanf("%d", move);
					if (move == 4) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 4) {
				printf(" |X|O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
		}
		else if (move == 8) {
			printf(" | | \n------\n |O|X\n------\n |X|O");
			scanf("%d", move);
			if (move == 7) {
				printf("O| | \n------\n |O|X\n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O| |X\n------\n |O|X\n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\n |O|X\n------\n |X|O");
				scanf("%d", move);
				if (move == 7) {
					printf("X| |O\n------\nO|O|X\n------\nX|X|O");
					scanf("%d", move);
					if (move == 2) {
						printf("X|X|O\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 2) {
					printf("X|X|O\n------\n |O|X\n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("X| |O\n------\nX|O|X\n------\nO|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 2) {
				printf("O|X| \n------\n |O|X\n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("O| | \n------\nX|O|X\n------\n |X|O");
				printf("result: O Won");
			}
		}
		else if (move == 7) {
			printf(" | | \n------\n |O|X\n------\nX|O| ");
			scanf("%d", move);
			if (move == 1) {
				printf("X|O| \n------\n |O|X\n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |O| \n------\nX|O|X\n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("O|X| \n------\n |O|X\n------\nX|O| ");
				scanf("%d", move);
				if (move == 4) {
					printf("O|X| \n------\nX|O|X\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 3) {
					printf("O|X|X\n------\n |O|X\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O|X|O\n------\n |O|X\n------\nX|O|X");
					scanf("%d", move);
					if (move == 4) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 3) {
				printf(" |O|X\n------\n |O|X\n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" |O| \n------\n |O|X\n------\nX|O|X");
				printf("result: O Won");
			}
		}
		else if (move == 1) {
			printf("X|O| \n------\n |O|X\n------\n | | ");
			scanf("%d", move);
			if (move == 3) {
				printf("X|O|X\n------\n |O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("X|O| \n------\nX|O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X|O| \n------\n |O|X\n------\nO|X| ");
				scanf("%d", move);
				if (move == 3) {
					printf("X|O|X\n------\n |O|X\n------\nO|X|O");
					scanf("%d", move);
					if (move == 4) {
						printf("X|O|X\n------\nX|O|X\n------\nO|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 9) {
					printf("X|O|O\n------\n |O|X\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("X|O|O\n------\nX|O|X\n------\nO|X| ");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf("X|O| \n------\n |O|X\n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X|O| \n------\n |O|X\n------\nX|O| ");
				printf("result: O Won");
			}
		}
		else if (move == 9) {
			printf(" | |O\n------\n |O|X\n------\n | |X");
			scanf("%d", move);
			if (move == 1) {
				printf("X| |O\n------\n |O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" | |O\n------\nX|O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" | |O\n------\n |O|X\n------\nX|O|X");
				scanf("%d", move);
				if (move == 4) {
					printf(" |O|O\n------\nX|O|X\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X|O|O\n------\n |O|X\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf(" |X|O\n------\nO|O|X\n------\nX|O|X");
					scanf("%d", move);
					if (move == 1) {
						printf("X|X|O\n------\nO|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 2) {
				printf(" |X|O\n------\n |O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" | |O\n------\n |O|X\n------\nO|X|X");
				printf("result: O Won");
			}
		}
		else if (move == 3) {
			printf(" | |X\n------\n |O|X\n------\n | |O");
			scanf("%d", move);
			if (move == 4) {
				printf("O| |X\n------\nX|O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("O|X|X\n------\n |O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("O| |X\n------\n |O|X\n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|O|X\n------\n |O|X\n------\n | |O");
				scanf("%d", move);
				if (move == 8) {
					printf("X|O|X\n------\nO|O|X\n------\n |X|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|O|X\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 4) {
					printf("X|O|X\n------\nX|O|X\n------\n |O|O");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf("X|O|X\n------\n |O|X\n------\nX|O|O");
					printf("result: O Won");
				}
			}
			else if (move == 7) {
				printf("O| |X\n------\n |O|X\n------\nX| |O");
				printf("result: O Won");
			}
		}
	}
	else if (move == 8) {
		printf(" | | \n------\n |O| \n------\n |X| ");
		scanf("%d", move);
		if (move == 4) {
			printf(" | | \n------\nX|O| \n------\nO|X| ");
			scanf("%d", move);
			if (move == 9) {
				printf(" | |O\n------\nX|O| \n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O| |X\n------\nX|O| \n------\nO|X| ");
				scanf("%d", move);
				if (move == 2) {
					printf("O|X|X\n------\nX|O| \n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O| |X\n------\nX|O|O\n------\nO|X|X");
					scanf("%d", move);
					if (move == 2) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf("O| |X\n------\nX|O|X\n------\nO|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 6) {
				printf(" | |O\n------\nX|O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
		}
		else if (move == 3) {
			printf(" | |X\n------\n |O|O\n------\n |X| ");
			scanf("%d", move);
			if (move == 4) {
				printf("O| |X\n------\nX|O|O\n------\n |X| ");
				scanf("%d", move);
				if (move == 7) {
					printf("O| |X\n------\nX|O|O\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O| |X\n------\nX|O|O\n------\nO|X|X");
					scanf("%d", move);
					if (move == 2) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 2) {
					printf("O|X|X\n------\nX|O|O\n------\n |X|O");
					printf("result: O Won");
				}
			}
			else if (move == 2) {
				printf(" |X|X\n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |X\n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" | |X\n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" | |X\n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf(" | | \n------\n |O|X\n------\n |X|O");
			scanf("%d", move);
			if (move == 2) {
				printf("O|X| \n------\n |O|X\n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O| |X\n------\n |O|X\n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("O| | \n------\nX|O|X\n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\n |O|X\n------\n |X|O");
				scanf("%d", move);
				if (move == 7) {
					printf("X| |O\n------\nO|O|X\n------\nX|X|O");
					scanf("%d", move);
					if (move == 2) {
						printf("X|X|O\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 4) {
					printf("X| |O\n------\nX|O|X\n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("X|X|O\n------\n |O|X\n------\nO|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 7) {
				printf("O| | \n------\n |O|X\n------\nX|X|O");
				printf("result: O Won");
			}
		}
		else if (move == 2) {
			printf(" |X| \n------\n |O| \n------\nO|X| ");
			scanf("%d", move);
			if (move == 1) {
				printf("X|X|O\n------\n |O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O|X|X\n------\n |O| \n------\nO|X| ");
				scanf("%d", move);
				if (move == 6) {
					printf("O|X|X\n------\n |O|X\n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O|X|X\n------\nO|O| \n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("O|X|X\n------\nX|O| \n------\nO|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf(" |X|O\n------\n |O| \n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf(" |X|O\n------\n |O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |X|O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
		}
		else if (move == 1) {
			printf("X| | \n------\nO|O| \n------\n |X| ");
			scanf("%d", move);
			if (move == 7) {
				printf("X| | \n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("X|X| \n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("X| |X\n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("X| |O\n------\nO|O|X\n------\n |X| ");
				scanf("%d", move);
				if (move == 2) {
					printf("X|X|O\n------\nO|O|X\n------\nO|X| ");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf("X| |O\n------\nO|O|X\n------\nX|X|O");
					scanf("%d", move);
					if (move == 2) {
						printf("X|X|O\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 9) {
					printf("X| |O\n------\nO|O|X\n------\nO|X|X");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf("X| | \n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
		}
		else if (move == 9) {
			printf(" | | \n------\n |O| \n------\nO|X|X");
			scanf("%d", move);
			if (move == 1) {
				printf("X| |O\n------\n |O| \n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf(" | |O\n------\n |O|X\n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" | |O\n------\nX|O| \n------\nO|X|X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" | |X\n------\n |O|O\n------\nO|X|X");
				scanf("%d", move);
				if (move == 1) {
					printf("X| |X\n------\nO|O|O\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf(" |X|X\n------\nO|O|O\n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("O| |X\n------\nX|O|O\n------\nO|X|X");
					scanf("%d", move);
					if (move == 2) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 2) {
				printf(" |X|O\n------\n |O| \n------\nO|X|X");
				printf("result: O Won");
			}
		}
		else if (move == 7) {
			printf(" | | \n------\n |O| \n------\nX|X|O");
			scanf("%d", move);
			if (move == 1) {
				printf("X| | \n------\nO|O| \n------\nX|X|O");
				scanf("%d", move);
				if (move == 3) {
					printf("X| |X\n------\nO|O|O\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("X|O| \n------\nO|O|X\n------\nX|X|O");
					scanf("%d", move);
					if (move == 3) {
						printf("X|O|X\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 2) {
					printf("X|X| \n------\nO|O|O\n------\nX|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 4) {
				printf("O| | \n------\nX|O| \n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O| |X\n------\n |O| \n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O| | \n------\n |O|X\n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("O|X| \n------\n |O| \n------\nX|X|O");
				printf("result: O Won");
			}
		}
	}
	else if (move == 7) {
		printf(" | | \n------\n |O| \n------\nX| | ");
		scanf("%d", move);
		if (move == 9) {
			printf(" | | \n------\n |O| \n------\nX|O|X");
			scanf("%d", move);
			if (move == 1) {
				printf("X|O| \n------\n |O| \n------\nX|O|X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" |O|X\n------\n |O| \n------\nX|O|X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X| \n------\n |O|O\n------\nX|O|X");
				scanf("%d", move);
				if (move == 4) {
					printf("O|X| \n------\nX|O|O\n------\nX|O|X");
					scanf("%d", move);
					if (move == 3) {
						printf("O|X|X\n------\nX|O|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 3) {
					printf(" |X|X\n------\nO|O|O\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X|X| \n------\nO|O|O\n------\nX|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 6) {
				printf(" |O| \n------\n |O|X\n------\nX|O|X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" |O| \n------\nX|O| \n------\nX|O|X");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf(" | | \n------\n |O|X\n------\nX|O| ");
			scanf("%d", move);
			if (move == 4) {
				printf(" |O| \n------\nX|O|X\n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|O| \n------\n |O|X\n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("O|X| \n------\n |O|X\n------\nX|O| ");
				scanf("%d", move);
				if (move == 9) {
					printf("O|X|O\n------\n |O|X\n------\nX|O|X");
					scanf("%d", move);
					if (move == 4) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 3) {
					printf("O|X|X\n------\n |O|X\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("O|X| \n------\nX|O|X\n------\nX|O|O");
					printf("result: O Won");
				}
			}
			else if (move == 3) {
				printf(" |O|X\n------\n |O|X\n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" |O| \n------\n |O|X\n------\nX|O|X");
				printf("result: O Won");
			}
		}
		else if (move == 4) {
			printf("O| | \n------\nX|O| \n------\nX| | ");
			scanf("%d", move);
			if (move == 8) {
				printf("O| | \n------\nX|O| \n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O| |X\n------\nX|O| \n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O| | \n------\nX|O|X\n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("O| | \n------\nX|O| \n------\nX|O|X");
				scanf("%d", move);
				if (move == 6) {
					printf("O|O| \n------\nX|O|X\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("O|X|O\n------\nX|O| \n------\nX|O|X");
					scanf("%d", move);
					if (move == 6) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 3) {
					printf("O|O|X\n------\nX|O| \n------\nX|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 2) {
				printf("O|X| \n------\nX|O| \n------\nX| |O");
				printf("result: O Won");
			}
		}
		else if (move == 1) {
			printf("X| | \n------\nO|O| \n------\nX| | ");
			scanf("%d", move);
			if (move == 2) {
				printf("X|X| \n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("X| |X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("X| | \n------\nO|O|X\n------\nX|O| ");
				scanf("%d", move);
				if (move == 2) {
					printf("X|X|O\n------\nO|O|X\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("X|X|O\n------\nO|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 3) {
					printf("X|O|X\n------\nO|O|X\n------\nX|O| ");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("X|O| \n------\nO|O|X\n------\nX|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf("X| | \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X| | \n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
		}
		else if (move == 8) {
			printf(" | | \n------\n |O| \n------\nX|X|O");
			scanf("%d", move);
			if (move == 3) {
				printf("O| |X\n------\n |O| \n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| | \n------\nO|O| \n------\nX|X|O");
				scanf("%d", move);
				if (move == 3) {
					printf("X| |X\n------\nO|O|O\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("X|O| \n------\nO|O|X\n------\nX|X|O");
					scanf("%d", move);
					if (move == 3) {
						printf("X|O|X\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 2) {
					printf("X|X| \n------\nO|O|O\n------\nX|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 4) {
				printf("O| | \n------\nX|O| \n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O| | \n------\n |O|X\n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("O|X| \n------\n |O| \n------\nX|X|O");
				printf("result: O Won");
			}
		}
		else if (move == 3) {
			printf(" | |X\n------\nO|O| \n------\nX| | ");
			scanf("%d", move);
			if (move == 6) {
				printf(" | |X\n------\nO|O|X\n------\nX| |O");
				scanf("%d", move);
				if (move == 1) {
					printf("X|O|X\n------\nO|O|X\n------\nX| |O");
					scanf("%d", move);
					if (move == 8) {
						printf("X|O|X\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 8) {
					printf("O| |X\n------\nO|O|X\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("O|X|X\n------\nO|O|X\n------\nX| |O");
					printf("result: O Won");
				}
			}
			else if (move == 9) {
				printf(" | |X\n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" | |X\n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
		}
		else if (move == 2) {
			printf(" |X| \n------\nO|O| \n------\nX| | ");
			scanf("%d", move);
			if (move == 9) {
				printf(" |X| \n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" |X|X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|X| \n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf(" |X| \n------\nO|O|X\n------\nX| |O");
				scanf("%d", move);
				if (move == 1) {
					printf("X|X|O\n------\nO|O|X\n------\nX| |O");
					scanf("%d", move);
					if (move == 8) {
						printf("X|X|O\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 3) {
					printf("O|X|X\n------\nO|O|X\n------\nX| |O");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O|X| \n------\nO|O|X\n------\nX|X|O");
					printf("result: O Won");
				}
			}
			else if (move == 8) {
				printf(" |X| \n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
		}
	}
	else if (move == 4) {
		printf(" | | \n------\nX|O| \n------\n | | ");
		scanf("%d", move);
		if (move == 9) {
			printf(" | | \n------\nX|O| \n------\n |O|X");
			scanf("%d", move);
			if (move == 7) {
				printf(" |O| \n------\nX|O| \n------\nX|O|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|O| \n------\nX|O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" |O|X\n------\nX|O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|O\n------\nX|O| \n------\n |O|X");
				scanf("%d", move);
				if (move == 1) {
					printf("X|X|O\n------\nX|O| \n------\nO|O|X");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf("O|X|O\n------\nX|O| \n------\nX|O|X");
					scanf("%d", move);
					if (move == 6) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf(" |X|O\n------\nX|O|X\n------\nO|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 6) {
				printf(" |O| \n------\nX|O|X\n------\n |O|X");
				printf("result: O Won");
			}
		}
		else if (move == 7) {
			printf("O| | \n------\nX|O| \n------\nX| | ");
			scanf("%d", move);
			if (move == 3) {
				printf("O| |X\n------\nX|O| \n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("O| | \n------\nX|O| \n------\nX|O|X");
				scanf("%d", move);
				if (move == 6) {
					printf("O|O| \n------\nX|O|X\n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 3) {
					printf("O|O|X\n------\nX|O| \n------\nX|O|X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("O|X|O\n------\nX|O| \n------\nX|O|X");
					scanf("%d", move);
					if (move == 6) {
						printf("O|X|O\n------\nX|O|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 2) {
				printf("O|X| \n------\nX|O| \n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("O| | \n------\nX|O| \n------\nX|X|O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O| | \n------\nX|O|X\n------\nX| |O");
				printf("result: O Won");
			}
		}
		else if (move == 1) {
			printf("X| | \n------\nX|O| \n------\nO| | ");
			scanf("%d", move);
			if (move == 3) {
				printf("X|O|X\n------\nX|O| \n------\nO| | ");
				scanf("%d", move);
				if (move == 6) {
					printf("X|O|X\n------\nX|O|X\n------\nO|O| ");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("X|O|X\n------\nX|O| \n------\nO|O|X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("X|O|X\n------\nX|O|O\n------\nO|X| ");
					scanf("%d", move);
					if (move == 9) {
						printf("X|O|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 6) {
				printf("X| |O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("X| |O\n------\nX|O| \n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X| |O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("X|X|O\n------\nX|O| \n------\nO| | ");
				printf("result: O Won");
			}
		}
		else if (move == 2) {
			printf("O|X| \n------\nX|O| \n------\n | | ");
			scanf("%d", move);
			if (move == 3) {
				printf("O|X|X\n------\nX|O| \n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O|X| \n------\nX|O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("O|X| \n------\nX|O| \n------\nO| |X");
				scanf("%d", move);
				if (move == 8) {
					printf("O|X|O\n------\nX|O| \n------\nO|X|X");
					printf("result: O Won");
				}
				else if (move == 3) {
					printf("O|X|X\n------\nX|O|O\n------\nO| |X");
					scanf("%d", move);
					if (move == 8) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf("O|X|O\n------\nX|O|X\n------\nO| |X");
					printf("result: O Won");
				}
			}
			else if (move == 7) {
				printf("O|X| \n------\nX|O| \n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("O|X| \n------\nX|O| \n------\n |X|O");
				printf("result: O Won");
			}
		}
		else if (move == 8) {
			printf(" | | \n------\nX|O| \n------\nO|X| ");
			scanf("%d", move);
			if (move == 1) {
				printf("X| |O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|O\n------\nX|O| \n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf("O| |X\n------\nX|O| \n------\nO|X| ");
				scanf("%d", move);
				if (move == 2) {
					printf("O|X|X\n------\nX|O| \n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("O| |X\n------\nX|O|X\n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O| |X\n------\nX|O|O\n------\nO|X|X");
					scanf("%d", move);
					if (move == 2) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 6) {
				printf(" | |O\n------\nX|O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" | |O\n------\nX|O| \n------\nO|X|X");
				printf("result: O Won");
			}
		}
		else if (move == 3) {
			printf(" |O|X\n------\nX|O| \n------\n | | ");
			scanf("%d", move);
			if (move == 8) {
				printf(" |O|X\n------\nX|O| \n------\n |X|O");
				scanf("%d", move);
				if (move == 7) {
					printf("O|O|X\n------\nX|O| \n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X|O|X\n------\nX|O| \n------\nO|X|O");
					scanf("%d", move);
					if (move == 6) {
						printf("X|O|X\n------\nX|O|X\n------\nO|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf("O|O|X\n------\nX|O|X\n------\n |X|O");
					printf("result: O Won");
				}
			}
			else if (move == 6) {
				printf(" |O|X\n------\nX|O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" |O|X\n------\nX|O| \n------\nX|O| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" |O|X\n------\nX|O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|O|X\n------\nX|O| \n------\n |O| ");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf(" | | \n------\nX|O|X\n------\nO| | ");
			scanf("%d", move);
			if (move == 9) {
				printf(" | |O\n------\nX|O|X\n------\nO| |X");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" | |O\n------\nX|O|X\n------\nO|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\nX|O|X\n------\nO| | ");
				printf("result: O Won");
			}
			else if (move == 3) {
				printf(" | |X\n------\nX|O|X\n------\nO| |O");
				scanf("%d", move);
				if (move == 2) {
					printf("O|X|X\n------\nX|O|X\n------\nO| |O");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O| |X\n------\nX|O|X\n------\nO|X|O");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X| |X\n------\nX|O|X\n------\nO|O|O");
					printf("result: O Won");
				}
			}
		}
	}
	else if (move == 5) {
		printf(" | |O\n------\n |X| \n------\n | | ");
		scanf("%d", move);
		if (move == 4) {
			printf(" | |O\n------\nX|X|O\n------\n | | ");
			scanf("%d", move);
			if (move == 8) {
				printf(" | |O\n------\nX|X|O\n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("O| |O\n------\nX|X|O\n------\n | |X");
				scanf("%d", move);
				if (move == 7) {
					printf("O|O|O\n------\nX|X|O\n------\nX| |X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("O|X|O\n------\nX|X|O\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nX|X|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 8) {
					printf("O|O|O\n------\nX|X|O\n------\n |X|X");
					printf("result: O Won");
				}
			}
			else if (move == 7) {
				printf(" | |O\n------\nX|X|O\n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|O\n------\nX|X|O\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |O\n------\nX|X|O\n------\n | |O");
				printf("result: O Won");
			}
		}
		else if (move == 7) {
			printf("O| |O\n------\n |X| \n------\nX| | ");
			scanf("%d", move);
			if (move == 9) {
				printf("O|O|O\n------\n |X| \n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("O|X|O\n------\n |X| \n------\nX|O| ");
				scanf("%d", move);
				if (move == 4) {
					printf("O|X|O\n------\nX|X|O\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("O|X|O\n------\nX|X|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf("O|X|O\n------\nO|X|X\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 9) {
					printf("O|X|O\n------\nO|X| \n------\nX|O|X");
					scanf("%d", move);
					if (move == 6) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 8) {
				printf("O|O|O\n------\n |X| \n------\nX|X| ");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O|O|O\n------\n |X|X\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("O|O|O\n------\nX|X| \n------\nX| | ");
				printf("result: O Won");
			}
		}
		else if (move == 2) {
			printf(" |X|O\n------\n |X| \n------\n |O| ");
			scanf("%d", move);
			if (move == 1) {
				printf("X|X|O\n------\n |X| \n------\n |O|O");
				scanf("%d", move);
				if (move == 7) {
					printf("X|X|O\n------\n |X|O\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("X|X|O\n------\nX|X| \n------\nO|O|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("X|X|O\n------\n |X|X\n------\nO|O|O");
					printf("result: O Won");
				}
			}
			else if (move == 7) {
				printf(" |X|O\n------\n |X| \n------\nX|O|O");
				scanf("%d", move);
				if (move == 1) {
					printf("X|X|O\n------\n |X|O\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf(" |X|O\n------\nX|X|O\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf(" |X|O\n------\nO|X|X\n------\nX|O|O");
					scanf("%d", move);
					if (move == 1) {
						printf("X|X|O\n------\nO|X|X\n------\nX|O|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 4) {
				printf(" |X|O\n------\nX|X|O\n------\n |O| ");
				scanf("%d", move);
				if (move == 7) {
					printf(" |X|O\n------\nX|X|O\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X|X|O\n------\nX|X|O\n------\n |O|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O|X|O\n------\nX|X|O\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nX|X|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 6) {
				printf(" |X|O\n------\nO|X|X\n------\n |O| ");
				scanf("%d", move);
				if (move == 7) {
					printf("O|X|O\n------\nO|X|X\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 9) {
					printf("O|X|O\n------\nO|X|X\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 1) {
					printf("X|X|O\n------\nO|X|X\n------\n |O|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|X|O\n------\nO|X|X\n------\nX|O|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 9) {
				printf("O|X|O\n------\n |X| \n------\n |O|X");
				scanf("%d", move);
				if (move == 7) {
					printf("O|X|O\n------\n |X|O\n------\nX|O|X");
					scanf("%d", move);
					if (move == 4) {
						printf("O|X|O\n------\nX|X|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf("O|X|O\n------\nO|X|X\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 4) {
					printf("O|X|O\n------\nX|X|O\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nX|X|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
		}
		else if (move == 8) {
			printf(" |O|O\n------\n |X| \n------\n |X| ");
			scanf("%d", move);
			if (move == 9) {
				printf("O|O|O\n------\n |X| \n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O|O|O\n------\n |X|X\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("O|O|O\n------\n |X| \n------\nX|X| ");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|O|O\n------\n |X| \n------\n |X|O");
				scanf("%d", move);
				if (move == 7) {
					printf("X|O|O\n------\n |X|O\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("X|O|O\n------\nX|X|O\n------\n |X|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("X|O|O\n------\nO|X|X\n------\n |X|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|O|O\n------\nO|X|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 4) {
				printf("O|O|O\n------\nX|X| \n------\n |X| ");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf(" | |O\n------\nO|X|X\n------\n | | ");
			scanf("%d", move);
			if (move == 7) {
				printf("O| |O\n------\nO|X|X\n------\nX| | ");
				scanf("%d", move);
				if (move == 8) {
					printf("O|O|O\n------\nO|X|X\n------\nX|X| ");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("O|X|O\n------\nO|X|X\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 9) {
					printf("O|O|O\n------\nO|X|X\n------\nX| |X");
					printf("result: O Won");
				}
			}
			else if (move == 2) {
				printf(" |X|O\n------\nO|X|X\n------\n |O| ");
				scanf("%d", move);
				if (move == 1) {
					printf("X|X|O\n------\nO|X|X\n------\n |O|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|X|O\n------\nO|X|X\n------\nX|O|O");
						printf("result: Draw");
					}
				}
				else if (move == 7) {
					printf("O|X|O\n------\nO|X|X\n------\nX|O| ");
					scanf("%d", move);
					if (move == 9) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 9) {
					printf("O|X|O\n------\nO|X|X\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 9) {
				printf("O| |O\n------\nO|X|X\n------\n | |X");
				scanf("%d", move);
				if (move == 7) {
					printf("O|O|O\n------\nO|X|X\n------\nX| |X");
					printf("result: O Won");
				}
				else if (move == 2) {
					printf("O|X|O\n------\nO|X|X\n------\nO| |X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O| |O\n------\nO|X|X\n------\nO|X|X");
					printf("result: O Won");
				}
			}
			else if (move == 1) {
				printf("X| |O\n------\nO|X|X\n------\n | |O");
				scanf("%d", move);
				if (move == 2) {
					printf("X|X|O\n------\nO|X|X\n------\n |O|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|X|O\n------\nO|X|X\n------\nX|O|O");
						printf("result: Draw");
					}
				}
				else if (move == 7) {
					printf("X| |O\n------\nO|X|X\n------\nX|O|O");
					scanf("%d", move);
					if (move == 2) {
						printf("X|X|O\n------\nO|X|X\n------\nX|O|O");
						printf("result: Draw");
					}
				}
				else if (move == 8) {
					printf("X|O|O\n------\nO|X|X\n------\n |X|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|O|O\n------\nO|X|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 8) {
				printf(" |O|O\n------\nO|X|X\n------\n |X| ");
				scanf("%d", move);
				if (move == 9) {
					printf("O|O|O\n------\nO|X|X\n------\n |X|X");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X|O|O\n------\nO|X|X\n------\n |X|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|O|O\n------\nO|X|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 7) {
					printf("O|O|O\n------\nO|X|X\n------\nX|X| ");
					printf("result: O Won");
				}
			}
		}
		else if (move == 1) {
			printf("X| |O\n------\n |X| \n------\n | |O");
			scanf("%d", move);
			if (move == 7) {
				printf("X| |O\n------\n |X|O\n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("X|X|O\n------\n |X|O\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("X| |O\n------\nX|X|O\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("X| |O\n------\nO|X|X\n------\n | |O");
				scanf("%d", move);
				if (move == 2) {
					printf("X|X|O\n------\nO|X|X\n------\n |O|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|X|O\n------\nO|X|X\n------\nX|O|O");
						printf("result: Draw");
					}
				}
				else if (move == 7) {
					printf("X|O|O\n------\nO|X|X\n------\nX| |O");
					scanf("%d", move);
					if (move == 8) {
						printf("X|O|O\n------\nO|X|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
				else if (move == 8) {
					printf("X|O|O\n------\nO|X|X\n------\n |X|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|O|O\n------\nO|X|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 8) {
				printf("X| |O\n------\n |X|O\n------\n |X|O");
				printf("result: O Won");
			}
		}
		else if (move == 9) {
			printf("O| |O\n------\n |X| \n------\n | |X");
			scanf("%d", move);
			if (move == 4) {
				printf("O|O|O\n------\nX|X| \n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("O|O|O\n------\n |X| \n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf("O|X|O\n------\n |X| \n------\n |O|X");
				scanf("%d", move);
				if (move == 7) {
					printf("O|X|O\n------\nO|X| \n------\nX|O|X");
					scanf("%d", move);
					if (move == 6) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 6) {
					printf("O|X|O\n------\nO|X|X\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nO|X|X\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 4) {
					printf("O|X|O\n------\nX|X|O\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|O\n------\nX|X|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 8) {
				printf("O|O|O\n------\n |X| \n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O|O|O\n------\n |X|X\n------\n | |X");
				printf("result: O Won");
			}
		}
	}
	else if (move == 3) {
		printf(" | |X\n------\n |O| \n------\n | | ");
		scanf("%d", move);
		if (move == 2) {
			printf("O|X|X\n------\n |O| \n------\n | | ");
			scanf("%d", move);
			if (move == 4) {
				printf("O|X|X\n------\nX|O| \n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 6) {
				printf("O|X|X\n------\n |O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("O|X|X\n------\n |O| \n------\n |X|O");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("O|X|X\n------\n |O| \n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("O|X|X\n------\n |O|O\n------\n | |X");
				scanf("%d", move);
				if (move == 4) {
					printf("O|X|X\n------\nX|O|O\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|X\n------\nX|O|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 7) {
					printf("O|X|X\n------\nO|O|O\n------\nX| |X");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O|X|X\n------\nO|O|O\n------\n |X|X");
					printf("result: O Won");
				}
			}
		}
		else if (move == 8) {
			printf(" | |X\n------\n |O|O\n------\n |X| ");
			scanf("%d", move);
			if (move == 4) {
				printf("O| |X\n------\nX|O|O\n------\n |X| ");
				scanf("%d", move);
				if (move == 7) {
					printf("O| |X\n------\nX|O|O\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O| |X\n------\nX|O|O\n------\nO|X|X");
					scanf("%d", move);
					if (move == 2) {
						printf("O|X|X\n------\nX|O|O\n------\nO|X|X");
						printf("result: Draw");
					}
				}
				else if (move == 2) {
					printf("O|X|X\n------\nX|O|O\n------\n |X|O");
					printf("result: O Won");
				}
			}
			else if (move == 1) {
				printf("X| |X\n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" | |X\n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|X\n------\nO|O|O\n------\n |X| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" | |X\n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
		}
		else if (move == 7) {
			printf(" | |X\n------\n |O|O\n------\nX| | ");
			scanf("%d", move);
			if (move == 9) {
				printf(" | |X\n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X| |X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("O| |X\n------\nX|O|O\n------\nX| | ");
				scanf("%d", move);
				if (move == 2) {
					printf("O|X|X\n------\nX|O|O\n------\nX| |O");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("O| |X\n------\nX|O|O\n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("O| |X\n------\nX|O|O\n------\nX|O|X");
					scanf("%d", move);
					if (move == 2) {
						printf("O|X|X\n------\nX|O|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
			}
			else if (move == 2) {
				printf(" |X|X\n------\nO|O|O\n------\nX| | ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf(" | |X\n------\nO|O|O\n------\nX|X| ");
				printf("result: O Won");
			}
		}
		else if (move == 1) {
			printf("X|O|X\n------\n |O| \n------\n | | ");
			scanf("%d", move);
			if (move == 6) {
				printf("X|O|X\n------\n |O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("X|O|X\n------\nO|O| \n------\n |X| ");
				scanf("%d", move);
				if (move == 7) {
					printf("X|O|X\n------\nO|O|O\n------\nX|X| ");
					printf("result: O Won");
				}
				else if (move == 9) {
					printf("X|O|X\n------\nO|O|O\n------\n |X|X");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("X|O|X\n------\nO|O|X\n------\n |X|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|O|X\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 4) {
				printf("X|O|X\n------\nX|O| \n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf("X|O|X\n------\n |O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("X|O|X\n------\n |O| \n------\nX|O| ");
				printf("result: O Won");
			}
		}
		else if (move == 9) {
			printf(" | |X\n------\n |O|O\n------\n | |X");
			scanf("%d", move);
			if (move == 1) {
				printf("X| |X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf(" | |X\n------\nX|O|O\n------\n |O|X");
				scanf("%d", move);
				if (move == 2) {
					printf("O|X|X\n------\nX|O|O\n------\n |O|X");
					scanf("%d", move);
					if (move == 7) {
						printf("O|X|X\n------\nX|O|O\n------\nX|O|X");
						printf("result: Draw");
					}
				}
				else if (move == 1) {
					printf("X|O|X\n------\nX|O|O\n------\n |O|X");
					printf("result: O Won");
				}
				else if (move == 7) {
					printf(" |O|X\n------\nX|O|O\n------\nX|O|X");
					printf("result: O Won");
				}
			}
			else if (move == 8) {
				printf(" | |X\n------\nO|O|O\n------\n |X|X");
				printf("result: O Won");
			}
			else if (move == 2) {
				printf(" |X|X\n------\nO|O|O\n------\n | |X");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" | |X\n------\nO|O|O\n------\nX| |X");
				printf("result: O Won");
			}
		}
		else if (move == 6) {
			printf(" | |X\n------\n |O|X\n------\n | |O");
			scanf("%d", move);
			if (move == 1) {
				printf("X|O|X\n------\n |O|X\n------\n | |O");
				scanf("%d", move);
				if (move == 7) {
					printf("X|O|X\n------\n |O|X\n------\nX|O|O");
					printf("result: O Won");
				}
				else if (move == 4) {
					printf("X|O|X\n------\nX|O|X\n------\n |O|O");
					printf("result: O Won");
				}
				else if (move == 8) {
					printf("X|O|X\n------\nO|O|X\n------\n |X|O");
					scanf("%d", move);
					if (move == 7) {
						printf("X|O|X\n------\nO|O|X\n------\nX|X|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 2) {
				printf("O|X|X\n------\n |O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf("O| |X\n------\n |O|X\n------\nX| |O");
				printf("result: O Won");
			}
			else if (move == 4) {
				printf("O| |X\n------\nX|O|X\n------\n | |O");
				printf("result: O Won");
			}
			else if (move == 8) {
				printf("O| |X\n------\n |O|X\n------\n |X|O");
				printf("result: O Won");
			}
		}
		else if (move == 4) {
			printf(" |O|X\n------\nX|O| \n------\n | | ");
			scanf("%d", move);
			if (move == 8) {
				printf(" |O|X\n------\nX|O| \n------\n |X|O");
				scanf("%d", move);
				if (move == 7) {
					printf("O|O|X\n------\nX|O| \n------\nX|X|O");
					printf("result: O Won");
				}
				else if (move == 6) {
					printf("O|O|X\n------\nX|O|X\n------\n |X|O");
					printf("result: O Won");
				}
				else if (move == 1) {
					printf("X|O|X\n------\nX|O| \n------\nO|X|O");
					scanf("%d", move);
					if (move == 6) {
						printf("X|O|X\n------\nX|O|X\n------\nO|X|O");
						printf("result: Draw");
					}
				}
			}
			else if (move == 6) {
				printf(" |O|X\n------\nX|O|X\n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 9) {
				printf(" |O|X\n------\nX|O| \n------\n |O|X");
				printf("result: O Won");
			}
			else if (move == 1) {
				printf("X|O|X\n------\nX|O| \n------\n |O| ");
				printf("result: O Won");
			}
			else if (move == 7) {
				printf(" |O|X\n------\nX|O| \n------\nX|O| ");
				printf("result: O Won");
			}
		}
	}
	return 0;
}