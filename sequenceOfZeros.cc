#include <iostream>
#include <cstring>
using namespace std;

//creating function to return longest sequence of zeros
string longestSequenceOfZeros(string str){
  //variable for keeping track of how many zeros is the longest
  int longest = 0;
  //variable for keeping track of how long the current string of zeros is
  int current = 0;
  //loop for traversing the string
  for(int i = 0; i < str.length(); i++){
    //checking to see if character we are at is a zero, then incrementing current count by 1
    if(str[i] == '0'){
      current++;
    //if not zero then we check to see if the length of zeros is the biggest at i. If so, we update with new length
    }
    else{
      if(current > longest && current != 0){
	longest = current;
	current = 0;
      }
    }
   
      
  }
  //if statement checking to see if there was in fact at least one zero, if not returning ""
  if(longest > 0){
    //creating string to be returned
    string howMany = "";
    //filling string with the amount of zeros we need
    for(int i = 0; i < longest; i++){
      howMany[i] = '0';
    }
    for(int i = 0; i < longest; i++){
      cout << howMany[i];
    }
    cout << endl;
    return howMany;
  }
  else{
    cout << "" << endl;
    return "";
  }
}

int main(){
  longestSequenceOfZeros("01100001011000");
  longestSequenceOfZeros("100100100");
  longestSequenceOfZeros("111111111");

}
