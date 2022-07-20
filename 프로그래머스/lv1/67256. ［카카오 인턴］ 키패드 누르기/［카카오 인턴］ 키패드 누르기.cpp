#include <string>
#include <vector>
#include <cmath>
using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    int left_hand = 10, right_hand = 12;    // *, #
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {    // 1, 4, 7 입력
            answer += "L";
            left_hand = numbers[i];
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {   // 3, 6, 9 입력
            answer += "R";
            right_hand = numbers[i];
        }
        else {  // 2, 5, 8, 0 입력
            if (numbers[i] == 0)
                numbers[i] = 11;
            
            // 왼손, 오른손과 누를 번호의 거리
            int dis_l = abs(numbers[i] - left_hand) / 3 + abs(numbers[i] - left_hand) % 3;
            int dis_r = abs(numbers[i] - right_hand) / 3 + abs(numbers[i] - right_hand) % 3;
            if (dis_l == dis_r) {   // 왼손, 오른손 거리가 같을 때
                if (hand == "right") {
                    answer += "R";
                    right_hand = numbers[i];
                }
                else {
                    answer += "L";
                    left_hand = numbers[i];
                }
            }
            else if (dis_l > dis_r) {   // 왼손 거리가 더 멀면
                answer += "R";
                right_hand = numbers[i];
            }
            else {  // 오른손 거리가 더 멀면
                answer += "L";
                left_hand = numbers[i];
            }
        }
    }
    return answer;
}