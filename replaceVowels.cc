#include <iostream>
//including string library
#include <string>
using namespace std;


string vowelReplace(string phrase, char vowel){
  //for loop that parses the phrase
  for(int i = 0; i < phrase.length(); i++){
    //if statement for checking to see if char at i is a vowel
    if(phrase.at(i) == 'a' || phrase.at(i) == 'e' || phrase.at(i) == 'i' || phrase.at(i) == 'o' || phrase.at(i) == 'u' ){
      //changing char at i to the vowel we want
      phrase.at(i) = vowel;
    }
  }
  //returning phrase after all vowels are replaced with the one we want
  return phrase;
}


int main(){
  //test case
  cout << vowelReplace("apples and bananas", 'u');

}
