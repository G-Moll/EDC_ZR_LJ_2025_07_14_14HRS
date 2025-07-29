#include <iostream>
using namespace std;

int main() {
    // 1, (50) 1000
    int counter = 1;
    int limit = 1000;
    while( counter <= limit ) {
        if( counter == 50 ) {
            cout << "Usuario mayor de edad y vive en Cuauhtémoc" << endl;
            break;
        }
        cout << counter << endl;
        counter ++;
    }

    return 0;
}
