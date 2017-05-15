#include <iostream>
#include <queue>

using namespace std;

#define MAX 50000001
long long int SIGNAL = 1983;

long long int get_signal(unsigned int i) {
	if( i == 0 ) {
		return SIGNAL % 10000 + 1;
	}
	SIGNAL = (SIGNAL * 214013 + 2531011) % ((long long int)1<<32);
	return SIGNAL % 10000 + 1;
}

long long int solve(int k, int n) {
	int signal, count = 0, sum = 0;
	queue<int> my_queue;
	for(int i =0 ;i < n ; i++) {
		signal = get_signal(i);
		my_queue.push(signal);
		sum += signal;
		while(sum > k) {
			sum -= my_queue.front();
			my_queue.pop();
		}

		// cout << sum << endl;
		if(sum == k) {
			count ++;
			sum -= my_queue.front();
			my_queue.pop();
		}
	}
	return count;
}
int main() {
	int tc;
	int k, n;

	scanf("%d\n", &tc);

	for(int i = 0 ;i < tc ; i ++) {
		SIGNAL = 1983;
		scanf("%d %d\n", &k, &n);
		cout << solve(k, n) << endl;
	}
	return 0;
}