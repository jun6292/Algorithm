#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp(pair<int, string> a, pair<int, string> b) {
    return a.first < b.first;
}

int main() 
{
    int N;
    int age;
    string name;
    vector<pair<int, string>> v;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> age >> name;
        v.push_back({age, name});
    }
    stable_sort(v.begin(), v.end(), cmp);
    for (auto n : v)
        cout << n.first << " " << n.second << "\n";
    return 0;
}