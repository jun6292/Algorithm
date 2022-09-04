#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    // 참외밭
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // K: 단위 면적 당 자라는 참외의 수, direc: 방향, length: 변의 길이
    int K, direc, length;
    // big_sq: 육각형에서 큰 사각형, little_sq: 육각형에서 작은 사각형, check: 큰 사각형을 이루는 변의 인덱스
    int big_sq = 0, little_sq = 0, check = 0;
    vector<pair<int, int>> v;

    cin >> K;    
    for (int i = 0; i < 6; i++) {
        cin >> direc >> length;
        v.push_back({direc, length});   // 방향, 길이
    }
    // 곱한 값중 가장 큰값을 저장
    // 마지막 입력과 첫 번째 입력의 곱이 가장 큰 사각형이 될 수 있음을 인지 !
    for (int i = 0; i < 6; i++) {
        if (big_sq < v[i].second * v[(i + 1) % 6].second) {
            big_sq = v[i].second * v[(i + 1) % 6].second;
            check = i;
        }
    }
    // 큰 사각형의 한 변 인덱스의 +3, 4번째 변의 곱이 작은 사각형일 수 밖에 없음.
    little_sq = v[(check + 3) % 6].second * v[(check + 4) % 6].second;
    cout << (big_sq - little_sq) * K << "\n";

    return 0;
}