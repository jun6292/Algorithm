#include <iostream>

using namespace std;

int tmp[500000];
int cnt = 0;

void merge(int a[], int l, int mid, int r, int K) {
    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j])
            tmp[k++] = a[i++];
        else
            tmp[k++] = a[j++];
    }
    while (i <= mid)
        tmp[k++] = a[i++];
    while (j <= r)
        tmp[k++] = a[j++];
    for (int x = l; x <= r; x++) {
        a[x] = tmp[x];
        cnt++;
        if (K == cnt)
            cout << tmp[x] << "\n";
    }
}

void merge_sort(int a[], int l, int r, int K) {
    if (l < r) {
        int mid = (l + r) / 2;
        merge_sort(a, l, mid, K);
        merge_sort(a, mid + 1, r, K);
        merge(a, l, mid, r, K);
    }
}

int main(void)
{
    // 알고리즘 수업 - 병합 정렬 1
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;   // 배열의 크기 N, 저장 횟수 K
    cin >> N >> K;
    int* a = new int [N];
    for (int i = 0; i < N; i++)
        cin >> a[i];

    merge_sort(a, 0, N - 1, K);
    if (cnt < K)
        cout << "-1\n";
    // for (int i = 0; i < N; i++)
    //     cout << a[i] << " ";
    return 0;
}