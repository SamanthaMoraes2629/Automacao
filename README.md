# Automacao
 Este script automatiza o processo de login em um site, e preenchimento de formulários com dados extraídos de um arquivo CSV, utilizando as bibliotecas PyAutoGUI, PyGetWindow e Pandas. O código é projetado para facilitar o preenchimento de informações de produtos em um formulário web de forma eficiente e repetitiva.

# Requisitos

Antes de executar o script, certifique-se de ter instaladas as seguintes bibliotecas:
> pip install pyautogui pygetwindow pandas

# Como Funciona

O script segue os seguintes passos:

- Abre o Google Chrome usando pyautogui.
- Verifica se a janela do Chrome está maximizada e a maximiza se necessário.
- Acessa o site de login https://dlp.hashtagtreinamentos.com/python/intensivao/login.
- Insere as credenciais de login.
- Lê a tabela de produtos do arquivo produtos.csv.
Para cada linha da tabela:

- Preenche os campos do formulário na página.
- Avança para o próximo produto.
- Faz o envio dos dados.
- Realiza o scroll para garantir a visibilidade dos campos.

# Estrutura do CSV

O arquivo produtos.csv deve conter as seguintes colunas:

- Código
- Marca
- Tipo
- Categoria
- Preço Unitário
- Custo
- Observação

# Observações

- Os valores x, y utilizados em pyautogui.click(x, y) podem precisar de ajustes conforme a resolução e a interface do usuário.

- O tempo de espera (time.sleep) pode precisar de ajustes conforme a velocidade da conexão e da máquina.

- O script pressiona tab para navegar entre os campos e enter para enviar os dados.

#Executando o Script

Para executar o script, utilize:
> python main.py
Certifique-se de que o Google Chrome está instalado e configurado corretamente.

Este projeto foi criado para fins educacionais e pode ser adaptado para outras necessidades de automação de tarefas repetitivas.
