#include <iostream>
#include <string>
using namespace std;

struct Car {
    string brand;
    string model;
    int year;
    bool used;
};

Car factoryCar( string brand, string model, int year, bool used ) {
    Car templeteCar;
    templeteCar.brand = brand;
    templeteCar.model = model;
    templeteCar.year = year;
    templeteCar.used = used;
    return templeteCar;
}

int main() {
    // Refactory
    Car carOne = factoryCar( "Audi", "A5", 2022, true );
    // carOne.brand = "Audi";
    // carOne.model = "A5";
    // carOne.year = 2022;
    // carOne.used = true;
    cout << carOne.brand << endl;
    cout << carOne.model << endl;
    cout << carOne.year << endl;
    cout << carOne.used << endl;
    
    Car carTwo = factoryCar( "BMW", "M5", 2020, false );
    // carTwo.brand = "BMW";
    // carTwo.model = "M5";
    // carTwo.year = 2020;
    // carTwo.used = false;
    cout << carTwo.brand << endl;
    cout << carTwo.model << endl;
    cout << carTwo.year << endl;
    cout << carTwo.used << endl;

    Car carBis = factoryCar( "Mercedes Benz", "CLK", 1995, true );
    cout << carBis.brand << endl;
    Car carFour = factoryCar( "Lotus", "Elite", 2000, false );
    cout << carFour.brand << endl;

    return 0;
}
