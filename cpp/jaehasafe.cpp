#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

int T, N;
char prev_pattern[20001] = {0, };
char curr_pattern[20001] = {0, };

vector<int> get_pi(char p[], int length) {
    int j=0;
    vector<int> pi(length, 0);
    for(int i = 1; i < length; i++){
        while(j > 0 && p[i] != p[j]) {
            j = pi[j-1];
        }

        if(p[i] == p[j]) {
            pi[i] = ++j;
        }
    }
    return pi;
}

int get_tick(char text[], char p[], vector<int> pi) {
	vector<int> ans;
	int length = strlen(text),count=0, j = 0;
	// text 2배로 증가시켜서 검색가능하게 만든다
	for(int i = length; i < length * 2; i++) {
		text[i] = text[i-length];
	}
	text[length * 2] = '\0';

	// 확인해보쟈~~
	// printf("%s\t%s\n", text, p);
	// for(int i = 0 ;i < length; i ++) {
		// printf("%d", pi[i]);
	// }
	// printf("\n");

	for(int i = 0 ; i < length*2 ; i++){
        while(j>0 && text[i] != p[j])
            j = pi[j-1];
        if(text[i] == p[j]){
        	j++;
            if(j == length){
            	// printf("%d\n", i - length + 1);
            	text[length] = '\0';
            	return i - length + 1;
            }
        }
    }
	//impossible
	return -1;
}

int main() {
	scanf("%d\n", &T);

	for(int i = 0; i < T; i++) {
		int count = 0, tmp, length;
		vector<int> pi;

		scanf("%d\n", &N);
		scanf("%s\n", prev_pattern); // 항상 text
		length = strlen(prev_pattern);

		for(int j = 0; j < N ; j++) {
			if(j & 1) {
				scanf("%s\n", prev_pattern);
				count += get_tick(curr_pattern, prev_pattern, get_pi(prev_pattern, length));

			} else {
				scanf("%s\n", curr_pattern);
				count += get_tick(curr_pattern, prev_pattern, get_pi(prev_pattern, length));
			}
		}

		printf("%d\n", count);
	}
	return 0;
}