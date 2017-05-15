#include <iostream>
#include <vector>
#include <string.h>

using namespcae std;

int L, length, max=0, max_index=0;
char[1000001] str;
int[1000001] pi = {0, };

void set_pi(char p[], int length) {
    int j = 0;

    for(int i = 1; i < length; i++){
        while(j > 0 && p[i] != p[j]) {
            j = pi[j-1];
        }

        if(p[i] == p[j]) {
            pi[i] = ++j;
        }

        if(pi[i] > max) {
        	max_index = i;
        }
    }
}

int main(){
	scanf("%d\n", &L);
	scanf("%s\n", str);
	length = strlen(str);

	set_pi(str, length);
	for(int i = first_zero+1; i < length; i++) {

	}
	return 0;
}