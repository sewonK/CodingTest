#include<stdio.h>
int N;
int time, size = 2, eaten, flag;
int sharkX, sharkY;
int map[21][21];
int dirx[4] = { 0, 0, 1, -1 };
int diry[4] = { 1, -1, 0, 0 };
int queue[100000];

void BFS(int firstX, int firstY) {
	int visit[21][21] = { 0 ,};
	int read = 0;
	int write = 0;
	queue[write++] = firstX;
	queue[write++] = firstY;
	visit[firstX][firstY] = 1;
	while (read < write) {
		int x = queue[read++];
		int y = queue[read++];
		int cnt = visit[x][y];
		for (int i = 0; i < 4; i++) {
			int newx = x + dirx[i];
			int newy = y + diry[i];
			if (newx < 0 || newx >= N || newy < 0 || newy >= N) continue;
			if (visit[newx][newy] == 0 && map[newx][newy] <= size) {
				visit[newx][newy] = cnt + 1;
				queue[write++] = newx;
				queue[write++] = newy;
			}
		}
	}

	//check
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (map[i][j] != 0 && map[i][j] != 9 && map[i][j] < size && visit[i][j] != 0) cnt++;
		}
	}
	if (cnt == 0) {
		flag = 1;
		return;
	}

	//catch
	int min = 1000;
	int catchX = -1, catchY = -1;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visit[i][j] != 0 && map[i][j] != 0 && map[i][j] != 9 && map[i][j] < size) {
				if (min > visit[i][j]) {
					min = visit[i][j];
					catchX = i;
					catchY = j;
				}
			}
		}
	}
	map[sharkX][sharkY] = 0; //기존 상어 위치는 0이 된다
	map[catchX][catchY] = 9; // 잡아먹고 상어가 좌표에 존재
	eaten++; //먹은 물고기 수
	if (eaten == size) {
		eaten = 0;
		size++; //상어 크기 증가
	}
	time += visit[catchX][catchY] - 1; //시간 늘어남
	sharkX = catchX; //상어 좌표 갱신
	sharkY = catchY;
}
int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] == 9) {
				sharkX = i;
				sharkY = j;
			}
		}
	}

	while (1) {
		BFS(sharkX, sharkY);
		if (flag == 1) break;
	}

	printf("%d", time);
	return 0;
}
