# 🪨 Pedra, Papel e Tesoura (Jokenpô) - Python

Um simples jogo de Pedra, Papel e Tesoura feito em Python, com animação estilo "JO-KEN-PÔ" e colorido no terminal. O objetivo é vencer o computador — o jogo continua até que o jogador ganhe.

---

## 🎮 Como funciona

O jogador escolhe uma opção (Pedra, Papel ou Tesoura) e o computador escolhe aleatoriamente. O jogo exibe:

- Animação "JO-KEN-PÔ"
- Resultado da rodada
- Quantas tentativas foram necessárias até a vitória do jogador

O terminal é colorido para uma melhor experiência visual.

---

## 📌 Regras

- Pedra ganha de Tesoura  
- Papel ganha de Pedra  
- Tesoura ganha de Papel  
- Empates reiniciam a rodada

---

## 💻 Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe o arquivo `jokenpo.py` (ou clone o repositório).
3. Execute com:

```bash
python jokenpo.py
```

---

## 📦 Requisitos

- Python 3.x
- Terminal com suporte a **códigos ANSI** (para cores)

---

## 🧠 Lógica do código

- Usa `randint` para escolher a jogada do computador.
- Usa `input()` para ler a jogada do jogador.
- Usa `sleep()` para criar a animação "JO-KEN-PÔ".
- Um loop `while True` garante que o jogo continue até a vitória.
- Variável `chances` conta quantas tentativas foram feitas.

---

## 🎨 Cores no terminal

As cores são definidas usando códigos ANSI:

- ⚪ Pedra: Branco
- 🔵 Papel: Azul
- 🟣 Tesoura: Roxo
- 🟥 Derrota: Vermelho
- 🟩 Vitória: Verde
- 🟡 Empate: Amarelo
- 🔹 Animação: Ciano
- ⬛ Reset: Padrão

---

## 📁 Estrutura

```
jokenpo/
│
├── jokenpo.py       # Código-fonte do jogo
└── README.md        # Este arquivo
```

---

## 🤖 Exemplo de gameplay

```
Suas opções de jogada:
[ 0 ] Para Pedra
[ 1 ] Para Papel
[ 2 ] Para Tesoura
>> Digite sua escolha: 1
JO
KEN
PÔ
EMPATE! Os dois escolheram Papel
Tente novamente!
...
Parabéns, você venceu!
Você precisou de 3 chances para acertar.
```

---

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---

## 🧑‍💻 Autor

Desenvolvido por **lywsmic**
