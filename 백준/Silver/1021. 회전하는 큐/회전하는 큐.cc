#include <iostream>
#include <deque>

using namespace std;

int main()
{
    // 회전하는 큐
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, pos;  // 큐의 크기, 뽑아내려고 하는 수의 개수, 뽑아내려고 하는 수의 위치
    deque<int> dq;  // 회전하는 큐
    int cnt = 0;

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        dq.push_back(i);
    }

    for (int i = 0; i < M; i++) {
        // deque에서 pos의 위치가 맨 앞이랑 가까운지 맨 뒤랑 가까운지 판단
        cin >> pos;
        int pos_idx = 0;
        for (int j = 0; j < dq.size(); j++) {
            if (dq[j] == pos) {
                pos_idx = j;
                break;
            }
        }
        if (pos_idx < dq.size() - pos_idx) {
            // 왼쪽에 가까우므로 왼쪽으로 이동
            while (pos != dq.front()) {
                dq.push_back(dq.front());
                dq.pop_front();
                cnt++;
            }
            dq.pop_front();
        }
        else {
            // 오른쪽에 가깝거나 중간이므로 오른쪽으로 이동
            while (pos != dq.front()) {
                dq.push_front(dq.back());
                dq.pop_back();
                cnt++;
            }
            dq.pop_front();
        }
    }

    cout << cnt << "\n";
	return 0;
}