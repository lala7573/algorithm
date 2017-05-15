#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool solve(const char * line) {
	char tmp;
	stack<char> mystack;
	
	for(int i = 0 ; line[i]!='\0' ; i++) {
		if(line[i] == '{' ||line[i] == '(' || line[i] == '[')  {
			mystack.push(line[i]);
			continue;
		}

		if(mystack.empty()) {
			return false;
		}
		if(line[i]=='}') {
			tmp = mystack.top();
			if(tmp != '{') {
				return false;
			}
		} else if(line[i] == ')') {
			tmp = mystack.top();
			if(tmp != '(') {
				return false;
			}
		} else if(line[i] == ']') {
			tmp = mystack.top();
			if(tmp != '[') {
				return false;
			}
		}
		mystack.pop();
	}
	if(mystack.empty()){
		return true;
	}
	return false;
}

int main() {
	int tc;
	string line;

	scanf("%d\n", &tc);

	for(int i = 0 ;i < tc ; i++) {
		getline(cin, line);
		// cout << line;
		string answer = ((solve(line.c_str()))? "YES\n": "NO\n");
		cout <<  answer;
	}
	return 0;
}