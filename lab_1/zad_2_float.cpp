#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <float.h>
using namespace std;

float fn1(float x) {
    return powf(x, 8) - 8*powf(x, 7) + 28*powf(x, 6) - 56*powf(x,5)+70*powf(x,4)-56*powf(x, 3)+28*powf(x, 2)-8*x+1;
}
float fn2(float x) {
    return (((((((x-8)*x +28)*x - 56)*x + 70)*x-56)*x+28)*x-8)*x+1;
}
float fn3(float x) {
    return powf(x-1, 8);
}
float fn4(float x) {
    if(x==1) return 0; 
    return powf(M_E, 8*logf(abs(x-1)));
}
int main() {
    ofstream file;
    file.open("float.csv");
    file << setprecision(FLT_DIG);
    file << "Function 1 \n";
    for(int i=0; i<=100; i++) {
        float x =  0.99f + i*0.0002f;
        float result = fn1(x);
        file << x << "," << result << "\n";
    }
    file << "Function 2 \n";
    for(int i=0; i<=100; i++) {
        float x = 0.99f + i*0.0002f;
        float result = fn2(x);
         file << x << "," << result << "\n";
    }
    file << "Function 3 \n";
   for(int i=0; i<=100; i++) {
        float x = 0.99f + i*0.0002f;
        float result = fn3(x);
        file << x << "," << result << "\n";
    }
    file << "Function 4 \n";
    for(int i=0; i<=100; i++) {
        float x = 0.99f + i*0.0002f;
        float result = fn4(x);
        file << x << "," << result << "\n";
    }
    file.close();
    return 0;
}


