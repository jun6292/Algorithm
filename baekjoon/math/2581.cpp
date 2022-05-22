#include <iostream>
using namespace std;

bool is_prime(int n){  // 소수 판별 함수
  if (n == 1)
    return 0;
  for(int i = 2; i * i <= n; i++){
    if (n % i == 0)
      return 0;
  }
  return 1;
}

int main(void) {
  int min, max, m;
  int min_prime;
  int prime_sum = 0;
  int cnt = 0;  // 소수의 갯수 카운트
  cin >> min >> max;
  m = min;
  while (m <= max){ // 소수 중 최솟값
    if (is_prime(m)){
      min_prime = m;
      break;
    }
    m++;
  }
  while (min <= max){ // 소수 합
    if (is_prime(min)){
      cnt++;
      prime_sum += min;
    }
    min++;
  }
  if (cnt == 0) // 소수가 없을 때
    cout << "-1\n";
  else
  {
    cout << prime_sum << "\n";  
    cout << min_prime;
  }
  return 0;
}
