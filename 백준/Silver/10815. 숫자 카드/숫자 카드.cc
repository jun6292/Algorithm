#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, num1, M, num2;
    vector<int> v1, v2;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> num1;
        v1.push_back(num1);
    }
    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> num2;
        v2.push_back(num2);
    }   // 입력
    sort(v1.begin(), v1.end());
    for (int i = 0; i < M; i++) {
        cout << binary_search(v1.begin(), v1.end(), v2[i]) << " ";
    }   // 출력
    return 0;
}