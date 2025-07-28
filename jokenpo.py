from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
cores = {
    'cinza':'\033[1;37m', # pedra
    'azul':'\033[1;34m', # papel
    'roxo':'\033[1;35m', # tesoura
    'vermelho':'\033[1;31m', # pc vence
    'verde':'\033[1;32m', # jogador vence
    'amarelo':'\033[1;33m', # empate
    'azulclaro':'\033[1;36m', # JO KEN PÔ
    'reset':'\033[m' # nulo
}
pc = randint(0, 2)
chances = 0
print(f"""
Suas opções de jogada:
{cores['cinza']}[ 0 ] Para Pedra{cores['reset']}
{cores['azul']}[ 1 ] Para Papel{cores['reset']}
{cores['roxo']}[ 2 ] Para Tesoura{cores['reset']}""")
jogador = int(input(f">> Digite sua escolha: "))

# 0 = pedra
# 1 = papel
# 2 = tesoura

while True: # Executar o código sempre, até o jogador vencer
    sleep(0.5)
    print(f"{cores['azulclaro']}JO{cores['reset']}")
    sleep(0.5)
    print(f"{cores['azulclaro']}KEN{cores['reset']}")
    sleep(0.5)
    print(f"{cores['azulclaro']}PÔ{cores['reset']}")
    sleep(1)
    if jogador > 2 or jogador < 0:
        print(f"{cores['vermelho']}{jogador}{cores['reset']} não é uma opção válida. Tente novamente.")
        jogador = int(input(f">> Digite sua escolha: "))
    if pc == jogador:
        print(f"{cores['amarelo']}EMPATE! Os dois escolheram {itens[jogador]}{cores['reset']}")
        print(f"{cores['cinza']}Tente novamente!{cores['reset']}")
        jogador = int(input(f">> Digite sua escolha: "))
        chances += 1
    if pc == 0: # pc jogou pedra
        if jogador == 1:
            print(f"{cores['verde']}Parabéns, você venceu!{cores['reset']}")
            break
        elif jogador == 2:
            print(f"{cores['vermelho']}Infelizmente você perdeu.{cores['reset']} Você jogou {itens[jogador]} e o PC jogou {itens[pc]}.")
            print(f"{cores['cinza']}Tente novamente{cores['reset']}")
            jogador = int(input(f">> Digite sua escolha: "))
            chances += 1
    if pc == 1: # pc jogou papel
        if jogador == 0:
            print(f"{cores['vermelho']} Infelizmente você perdeu.{cores['reset']} Você jogou {itens[jogador]} e o PC jogou {itens[pc]}")
            print(f"{cores['cinza']}Tente novamente{cores['reset']}")
            jogador = int(input(f">> Digite sua escolha: "))
            chances += 1
        elif jogador == 2:
            print(f"{cores['verde']}Parabéns! Você venceu. {cores['reset']}")
            break
    if pc == 2: # pc jogou tesoura
        if jogador == 0:
            print(f"{cores['verde']}Parabéns, você venceu!{cores['reset']}")
            break
        if jogador == 1:
            print(f"{cores['vermelho']}Infelizmente você perdeu. Você jogou {itens[jogador]} e o PC jogou {itens[pc]}")
            print(f"{cores['cinza']}Tente novamente{cores['reset']}", end=' ')
            jogador = int(input(f">> Digite sua escolha: "))
            chances += 1
if chances == 0:
    print(f"Caramba! Você {cores['azulclaro']}acertou de primeira{cores['reset']}!")
elif chances == 1:
    print(f"Foi necessária somente {cores['azulclaro']}uma chance{cores['reset']} para você acertar, parabéns.")
else:
    print(f"Você precisou de {cores['azulclaro']}{chances} chances{cores['reset']} para acertar.")
