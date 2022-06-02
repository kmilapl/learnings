/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica2;

/**
 *
 * @author camilalira
 */
public class ClienteApp {
    
    public static void main(String[] args){
        ClientePF clientepf1 = new ClientePF("Camila Lira", "Rua das Flores 17B", "765897765412");
        ClientePJ clientepj1 = new ClientePJ("Vet FAM", "Rua Alibaba 7589", "76541029008");
        
        System.out.println("Dados da Pessoa Fisica 1: " +clientepf1.getNome() + " " +clientepf1.getEndereco() +clientepf1.getCpf());
        System.out.println("Dados da Pessoa Juridica 1: " +clientepj1.getNome() + " " +clientepj1.getEndereco() +clientepj1.getCnpj());
    }
}
