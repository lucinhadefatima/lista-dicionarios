
#tupla
atributos = ("nome","email","profisao")
#lista de dicionario
usuarios = [
{
    atributos[0]:"fulano de tal",
    atributos[1]:"fulano@gmail.com",
    atributos[2]:"programador"
},
{
    atributos[0]:"cicrano da silva",
    atributos[1]:"cicrano@gmail.com",
    atributos[2]:"administrador"
},
{
    atributos[0]: "beltrano de souza",
    atributos[1]:"beltrano@gmail.com",
    atributos[2]:"recepicionista"
}
]
#cadastrar um novo usuario
usuario = {}
for atributo in atributos:
        usuario [atributo] = input(f"informe o valor do campo {atributo}:")
        usuarios.append(usuario)
   #exibir aos dados de cada usuario
for usuario in usuarios:
      for atributo in atributos:
            print(f"{atributo}:{usuarios.get(atributos)}.")




