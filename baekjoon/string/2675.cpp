#include <iostream>
#include <string>
using namespace std;

int main() {
	int Test;
	cin >> Test;
	for(int i = 0; i < Test; i++){
		int Reps;
		string S;
		cin >> Reps >> S;
		for(int i2 = 0; i2 < S.length(); i2++){
			for (int i3 = 0; i3 < Reps; i3++)
				cout << S[i2];
		}
		cout << '\n';
	} 
	return 0;
}
