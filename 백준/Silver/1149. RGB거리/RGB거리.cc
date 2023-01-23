#include <iostream>
#include <algorithm>

using namespace std;

int rgb[1001][3];   // 입력을 저장하기 위한 배열

int main()
{
    // RGB거리
    ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N;
    int r, g, b;
    int min_cost = 0;   // 최소비용

    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> r >> g >> b;
        rgb[i][0] = r + (min(rgb[i - 1][1], rgb[i - 1][2]));
        rgb[i][1] = g + (min(rgb[i - 1][0], rgb[i - 1][2]));
        rgb[i][2] = b + (min(rgb[i - 1][0], rgb[i - 1][1]));
        min_cost = min(rgb[i][0], min(rgb[i][1], rgb[i][2]));
    }
    cout << min_cost << '\n';
}