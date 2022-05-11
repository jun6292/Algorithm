#include <iostream>
#include <string>
using namespace std;

int main() {
	int alpha[26] = { 0 };
	int cnt = 0;
	string S;
	cin >> S;

	for(int i = 0; i < S.length(); i++){
		if (S[i] >= 'a' && S[i] <= 'z')
			S[i] -= 32;
		alpha[S[i] - 'A']++;
	}
	int max = alpha[0];
	int max_idx = 0;
	for(int i = 0; i < 26; i++){
		if (max < alpha[i]){
			max = alpha[i];
			max_idx = i;
		}
	}
	for(int i = 0; i < 26; i++){
		if (max == alpha[i])
			cnt++;
	}
	if (cnt > 1)
		cout << "?";
	else
		cout << char(max_idx + 65);
	return 0;
}
