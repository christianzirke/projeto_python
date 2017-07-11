/site_acoes/
  settings.py
    Arquivo de configuração do django
  urls.py
    Arquivo com as urls iniciais do sistema, todas as requisições passam por ali

/static/

/site_app/
  site_app_scraper/
    site_app_scraper/
      spiders/
        news.py
            Spider pra importar as notícias, faz uma requisição pra buscar todos
          os códigos das empresas, e recursivamente (pq achei bonitinho fazer recursivo),
          busca as notícias de uma empresa, verifica se tem alguma na lista e manda dnvo
        wiki.py
            Spider pra importar as empresas. Faz uma requisição pra pegar uma lista de
          links de wikipedia pra importar os dados. Retira (se existir) vários dados
          da tabela de infobox da wiki.
      items.py
          Define os items das spiders que contém os dados que nos interessa
      pipelines.py
          Define os(o) estágio de processamento dos items. No caso só tem 1, que
        ele identifica qual o item e faz a requisição correta
  templates/
    registration/
      login.html
          Formulário de login
      register.html
          Formulário de cadastro
    site_app/
      base.html
          Layout base do sistema, tem o header e o footer das telas internas
      company_details.html
          Template mostrando mais detalhes da empresa
      company_small_details.html
          Template pequeno pra ser replicado no dashboard
      dashboard.html
          Template principal do usuário
      wikipedia.html
          Template pequeno pra ser renderizado nos detalhes da empresa, serve pra
        formatar os dados da wiki
  templatetags/
    company_details.py
        Faz o papel do views.py pra templates internos, que não são chamados direto pelo views,
      mas precisam de um tratamento antes (manipulação dos dados)
    wikipedia.py
        Faz o papel do views.py pra templates internos, que não são chamados direto pelo views,
      mas precisam de um tratamento antes (manipulação dos dados)
  views.py
      Possui os métodos que são chamados dependendo da rota que foi acessada.
  utils.py
      Tem classes que não fazem parte do domínio do problema, mas foram uteis de
    pra resolução
  urls.py
      Define as rotas internas do app (extenção do site_app/urls.py)
  models.py
      Define os models do app
  forms.py
      Define o(os) campos de formulários do app
