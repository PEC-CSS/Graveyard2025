#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;


int wealthy(vector<int>& v) {
    int n=v.size();
    if(n==1) return v[0];
    int m1=v[0];
    int m2=max(v[0], v[1]);
    for(int i=2; i<n; i++)
    {
        if(v[i] + m1 > m2)
        {
            int temp=m2;
            m2 = m1 + v[i];
            m1=temp;
        }

        else
        m1 = m2;
    }
    return m2;
}
int main()
{
    vector<int> v={1,2,3};
    cout<<wealthy(v);
}
