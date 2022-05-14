#include <iostream>
#include <string>
using namespace std;

int main() {
	string s1, s2;
	string answer;
	char tmp;
	cin >> s1 >> s2;
	for(int i = 2; i >= 0; i--){
		if(s1[i] > s2[i]){
			answer = s1;
			break;
		}
		else if (s1[i] < s2[i]){
	        answer = s2;
		    break;
		}
	}
	tmp = answer[2];
	answer[2] = answer[0];
	answer[0] = tmp;
	cout << answer;
	return 0;
}
