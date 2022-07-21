int pins[] = {2, 3, 4, 5, 6, 7}; 
int i = 0; 
int t = 50; 

void setup() 
{ 
  for (i=0; i<6; i++) 
  { 
    pinMode(pins[i], OUTPUT); 
  } 
} 

void loop() 
{ 
  for (i=0; i<6; i++)
  { 
    digitalWrite(pins[i], HIGH); 
    delay(t); 
    digitalWrite(pins[i], LOW); 
    delay(t); 
  } 
  for (i=5; i>=0; i--) 
  { 
    digitalWrite(pins[i], HIGH); 
    delay(t); 
    digitalWrite(pins[i], LOW); 
    delay(t); 
  } 
}
