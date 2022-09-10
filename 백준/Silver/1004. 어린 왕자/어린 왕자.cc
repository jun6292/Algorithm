#include <iostream>
#include <cmath>

using namespace std;

// 두 점 사이의 거리
double dist(double x1, double y1, double x2, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main()
{
    // 어린 왕자
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T, n;   // 테스트 케이스 수, 행성계의 개수
    int x1, y1, x2, y2;     // 출발점과 도착점
    int Cx, Cy, r;  // 중점과 반지름

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> n;
        int ans = 0;
        for (int j = 0; j < n; j++) {
            cin >> Cx >> Cy >> r;
            if (dist(x1, y1, Cx, Cy) < r)
                if (dist(x2, y2, Cx, Cy) > r)
                    ans++;
            if (dist(x2, y2, Cx, Cy) < r)
                if (dist(x1, y1, Cx, Cy) > r)
                    ans++;
        }
        cout << ans << "\n";
    }

    return 0;
}