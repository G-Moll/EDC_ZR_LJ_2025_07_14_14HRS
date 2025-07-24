// switch
// Control Structures
//  Selectives Structures

#include <iostream>
using namespace std;

int main() {
    int option = -1;

    switch( option ) {
        case 10:
            cout << "Grupo extra" << endl;
            break;
        case 20:
        case 40:
            cout << "Grupo 2" << endl;
            break;
        case -1:
        case -100:
        case -10:
            cout << "Grupo Negativo" << endl;
            break;
        case 2:
        case 1:
        case 3:
            cout << "Grupo 1" << endl;
            break;
        default:
            cout << "No hay coincidencias..." << endl;
    }

    return 0;
}
