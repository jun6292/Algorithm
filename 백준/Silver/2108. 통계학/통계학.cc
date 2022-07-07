#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<int> arr;
    int cnt[8001] = { 0 };
    int N, tmp, most_val;
    int sum = 0, most = -1;
    bool second = false;    
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        arr.push_back(tmp);
        sum += tmp;
        cnt[arr[i] + 4000]++;
    }
    sort(arr.begin(), arr.end());
    for (int i = 0; i < 8001; i++) {
        if (cnt[i] == 0)
            continue;
        if (cnt[i] == most) {
            if (second) {
                most_val = i - 4000;
                second = false;
            }
        }
        if (cnt[i] > most) {
            most = cnt[i];
            most_val = i - 4000;
            second = true;
        }
    }
    float result = (float)sum / N;
    if (result > -0.5 && result < 0)
        cout << 0 << "\n";
    else
        cout << round(result) << "\n";  // 산술평균
    cout << arr[N / 2] << "\n";    // 중앙값
    cout << most_val << "\n";   // 최빈값
    cout << arr[arr.size() - 1] - arr[0] << "\n";   // 범위
    return 0;
}