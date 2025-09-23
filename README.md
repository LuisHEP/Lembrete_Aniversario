
## 🛠️ Como Funciona

1. **Inicialização:** Ao fazer login no Windows, o script é executado automaticamente
2. **Delay:** Aguarda 5 segundos para não interferir na inicialização do sistema
3. **Verificação:** Compara a data atual com as datas de aniversário do arquivo
4. **Notificação:** Se houver aniversariantes, exibe um pop-up com os detalhes

## 🐛 Solução de Problemas

### O script não executa automaticamente
- Verifique se o atalho está na pasta de inicialização correta
- Confirme que o Python está instalado e associado a arquivos `.pyw`

### Caracteres especiais não aparecem corretamente
- Certifique-se de que o arquivo `aniversarios.txt` está salvo em UTF-8

### Notificação não aparece
- Verifique se a data do sistema está correta
- Confirme o formato das datas no arquivo (DD/MM/AAAA)
- Certifique-se de que não há espaços extras nos nomes ou datas

### Script abre uma janela do terminal
- Use o arquivo `.pyw` em vez de `.py` para executar sem terminal

## 💡 Dicas

- Mantenha o arquivo `aniversarios.txt` atualizado com novos contatos
- Use comentários (linhas começando com `#`) para organizar seus contatos
- O arquivo é simples texto, fácil de fazer backup ou migrar

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

## 🤝 Contribuições

Contribuições são bem-vindas! Se encontrar algum problema ou tiver sugestões, abra uma issue no GitHub.

---

**Desenvolvido com Python e Tkinter** 🐍
