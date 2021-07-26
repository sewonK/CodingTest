#include <stdio.h>
int n, m, r, c, d, cnt, t = 0;
int dirx[4] = { -1, 0, 1, 0 };
int diry[4] = { 0, 1, 0, -1 };

int board[51][51];
int clean;
void find(int x, int y) {
	if (!(x >= 0 && x < n && y >= 0 && y < m)) return;
	if (board[x][y] == 0) {
		board[x][y] = 2;
		cnt++;
	}

	if (d == 0) d = 4;
	if (x + dirx[d - 1] >= 0 && x + dirx[d - 1] < n && y + diry[d - 1] >= 0 && y + diry[d - 1] < n && board[x + dirx[d - 1]][y + diry[d - 1]] == 0) {
		d--;
		find(x + dirx[d], y + diry[d]);
	}
	if (t == 1) return;
	else {
		for (int i = 0; i < 4; i++) {
			if (d == 0) d = 4;
			d--;
			if (board[x + dirx[d]][y + diry[d]] != 0) clean++;
			else {
				clean = 0;
				find(x + dirx[d], y + diry[d]);
				break;
			}
		}

		if (t == 1) return;
		if (clean == 4) {
			if (x - dirx[d] < n && x - dirx[d] >= 0 && y - diry[d] < m && y - diry[d] >= 0 && board[x - dirx[d]][y - diry[d]] == 1) {
				t = 1;
				return;
			}
			else {
				clean = 0;
				find(x - dirx[d], y - diry[d]);
				if (t == 1) return;
			}
		}

		if (t == 1) return;
	}
}

int main() {
	int i, j;
	scanf("%d %d", &n, &m);
	scanf("%d %d %d", &r, &c, &d);
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			scanf("%1d", &board[i][j]);
		}
	}
	find(r, c);
	printf("%d", cnt);
	return 0;
}
