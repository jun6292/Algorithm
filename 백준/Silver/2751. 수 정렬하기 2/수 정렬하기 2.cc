#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    int n;
    vector<int> num;
    for (int i = 0; i < N; i++) {
        cin >> n;
        num.push_back(n);
    }
    sort(num.begin(), num.end());
    for (int i = 0; i < num.size(); i++)
        cout << num[i] << "\n";
    return 0;
}