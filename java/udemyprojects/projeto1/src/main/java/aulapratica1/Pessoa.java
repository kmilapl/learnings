/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aulapratica1;

/**
 *
 * @author camilalira
 */
public class Pessoa {
    private int codigo;
    private String nome;

    public Pessoa(int codigo, String nome){
        this.codigo=codigo;
        this.nome=nome;
    }
    public String getNome(){
        return nome;
    }
}
