#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
  int N, num;
  vector<int> nb;
  cin >> N;
  for (int i = 0; i < N; i++){
    cin >> num;
    nb.push_back(num);
  }
  sort(nb.begin(), nb.end());
  for (int i = 0; i < nb.size(); i++)
    cout << nb[i] << "\n";
  return 0;
}