#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // 약수
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, num;
    vector<int> n;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> num;
        n.push_back(num);
    }
    
    sort(n.begin(), n.end());
    cout << n[0] * n[n.size() - 1] << "\n";

    return 0;
}