#include <iostream>
using namespace std;

bool simonSays(int a[], int b[]){
  //initializing length of accepted arrays
  int lent = sizeof(a) / sizeof(a[0]);
  //creating for loop to parse arrays; if a[i] is not equal to b[i+1] then it will break out and return false
  //in the case that every a[i] = b[i+1] it will reach end of for loop and return true
  for(int i = 0; i < lent - 1; i++){
    if(a[i] != b[i+1])
      return false;
  }
  return true;
}


int main(){
  //initializing test case arrays
  int a[] = {1, 2, 3, 4, 5};
  int b[] = {0, 1, 2, 3, 4};
  //printing if it is true or false ***figure out why it prints true and false as 1 or 0
  cout << simonSays(a, b);

}

