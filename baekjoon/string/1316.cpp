#include <iostream>
#include <string>
using namespace std;

int main() {
	int N, j;
	string str;
	int cnt = 0;
	cin >> N;
	for(int i = 0; i < N; i++){
		cin >> str;
		int arr[26] = { 0 };
		arr[str[0] - 'a'] = 1;
		for(j = 1; j < str.length(); j++){
			if (str[j - 1] != str[j]){
				if(arr[str[j] - 'a'] == 0)
					arr[str[j] - 'a']++;
				else
					break;
			}
		}
		if (j == str.length())
			cnt++;
	}
	cout << cnt;
	return 0;
}
