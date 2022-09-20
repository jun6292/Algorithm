#include <string>
#include <vector>
#include <cmath>

using namespace std;

// 퀸을 그 자리에 둘 수 있는지 판별하는 함수
bool is_promising(int* board, int cdx) {
    for (int i = 0; i < cdx; i++) {
        // 퀸이 같은 열에 있거나 대각선 상에 있는 경우
        if (board[i] == board[cdx] || cdx - i == abs(board[cdx] - board[i]))
            return false;
    }
    return true;
}

void nqueen(int* board, int cdx, int n, int& answer) {
    if (cdx == n)   // 퀸을 끝까지 놓았다면 카운트
        answer++;
    else {  // 백트래킹, 퀸을 둘 수 없다면 이전 단계로 돌아가서 반복
        for (int i = 0; i < n; i++) {
            board[cdx] = i;
            if (is_promising(board, cdx)) {
                nqueen(board, cdx + 1, n, answer);
            }   
        }
    }
}

int solution(int n) {
    int* board = new int [n];
    int answer = 0;
    nqueen(board, 0, n, answer);   // 첫번째 행부터 퀸을 놓아본다.
    return answer;
}