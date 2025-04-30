#include <string>
// #include <iostream>
using namespace std;

void digitalWrite(){
}
string OUTPUT = " ";

void pinMode(int x, string y){}




void setup(){
    pinMode(13, OUTPUT);
}

void loop(){
    digitalWrite();
}




int main() {
    setup();

    while (true) {
        loop();
    }
}