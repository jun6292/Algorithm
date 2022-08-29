#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    priority_queue<int> pq;
    queue<pair<int, int>> q;
    // 우선순위 큐에 중요도 삽입, pair 큐에 순서와 중요도 삽입
    for (int i = 0; i < priorities.size(); i++) {
        pq.push(priorities[i]);
        q.push({i, priorities[i]});
    }
    
    while (!q.empty()) {
        int idx = q.front().first;
        int imp = q.front().second;
        
        // 인쇄 대기목록에서 imp보다 중요도가 높은 문서가 존재하면 대기목록의 가장 마지막에 넣는다.
        if (pq.top() > imp) {
            q.push(q.front());
            q.pop();
        }
        // 그렇지 않으면 인쇄
        else {
            pq.pop();
            q.pop();
            answer++;
            if (location == idx)    // 인쇄를 요청한 문서가 나오면
                break;
        }
    }
    
    return answer;
}