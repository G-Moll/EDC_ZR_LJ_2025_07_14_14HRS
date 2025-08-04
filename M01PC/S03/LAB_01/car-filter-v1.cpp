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

void carInfo( Car carData ) {
    cout << "Car info - " <<
        "Brand: " << carData.brand <<
        ", Model: " << carData.model <<
        ", Year: " << carData.year <<
        ", Used: " << carData.used << endl;
}

int main() {
    // Refactory
    Car carOne = factoryCar( "Audi", "A5", 2022, true );
    carInfo( carOne );
    // carOne.brand = "Audi";
    // carOne.model = "A5";
    // carOne.year = 2022;
    // carOne.used = true;
    // cout << carOne.brand << endl;
    // cout << carOne.model << endl;
    // cout << carOne.year << endl;
    // cout << carOne.used << endl;
    
    Car carTwo = factoryCar( "BMW", "M5", 2020, false );
    carInfo( carTwo );
    // carTwo.brand = "BMW";
    // carTwo.model = "M5";
    // carTwo.year = 2020;
    // carTwo.used = false;
    // cout << carTwo.brand << endl;
    // cout << carTwo.model << endl;
    // cout << carTwo.year << endl;
    // cout << carTwo.used << endl;

    Car carBis = factoryCar( "Mercedes Benz", "CLK", 1995, true );
    carInfo( carBis );
    // cout << carBis.brand << endl;
    Car carFour = factoryCar( "Lotus", "Elite", 2000, false );
    carInfo( carFour );
    // cout << carFour.brand << endl;

    return 0;
}
