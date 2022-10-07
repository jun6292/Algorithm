#include <iostream>

using namespace std;

int main()
{
    // 팩토리얼 0의 개수
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int cnt = 0;

    cin >> N;
    // 0을 만드는 요소는 소인수 2와 5로 이루어진다.
    // 2와 5가 곱해져야 0이 한 개 만들어지므로 곱해지는 5의 갯수만 카운트한다.
    for (int i = 1; i <= N; i++) {
        if (i % 5 == 0)
            cnt++;
        if (i % 25 == 0)    // 5가 2개 포함됨.
            cnt++;
        if (i % 125 == 0)   // 5가 3개 포함됨.
            cnt++;    
    }
    cout << cnt << "\n";
    return 0;
}