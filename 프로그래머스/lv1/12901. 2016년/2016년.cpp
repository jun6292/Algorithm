#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string  answer = "";
    string  days[7] = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };
    int     months[12] = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int     day_cnt = 0;
    
    for (int i = 0; i < a - 1; i++){
        day_cnt += months[i];
    }
    day_cnt += b;
    answer = days[(day_cnt - 1) % 7];
    return answer;
}