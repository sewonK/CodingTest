#include <stdio.h>
int N, K, turn, flag;
int map[13][13]; //맵 저장
int board[13][13][5]; //말 저장
int idx[13][13]; //말 저장되어있는 순서
int dirx[5] = { 0, 0, 0, -1, 1 }; //1이 왼쪽 2 오른쪽 3 위 4 아래
int diry[5] = { 0, 1, -1, 0, 0 };

struct horse {
	int x, y, dir, order;
}h[12];

void endcheck() {
	for (int i = 1; i < 13; i++) {
		for (int j = 1; j < 13; j++) {
			if (idx[i][j] >= 4) {
				flag = 1;
				return;
			}
		}
	}
	return;
}
void move() {
	for (int i = 1; i <= K; i++) {
		int newx = h[i].x + dirx[h[i].dir];
		int newy = h[i].y + diry[h[i].dir];
		int currentx = h[i].x;
		int currenty = h[i].y;
		int currentorder = h[i].order;
		int currentend = idx[h[i].x][h[i].y];
		//파란색의 경우

		/*printf("\n");
		for (int j = 1; j <= 6; j++) {
			for (int k = 1; k <= 6; k++) {
				printf("%d", idx[j][k]);
			}
			printf("\n");
		}
		printf("\n");*/

		if ((newx <= 0 || newx > N || newy <= 0 || newy > N) || map[newx][newy] == 2) {
			if (h[i].dir == 1) h[i].dir = 2;
			else if (h[i].dir == 2) h[i].dir = 1;
			else if (h[i].dir == 3) h[i].dir = 4;
			else if (h[i].dir == 4) h[i].dir = 3;
			int bluex = currentx + dirx[h[i].dir];
			int bluey = currenty + diry[h[i].dir];
			endcheck();
			if (flag == 1) return;
			if ((bluex <= 0 || bluex > N || bluey <= 0 || bluey > N) || map[bluex][bluey] == 2) continue; //방향을 바꿔도 파란색이면 가만히 있는다
			else {
				if (map[bluex][bluey] == 1) {
					for (int j = currentorder; j < currentend; j++) { //내 순서부터 내 위치의 마지막 순서까지
						int ord = board[currentx][currenty][j]; //현재 내 위치부터 board에 순서대로 저장되어있는 말을 꺼낸다. 말 번호를 꺼냄
						board[currentx][currenty][j] = 0; //기존 말 삭제
						idx[currentx][currenty]--; //기존에 있던 곳 삭제

						h[ord].x = bluex;
						h[ord].y = bluey;
						h[ord].order = idx[bluex][bluey];
						board[bluex][bluey][idx[bluex][bluey]++] = ord;
					}
					//순서 바꾸기// 0 1 2 3 4 5 6 7 8
					int t = 0; // 0 0 1 2 3 4 5 6
					int neworder = h[i].order;
					for (int j = neworder; j < (idx[bluex][bluey] + neworder) / 2; j++) {
						int ord1 = board[bluex][bluey][j];
						int ord2 = board[bluex][bluey][idx[bluex][bluey] - t++ - 1];
						int tmp1 = h[ord1].order;
						int tmp2 = h[ord2].order;

						h[ord1].order = tmp2; //순서 바꿔주고
						h[ord2].order = tmp1;

						board[bluex][bluey][tmp1] = ord2; //말 위치 바꿔줌
						board[bluex][bluey][tmp2] = ord1;
					}
				}
				else if (map[bluex][bluey] == 0) {
					for (int j = currentorder; j < currentend; j++) {
						int ord = board[currentx][currenty][j]; //현재 board에 순서대로 저장되어있는 말을 꺼낸다
						board[currentx][currenty][j] = 0; //기존 말 삭제
						idx[currentx][currenty]--; //기존에 있던 곳 삭제

						h[ord].x = bluex;
						h[ord].y = bluey;
						h[ord].order = idx[bluex][bluey];
						board[bluex][bluey][idx[bluex][bluey]++] = ord;
					}
				}
			}
		}

		//흰색 칸일 경우
		else if(map[newx][newy] == 0){
			for (int j = currentorder; j < currentend; j++) {
				int ord = board[currentx][currenty][j]; //현재 board에 순서대로 저장되어있는 말을 꺼낸다
				board[currentx][currenty][j] = 0; //기존 말 삭제
				idx[currentx][currenty]--; //기존에 있던 곳 삭제

				h[ord].x = newx;
				h[ord].y = newy;
				h[ord].order = idx[newx][newy];
				board[newx][newy][idx[newx][newy]++] = ord;
			}
		}

		//빨간 칸일 경우
		else if(map[newx][newy] == 1){
			for (int j = currentorder; j < currentend; j++) { //내 순서부터 내 위치의 마지막 순서까지
				int ord = board[currentx][currenty][j]; //현재 내 위치부터 board에 순서대로 저장되어있는 말을 꺼낸다. 말 번호를 꺼냄
				board[currentx][currenty][j] = 0; //기존 말 삭제
				idx[currentx][currenty]--; //기존에 있던 곳 삭제

				h[ord].x = newx;//말번호 위치 이동
				h[ord].y = newy;
				h[ord].order = idx[newx][newy]; //말 순서를 새로운 곳의 순서로.
				board[newx][newy][idx[newx][newy]++] = ord; //새로운 곳에 말을 넣어준다.
			}
			//순서 바꾸기
			int t = 0;
			int neworder = h[i].order;
			for (int j = neworder; j < (idx[newx][newy] + neworder) / 2; j++) {
				int ord1 = board[newx][newy][j];
				int ord2 = board[newx][newy][idx[newx][newy] - t++ - 1];
				int tmp1 = h[ord1].order;
				int tmp2 = h[ord2].order;
					
				h[ord1].order = tmp2; //순서 바꿔주고
				h[ord2].order = tmp1;

				board[newx][newy][tmp1] = ord2; //말 위치 바꿔줌
				board[newx][newy][tmp2] = ord1;
			}
		}
		
		endcheck();
		if (flag == 1) return;
	}
}


int main() {
	scanf("%d %d", &N, &K);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	for (int i = 1; i <= K; i++) {
		scanf("%d %d %d", &h[i].x, &h[i].y, &h[i].dir);
		h[i].order = idx[h[i].x][h[i].y];
		board[h[i].x][h[i].y][idx[h[i].x][h[i].y]++] = i; //보드의 x, y 위치에 순서대로 말 저장(방향은 h구조체의 인덱스에 저장되어있음)
	}

	while (1) {
		move();
		endcheck();
		turn++;
		if (turn > 1000) {
			turn = -1;
			break;
		}
		if (flag == 1) break;
	}

	printf("%d", turn);
	return 0;
}
