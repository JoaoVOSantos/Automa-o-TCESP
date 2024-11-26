
# 🐍 Automação com Selenium - Geração de Certificados no TCE-SP

Este projeto é uma automação em Python que utiliza **Selenium WebDriver** para acessar o portal do TCE-SP, fazer login com credenciais fornecidas, gerar certificados de atualização cadastral e baixá-los automaticamente para um diretório predefinido no sistema.

---

## 🚀 Funcionalidades

- Login automático no portal do TCE-SP com múltiplos usuários.
- Navegação até a página de cadastro e geração do certificado.
- Download automático do certificado no diretório de downloads padrão.
- Logout automático após o processamento.

---

## 🛠️ Instalação e Configuração

Siga os passos abaixo para configurar o ambiente e gerar o executável.

### 1. **Pré-requisitos**

Certifique-se de que você possui os seguintes itens instalados no sistema:

- **Python 3.8+**: [Baixe aqui](https://www.python.org/downloads/)
- **Google Chrome**: [Baixe aqui](https://www.google.com/intl/pt-BR/chrome/)
- **ChromeDriver**: [Baixe aqui](https://chromedriver.chromium.org/downloads) (a versão deve ser compatível com a do navegador Chrome instalado).

### 2. **Clonar ou Obter o Código**

Baixe o código-fonte do projeto ou clone o repositório no diretório desejado:

```bash
git clone https://github.com/JoaoVOSantos/Automa-o-TCESP.git
cd selenium-tce-sp
```

### 3. **Instalar Dependências**

Instale as bibliotecas necessárias com o **pip**:

```bash
pip install selenium
```

### 4. **Adicionar o ChromeDriver ao Diretório**

- Baixe o arquivo `chromedriver.exe` compatível com a versão do Chrome instalado.
- Copie o arquivo para o mesmo diretório onde está o script Python.

### 5. **Gerar o Executável**

Para facilitar a utilização, você pode criar um executável do script usando o **PyInstaller**. Instale o PyInstaller:

```bash
pip install pyinstaller
```

Gere o executável com o comando:

```bash
pyinstaller --onefile --noconsole --add-data "chromedriver.exe;." nome_do_script.py
```

Isso criará um executável na pasta `dist`.

---

## 🖥️ Como Usar

1. **Mover o Executável**
   - Copie o arquivo `.exe` gerado na pasta `dist` para o diretório onde será executado.

2. **Executar o Programa**
   - Execute o `.exe` com um duplo clique. O programa irá:
     - Solicitar as credenciais de login.
     - Acessar o portal do TCE-SP.
     - Gerar os certificados automaticamente.
     - Salvar os certificados no diretório padrão de downloads.

3. **Observação**
   - Caso o diretório padrão de downloads não exista, o arquivo será salvo no mesmo local onde está o executável.

---

## 📂 Estrutura de Diretórios

- `nome_do_script.py`: Código-fonte principal do projeto.
- `chromedriver.exe`: Driver do navegador Chrome.
- `dist/`: Diretório onde o executável será gerado.

---

## 📝 Notas Importantes

- **Atenção**: Certifique-se de que as credenciais de login fornecidas no script são válidas.
- **Melhorias**: Adicione tratamento para possíveis erros de conexão ou mudanças no layout do portal TCE-SP.
- **Diretório de Downloads**: Verifique se você possui permissões de gravação na pasta `Downloads` ou no diretório alternativo especificado.

---

## 📅 Feito por João Vitor em uma segunda/terça qualquer

Obrigado por usar este projeto! 😄
