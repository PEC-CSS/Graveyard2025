#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

// Function to check if a given overload factor is feasible
bool isFeasible(int N, int K, const vector<int>& C, int overload) {
    int changes = 0;
    int current_min = C[0] - overload;
    int current_max = C[0] + overload;

    for (int i = 1; i < N; ++i) {
        // Update the range for the current dock
        current_min = max(current_min, C[i] - overload);
        current_max = min(current_max, C[i] + overload);

        // If the range is invalid, we need to start a new segment
        if (current_min > current_max) {
            changes++;
            current_min = C[i] - overload;
            current_max = C[i] + overload;
        }

        // If the number of changes exceeds K, the overload factor is not feasible
        if (changes > K) {
            return false;
        }
    }
    return true;
}

// Function to find the minimal overload factor
int findMinOverload(int N, int K, const vector<int>& C) {
    int low = 0;
    int high = *max_element(C.begin(), C.end()) - *min_element(C.begin(), C.end());
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
    int T;
    cin >> T;

    while (T--) {
        int N, K;
        cin >> N >> K;

        vector<int> C(N);
        for (int i = 0; i < N; ++i) {
            cin >> C[i];
        }

        // If K >= N-1, the overload factor is 0
        if (K >= N - 1) {
            cout << 0 << endl;
            continue;
        }

        // Otherwise, find the minimal overload factor
        int overload = findMinOverload(N, K, C);
        cout << overload << endl;
    }

    return 0;
}