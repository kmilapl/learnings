/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica4;

/**
 *
 * @author camilalira
 */
public class ClienteApp {
    
    public static void main(String[] args){
        ClientePF clientepf1 = new ClientePF("Camila Lira", "Rua das Flores 17B", "765897765412");
        ClientePJ clientepj1 = new ClientePJ("Vet FAM", "Rua Alibaba 7589", "76541029008");
        
        System.out.println(clientepf1.toString());
        System.out.println(clientepj1.toString());
    }
}