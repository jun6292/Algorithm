#include <iostream>
#include <string>
using namespace std;

int main() {
	string str;
	int cnt = 0;
	cin >> str;
	for(int i = 0; i < str.length(); i++){
		if (str[i] == 'd' && str[i + 1] == 'z' && str[i + 2] == '='){
			i += 2;
		}
		else if (str[i] == 'c' || str[i] == 'd' || str[i] == 's' || str[i] == 'z'){
			if (str[i + 1] == '=' || str[i + 1] == '-'){
				i++;
			}
		}
		else if (str[i] == 'l' || str[i] == 'n'){
			if (str[i + 1] == 'j'){
				i++;
			}
		}
		cnt++;
	}
	cout << cnt;
	return 0;
}
