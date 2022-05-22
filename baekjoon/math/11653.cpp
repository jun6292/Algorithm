#include <iostream>
using namespace std;

int main(void) {
  int N;
  cin >> N;
  int i = 2;
  while (N > 0){
    if (N == 1)
      break;
    if (N % i == 0){
      N /= i;
      cout << i << "\n";
      i--;
    }
    i++;
  }
  return 0;
}
