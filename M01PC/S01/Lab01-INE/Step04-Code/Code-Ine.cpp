#include <iostream>
#include <thread>
#include <chrono>
using namespace std;
using namespace chrono;
using namespace this_thread;

void processingTask() {
    sleep_for( milliseconds( 1700 ) );
}

void getBallots() {
    cout << "Recibiendo boletas..." << endl;
    processingTask();
    cout << "Boletas checadas..!" << endl;
}
void chooseCandidates() {
    cout << "Escogiendo candidatos..." << endl;
    processingTask();
    cout << "Candidatos seleccionados..!" << endl;
}
void castVotes() {
    cout << "Llenar urnas..." << endl;
    processingTask();
    cout << "Urnas llenadas..!" << endl;
}
void markThumb() {
    cout << "Sellando pulgar..." << endl;
    processingTask();
    cout << "Pulgar sellado..!" << endl;
}

int main() {

    int numCasillaVotante = 10;
    int numVotante = 2010;
    int numCasillaVisitada = 10;

    if( numCasillaVotante == numCasillaVisitada && numVotante >= 1200 && numVotante <= 2500 ) {
        cout << "Si Puede votar" << endl;
        getBallots();
        chooseCandidates();
        castVotes();
        markThumb();
        cout << "Voto hecho..!" << endl;
    }
    else {
        cout << "No puede votar" << endl;
    }

    return 0;
}
