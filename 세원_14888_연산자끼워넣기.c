#include <stdio.h>
int N, max = -1000000001, min = 1000000001;
int A[12];
int operations[4]; //+ - * /

void DFS(int num, int result, int operationN) { //초기 result값은 A[1]
	if (num == N) {
		if (result > max) max = result;
		if (result < min) min = result;
		return;
	}
	if (operationN > 4) return;
	
	if (operations[operationN] > 0) {
		operations[operationN]--;
		if (operationN == 0) {
			result += A[num + 1];
			DFS(num + 1, result, 0);
			result -= A[num + 1];
		}
		else if (operationN == 1) {
			result -= A[num + 1];
			DFS(num + 1, result, 0);
			result += A[num + 1];
		}
		else if (operationN == 2) {
			result *= A[num + 1];
			DFS(num + 1, result, 0);
			result /= A[num + 1];
		}
		else if (operationN == 3) {
			result /= A[num + 1];
			DFS(num + 1, result, 0);
			result *= A[num + 1];
		}
		operations[operationN]++;
		DFS(num, result, operationN + 1);
	}
	else DFS(num, result, operationN + 1);
	
	return;
}
int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &A[i]);
	}
	for (int i = 0; i < 4; i++) {
		scanf("%d", &operations[i]);
	}

	DFS(1, A[1], 0);
	printf("%d\n%d", max, min);
	return 0;
}
