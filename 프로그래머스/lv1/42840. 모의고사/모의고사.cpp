#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    // 수포자 1, 2, 3의 찍기 규칙
    int num1[5] = {1, 2, 3, 4, 5}, num2[8] = {2, 1, 2, 3, 2, 4, 2, 5}, num3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    //  수포자 1, 2, 3의 맞은 문제 수
    int cnt[3] = {0, 0, 0};     
    for (int i = 0; i < answers.size(); i++){
        if (answers[i] == num1[i % 5])
            cnt[0]++;
        if (answers[i] == num2[i % 8])
            cnt[1]++;
        if (answers[i] == num3[i % 10])
            cnt[2]++;
    }
    // 문제를 가장 많이 맞힌 사람
    int max_cnt = max(max(cnt[0], cnt[1]), cnt[2]);
    for (int i = 0; i < 3; i++){
        if (max_cnt == cnt[i])
            answer.push_back(i + 1);
    }
    return answer;
}