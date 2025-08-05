#include <iostream>
#include <string>
using namespace std;

string usedInfo[ 2 ] = { "No", "Si" };

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
    cout << "Info: " <<
        "Marca: " << carData.brand <<
        ", Model0: " << carData.model <<
        ", Año: " << carData.year <<
        ", Usado: " << usedInfo[ carData.used ] << endl;
}

void carsFilter( Car* carsData, int elements ) {
    int minYear, maxYear;
    bool used;
    Car currentCar;

    cout << "BUSCANDO AUTOS:" << endl;
    cout << "Min búsqueda: ";
    cin >> minYear;
    cout << "Max búsqueda: ";
    cin >> maxYear;
    cout << "¿Busca modelos nuevos? Si(1) No(0): ";
    cin >> used;
    
    for( int i = 0; i < elements; i ++ ) {
        currentCar = carsData[ i ];
        if( currentCar.year >= minYear && currentCar.year <= maxYear && currentCar.used != used ) {
            carInfo( currentCar );
        }
    }
}

int main() {
    Car carOne = factoryCar( "Audi", "A5", 2022, true );
    Car carTwo = factoryCar( "BMW", "M5", 2020, false );
    Car carBis = factoryCar( "Mercedes Benz", "CLK", 1995, true );
    Car carFour = factoryCar( "Lotus", "Elite", 2000, false );

    Car cars[] = {
        // carOne, carTwo, carBis, carFour,
        factoryCar( "Tesla", "Model T", 2021, false ),
        factoryCar( "Dodge", "Challenger", 1999, true ),
        factoryCar( "Mitsubishi", "Lancer EVO", 1996, true ),
        factoryCar( "Subaru", "CrossTrek", 2026, false ),
        factoryCar( "Cupra", "Formentor", 2025, false ),
        factoryCar( "Chevrolet", "Corvette", 2024, false )
    };

    //                  Array 20kb             Car 4kb
    int carsElements = sizeof( cars ) / sizeof( cars[ 0 ] );
    carsFilter( cars, carsElements );

    return 0;
}
