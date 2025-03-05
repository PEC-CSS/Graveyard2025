#include <cstdlib> 
#include <iostream>
using namespace std;
int main(){
    
    bool flag = false;
    
    
    int randomNumber = rand() % 100 + 1;// 1 to 100 random number 
    while (flag == false){
        std::cout << "enter a number";
        int number  ;
        std::cin >> number ;
        if(randomNumber==number){
           
            flag = true;
        }
        if(randomNumber>number){
           cout<<"the numebr is bigger than you guessed";
           
        }
        if(randomNumber<number){
            cout<<"the numeber is smaller than you guessed";
            
         }

    }
    
    std::cout<<"congratulation u guessed it right";
    return 0;
}