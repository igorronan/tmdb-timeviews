# TMDB - Series e Filmes já assistidos

Este projeto tem como objetivo dar visibilidade dos filmes e series já vistos e que foram catalogados no site TMDB.
Levamos em consideração a sua lista de avaliações neste site para trazer a listagem já visualizada e também contabilizar o tempo total já gasto na frente da telinha.

## Preparando Ambiente

* Python 3
        - https://www.python.org/downloads/


## Preparando Integração

* Cadastro no themoviedb.org
        - Após cadastro no site, acessar o menu Configurações > API e pegar sua chave v3 auth;


## Modo de uso

* Editar o arquivo tmdb.py para alterar as variaveis de Key, Username e Password;
* Executar o arquivo tmdb.py no terminal (python3 tmdb.py)

## Saidas

* Irá ser emitido duas saidas, uma visual para ir conferindo em tempo de execução e uma em arquivo com os detalhes e os resumos.

```sh
    RELATORIO FINAL
    - Duration: 			0:04:49.309173
    - Tempo Assistido: 		217 Dias 7 Hrs 22 Min
    - Total de Filmes: 		920
    - Total de Series: 		80 
    - Total de Episodios: 	5720 

    LISTA GERAL
    TIPO: 	TEMPO 	VOTO|MEDIA 	TITULO TEMPORADA EPISODIOS
    movie: 	00:04 	08.0|06.1 	Ms. Marvel: Guia Para Fãs 
    movie: 	02:02 	08.0|07.7 	Sonic 2: O Filme 
    movie: 	02:28 	08.0|06.7 	Matrix Resurrections 
    [...]
    tv: 	73:00 	09.0|08.4 	Game of Thrones | Sessions: 8 Episodes: 73
    tv: 	23:15 	08.0|05.9 	C.S.I.: Cyber | Sessions: 2 Episodes: 31
    tv: 	32:15 	09.0|08.2 	Mr. Robot | Sessions: 4 Episodes: 45
    tv: 	05:50 	08.0|08.6 	Chernobyl | Sessions: 1 Episodes: 5
    tv: 	76:40 	08.0|08.1 	Fronteiras | Sessions: 5 Episodes: 100
```