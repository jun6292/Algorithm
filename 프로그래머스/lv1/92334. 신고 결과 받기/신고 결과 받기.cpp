#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer; // 유저별 받은 결과 메일 수
    map <string, int> report_cnt; // 유저별 신고당한 횟수
    map <string, set<string>> report_map;   // 유저별 신고한 타 유저 map, 중복 제거
    for (string s : report) {
        int bnk = s.find(' ');  // 공백기준 문자열 parsing
        string first = s.substr(0, bnk);    // 신고한 사람
        string second = s.substr(bnk);      // 신고 당한 사람
        
        // first가 second를 신고하지 않았다면
        if (report_map[first].find(second) == report_map[first].end()) {
            report_cnt[second]++;   // 신고횟수 늘려주고
            report_map[first].insert(second);   // report_map에 추가
        }
    }
    
    for (string s : id_list) {
        int result = 0;
        // k회 이상 신고 당한 사람 존재
        for (string str : report_map[s]) {
            if (report_cnt[str] >= k)
                result++;
        }
        answer.push_back(result);
    }
    return answer;
}