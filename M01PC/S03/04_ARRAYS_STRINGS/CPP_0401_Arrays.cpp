#include <iostream>
using namespace std;

int main() {
    // Arrays (Lists)
    // - Data Structures
    // - Collections
    // - Iterables
                      // 0    1    2    3    4
    char alphabet[] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' };
    bool randomValues[] = { true, false, true, true, 1 == 1, 2 != 4 };
    int notes[] = { 8, 7, 10, 7, 9 };

    for( int i = 0; i < 12; i ++ ) {
        cout << alphabet[ i ] << endl;
    }

    cout << alphabet[ 5 ] << endl;
    return 0;
}
