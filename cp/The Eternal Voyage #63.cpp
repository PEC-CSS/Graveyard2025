#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> v(n);
    int sum = 0;
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    for(int i = 0; i < n; i++){
        int t;
        cin >> t;
        v[i] -= t;
        sum += v[i];
    }
    if(sum < 0){
        cout << "-1";
        return 0;
    }
    sum = 0;
    int index = -1, greatest = 0, starting_index = 0;
    for(int i = 0; i < n; i++){
        sum += v[i];
        if(sum < 0){
            sum = 0;
            starting_index = i + 1;
            continue;
        }
        if(sum > greatest){
            greatest = sum;
            index = starting_index;
        }
    }
    cout << index;
}
