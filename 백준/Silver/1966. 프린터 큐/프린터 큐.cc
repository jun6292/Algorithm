#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    // 프린터 큐
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // T: 테스트 케이스 수, N: 문서의 개수, M: 현재 queue에서 몇 번째 놓여 있는지, imp: 중요도
    int T, N, M, imp;
    
    cin >> T;
    for (int i = 0; i < T; i++) {
        int cnt = 0;
        priority_queue<int> pq;     // 문서 중요도
        queue<pair<int, int>> q;    // 문서 정보

        cin >> N >> M;
        for (int j = 0; j < N; j++) {
            cin >> imp;
            q.push({j, imp});
            // q.emplace(j, imp);
            pq.push(imp);
        }

        while (!q.empty()) {
            int idx = q.front().first;          // 문서 순서
            int importance = q.front().second;  // 문서 중요도
            // 중요도가 밀리면 q에서 뒤로 보냄
            if (pq.top() > importance) {    
                q.push(q.front());
                q.pop();
            }
            else {  // 인쇄
                pq.pop();
                q.pop();
                cnt++;
                if (idx == M) {
                    cout << cnt << "\n";
                    break;
                }
            }
        }
    }
    return 0;
}