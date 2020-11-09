#include <iostream>
using namespace std;

int * arrayOfMultipliers (int num, int length){
  //note cannot initialize the array of arbitrary variable "length" since the
  //array needs to be static from the compilation, although I am able to add
  //more numbers to the array than the length specified. Why?
  //Answer : while it doesn't cause compilation error, it could cause a runtime
  //error in that there could be a value already in the location of memory past
  //the alloted memory slots for the static length of the array.
  static int a[5];
  //initializing first element to num to practice writing quicker code, reducing
  //the number of times the for loop is run by one
  cout << "adding " << num << endl;
  a[0] = num;
  //for loop to fill the array with the "num" multiplied by where we are
  /////////
  //note I created a variable for each number to optimize since we both print the
  //number and place in the array.
  for(int i = 1; i < length; i++){
    int j = num * (i + 1);
    cout << "adding " << j << endl;
    a[i] = j;
  }
  //returning "a" actually returns a pointer to the first element in the array
  //////////
  //doing this requires us to dereference the pointer to access the value in
  //location. Once dereferenced, we have to run a for loop in main which
  //parses the array by adding 1 to the pointer value for each value in the array
  return a;
 }

int main(){
  //creating variables for the console and asking for input
  int length, num;
  cout << "What number?" << endl;
  cin >> num;
  cout << "How many times?" << endl;
  cin >> length;
  //setting pointer "pointerToArray" equal to the location of the array we
  //make in funtion "arrayOfMultipliers".
  int *pointerToArray = arrayOfMultipliers(num, length);
  //as mentioned in the function, we have to dereference the pointer in increasing
  //order by one since the values held in those positions are "int". 
  for(int i = 0; i < length; i++){
    cout << *(pointerToArray + i) << " ";
  }
  
  return 0;
}
