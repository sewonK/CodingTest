#include <stdio.h>
int N, K, L, currentx = 1, currenty = 1, currentdir, tailx, taily, time;
int applemap[101][101]; //사과 있으면 1
int snakemap[101][101]; //뱀 있으면 1
int queue[100000];
int dirx[4] = {0, -1, 0, 1}; // 오 상 왼 하
int diry[4] = {1, 0, -1, 0};
struct changedir {
	int time;
	int dir;
}change[101];

void move() {
	int idx = 0;
	int read = 0;
	int write = 0;
	queue[write++] = currentx;
	queue[write++] = currenty;
	tailx = queue[read++];
	taily = queue[read++];
	snakemap[currentx][currenty] = 1;
	while (1) {
		int headx = currentx + dirx[currentdir];
		int heady = currenty + diry[currentdir];
		queue[write++] = headx;
		queue[write++] = heady;
		time++;
		if (headx > N || headx <= 0 || heady > N || heady <= 0 || snakemap[headx][heady] == 1) break;
		snakemap[headx][heady] = 1; //머리를 다음 칸으로
		currentx = headx;
		currenty = heady; //현재위치 갱신
		if (applemap[headx][heady] == 1) applemap[headx][heady] = 0; //사과가 있으면 사과가 없어지고 꼬리는 그대로
		else {
			snakemap[tailx][taily] = 0; //사과가 없으면 꼬리칸 비워주기
			tailx = queue[read++];
			taily = queue[read++]; //꼬리칸 갱신
		}
		if (time == change[idx].time) {
			if (change[idx].dir == 1) { //왼쪽으로 회전 //오 -> 상 -> 왼 -> 하
				currentdir = (currentdir + 1) % 4;
			}
			else { //오른쪽으로 회전 //오 -> 하 -> 왼 -> 상
				if (currentdir - 1 < 0) currentdir = 3;
				else currentdir = (currentdir - 1) % 4;
			}
			idx++;
		}
	}
	return;
}

int main() {
	scanf("%d %d", &N, &K);
	for (int i = 0; i < K; i++) {
		int applex;
		int appley;
		scanf("%d %d", &applex, &appley);
		applemap[applex][appley] = 1; //사과 두기, 좌표는 1, 1부터 시작
	}
	scanf("%d", &L);
	for (int i = 0; i < L; i++) {
		char direction;
		scanf("%d", &change[i].time);
		scanf(" %c", &direction);
		if (direction == 'L') change[i].dir = 1; //왼쪽으로 회전 // 오 -> 상 -> 왼 -> 하
		else change[i].dir = 0; //오른쪽으로 회전 // 오 -> 하 -> 왼 -> 상
	}

	move();
	printf("%d", time);
	return 0;
}
