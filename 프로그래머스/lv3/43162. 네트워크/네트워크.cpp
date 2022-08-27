#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n, false);
    
    for (int i = 0; i < n; i++) {
        
        if (visited[i])
            continue;
        
        queue<int> q;
        q.push(i);
        
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            
            if (visited[v])
                continue;
            
            visited[v] = true;
            
            for (int j = 0; j < n; j++) {
                if (v != j && computers[v][j] == 1 && !visited[j])
                    q.push(j);
            }
        }
        
        answer++;
    }
    
    return answer;
}