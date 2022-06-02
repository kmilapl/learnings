/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica2;

/**
 *
 * @author camilalira
 * extends = clientepj HERDA da classe pai cliente
 */
public class ClientePJ extends Cliente{
    private String cnpj;
    
    public ClientePJ(String nome, String endereco, String cnpj){
        super(nome, endereco);
        this.cnpj=cnpj;
    }
    
    public String getCnpj(){
        return cnpj;
    }
    
    public void setCnpj(String cnpj){
        this.cnpj=cnpj;
    }
}
