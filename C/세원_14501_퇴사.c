#include <stdio.h>
int N;
int t[16];
int p[16];
int isavailable[16];
int max = -1;
void DFS(int n, int sum) {
	if (n > N) {
		if (max < sum) max = sum;
		return;
	}
	if (n + t[n] - 1 > N) DFS(n + 1, sum);
	else if(isavailable[n] == 0){
		for (int i = n; i <= n + t[n] - 1; i++) isavailable[i] = 1;
		DFS(n + t[n], sum + p[n]);
		for (int i = n; i <= n + t[n] - 1; i++) isavailable[i] = 0;
		DFS(n + 1, sum);
	}
}

int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d %d", &t[i], &p[i]);
	}
	DFS(1, 0);
	printf("%d", max);
	return 0;
}
