/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica1;

/**
 *
 * @author camilalira
 * Encapsulamento é o mecanismo utilizado com o objetivo de esconder detalhes de implementação das classes.
 * Uma classe deve impedir o acesso direto aos seus atributos e métodos internos e disponibilizar métodos pülibcos.
 */
public class PessoaApp {
    
    public static void main(String [] args){
        Pessoa pessoa1 = new Pessoa(1, "Camila");
        Pessoa pessoa2 = new Pessoa(2, "Ana");
        
        
        System.out.println("o nome da Pessoa 1 é: " +pessoa1.getNome());
    }
}
