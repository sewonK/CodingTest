#include<stdio.h>
int N, L;
int map[101][101];
int issloped[101][101];
int cnt, visit;
int abs(int a) {
	if (a < 0) return -a;
	return a;
}
void ispossible(int n) { //(i,0) (0,i) 가로 세로 확인.
	for (int i = 0; i < N - 1; i++) { // 세로는 x로 고정, 가로 확인, 
		if (map[n][i] == map[n][i + 1]) continue; //ok
		else if (abs(map[n][i] - map[n][i + 1]) == 1) {
			if (map[n][i] > map[n][i + 1]) {
				if (i + L >= N) return; //슬로프를 놓을 때 범위 밖이면 불가능(4)
				else {
					int height = map[n][i + 1];
					for (int j = i + 1; j <= i + L; j++) { //슬로프를 놓을 수 있는지 체크
						if (issloped[n][j] == 1) return;//놓을 자리에 이미 슬로프가 있으면 불가능(1)
						if (height != map[n][j]) return; //놓을 자리의 높이가 모두 같지 않으면 불가능(3)
					}
					for (int j = i + 1; j <= i + L; j++) { //슬로프 놓기
						issloped[n][j] = 1;
					}
				}
			}

			else {
				if (i - L + 1 < 0) return; //슬로프를 놓을 때 범위 밖이면 불가능(4)
				else {
					int height = map[n][i];
					for (int j = i - L + 1; j <= i; j++) { //슬로프를 놓을 수 있는지 체크
						if (issloped[n][j] == 1) return;//놓을 자리에 이미 슬로프가 있으면 불가능(1)
						if (height != map[n][j]) return; //놓을 자리의 높이가 모두 같지 않으면 불가능(3)
					}
					for (int j = i - L + 1; j <= i; j++) { //슬로프 놓기
						issloped[n][j] = 1;
					}
				}
			}
		}
		else if (abs(map[n][i] - map[n][i + 1]) > 1) return; //높이 차이가 2이상인 경우
	}
	cnt++; // return되지 않고 빠져나오면 그 길은 갈 수 있는 길이다.
	return;
}
void ispossible2(int n){
	for (int i = 0; i < N - 1; i++) { // 가로는 y로 고정, 세로 확인, 
		if (map[i][n] == map[i + 1][n]) continue; //ok
		else if (abs(map[i][n] - map[i + 1][n]) == 1) {
			if (map[i][n] > map[i + 1][n]) {
				if (i + L >= N) return; //슬로프를 놓을 때 범위 밖이면 불가능(4)
				else {
					int height = map[i + 1][n];
					for (int j = i + 1; j <= i + L; j++) { //슬로프를 놓을 수 있는지 체크
						if (issloped[j][n] == 1) return;//놓을 자리에 이미 슬로프가 있으면 불가능(1)
						if (height != map[j][n]) return; //놓을 자리의 높이가 모두 같지 않으면 불가능(3)
					}
					for (int j = i + 1; j <= i + L; j++) { //슬로프 놓기
						issloped[j][n] = 1;
					}
				}
			}

			else {
				if (i - L + 1 < 0) return; //슬로프를 놓을 때 범위 밖이면 불가능(4)
				else {
					int height = map[i][n];
					for (int j = i - L + 1; j <= i; j++) { //슬로프를 놓을 수 있는지 체크
						if (issloped[j][n] == 1) return;//놓을 자리에 이미 슬로프가 있으면 불가능(1)
						if (height != map[j][n]) return; //놓을 자리의 높이가 모두 같지 않으면 불가능(3)
					}
					for (int j = i - L + 1; j <= i; j++) { //슬로프 놓기
						issloped[j][n] = 1;
					}
				}
			}
		}
		else if (abs(map[i][n] - map[i + 1][n]) > 1) return; //높이 차이가 2이상인 경우
	}
	cnt++; // return되지 않고 빠져나오면 그 길은 갈 수 있는 길이다.
	return;
}
int main() {
	scanf("%d %d", &N, &L);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		ispossible(i); //가로 확인.
		for (int j = 0; j < N; j++) issloped[i][j] = 0;
		ispossible2(i); //세로확인
		for (int j = 0; j < N; j++) issloped[j][i] = 0;
	}
	printf("%d", cnt);
	return 0;
}
