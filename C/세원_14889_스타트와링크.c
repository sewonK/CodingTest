#include <stdio.h>
int N, sol = 9999999, start, link;
int s[21][21];
int isTeamStart[21];
int abs(int a) {
	if (a < 0) return -a;
	else return a;
}
void count() {
	for (int i = 1; i <= N; i++) {
		int team = isTeamStart[i];
		for (int j = 1; j <= N; j++) {
			if (team == 1) {
				if (team == isTeamStart[j]) start += s[i][j];
			}
			else {
				if (team == isTeamStart[j]) link += s[i][j];
			}
		}
	}
	return;
}
void DFS(int n, int cnt) {
	if (cnt == N / 2) {
		start = 0;
		link = 0;
		count();
		if (sol > abs(start - link)) sol = abs(start - link);
		return;
	}
	if (n > N) return;
	
	isTeamStart[n] = 1;
	DFS(n + 1, cnt + 1);
	isTeamStart[n] = 0;
	DFS(n + 1, cnt);

	return;
}

int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			scanf("%d", &s[i][j]);
		}
	}
	DFS(1, 0);
	printf("%d", sol);
	return 0;
}
