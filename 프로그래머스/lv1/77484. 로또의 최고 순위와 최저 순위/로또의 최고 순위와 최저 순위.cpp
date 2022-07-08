#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int cnt = 0;
    int rank = 6;
    // 일치하는 번호의 갯수 세기
    for (int i = 0; i < win_nums.size(); i++) {
        if (find(lottos.begin(), lottos.end(), win_nums[i]) != lottos.end()) {   
            cnt++;
        }
    }
    // 최저 순위
    if (cnt > 1)    // 1개 번호만 일치할 경우 6위 유지
        rank -= (cnt - 1);
    answer.push_back(rank); 
    
    // 최고 순위를 구하기 위해 0을 일치하는 숫자로 판단
    for (int i = 0; i <lottos.size(); i++) {
        if (lottos[i] == 0){
            if (cnt == 0){  // 일치하는 번호가 없었을 때, 0을 일치하는 숫자로 판단하더라도 0이 1개일 때 순위는 6위
                rank = 6;
                cnt++;
            }
            else
                rank -= 1;
        }
    }
    answer.insert(answer.begin(), rank);    // 최고 순위를 앞에 삽입
    return answer;
}