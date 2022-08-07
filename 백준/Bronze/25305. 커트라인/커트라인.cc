#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, k, x;
    vector<int> rank;
    cin >> N >> k;
    for (int i = 0; i < N; i++) {
        cin >> x;
        rank.push_back(x);
    }
    sort(rank.begin(), rank.end(), greater<int>());
    cout << rank[k - 1] << "\n";
    return 0;
}