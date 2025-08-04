import requests

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        nome = dados["name"].capitalize()
        numero = dados["id"]
        tipo = [tipo["type"]["name"].capitalize() for tipo in dados["types"]]
        altura = dados["height"] / 10 # vem em decímetros
        peso = dados["weight"] / 10   # vem em hectogramas
        habilidades = [h["ability"]["name"].capitalize() for h in dados["abilities"]]
        imagem = dados["sprites"]["front_default"]


        print(f"\n Nome: {nome}")
        print(f" Número: {numero}")
        print(f" Tipo(s): {', '.join(tipo)}")
        print(f" Altura: {altura} m")
        print(f" Peso: {peso} kg")
        print(f" Habilidades: {", ".join(habilidades)}")
        print(f" Imagem: {imagem}")

    else:
        print("\n Pokémon não encontrado. Verifique o nome e tente novamente.")

# Interface simples no terminal
while True:
    nome_pokemon = input("\nDigite o nome ou número do Pokémon (ou 'sair'): ")
    if nome_pokemon == "sair":
        break
    buscar_pokemon(nome_pokemon)





