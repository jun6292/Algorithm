#include <iostream>
#include <string>
using namespace std;

int main() {
	int cnt = 0;
	string str;
	getline(cin, str);
	int i = 0;
	while (str[i] != '\0'){
		while (str[i] == ' ')
			i++;
		if (str[i] > 32)
			cnt++;
		while (str[i] > 32)
			i++;
	}
	cout << cnt;
	return 0;
}
