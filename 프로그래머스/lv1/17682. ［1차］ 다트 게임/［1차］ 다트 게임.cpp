#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    int score = 0;  // 해당 점수
    int tmp = 0;    // 바로 전에 얻은 점수
    for (int i = 0; i < dartResult.size(); i++) {
        if ('0' <= dartResult[i] && dartResult[i] <= '9') {
            tmp = score;    // 바로 전에 얻은 점수를 저장
            if (dartResult[i + 1] == '0') {
                score = 10;
                i++;
            }
            else
                score = dartResult[i] - '0';
        }
        // 'S'일 경우 score^1이므로 변화 X
        else if (dartResult[i] == 'S' || dartResult[i] == 'D' || dartResult[i] == 'T') {
            if (dartResult[i] == 'D')
                score = pow(score, 2);
            else if (dartResult[i] == 'T')
                score = pow(score, 3);
            
            if (dartResult[i + 1] == '*') {     // 스타상일 경우 해당 점수와 바로 전에 얻은 점수를 각 2배
                answer -= tmp;
                tmp *= 2;
                score *= 2;
                answer += tmp;
                i++;
            }
            else if (dartResult[i + 1] == '#') {    // 아차상일 경우 해당점수만 * -1
                score *= -1;    
                i++;
            }
            answer += score;
        }
    }
    return answer;
}