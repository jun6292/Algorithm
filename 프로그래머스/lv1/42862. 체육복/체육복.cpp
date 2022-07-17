#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());
    
    // reserve 배열을 지워나가며 체육수업을 들을 수 있는 학생을 추가
    // 여벌 체육복을 가지고 있는 학생이 도난당했을 경우
    for(int i = 0; i < lost.size(); i++) {
        for(int j = 0 ; j < reserve.size(); j++) {
            if(lost[i] == reserve[j]) {
                lost.erase(lost.begin() + i);
                reserve.erase(reserve.begin() + j);
                i = -1;
                break;
            }
        }
    }
    // 체육수업을 들을 수 있는 최소학생 수
    int answer = n - lost.size();
    
    for (int i = 0; i < lost.size(); i++) {
        // 체육복을 모두 빌려주었거나, 모든 학생이 체육수업을 들을 수 있으면 반복문 종료
        if (answer == n || reserve.size() == 0)
            break;
        // 앞 번호 학생에게 체육복 빌려주기
        if (find(reserve.begin(), reserve.end(), lost[i] + 1) != reserve.end()) {
            answer++;
            reserve.erase(find(reserve.begin(), reserve.end(), lost[i] + 1));
        }
        // 뒷 번호 학생에게 체육복 빌려주기
        if (find(reserve.begin(), reserve.end(), lost[i] - 1) != reserve.end()) {
            answer++;
            reserve.erase(find(reserve.begin(), reserve.end(), lost[i] - 1));
        }
    }
    return answer;
}