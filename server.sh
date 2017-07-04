
#!/bin/bash
cmd_scrapyd="sh /home/christian/projetos/projeto_python/site_app/site_app_scraper/scrapyd.sh"
cmd_server="./manage.py runserver 127.0.0.1:8080"

$cmd_scrapyd &
$cmd_server &
