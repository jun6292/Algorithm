#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(pair<int, double>& a, pair<int, double>& b) {
	if (a.second == b.second)       // 실패율이 같다면
        return a.first < b.first;   // 스테이지를 오름차순으로 정렬
	return a.second > b.second;     // 실패율의 내림차순 정렬
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<int, double>> fail;
    for (int i = 1; i <= N; i++) {
        int not_clear = 0;  // 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        int total = 0;      // 스테이지에 도달한 플레이어 수
        for (int j = 0; j < stages.size(); j++) {
            if (stages[j] >= i) {
                total++;
                if (stages[j] == i)
                    not_clear++;
            }
        }
        if (total == 0) // divide by 0, 예외처리
            total = 1;
        fail.push_back({i, (double)not_clear / total});    // 실패율
    }
    sort(fail.begin(), fail.end(), cmp);
    for (auto it : fail) {
        answer.push_back(it.first);
    }
    return answer;
}