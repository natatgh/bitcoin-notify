
# Bitcoin Notify

Bitcoin Notify é uma aplicação Python projetada para notificar os usuários sobre mudanças nos preços do Bitcoin. A aplicação é compilada em um executável usando PyInstaller e utiliza o módulo `plyer` para notificações.

## Estrutura do Projeto

```
bitcoin_notify/
│
├── __pycache__/
├── build/
├── dist/
│   ├── bitcoin_notify/
│   │   ├── _internal/
│   │   └── bitcoin_notify.exe
├── src/
├── bitcoin_notify.py
├── bitcoin_notify.spec
└── hook-plyer.py
```

### Pastas e Arquivos

- **__pycache__/**: Contém arquivos de bytecode Python.
- **build/**: Diretório onde o PyInstaller armazena arquivos temporários durante o processo de construção.
- **dist/**: Diretório onde o executável standalone e os arquivos associados são armazenados.
  - **bitcoin_notify/**: Contém o executável compilado e arquivos internos.
  - **bitcoin_notify.exe**: O executável standalone da aplicação Bitcoin Notify.
- **src/**: Diretório para código-fonte (se aplicável, atualmente vazio).
- **bitcoin_notify.py**: O script Python principal para a aplicação Bitcoin Notify.
- **bitcoin_notify.spec**: O arquivo de especificação do PyInstaller para construir o executável.
- **hook-plyer.py**: Arquivo de hook para integrar o módulo `plyer` com o PyInstaller.

## Pré-requisitos

Para executar ou construir a aplicação a partir do código-fonte, você precisará de:

- Python 3.6 ou superior
- PyInstaller
- plyer

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seuusuario/bitcoin_notify.git
   cd bitcoin_notify
   ```

2. Instale as dependências necessárias:
   ```sh
   pip install -r requirements.txt
   ```

## Construindo o Executável

Para construir o executável, execute o seguinte comando:
```sh
pyinstaller --onefile --additional-hooks-dir=. bitcoin_notify.spec
```

O executável será criado no diretório `dist/bitcoin_notify/`.

## Uso

Para executar a aplicação a partir do código-fonte:
```sh
python bitcoin_notify.py
```

Para executar o executável standalone:
```sh
./dist/bitcoin_notify/bitcoin_notify.exe
```

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- [plyer](https://github.com/kivy/plyer) pelo suporte a notificações
- [PyInstaller](https://www.pyinstaller.org/) por construir o executável standalone

## Contato

Para mais informações, entre em contato com Natã Alexandre da Silva em [natatgh@gmail.com].
