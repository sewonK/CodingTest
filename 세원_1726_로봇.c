#include <stdio.h>
int m, n, startX, startY, startD, finX, finY, finD;
int board[101][101];
int visited[101][101][4];
int dirx[4] = { 0, 0, 1, -1 }; //동서남북 0, 1, 2, 3 
int diry[4] = { 1, -1, 0, 0 };
int queue[1000000];
int BFS(int x, int y) {
	int read = 0;
	int write = 0;
	queue[write++] = x;
	queue[write++] = y;
	queue[write++] = startD;
	queue[write++] = 0;
	visited[x][y][startD] = 1;

	while (read < write) {
		int i = queue[read++];
		int j = queue[read++];
		int dir = queue[read++];
		int cnt = queue[read++];
		if (i == finX && j == finY && dir == finD) return cnt;
		for (int l = 1; l <= 3; l++) {
			int nextX = i + dirx[dir] * l;
			int nextY = j + diry[dir] * l;
			if (visited[nextX][nextY][dir] == 1) continue;
			if (0 < nextY && nextY <= n && 0 < nextX && nextX <= m && !board[nextX][nextY]) {
				visited[nextX][nextY][dir] = 1;
				queue[write++] = nextX;
				queue[write++] = nextY;
				queue[write++] = dir;
				queue[write++] = cnt + 1;
			}
			else break;
		}

		for (int k = 0; k < 4; k++) {
			if (dir != k && visited[i][j][k] == 0) {
				visited[i][j][k] = 1;
				if ((dir == 0 && k == 1) || (dir == 1 && k == 0) || (dir == 2 && k == 3) || (dir == 3 && k == 2)) {
					queue[write++] = i;
					queue[write++] = j;
					queue[write++] = k;
					queue[write++] = cnt + 2;
				}
				else {
					queue[write++] = i;
					queue[write++] = j;
					queue[write++] = k;
					queue[write++] = cnt + 1;
				}
				
			}
		}
	}

	return -1;
}

int main() {
	
	scanf("%d %d", &m, &n);
	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%1d", &board[i][j]);
		}
	}
	scanf("%d %d %d", &startX, &startY, &startD);
	startD--;
	scanf("%d %d %d", &finX, &finY, &finD);
	finD--;
	
	printf("%d", BFS(startX, startY));
	
	return 0;
}
