#include <iostream>
#include <cmath>

using namespace std;

int g_cnt = 0;

bool is_promising(int* board, int cdx) {
    int i = 0;
    while (i < cdx) {
        if (board[i] == board[cdx] || cdx - i == abs(board[cdx] - board[i]))
            return false;
        i++;
    }
    return true;
}

void N_Queen(int* board, int N, int cdx) {
    int i;
    if (cdx == N)
        g_cnt++;
    else {
        i = 0;
        while (i < N) {
            board[cdx] = i;
            if (is_promising(board, cdx))
                N_Queen(board, N, cdx + 1);
            i++;
        }
    }
}

int main()
{
    // N-Queen
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int *board = new int[N];
    N_Queen(board, N, 0);
    cout << g_cnt << "\n";

    return 0;
}