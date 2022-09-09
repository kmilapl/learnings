def get_Idades(aTupla):
  idades = ()
  nomes = ()

  for t in aTupla:
    idades = idades + ( t[0], )
    nomes = nomes = ( t[1], )

  mais_jovem = min(idades)
  mais_velho = max(idades)
  num_pessoas = len(nomes)

  return(mais_jovem, mais_velho, num_pessoas)

relacao = ((15, 'Joana'),
          (35, 'Pedro'),
          (54, 'Claudiney'),
          (27, 'Sofia'),
          (10, 'Ana'))

(jovem, idoso, pessoas) = get_Idades( relacao )

print(jovem)
print(idoso)
print(pessoas)
