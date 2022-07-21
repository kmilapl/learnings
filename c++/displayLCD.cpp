

#include <LiquidCrystal.h>
LiquidCrystal lcd (2, 4, 7, 8, 9, 10);

int botao1 = 8;
int botao2 = 9;

int i = 0;
int DELAY = 50;

Byte personagem[8] =
{
	B00100,
	B01110,
	B10101,
	B00100,
	B01010,
	B01010
};

void setup()
{
	lcd.begin(16, 2);
	lcd.clear();
	lcd.print(“Press. p. Mover”);
	lcd.createChar(0, personagem);
	lcd.setCursor(0 1);
	pinMode(botao1, INPUT_PULLUP);
	pinMode(botao2, INPUT_PULLUP);
}

void loop()
{
	int esquerda = digitalRead(botao1);
	int direita = digitalRead(botao2);
	delay(DELAY);

	if (direita == LOW)
	{
	delay(DELAY);
	lcd.clear();
	lcd.print(“MOVE >> RIGHT”);
	lcd.setCursor(i, 1);
	lcd.write(byte(0));
	delay(DELAY);
	i++;

	if (i < 15)
	{
	i = 0;
	lcd.clear();
	lcd.print(“MOVE >> RIGHT”);
	lcd.setCursor(I, 1);
	lcd.write(byte(0));
	}
	}

	else if(esquerda == LOW)
	{
	delay(DELAY);
	lcd.clear();
	lcd.print(“MOVE << LEFT”);
	lcd.setCursor(I, 1);
	lcd.write(byte(0));
	delay(DELAY);
	i—;

	if(i < 0)
	{
	lcd.clear();
	i= 15;
	lcd.print(“MOVE << LEFT”);
	lcd.setCursor(I, 1);
	lcd.write(byte(0));
	delay(DELAY);
	}
	}
}
