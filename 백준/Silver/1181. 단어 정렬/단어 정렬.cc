#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp(string a, string b) {
    if (a.size() == b.size())
        return a < b;
    return a.size() < b.size();
}

int main() 
{
    int N;
    string str;
    vector<string> words;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> str;
        words.push_back(str);
    }
    sort(words.begin(), words.end(), cmp);
    words.erase(unique(words.begin(), words.end()), words.end());
    for (auto n : words)
        cout << n << "\n";
    return 0;
}