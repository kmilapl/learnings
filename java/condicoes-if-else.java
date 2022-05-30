package domain;

public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        //a condição if só executa se for verdadeira, se for falsa ela não executa
        //usamos o else para "senão", pois se o if for falso, ele irá executar o else
        //usamos o else if para inserir mais uma condição antes de cair no else
        
            if(false){
                System.out.println("Verdadeiro");
            }else{
                System.out.println("Falso");

            }
            
        //teste:
            int idade = 18;
            
            if(idade >= 18){
                System.out.println("Pode entrar");
            }else if(idade >= 16){
                System.out.println("Entrada permitida somente com acompanhante maior de idade!");
            }else{
                System.out.println("Muito novo! Não pode entrar.");
            }

    }

}
