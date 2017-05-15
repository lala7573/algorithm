#include <iostream>
#include <vector>
#include <string>
using namespace std;

int C, N, Q, a, b;

int set_height(const vector<int> & familytree, vector<int> & heighttree, int idx) {
	if(idx == -1) {
		return 0;
	}

	if(heighttree[idx] != -1) {
		return heighttree[idx];
	}

	return heighttree[idx] = set_height(familytree, heighttree, familytree[idx]) + 1;
}

int _get_chon_su(const vector<int> & familytree, vector<int> & heighttree, int a, int b, int acc) {
	if(a == b) {
		return acc;
	}
	// a != b 에 대한 처리
	if(heighttree[a] == heighttree[b]) { // 높이가 같다
		return _get_chon_su(familytree, heighttree, familytree[a], familytree[b], acc+2);
	} else if (heighttree[a] > heighttree[b]) {
		return _get_chon_su(familytree, heighttree, familytree[a], b, acc+1);
	} else {
		return _get_chon_su(familytree, heighttree, a, familytree[b], acc+1);
	}
}

int get_chon_su(const vector<int> & familytree, vector<int> & heighttree, int a, int b) {
	return _get_chon_su(familytree, heighttree, a, b, 0);
}
int main() {
	scanf("%d\n", &C);

	for(int i = 0 ;i < C; i++) {
		scanf("%d %d\n", &N, &Q);
		vector<int> familytree(N, -1), heighttree(N, -1);
		heighttree[0] = 0;
		for(int j = 1 ;j < N ; j++) {
			scanf("%d ", &familytree[j]);
		}
		for(int j = 1 ; j < N; j++) {
			set_height(familytree, heighttree, j);
		}

		for(int k = 0; k < Q; k++) {
			scanf("%d %d\n", &a, &b);
			printf("%d\n", get_chon_su(familytree, heighttree, a, b));
		}

	}

	return 0;
}