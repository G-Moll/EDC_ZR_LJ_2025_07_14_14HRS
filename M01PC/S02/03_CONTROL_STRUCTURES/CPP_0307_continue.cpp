#include <iostream>
using namespace std;

int main() {
    int mult = 35;
    int limit = 1000;
    
    for( int i = 1; i < limit; i++ ) {
        if( i % mult != 0 ) {
            continue;
        }
        cout << i << " es multiplo de " << mult << endl;
        cout << i << endl;
    }

    return 0;
}
