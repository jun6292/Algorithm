#include <iostream>
#include <string>

using namespace std;
int main() {
	string S;
	string alphabet = "abcdefghijklmnopqrstuvwxyz";
	cin >> S;
	for(int i = 0; i < alphabet.length(); i++)
		cout << (int)S.find(alphabet[i]) << " ";
	return 0;
}

// #include <iostream>
// // using namespace std;
//
// // int main(void)
// // {
// //   int alpha[26];
// //   for(int i = 0; i < 26; i++) 
// //     alpha[i] = -1;
// //   char S[100];
// //   cin >> S;
//
// //   int j = 0;
// //   while (S[j]){
// //     if (S[j] >= 'a' && S[j] <= 'g')
// //       alpha[(S[j] % 26) - 19] = j;
// //     else if (S[j] >= 'h' && S[j] <= 'z')
// //       alpha[(S[j] % 26) + 7] = j;
// //     j++;
// //   }
//   
//   //   for (int i = 0; i < 26; i++)
//   //     cout << alpha[i] << ' ';
//   //   cout << '\n';
//   //   return 0;
//   // }
