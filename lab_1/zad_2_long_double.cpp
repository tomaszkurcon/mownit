#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <float.h>
using namespace std;

long double fn1(long double x) {
    return powl(x, 8) - 8*powl(x, 7) + 28*powl(x, 6) - 56*powl(x,5)+70*powl(x,4)-56*powl(x, 3)+28*powl(x, 2)-8*x+1;
}
long double fn2(long double x) {
    return (((((((x-8)*x +28)*x - 56)*x + 70)*x-56)*x+28)*x-8)*x+1;
}
long double fn3(long double x) {
    return powl(x-1, 8);
}
long double fn4(long double x) {
    if(x==1) return 0; 
    return powl(M_E, 8*logl(abs(x-1)));
}
int main() {
    ofstream file;
    file.open("long double.csv");
    file << setprecision(LDBL_DIG);
    file << "Function 1 \n";
    for(int i=0; i<=100; i++) {
        long double x = 0.99L + i*0.0002L;
        long double result = fn1(x);
        file  << x << "," << result << "\n";
    }
    file << "Function 2 \n";
    for(int i=0; i<=100; i++) {
        long double x = 0.99L + i*0.0002L;
        long double result = fn2(x);
        file << x << "," << result << "\n";
    }
    file << "Function 3 \n";
   for(int i=0; i<=100; i++) {
        long double x = 0.99L + i*0.0002L;
        long double result = fn3(x);
        file << x << "," << result << "\n";
    }
    file << "Function 4 \n";
    for(int i=0; i<=100; i++) {
        long double x = 0.99L + i*0.0002L;
        long double result = fn4(x);
        file << x << "," << result << "\n";
    }
    file.close();
    return 0;
}


