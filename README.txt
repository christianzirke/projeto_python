PACOTES (Podem não ser todos, não lembro de todos :( ):
  - scrapyd
  - python-scrapyd-api
  - googlefinance
  - wikipedia
  - pandas-datareader

Antes de fazer o makemigrations:
  - Comentar a linha 53 do urls.py, pra ele não começar a importar os dados (O django executa o server quando faz migração)
  - python manage.py makemigrations
  - python manage.py migrate
  - Descomentar a linha

Antes de rodar o servidor, verificar:
  - Porta no settings.py ta certa?
  - Postgresql tá rodando?
  - apaga a pasta dbs dentro do scraper
  - Coloca pra rodar o scrapyd na pasta do scraper no site_app

Agora sim dale no runserver
