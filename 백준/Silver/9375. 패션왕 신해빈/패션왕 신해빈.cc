#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(void)
{
    // 패션왕 신해빈
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T, n;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string dress, type;
        int cnt = 1;
        cin >> n;
        map<string, int> dress_map;
        for (int j = 0; j < n; j++) {
            // dress는 중복되지 않으므로 입력만하고 사용하지 않음
            cin >> dress >> type;
            // map에 해당 type이 없으면 삽입, 있으면 value 증가
            if (dress_map.find(type) == dress_map.end())
                dress_map.insert({type, 1});
            else
                dress_map[type]++;
        }
        // map의 value + 1을 전부 곱함
        for (auto d : dress_map)
            cnt = cnt * (d.second + 1);
        // 맨 몸인 경우의 수를 빼고 출력
        cout << cnt - 1 << '\n';
    }
    return 0;
}