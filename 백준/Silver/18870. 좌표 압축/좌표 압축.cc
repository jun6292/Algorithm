#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, num;
    cin >> N;
    vector<int> copy, origin;
    for (int i = 0; i < N; i++) {
        cin >> num;
        copy.push_back(num);
        origin.push_back(num);
    }
    sort(copy.begin(), copy.end());
    copy.erase(unique(copy.begin(), copy.end()), copy.end());
    for (int i = 0; i < N; i++) {
        cout << lower_bound(copy.begin(), copy.end(), origin[i]) - copy.begin() << " ";
    }
    return 0;
}