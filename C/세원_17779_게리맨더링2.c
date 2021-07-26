#include <stdio.h>
int N, sol = 999999, x, y, d1, d2;
int people[21][21];
int area[21][21];
int areaNum[6];

void setBoundary() { //경계선을 5번 선거구로 지정
	for (int i = 0; i <= d1; i++) {
		area[x + i][y - i] = 5;
	}
	for (int i = 0; i <= d2; i++) {
		area[x + i][y + i] = 5;
	}
	for (int i = 0; i <= d2; i++) {
		area[x + d1 + i][y - d1 + i] = 5;
	}
	for (int i = 0; i <= d1; i++) {
		area[x + d2 + i][y + d2 - i] = 5;
	}
}
void setArea5() { //5번 선거구 채우기
	for (int i = x + 1; i <= x + d1 + d2 - 1; i++) {
		int flag = 0;
		for (int j = y - d1; j <= N; j++) {
			if (flag == 0 && area[i][j] == 5) {
				flag = 1;
				continue;
			}
			if (flag == 1 && area[i][j] == 5) break;
			if (flag == 1) area[i][j] = 5;
		}
	}
}
void setArea() { //area배열에 선거구를 입력하는 함수
	setBoundary();
	setArea5();
	//구역 1
	for (int i = 1; i < x + d1; i++) {
		for (int j = 1; j <= y; j++) {
			if (area[i][j] == 0) area[i][j] = 1;
		}
	}
	//구역 2
	for (int i = 1; i <= x + d2; i++) {
		for (int j = y + 1; j <= N; j++) {
			if (area[i][j] == 0) area[i][j] = 2;
		}
	}
	//구역 3
	for (int i = x + d1; i <= N; i++) {
		for (int j = 1; j < y - d1 + d2; j++) {
			if (area[i][j] == 0) area[i][j] = 3;
		}
	}
	//구역 4
	for (int i = x + d2 + 1; i <= N; i++) {
		for (int j = y - d1 + d2; j <= N; j++) {
			if (area[i][j] == 0) area[i][j] = 4;
		}
	}

}
void countNum() { //선거구 별 인원 계산해서 인구차이 최소값을 정하는 함수. 선거구는 적어도 한 구역을 포함해야하므로 인원 수가 없으면 리턴하게해야한다
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (area[i][j] == 1) areaNum[1]+=people[i][j];
			else if (area[i][j] == 2) areaNum[2]+=people[i][j];
			else if (area[i][j] == 3) areaNum[3]+=people[i][j];
			else if (area[i][j] == 4) areaNum[4]+=people[i][j];
			else if (area[i][j] == 5) areaNum[5]+=people[i][j];
			else return;
		}
	}
	int max = -1, min = 99999;
	for (int i = 1; i <= 5; i++) {
		if (max < areaNum[i]) max = areaNum[i];
		if (min > areaNum[i]) min = areaNum[i];
	}
	int result = max - min;
	if (sol > result) sol = result;
}
void clear() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			area[i][j] = 0;
		}
	}
	for (int i = 1; i <= 5; i++) areaNum[i] = 0;
}
void DFS(int D1, int D2) {
	if (y - D1 < 1) return;
	if (x + D1 + D2 > N || y + D2 > N) {
		DFS(D1 + 1, 1);
		return;
	}
	d1 = D1;
	d2 = D2;
	setArea();
	countNum();
	clear();
	DFS(D1, D2 + 1);
}
int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			scanf("%d", &people[i][j]); //인구 수 입력받기(1부터 시작)
		}
	}
	
	for (int i = 1; i <= N; i++) {
		for (int j = 2; j <= N; j++) {
			x = i;
			y = j;
			DFS(1, 1);
		}
	}

	printf("%d", sol);
	return 0;
}
