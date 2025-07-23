// if, else if, else
// Control Structures
//  Conditional Structures

#include <iostream>
using namespace std;

int main() {
    if( 1 == 11 and 2 == 3 ) {
        cout << "Ok" << endl;
    }

    if( 1 == 1 ) {
        cout << "Ok" << endl;
    }
    else {
        cout << "No" << endl;
    }

    if( 1 == 2 ) {
        cout << "Ok (1)" << endl;
    }
    else if( 2 != 2 or 3 == 2 + 1 ) {
        cout << "Ok (2)" << endl;
    }
    else if( 3 == 3 ) {
        cout << "Ok (3)" << endl;
    }
    else {
        cout << "(Else) No" << endl;
    }

    if( 1 == 1 ) { cout << "OK" << endl; }
    if( 2 == 2 ) { cout << "OK" << endl; }
    if( 3 == 3 ) { cout << "OK" << endl; }
    if( 4 == 4 ) { cout << "OK" << endl; }
    if( 5 == 5 ) { cout << "OK" << endl; }

    return 0;
}

