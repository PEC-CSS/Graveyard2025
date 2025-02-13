#include <iostream>
#include<vector>
using namespace std;


int findsubArrayxork(const vector<int>& arr,int k){
int i=0;
int n =arr.size();


for(int st=0;st<n;st++){
     int XorVal =0;
    for(int end=st;end<n;end++){
        XorVal ^= arr[end];
        if(XorVal == k){
            i++;
        }
    }
}
return i;
}





int main() {
     const vector<int>arr={4,2,2,6,4};
    int k=6;
    cout<<findsubArrayxork(arr,k);

    return 0;
}