#include <string>
#include <vector>

using namespace std;

void hanoi(vector<vector<int>>& v, int n, int from, int to, int by) {
	if (n == 1) {   // 종료 조건
        v.push_back({from, to});
    }
    else {
    	hanoi(v, n - 1, from, by, to);
        v.push_back({from, to});
        hanoi(v, n - 1, by, to, from);
    }
}

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer;
    hanoi(answer, n, 1, 3, 2);
    return answer;
}