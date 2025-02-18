#include <bits/stdc++.h>
using namespace std;

int main() {
    long long no_of_test_cases;
    cin >> no_of_test_cases;

    for (long long i = 1; i <= no_of_test_cases; i++) 
    {
        long long num_shops; // Number of shops
        long long x; // Daily budget
        cin >> num_shops >> x;
        long long sweet_prices[num_shops];

        for (long long i = 0; i < num_shops; i++) {
            cin >> sweet_prices[i]; // Input prices
        }

        sort(sweet_prices, sweet_prices + num_shops); // Sort in ascending order

        long long total_price = 0;
        long long total_sweets = 0; 

        for (long long i = 0; i < num_shops; i++) 
        {
            total_price += sweet_prices[i]; 

            if (total_price <= x) 
            {

                long long remaining_budget = x - total_price;


                long long additional_days = remaining_budget / (i + 1);


                total_sweets += additional_days + 1;
            }
        }

        cout << total_sweets << endl;
    }

}
