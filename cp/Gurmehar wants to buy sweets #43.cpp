#include <bits/stdc++.h>
using namespace std;

int main() {
    int no_of_test_cases;
    cin >> no_of_test_cases;
    
    for (int i = 1; i <= no_of_test_cases; i++) 
    {
        int num_shops; // Number of shops
        int x; // Daily budget
        cin >> num_shops >> x;
        int sweet_prices[num_shops];

        for (int i = 0; i < num_shops; i++) {
            cin >> sweet_prices[i]; // Input prices
        }

        sort(sweet_prices, sweet_prices + num_shops); // Sort in ascending order

        int total_price = 0;
        int total_sweets = 0; 

        for (int i = 0; i < num_shops; i++) 
        {
            total_price += sweet_prices[i]; 

            if (total_price <= x) 
            {
                
                int remaining_budget = x - total_price;

                
                int additional_days = remaining_budget / (i + 1);

                
                total_sweets += additional_days + 1;
            }
        }

        cout << total_sweets << endl;
    }

}
