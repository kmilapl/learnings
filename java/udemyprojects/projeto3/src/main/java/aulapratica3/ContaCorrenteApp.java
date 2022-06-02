/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica3;

/**
 *
 * @author camilalira
 * Sobrecarga = flexibiliza o codigo, permite que instancie o objeto de N formas
 */
public class ContaCorrenteApp {
    public static void main(String[] args){
        
        ContaCorrente contacomum = new ContaCorrente(123, 555);
        ContaCorrente contaespecial = new ContaCorrente (123, 890, 10000.00f);
    }
    
}
