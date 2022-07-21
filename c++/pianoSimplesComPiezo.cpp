int som = 11;

int bot1 = 10;
int bot2 = 6;
int bot3 = 5;
int bot4 = 3;
int temp = 10;

void setup()
{
	pinMode(som, OUTPUT);
	pinMode(bot1, INPUT_PULLUP);
	pinMode(bot2, INPUT_PULLUP);
	pinMode(bot3, INPUT_PULLUP);
	pinMode(bot4, INPUT_PULLUP);
}

void LOOP()
{
	int buttonState1 = digitalRead(bot1);
	int buttonState2 = digitalRead(bot2);
	int buttonState3 = digitalRead(bot3);
	int buttonState4 = digitalRead(bot4);

if (buttonState1 == LOW)
{
tone(som, 300, temp);
}

if (buttonState2 == LOW)
{
tone(som, 500, temp);
}

if (buttonState3 == LOW)
{
tone(som, 700, temp);
}

if (buttonState4 == LOW)
{
tone(som, 900, temp);
}

}
