#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i=0; i<n; i++) cin>>v[i];
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
    cout<<m2;
}
