#include <iostream>
#include <vector>

using namespace std;

struct Node {
	int x, y, r;
	int count;
	bool is_leaf;
	Node* parent;
	vector<Node*> child_nodes;
}

struct Tree {
	int * root;
	vector<int *> leaf_nodes;
}

Tree * make_tree(Tree * tree) {
	

}


int C, N;
Node fortress[100][3];

void fill_node_info() {
	for(int i = 0 ;i < N ; i ++) {
		f
	}
}

int how_many_get_over() {
	int count = 0;
	// Node에 정보 채우기


	// 직속 자식인지 체크하면서 fortress 트리를 만든다. O(N^2)
	Tree * tree = new Tree;
	int * tree = make_tree(tree);

	// leaf node를 찾아서 저장한다.
	vector<Node> leafs = blah-blah;
	// parent를 따라 올라가면서 깊이가 더 깊은걸 저장
	int max;

	return count;
}
int main(void) {
	scanf("%d\n", &C);

	for(int i = 0 ;i < C ; i++) {
		scanf("%d\n", &N);

		for(int j = 0 ;j < N ; j++) {
			scanf("%d %d %d\n", &fortress[j].x, &fortress[j].y, &fortress[j].r);
		}

		printf("%d\n", how_many_get_over())
	}
	return 0;
}