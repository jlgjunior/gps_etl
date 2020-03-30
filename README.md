# gps_etl

Processa dados dos arquivos na pasta dataSrc pegando informações de um GPS dos pontos para descobrir a localização a qual se referem,
<br/>
<br/>
Para descobrir a locallzação é utilizada a API do google maps e os dados são armazenados em uma base chamada gps_etl_dev que deve ser criada no postgres (com acesso de um usuário com nome application e senha application).
<br/><br/
Para inicializar a base de dados com as tabelas, é necessário rodar os comandos:
<br/>
python3 manage.py db init
<br/>
python3 manage.py db migrate
<br/>
python3 manage.py db upgrade

<br/>
<br/>

Após isso é necessário apenas rodar o comando:
<br/>
python3 ETL.py
<br/>
<br/>
Para modificações futuras seria possível reunir informações sobre o tipo de local, quando vem ao caso, bem como a menor distância entre o ponto de partida do GPS até a direção desejada (também poderia se verificar o destino final utilizando o bearing com a API do google maps).

