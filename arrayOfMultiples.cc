#include <iostream>
#include <array>
using namespace std;

int[] arrayOfMultiplers (int num, int length){
  int[length]  a = {0};
  int multiplier = 1;
  for(int i = 0; i < length; i++){
    a[i] = num * multiplier;
    multiplier++;
  }

  return a;
 }

int main(){
  cout << arrayOfMultipliers(7, 5);
  

}
