#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    int check = 0;  // 총 진행한 작업의 개수
    
    while (check < progresses.size()) {
        int cnt = 0;    // 한 번에 배포한 작업의 개수
        
        for (int i = check; i < progresses.size(); i++)   // 선입선출, 큐에 순서대로 삽입
            q.push(progresses[i]);
        if (q.front() >= 100) {
            while (q.front() >= 100 && !q.empty()) {
                q.pop();
                cnt++;
            }
            answer.push_back(cnt);
            check += cnt;
        }
        else {
            while (!q.empty())
                q.pop();
            for (int j = 0; j < progresses.size(); j++)
                progresses[j] += speeds[j];
        }
    }
    return answer;
}