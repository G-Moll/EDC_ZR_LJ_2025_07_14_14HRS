#include <iostream>
using namespace std;

int main() {
    // > >= < >= == != (true 1/false 0)
    int a = 10;
    int m = 3;
    int z = 8;

    // and
    cout << ( a == z and m != a ) << endl;
    //          0          1
    cout << ( 1 == 1 and 1 != 0 ) << endl;
    //          1          1
    cout << ( 1 == 2 and 1 != 1 ) << endl;
    //          0          0

    // or
    cout << ( a == z or m != a ) << endl;
    //          0          1
    cout << ( 1 == 1 or 1 != 0 ) << endl;
    //          1          1
    cout << ( 1 == 2 or 1 != 1 ) << endl;
    //          0          0

    // Not !
    cout << ( true ) << endl;
    cout << ( !true ) << endl;
    cout << ( !!true ) << endl;

    return 0;
}
