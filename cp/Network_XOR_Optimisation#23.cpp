#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

void compute(int index, int n, unordered_set <int> &s, vector<int> &v, vector<int> current){

    if(index == n){
        int q = 0;
        for(int i : current){
            q = q ^ i;
        }
        s.insert(q);
        return;
    }
    current.push_back(v[index]);
    compute(index + 1, n, s, v, current);
    current.pop_back();

    for(int j = 0; j < current.size(); j++){
        current[j] += v[index];
        compute(index + 1, n, s, v, current);
        current[j] -= v[index];
    }
}
int main()
{
    int n;
    cin>>n;
    vector<int> v(n);
    int q=0;
    unordered_set<int> s;
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    vector<int> current ={};
    compute(0, n, s, v, current);
    cout << s.size();
}
