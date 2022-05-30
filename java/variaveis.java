package domain;
//String - textos
//Byte - números inteiros (-128 até 127)
//Int - números inteiros (-2147483648 até 2147483647)
//Long - números (-9223372036854775808 até 9223372036854775807)
//Float - números decimais (1.1234567 até 7 casas decimais)
//Double - números decimais (1.123456789 até 15 casas decimais)
//Boolean - valores booleanos (true ou false)
//Final - constante: variável que não pode ter seu valor alterado, um valor fixo

public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        //Tipo de variável - nome da variável - valor da variável
        final String NOME = "Camila Lira";
        Byte idade = 23;
        Double altura = 1.50;
        Boolean feminino = true;
        System.out.println(NOME);
        System.out.println(idade);
        System.out.println(altura);
        System.out.println(feminino);
    }

}
