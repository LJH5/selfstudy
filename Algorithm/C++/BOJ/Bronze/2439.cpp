#include <bits/stdc++.h>
using namespace std;

void star(int n) {
    for (int i = n-1; i >= 0; i--) {
        for (int j = 0; j < n; j++) {
            if (i <= j) {
                cout << "*";
            }
            else {
                cout << " ";
            }
        }
        cout << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    star(n);

    return 0;
}
