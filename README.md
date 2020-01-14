# Teste GraphQL Captalys!

Para realização desse teste foi utilizado os seguintes pacotes:

 - [ariadne](https://github.com/mirumee/ariadne)
 - [Django](https://docs.djangoproject.com/en/3.0/)
 - [requests](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html)
 - [python-decouple](https://github.com/henriquebastos/python-decouple)


## Server

O server utlizado para deploy foi o [heroku](http://www.heroku.com/)
Para acessar o o playground do graphql server acessar a [URL](http://graphql-jovito.herokuapp.com/)

## Exemplo de query

Query pra acessar os repositórios de um usuário específico:

```javascript
  {
    repos(user: "thiagoliof"){
      name,
      description
    }
  }
```

Query para acessar os detalhes de um repositório específico:

```javascript
{
  repo(user: "thiagoliof", repo: "backend"){
    name,
    full_name
  }
}
```

## Deploy para o servidor

Instalar o  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line).

caso ainda não tenha feito o login:

```
$ heroku login
```
#### Clonar o repositório

Use o Git to clone para clonar o projeto graphql-jovito

```
$ heroku git:clone -a graphql-jovito
$ cd graphql-jovito
```
#### Publicar alterações
```
git push heroku master --force
```
