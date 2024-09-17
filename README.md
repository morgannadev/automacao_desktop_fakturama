# Descrição do projeto
Neste projeto, criamos uma automação RPA com Python e utilizando as ferramentas da BotCity que realizará busca de informações numa planilha Excel para cadastro de produtos em um sistema desktop chamado Fakturama, com apoio da visão computacional.

# Preparar o ambiente
Para executar este projeto, você deverá fazer a etapa de [pré-requisitos desta documentação](https://documentation.botcity.dev/pt/getting-started/prerequisites/), que basicamente são os itens abaixo.

## Pré-requisitos:
- [Conta BotCity](https://developers.botcity.dev/app/signup);
- [BotCity Studio SDK](https://documentation.botcity.dev/pt/getting-started/botcity-studio-sdk/);
- [Python 3.7 ou superior](https://www.python.org/downloads/);
- [Java 11 ou superior](https://www.oracle.com/java/technologies/downloads/);
- Ter uma IDE instalada, por exemplo: [Visual Studio Code](https://code.visualstudio.com/download) ou [PyCharm](https://www.jetbrains.com/pycharm/download/).

Ao instalar o BotCity Studio SDK, caso aconteça algum problema, você pode usar a ferramenta de diagnóstico para validar o que pode ter acontecido. Para acessar essa ferramenta, verifique [este link](https://documentation.botcity.dev/pt/getting-started/botcity-studio-sdk/#ferramenta-de-diagnostico) da documentação.

⚠️ Para este exemplo, vamos utilizar o [plugin BotCity Studio para Visual Studio Code](https://documentation.botcity.dev/pt/studio/vscode/). Você pode instalar seguindo as orientações da documentação. Se você for utilizar outra IDE, o desenvolvimento com visão computacional deverá ser feita seguindo [o passo-a-passo da documentação](https://documentation.botcity.dev/pt/frameworks/desktop/computer-vision/) com a ferramenta BotCity Studio.

# Antes de executar
Atenção aos passos que deverá seguir obrigatoriamente após fazer o fork e clone do projeto em seu computador.

## 01. Crie ambiente virtual (opcional)
Você pode utilizar ambiente virtual com o Python, se preferir. E para criá-lo, execute o seguinte comando:
```
python -m venv venv
```

Após a criação, é necessário ativá-lo. Para isso, execute o comando abaixo:
```
venv\Scripts\activate
```

## 02. Instale as dependências do `requirements.txt`
Para fazer a instalação das dependências do projeto, você deve executar no terminal da sua IDE o comando abaixo, a partir da pasta do projeto:
```
pip install --upgrade -r requirements.txt
```

## 03. Valide permissionamento
Para executar no seu computador ou máquina virtual, garanta que você tem permissão para rodar scripts, códigos etc.

## 04. Instale o Fakturama
Se você quiser seguir o passo com o mesmo software, você poderá fazer o download do programa pelo [site do Fakturama](https://www.fakturama.info/).

## 05. Resolução e visão computacional
O desenvolvimento deste robô foi feito em um sistema com o tema light e com uma determinada resolução. Os recortes feitos são alocados automaticamente na pasta `resources` do projeto. Dependendo do ambiente que você estiver, pode ser que seja necessário refazer os recortes, para que o algoritmo da visão computacional possa identificar os elementos.

Você pode ter mais orientações de [como resolver problemas sobre visão computacional neste artigo](https://dev.to/botcitydev/dicas-sobre-desenvolvimento-de-automacao-com-visao-computacional-1132).

# Para executar local
Você pode executar clicando no botão de play ou de execução da sua IDE favorita, ou ainda executar o comando abaixo no seu terminal:
```
python bot.py
```

# Para executar no BotCity Orquestrador
Lembre-se de seguir as orientações da [documentação](https://documentation.botcity.dev/pt/tutorials/orchestrating-your-automation/) para fazer o deploy da sua automação no Orquestrador e executar com apoio do Runner.

# Próximos passos
Há diversas possibilidades de melhorias neste projeto e deixo à disponibilidade da comunidade para explorarmos essas melhorias e implementarmos. Algumas sugestões:
- Enviar mensagem via [Slack com o plugin disponível](https://documentation.botcity.dev/pt/plugins/slack/) na documentação para avisar que o produto foi cadastrado com sucesso ou erro;
- Configurações de resolução de tela;
- Entre outros.

Fiquem à vontade de mandar sugestões e correções pelas issues do projeto.
