int red = 13; 
int green = 8; 
int orange = 4; 
int blue = 2; 

int m1 = 3; 
int m2 = 5; 
int m3 = 3 * 5; 

int maxValue = 40; 
int i = 1; 

void setup() 
{ 
  pinMode(red, OUTPUT); 
  pinMode(green, OUTPUT); 
  pinMode(orange, OUTPUT); 
  pinMode(blue, OUTPUT); 
} 

void loop() 
{ 
  if ((i % m3) == 0) // FizzBuzz 
  { 
    digitalWrite (red, HIGH); 
    delay(500); 
    digitalWrite (red, LOW); 
    delay(500); 
  } 
  
  else if ((i % m1) == 0) // Fizz 
  { 
    digitalWrite(green, HIGH); 
    delay(500); 
    digitalWrite(green, LOW); 
    delay(500); 
  }
  else if ((i % m2) == 0) // Buzz 
  { 
    digitalWrite(orange, HIGH); 
    delay(500); 
    digitalWrite(orange, LOW); 
    delay(500); 
  } 
  
  else // Não é multiplo de nenhum 
  { 
    digitalWrite(blue, HIGH); 
    delay (500); 
    digitalWrite(blue, LOW); 
    delay (500); 
  } 
  
  i++; 

}
