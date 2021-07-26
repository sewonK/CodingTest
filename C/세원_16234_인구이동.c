#include <stdio.h>
int N, L, R, flag, sol;
int map[51][51];
int visit[51][51];
int dirx[4] = { 0, 0, 1, -1 };
int diry[4] = { 1, -1, 0, 0 };
int Queue[100000];

int abs(int a) {
	if (a < 0) return -a;
	else return a;
}

void BFS(int firstX, int firstY) {
	int read = 0;
	int write = 0;
	int sum = 0, cnt = 0;
	Queue[write++] = firstX;
	Queue[write++] = firstY;
	visit[firstX][firstY] = 1;
	while (read < write) {
		int x = Queue[read++];
		int y = Queue[read++];
		cnt++;
		sum += map[x][y];
		for (int k = 0; k < 4; k++) {
			int newx = x + dirx[k];
			int newy = y + diry[k];
			if (newx < 0 || newx >= N || newy < 0 || newy >= N) continue;
			if (visit[newx][newy] == 0 && abs(map[newx][newy] - map[x][y]) >= L && abs(map[newx][newy] - map[x][y]) <= R) {
				visit[newx][newy] = 1;
				Queue[write++] = newx;
				Queue[write++] = newy;
				flag = 1;
			}
		}
	}

	sum /= cnt;
	for (int i = 0; i < write; i += 2) {
		map[Queue[i]][Queue[i + 1]] = sum;
	}
}
int main() {
	scanf("%d %d %d", &N, &L, &R);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	while (1) {
		flag = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (visit[i][j] != 0) continue;
				BFS(i, j);
			}
		}
		
		if (flag == 0) break;
		else sol++;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				visit[i][j] = 0;
			}
		}
	}
	printf("%d", sol);
	return 0;
}
