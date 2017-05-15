#include <iostream>
#include <list>

#define NO_REMAIN "FRULA"

using namespace std;

int solve(char line[], int size_of_line, char bomb[], int size_of_bomb) {
	list<char> mylist;
	char newline[1000001];

	for(int i = 0, pointer = 0; line[i] != '\0'; i ++, pointer ++) {
		newline[pointer] = line[i];
		


	}
	return 1;
}
int main() {
	int size_of_line, size_of_bomb;
	char line[1000001];
	char bomb[37];
	scanf("%s\n", line);
	scanf("%s\n", bomb);

	int i;
	for(i = 0 ;line[i] != '\0'; i ++);
	size_of_line = i;

	for(i = 0 ;bomb[i] != '\0'; i ++);
	size_of_bomb = i;

	solve(line, size_of_line, bomb, size_of_bomb);
	return 0;
}
