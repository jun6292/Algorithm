#include <iostream>
using namespace std;

bool is_prime(int n){
  if (n == 1)
    return false;
  for(int i = 2; i * i <= n; i++){
    if (n % i == 0)
      return false;
  }
  return true;
}

int main(void) {
  int M, N;
  cin >> M >> N;
  while (M <= N){
    if (is_prime(M))
      cout << M << "\n";
    M++;
  }
  return 0;
}
