#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <float.h>
using namespace std;

double fn1(double x) {
    return pow(x, 8) - 8*pow(x, 7) + 28*pow(x, 6) - 56*pow(x,5)+70*pow(x,4)-56*pow(x, 3)+28*pow(x, 2)-8*x+1;
}
double fn2(double x) {
    return (((((((x-8)*x +28)*x - 56)*x + 70)*x-56)*x+28)*x-8)*x+1;
}
double fn3(double x) {
    return pow(x-1, 8);
}
double fn4(double x) {
    if(x==1) return 0; 
    return pow(M_E, 8*log(abs(x-1)));
}
int main() {
    ofstream file;
    file.open("double.csv");
    file << setprecision(DBL_DIG);
    file << "Function 1 \n";
    for(int i=0; i<=100; i++) {
        double x = 0.99 + i*0.0002;
        double result = fn1(x);
        file  << x << "," << result << "\n";
    }
    file << "Function 2 \n";
    for(int i=0; i<=100; i++) {
        double x = 0.99 + i*0.0002;
        double result = fn2(x);
         file << x << "," << result << "\n";
    }
    file << "Function 3 \n";
   for(int i=0; i<=100; i++) {
        double x = 0.99 + i*0.0002;
        double result = fn3(x);
        file << x << "," << result << "\n";
    }
    file << "Function 4 \n";
    for(int i=0; i<=100; i++) {
        double x = 0.99 + i*0.0002;
        double result = fn4(x);
        file << x << "," << result << "\n";
    }
    file.close();
    return 0;
}




