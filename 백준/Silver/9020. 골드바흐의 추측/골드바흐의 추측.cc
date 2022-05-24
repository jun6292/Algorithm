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
  int test;
  int n;
  int a, b;
  cin >> test;
  for(int i = 0; i < test; i++){
    cin >> n; // 4 <= n <= 10,000
    a = n/2;
    b = n/2;  // 두 소수의 차이가 가장 작게
    while (a >= 2){
      if (is_prime(a) && is_prime(b)){
        cout << a << " " << b << "\n";
        break;
      }
      a--;  // 하나씩 줄여가면서
      b++;  // 하나씩 늘려가면서
    }
  }
  return 0;
}