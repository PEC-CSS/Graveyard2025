#include <cstdlib> 
#include <iostream>
using namespace std;
int main(){
    int count = 0;
    bool flag = false;
    
    
    int randomNumber = rand() % 100 + 1;// 1 to 100 random number 
    while (flag == false){
        cout << "Enter a number = ";
        int number  ;
        cin >> number ;
        if(randomNumber==number){
           
            flag = true;
            count ++;
        }
        if(randomNumber>number){
           cout<<"The numeber is bigger than you guessed\n";
           count ++;
        }
        if(randomNumber<number){
            cout<<"the number is smaller than you guessed\n";
            count ++;
         }

    }
    
    cout<<"congratulation u guessed it right\n";
    cout<<"The number tries you took to guess was = "<<count;
    return 0;
}