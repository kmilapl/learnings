/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica2;

/**
 *
 * @author camilalira
 */
public class ClientePF extends Cliente{
    
    private String cpf;
    
    public ClientePF(String nome, String endereco, String cpf){
        super(nome, endereco);
        this.cpf=cpf;
    }
    
    public String getCpf(){
        return cpf;
    }
    
    public void setCpf(String cpf){
        this.cpf=cpf;
    }
}
