#include <iostream>
#include <map>

using namespace std;

int N, idx;
map<int, int> search_map;
map<int, int>::iterator get_floor(int x) {
	// x보다 작은 것들 중 가장 큰 것
	map<int, int>::iterator it = search_map.lower_bound(x);
	if (it != search_map.begin()) {
		--it;
	}
	return it;
}

map<int, int>::iterator get_ceil(int x) {
	// x보다 큰 것들 중 가장 작은 것
	map<int, int>::iterator it = search_map.upper_bound(x);
	return it;
}

int main(void) {
	scanf("%d\n", &N);
	scanf("%d\n", &idx);
	// arr[idx] = 0;
	search_map[idx] = 0;
	int current;
	long print=0;
	printf("%ld\n", print);
	for(int i = 1; i < N; i++) {
		scanf("%d\n", &idx);

		// Find parent
		map<int, int>::iterator smaller = get_floor(idx);
		map<int, int>::iterator bigger = get_ceil(idx);
		if(smaller->first == 0) {
			current = bigger->second + 1;
		} else if (bigger->first == 0) {
			current = smaller->second + 1;
		} else {
			current = max(bigger->second, smaller->second) + 1;
		}
		printf("%ld\n", print+=(current));
		search_map[idx] = current;
	}

	return 0;
}