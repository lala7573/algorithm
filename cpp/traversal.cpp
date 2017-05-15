#include <iostream>

using namespace std;

int C, N;
int preorder[101];
int inorder[101];
int postorder[101];

void print_postorder(int n, int pre_i, int in_i) {
	if(n < 1) {
		return;
	}
	if(n == 1) {
		printf("%d ", preorder[pre_i]);
		return;
	}
	int center_value = preorder[pre_i];

	// search center_value
	int i = 0;
	for(;i < n; i++) {
		if(center_value == inorder[in_i + i])
			break;
	}
	print_postorder(i, pre_i+1, in_i);
	print_postorder(n-1-i, pre_i+i+1, in_i+i+1);
	printf("%d ", center_value);
}

int main(void) {
	scanf("%d\n", &C);

	for(int i = 0 ;i < C ; i++) {
		scanf("%d\n", &N);
		for(int j = 0; j < N ; j++) {
			//전위 순회
			scanf("%d ", &preorder[j]);
		}
		scanf("\n");
		for(int j = 0; j < N ; j++) {
			//중위 순회
			scanf("%d ", &inorder[j]);
		}
		scanf("\n");

		print_postorder(N, 0, 0);
		printf("\n");
	}
	return 0;
}