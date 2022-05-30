package domain;
/*
== operador igual
< operador menor
> operador maior
<= operador menor ou igual
>= operador maior ou igual
!= operador diferente
*/

public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
            //== operador igual
        String nome1 = "Camila";
        String nome2 = "Amanda";
        String nome3 = "Camila";
        
        System.out.println(nome1 == nome2);
        System.out.println(nome1 == nome3);
        
        //< operador menor
        int numero1 = 30;
        int numero2 = 5;
        
        System.out.println(numero1 < numero2);
        
        //> operador maior
        System.out.println(numero1 > numero2);
        
        //<= operador menor ou igual
        System.out.println(numero1 <= numero2);
        System.out.println(numero2 <= numero1);
        
        //>= operador maior ou igual
        System.out.println(numero1 >= numero2);
        System.out.println(numero2 >= numero1);
        
        //!= operador diferente
        System.out.println(numero1 != numero2);
        System.out.println(nome1 != nome2);

    }

}
