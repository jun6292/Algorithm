#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    int cnt = 0;
    string str;
    unordered_set<string> s;
    for (int i = 0; i < N; i++) {
        cin >> str;
        s.insert(str);
    }
    for (int i = 0; i < M; i++) {
        cin >> str;
        if (s.find(str) != s.end())
            cnt++;
    }
    cout << cnt << "\n";
    return 0;
}