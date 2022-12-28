<div align="center" style="text-align: center;">
  <a href="#-sobre">Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-recursos-disponiveis">Recursos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-iniciando-o-projeto">Iniciando o Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-testes">Testes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-contribuindo">Contribuindo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-autores">Autores</a>
</div>

## 🤔 Sobre

O [**PROJ3CT**](https://link) é um software de processamento Backend, que fornece **APIs** para...

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

***General***:

- [fastAPI](https://localhost)
- [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [uvicorn](https://pypi.org/project/gunicorn/)
- [python-decouple](https://github.com/henriquebastos/python-decouple/)

## ✨ Recursos Disponiveis

Os recursos disponíveis da aplicação podem ser encontrados no  [swagger](http://localhost)

## 🏃 Iniciando o Projeto

### **Sem Docker** 🖥️

Para iniciar essa aplicação sem o docker, você irá precisar de [python](https://www.python.org/), [virtualenv](https://virtualenv.pypa.io/en/latest/) instalados no seu computador.

```bash
  # Crie o python environment

  $ make virtualenv

  # Ative o environment

  $ source env/bin/activate

  # Instale as dependências

  $ make install

  # Inicie a aplicação

  $ make run

  # Para desativar a máquina virtual python (virtualenv):

  $ deactivate
```



## **Com Docker** 🐳

Para iniciar essa aplicação com docker, siga as [instruções](https://docs.docker.com/get-docker/) de instalação, em seguida utilize o comando:

```bash
  $ make compose-up
```

## 🚨 Tests
### **Rodando os Testes** ✅

```bash
  ## Para rodar os testes unitários

  $ make test
```

### **Desenvolvendo com Testes** 🔥

O time utiliza a metologia [TDD](http://localhost) para implementação de novas funcionalidades, caso não possua conhecimento, é recomendável a leitura do artigo citado.

## 💁🏻 Contribuindo

1. **Clone** o projeto:
2. Crie sua **feature**/**fix** branch seguindo o padrão e faça suas modificações:

```bash
  # Os números são obtidos na plataforma GENTI

  # feature/número da tarefa
  # fix/número do fix
  # Exemplo tarefa 103574 no GENTI

  $ git checkout -b feature/103574
```

3. Caso necessário **versione** a aplicação e adicione as informações no arquivo [CHANGELOG](./CHANGELOG.md). Nós utilizamos [Semver](https://semver.org/lang/pt-BR/) para versionamento, para verificar as versões disponíveis visualize as [tags neste respositório](void);

``` bash
  # Script encontrado na raiz do projeto para versionamento.
  # Options: [major, minor, fix & dev] [-b "descrição do release"]

  $ ./create_release.sh option
```

4. **Formate** os arquivos:
```bash
  ## Para formatar os arquivos

  $ make format
```
5. **Commit** suas modificações:

```bash
  # Padrão seguido (message downcase):
  #
  # feat: a new feature
  # fix: a bug fix
  # docs: documentation only changes
  # style: changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
  # refactor: a code change that neither fixes a bug nor adds a feature
  # perf: a code change that improves performance
  # test: adding missing or correcting existing tests
  # support: changes to the build process or auxiliary tools and libraries such
  # as documentation generation or continous integration configuration

  $ git commit -m 'feat: insert your message'
```

6. **Push** para a branch:

```bash
  $ git push origin feature/103574
```

7. Realize um **pull request** :D
8. Realize um merge local na branch master com as suas alterações, e em seguida a delete.

```bash
  $ git checkout master
  $ git merge feature/103574
  $ git branch -d feature/103574
```

## ✍️ Autores

[Melo Brothers](https://github.com/melo-brothers/)
