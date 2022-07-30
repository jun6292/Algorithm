#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() 
{
    int N;
    vector<int> num;
    cin >> N;
    while (N) {
        num.push_back(N % 10);
        N /= 10;
    }
    sort(num.begin(), num.end(), greater<int>());
    for (int i : num)
        cout << i;
        
    return 0;
}