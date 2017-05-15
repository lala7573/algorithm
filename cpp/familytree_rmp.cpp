/**
* vector를 이용한 RMQ를 만들어서 풀자
* https://algospot.com/judge/problem/read/FAMILYTREE
**/
#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define ROOT 0
#define INT_MAX 2147483647


using namespace std;

struct node {
	int idx;
	int parent;
	int height;
	vector<node *> children;
};

int C, N, Q, a, b;
int parent;
vector<int> preordered;
vector<int> indexed;
vector<node *> familytree;
struct FAMILY_RMQ {
	int n;
	vector<int> commonAncestor;
	FAMILY_RMQ(const vector<int> & array) {
		n = array.size();
		commonAncestor.resize(n*4);
		init(array, 0, n-1, 1);
	}

	int init(const vector<int>& array, int left, int right, int node) {
		if(left == right) {
			return commonAncestor[node] = array[left];
		}
		int mid = (left + right) / 2;
		int leftCommon = init(array, left, mid, node*2);
		int rightCommon = init(array, mid+1, right, node*2+1);
		// printf("node idx : %d, left : %d, right %d, left common: %d, right common: %d\n", node, left, right, leftCommon, rightCommon);
		// printf("left height : %d\tright height : %d\n", familytree[leftCommon]->height, familytree[rightCommon]->height);
		if(familytree[leftCommon]->height < familytree[rightCommon]->height)
			return commonAncestor[node] = leftCommon;
		return commonAncestor[node] = rightCommon;
	}

	int query(int left, int right, int node, int nodeLeft, int nodeRight) {
		if(right < nodeLeft || nodeRight < left) {
			return INT_MAX;
		}
		if(left <= nodeLeft && nodeRight <= right){
			// printf("common : %d\n", commonAncestor[node]);
			return commonAncestor[node];
		}
		int mid = (nodeLeft + nodeRight) / 2;
		int leftCommon = query(left, right, node*2, nodeLeft, mid);
		int rightCommon = query(left, right, node*2+1, mid+1, nodeRight);

		// printf("node idx : %d, left : %d, right %d, left common: %d, right common: %d\n", node, left, right, leftCommon, rightCommon);
		if(leftCommon == INT_MAX) {
			return rightCommon;
		} else if (rightCommon == INT_MAX) {
			return leftCommon;
		} else {
			// printf("left height : %d\tright height : %d\n", familytree[leftCommon]->height, familytree[rightCommon]->height);
			if(familytree[leftCommon]->height < familytree[rightCommon]->height)
				return leftCommon;
			return rightCommon;
		}
	}

	int query(int left, int right) {
		// printf("%d, %d\n", left, right);
		int inner_left = indexed[left];
		int inner_right = indexed[right];
		if (inner_left > inner_right) {
			int tmp = inner_left;
			inner_left = inner_right;
			inner_right = tmp;
		}
		// printf("query %d, %d\n", inner_left, inner_right);
		return query(inner_left, inner_right, 1, 0, n-1);
	}
};

void preorder(node * current, vector<node *> & familytree, vector<int> & acc) {
	if(current->idx != 0) {
		current->height = familytree[current->parent]->height + 1;
	}

	indexed[current->idx] = acc.size();
	acc.push_back(current->idx);
	int children_size = current->children.size();
	for(int c_i = 0; c_i < children_size; c_i ++) {
		node * next = familytree[current->children[c_i]->idx];
		preorder(next, familytree, acc);
		acc.push_back(current->idx);
	}

	return;
}


int main() {
	scanf("%d\n", &C);

	for(int i = 0 ;i < C; i++) {
		scanf("%d %d\n", &N, &Q);
		indexed.clear();
		familytree.clear();
		indexed.resize(N);
		familytree.resize(N);

		for(int j = 0; j < N; j++) {
			familytree[j] = new node;
			familytree[j]->idx = j;
		}

		for(int j = 1 ;j < N ; j++) {
			scanf("%d ", &parent);
			familytree[j]->parent = parent;
			familytree[parent]->children.push_back(familytree[j]);
		}

		familytree[0]->parent = 0;
		familytree[0]->height = 0;
		preorder(familytree[0], familytree, preordered);

		// for(int j = 0 ;j < preordered.size(); j++) {
		// 	printf("%2d ", j);
		// }
		// printf("\n");

		// for(int j = 0 ;j < preordered.size(); j++) {
		// 	printf("%2d ", preordered[j]);
		// }
		// printf("\n");

		FAMILY_RMQ rmq = FAMILY_RMQ(preordered);
		// int common = rmq.query(7, 7);
		// printf("%d\n", common);
		for(int k = 0; k < Q; k++) {
			scanf("%d %d\n", &a, &b);
			// printf("(%d, %d) common ancestor : %d\n", a, b, rmq.query(a, b));
			int common_height = familytree[rmq.query(a, b)]->height;
			// printf("%d\n", common_height);
			printf("%d\n", familytree[a]->height + familytree[b]->height - common_height * 2);
		}

	}

	return 0;
}