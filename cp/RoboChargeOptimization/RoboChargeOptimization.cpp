#include <iostream>
#include <vector>

using namespace std;

bool isFeasible(int N, int K, const vector<int>& C, int overload) {
    int changes = 0;
    int current_min = C[0] - overload;
    int current_max = C[0] + overload;

    for (int i = 1; i < N; ++i) {
        current_min = max(current_min, C[i] - overload);
        current_max = min(current_max, C[i] + overload);
        if (current_min > current_max) {
            changes++;
            current_min = C[i] - overload;
            current_max = C[i] + overload;
        }
        if (changes > K) return false;
    }
    return true;
}

int findMinOverload(int N, int K, const vector<int>& C) {
    int low = 0;
    int high = 0;

    // Find the maximum difference in C (replaces max_element and min_element)
    int min_C = C[0], max_C = C[0];
    for (int i = 1; i < N; ++i) {
        if (C[i] < min_C) min_C = C[i];
        if (C[i] > max_C) max_C = C[i];
    }
    high = max_C - min_C;

    int result = high;

    // Binary search for the minimal overload factor
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (isFeasible(N, K, C, mid)) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, K;
        cin >> N >> K;
        vector<int> C(N);
        for (int i = 0; i < N; ++i) cin >> C[i];

        // If K >= N-1, the overload factor is 0
        if (K >= N - 1) {
            cout << 0 << '\n';
            continue;
        }

        // Otherwise, find the minimal overload factor
        int overload = findMinOverload(N, K, C);
        cout << overload << '\n';
    }

    return 0;
}