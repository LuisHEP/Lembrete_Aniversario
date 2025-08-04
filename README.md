# 🎉 Lembrete de Aniversários Automático — `niver.py`

Este é um pequeno utilitário em Python que verifica diariamente se algum contato faz aniversário no dia atual e exibe uma notificação pop-up com os aniversariantes. O script é configurado para iniciar automaticamente junto com o Windows.

## 🧩 Funcionalidades

- Verifica aniversários com base em um arquivo de texto (`aniversarios.txt`).
- Exibe uma notificação do sistema com o nome, idade e ano de nascimento dos aniversariantes.
- Cria automaticamente o arquivo de aniversariados caso não exista.
- Adiciona o script à pasta de inicialização do Windows (`Startup`), garantindo que ele seja executado a cada reinicialização do computador.

## 📁 Estrutura do Projeto

```bash
📁 niver/
 ┣ 📄 niver.py
 ┗ 📄 aniversarios.txt  ← gerado automaticamente, se não existir
```

## 🛠️ Requisitos

- Python 3.x
- Sistema Operacional: **Windows**
- Biblioteca padrão do Python (`tkinter`, `os`, `sys`, `datetime`) — já inclusas

## 🚀 Como Usar

1. **Clone o repositório ou baixe o `niver.py`:**
   ```bash
   git clone https://github.com/seu-usuario/niver.git
   ```

2. **Execute o script uma vez:**
   ```bash
   python niver.py
   ```

   - Isso irá:
     - Criar o arquivo `aniversarios.txt` (se não existir);
     - Adicionar um atalho `.bat` à pasta de inicialização do Windows para que o script rode automaticamente ao iniciar o sistema;
     - Exibir um aviso caso existam aniversariantes hoje.

3. **Edite o arquivo `aniversarios.txt`:**

   Use qualquer editor de texto para adicionar aniversários no seguinte formato:

   ```
   # Formato: Nome,DD/MM/AAAA
   Maria Silva,12/08/1998
   João Souza,04/11/2000
   ```

## 📌 Observações

- O script **não envia e-mails** nem salva dados em nuvem. Toda informação permanece local.
- O aviso só aparece se houver aniversariantes no dia atual.
- A pasta de inicialização do Windows utilizada é:
  ```
  C:\Users\SeuUsuario\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
  ```

## 🧼 Como Remover da Inicialização

Para impedir que o script seja executado automaticamente com o Windows, basta deletar o arquivo:

```
niver_startup.bat
```

que estará dentro da pasta `Startup` mencionada acima.

## 📃 Licença

Este projeto é de uso livre. Sinta-se à vontade para modificar e distribuir.

## 🙋‍♂️ Autor

Desenvolvido por **Luis Paladino**
