# Lembrete de Aniversário em Python

Um pequeno aplicativo em Python que verifica aniversários de contatos e exibe um lembrete com uma janela pop-up usando **Tkinter**. Ideal para ser executado junto com o Windows na inicialização, lembrando você dos aniversariantes do dia.

---

## Funcionalidades

* Verifica aniversários a partir de um arquivo de texto (`aniversarios.txt`).
* Mostra uma notificação pop-up com os aniversariantes do dia e suas idades.
* Cria automaticamente o arquivo `aniversarios.txt` com um exemplo caso não exista.
* Executa silenciosamente em segundo plano (sem console) usando o `.pyw`.

---

## Como usar

1. Clone o repositório ou baixe o arquivo `niver.pyw`.
2. Abra o arquivo `aniversarios.txt` e adicione os aniversários no formato:

```
Nome,DD/MM/AAAA
```

Exemplo:

```
Maria,12/06/1995
João,23/09/2000
```

3. Execute o arquivo `niver.pyw` clicando duas vezes (não abrirá console).
4. Para iniciar automaticamente com o Windows:

   * Copie o arquivo `.pyw` para a pasta `Shell:startup` do seu usuário:

     ```
     C:\Users\<SeuUsuário>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
     ```
   * Assim, ele será executado automaticamente ao iniciar o Windows.

---

## Estrutura do arquivo

* `niver.pyw`: Script principal do aplicativo.
* `aniversarios.txt`: Arquivo de dados com os aniversários dos contatos (gerado automaticamente se não existir).

---

## Requisitos

* Python 3.x
* Biblioteca padrão `tkinter` (já incluída no Python)
* Sistema operacional Windows (para inicialização automática com `.pyw`)

---

## Como funciona

1. Ao iniciar, o script cria o arquivo `aniversarios.txt` se não existir.
2. Lê os aniversários do arquivo.
3. Verifica se algum contato faz aniversário no dia atual.
4. Exibe um pop-up com os aniversariantes e suas idades.

---

## Observações

* Certifique-se de manter o arquivo `aniversarios.txt` no mesmo diretório do `niver.pyw`.
* Linhas vazias ou comentários (iniciadas com `#`) são ignoradas.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias, como adicionar notificações sonoras ou integração com calendários.
