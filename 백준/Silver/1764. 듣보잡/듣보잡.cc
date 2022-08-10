#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    int cnt = 0;
    string name;
    vector<string> v, same;
    cin >> N >> M;
    for (int i = 0; i < N + M; i++) {
        cin >> name;
        v.push_back(name);
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size() - 1; i++) {
        if (v[i] == v[i + 1]) {
            cnt++;
            same.push_back(v[i]);
        }
    }
    cout << cnt << "\n";
    for (auto i : same)
        cout << i << "\n";
    return 0;
}