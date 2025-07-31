#include <iostream>
using namespace std;
// Declare
void sumVoid() {
    // int x = 1 + 2;
    cout << ( 1 + 2 ) << endl;
}

int sumInt() {
    int result = 2 + 3;
    return result;
}

//                  10           -10
//              Parameters
int sumValues( int numOne, int numTwo ) {
    int result = numOne + numTwo;
    return result;
}

bool sumCheck( int numOne, int numTwo ) {
    int result = numOne + numTwo;
    if( result < 0 ) {
        return false;
    }
    else {
        return true;
    }
}


int main() {
    // Run, Evaluate, Call, Invoke
    // cout << sumVoid() << endl;
    // int z = sumInt();
    //                 Arguments
    int m = sumValues( 10, -10 );
    int l = sumValues( 20, -10 );
    int o = sumValues( 110, 200 );

    bool isPositive = sumCheck( 10, 20 );
    cout << isPositive << endl;



    // int c = sumValues( sumValues( 2000, 50 ), sumValues( sumValues( 1, 115 ), 12 ) );
    // cout << c << endl;




    // cout << m << endl;
    // cout << l << endl;
    // cout << o << endl;
    return 0;
}
