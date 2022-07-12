#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> stack;
    // 0 0 0 0 0
    // 0 0 1 0 3
    // 0 2 5 0 1
    // 4 2 4 4 2
    // 3 5 1 3 1
    for (int i = 0; i < moves.size(); i++) {
        for (int j = 0; j < board[moves[i] - 1].size(); j++) {  // 위에서부터
            if (board[j][moves[i] - 1] != 0) {
                stack.push_back(board[j][moves[i] - 1]);    // 인형을 stack에 넣는다
                board[j][moves[i] - 1] = 0;     // 다음 크레인이 왔을 때 중복해서 인형을 넣지 않기 위해 0 할당
                break;
            }
        }
    }
    int idx = 0;
    while (idx != stack.size() - 1) {
        if (stack.size() == 0)
            break;
        if (stack[idx] == stack[idx + 1]) { // 같은 모양의 인형이면,
            answer += 2;
            stack.erase(stack.begin() + idx, stack.begin() + idx + 2);  // 두 인형을 사라지게 한다.
            idx = -1;   // 미리 stack에 인형들을 넣어놨기 때문에 처음부터 다시 찾기 위해
        }
        idx++;
    }
    return answer;
}