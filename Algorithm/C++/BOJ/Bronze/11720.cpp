#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    int total_sum = 0;
    char c;
    for (int i = 0; i < n; i++) {
        cin >> c;
        total_sum += c - 48;    // �ƽ�Ű �ڵ带 �̿��Ͽ� �ذ�, '1'�� 49
    }

    cout << total_sum;

    return 0;
}
