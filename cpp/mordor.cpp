#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

//const int INT_MAX = numeric_limits<int>::max();
struct RMQ {
	int n;
	vector<int> rangeMin;
	RMQ(const vector<int> & array) {
		n = array.size();
		rangeMin.resize(n*4);
		init(array, 0, n-1, 1);
	}

	int init(const vector<int>& array, int left, int right, int node) {
		if(left == right)
			return rangeMin[node] = array[left];
		int mid = (left + right) / 2;
		int leftMin = init(array, left, mid, node*2);
		int rightMin = init(array, mid+1, right, node*2+1);
		printf("node idx : %d, left : %d, right %d, common: %d\n", node, leftMin, rightMin, min(leftMin, rightMin));
		return rangeMin[node] = min(leftMin, rightMin);
	}

	int query(int left, int right, int node, int nodeLeft, int nodeRight) {
		if(right < nodeLeft || nodeRight < left) return INT_MAX;
		if(left <= nodeLeft && nodeRight <= right)
			return rangeMin[node];
		int mid = (nodeLeft + nodeRight) / 2;
		return min(
			query(left, right, node*2, nodeLeft, mid),
			query(left, right, node*2+1, mid+1, nodeRight));
	}

	int query(int left, int right) {
		return query(left, right, 1, 0, n-1);
	}

	int update(int index, int newValue, int node, int nodeLeft, int nodeRight) {
		if(index < nodeLeft || nodeRight < index)
			return rangeMin[node];
		if(nodeLeft == nodeRight)
			return rangeMin[node] = newValue;
		int mid = (nodeLeft + nodeRight) / 2;
		return rangeMin[node] = min(
			update(index, newValue, node*2, nodeLeft, mid),
			update(index, newValue, node*2+1, mid+1, nodeRight));
	}

};

int main() {
	int C;
	int n, q, tmp;
	vector<int> positive_h, negative_h;
	int a, b;
	scanf("%d\n", &C);
	for(int i = 0; i < C; i++) {
		scanf("%d %d\n", &n, &q);
		vector<int> positive_h(n), negative_h(n);
		for(int j = 0; j < n; j++) {
			scanf("%d ", &positive_h[j]);
			negative_h[j] = -positive_h[j];
		}

		RMQ* min_rmq = new RMQ(positive_h);
		RMQ* max_rmq = new RMQ(negative_h);
		for(int k = 0; k < q; k++) {
			scanf("\n%d %d\n", &a, &b);
			int min = min_rmq->query(a, b);
			int max = -max_rmq->query(a, b);
			// cout << min << '\t' << max << endl;
			cout << max - min << endl;
		}

		printf("start\n");
		for(int j = 0 ;j < min_rmq->rangeMin.size(); j++) {
			printf("%d\n", min_rmq->rangeMin[j]);
		}
		printf("end\n");
	}
	return 0;
}