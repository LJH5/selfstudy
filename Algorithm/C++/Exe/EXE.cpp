#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int max = 0;
    int max_idx = 0;
    
    for (int i = 1; i < 10; i++) {
        int num;
        cin >> num;
        if (num > max) {
            max = num;
            max_idx = i;
        }
    }

    cout << max << "\n";
    cout << max_idx << "\n";

    return 0;
}
