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
  repo(user: "thiagoliof", repo: "captalys-django"){
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

Use o Git para para clonar o projeto captalys-django

```
$ git@github.com:thiagoliof/captalys-django.git
$ cd captalys-django
```

Precisamos remover o remote origin que está apontando para o github.
Vamos usar a estrutura de git do próprio heroku para fazer o deploy
```
$ git remote remove origin
```

Cria aplicação no heroku
```
$ heroku apps:create graphql-captalys
```


Configuração das variáveis de ambiente
(Estamos usando o DEBUG=True para poder usar o playground do graphQL)
```
$ heroku config:set SECRET_KEY='8m%xyej-l@1#61-4kep2$-16t!%sv$8ei03bra3@t=9e*lc*$%'

$ heroku config:set DEBUG=True

$ heroku config:set DISABLE_COLLECTSTATIC=1
```

#### Publicar aplicação
```
$ git push heroku master --force
```

#### Para visualizar a aplicação em produção
```
$ heroku open
```

