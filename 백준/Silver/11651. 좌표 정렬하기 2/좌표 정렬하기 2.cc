#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second)
        return a.first < b.first;
    return a.second < b.second;
}

int main() 
{
    int N;
    int x, y;
    vector<pair<int, int>> num;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        num.push_back({x, y});
    }
    sort(num.begin(), num.end(), cmp);
    for (auto n : num)
        cout << n.first << " " << n.second << "\n";
    return 0;
}