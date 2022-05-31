package domain;

public class HelloWorld {

    public static void main(String[] args) {
        
    int opcoes = 3;

    switch(opcoes){

        case 1:
            System.out.println("Abra a sua conta");
            break;

        case 2:
            System.out.println("Fatura do Cartão");
            break;

        case 3:
            System.out.println("Crédito Imobiliário");
            break;

        default:
            System.out.println("Escolha alguma opção válida");

    }

    }

}
