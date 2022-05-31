package domain;
//operadores lógicos:
//&& e
//|| ou

public class HelloWorld {

    public static void main(String[] args) {
        
        //esses operadores logicos só vão ser válidos se colocar duas condições ou mais
        //&& = if só será verdadeiro se as duas condições forem verdadeiras, se uma for falsa, vai cair no else
        //|| = se uma das duas condições forem verdadeiras, cairá no if mesmo se uma das condições for falsa
        
        if(10==10 && 10<20){
            System.out.println("Verdadeiro!");
        }else{
            System.out.println("Falso!");
        }

        if(20==10 || 10<20){
            System.out.println("Verdadeiro!");
        }else{
            System.out.println("Falso!");
        }

    }

}
