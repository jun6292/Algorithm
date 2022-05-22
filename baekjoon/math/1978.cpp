#include <iostream>
using namespace std;

int main(void) {
    int N;  // 주어진 수의 개수
    int num;
    int cnt = 0;  // 소수의 개수
    cin >> N;
    for (int i = 0; i < N; i++){
      cin >> num;
      int prime = 0;
      for(int j = 2; j * j <= num; j++){
        if (num % j == 0)
          prime++;
      }
      if (prime == 0 && num != 1)
        cnt++;
    }
    cout << cnt;
    return 0;
}
