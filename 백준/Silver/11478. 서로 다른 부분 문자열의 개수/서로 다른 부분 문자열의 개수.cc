#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string S;
    set<string> s_each_subs;
    cin >> S;
    int len = S.size();
    int idx = 0, npos = 1;
    while (true) {
        if (idx + npos > len || idx == len) {
            npos++;
            idx = 0;
        }
        string subs = S.substr(idx, npos);
        if (subs != S)
            s_each_subs.insert(subs);
        else 
            break;
        idx++;
    }
    // s_each_subs.size()는 진부분집합의 개수이므로 부분집합의 개수는 1을 더해야함.
    cout << s_each_subs.size() + 1 << "\n"; 
    return 0;
}