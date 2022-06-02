/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica4;

/**
 *
 * @author camilalira
 * tostring = retorna todas os atributos de uma só vez
 */
public class Cliente {
    
    private String nome;
    private String endereco;
    
    public Cliente(String nome, String endereco){
        this.nome=nome;
        this.endereco=endereco;
    }
    
    public String getNome(){
        return nome;
    }
    
    public String getEndereco(){
        return endereco;
    }
    
    public void setNome(String nome){
        this.nome=nome;
    }
    
    public void setEndereco(String endereco){
        this.endereco=endereco;
    }
    
    public String toString(){
        return "nome: " +nome + "endereço: " +endereco;
    }
}