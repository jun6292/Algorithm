#include <iostream>
using namespace std;

int self_num(int n)
{
  return (n + n/1000 + (n/100)%10 + (n/10)%10 + n%10);
}

int main(void)
{
  int i = 1;
  int n = 1;
  int arr[10001] = { 0 };
  int tmp;
   while (i <= 10000){
    tmp = self_num(i);
    if (tmp < 10001)
      arr[tmp] = 1;
    i++;
  }
  while (n < 10001){
    if (arr[n] != 1)
      cout << n << '\n';
    n++;
  }
  return 0;
}