#include <iostream>
#include <queue>

using namespace std;

int main()
{
    // 요세푸스 문제 0
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;
    cin >> N >> K;
    queue<int> q;
    // 큐에 숫자를 삽입
    for (int i = 1; i <= N; i++) {
        q.push(i);
    }
    // 순서대로 K번째 사람을 제거
    int cnt = 1;
    cout << "<";
    while (!q.empty()) {
        if (cnt % K == 0) {
            cout << q.front();
            q.pop();
            if (!q.empty())
                cout << ", ";
            else
                cout << ">";
        }
        else {
            q.push(q.front());
            q.pop();
        }
        cnt++;
    }
	return 0;
}