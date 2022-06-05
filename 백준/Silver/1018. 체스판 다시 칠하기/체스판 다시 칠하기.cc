#include <iostream>
using namespace std;

int main(void) {
    int N, M;

    // input
    cin >> N >> M;
    char** board = new char * [N];
	for (int i = 0; i < N; i++)
		board[i] = new char[M];
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			cin >> board[i][j];
    
    int cnt = 0;
    int min = (N * M) / 2 + 1;  // 다시 칠해야 하는 정사각형 개수의 최솟값

    // #BWBW
    for(int i = 0; i <= N - 8; i++){
        for(int j = 0; j <= M - 8; j++){
            cnt = 0;
                for(int k = i; k < i + 8; k++){
                    for(int l = j; l < j + 8; l++){
                        if ((k + l) % 2 == 0){
                            if (board[k][l] != 'B')
                                cnt++;
                        }
                        else {
                            if (board[k][l] != 'W')
                                cnt++;
                        }
                    }
                }
            if (cnt < min)
                min = cnt;
        }
    }
    // #WBWB
    for(int i = 0; i <= N - 8; i++){
        for(int j = 0; j <= M - 8; j++){
            cnt = 0;
                for(int k = i; k < i + 8; k++){
                    for(int l = j; l < j + 8; l++){
                        if ((k + l) % 2 == 0){
                            if (board[k][l] != 'W')
                                cnt++;
                        }
                        else {
                            if (board[k][l] != 'B')
                                cnt++;
                        }
                    }
                }
            if (cnt < min)
                min = cnt;
        }
    }
    cout << min;
    return 0;
}  