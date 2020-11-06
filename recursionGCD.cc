#include <iostream>
using namespace std;

int gcd(int a, int b){
  //creating basecase: if b isn't zero then the GCD can't be zero.
  //the recursion statement translates to running gcd again though with b as the first int and
  //the remainder of a/b as the second int
  if(b != 0)
    return gcd(b, a % b);
  else
    return a;
}

int main(){
  //test case
  cout << gcd(2, 6);
}


