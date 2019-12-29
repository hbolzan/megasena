#!/usr/bin/python3
import functools
import copy
import psycopg2

quantidade_de_dezenas = 6
maior_dezena = 60
sql_base = "insert into todos_os_jogos(d1, d2, d3, d4, d5, d6) values({}, {}, {}, {}, {}, {});"

def incrementar_a_partir_da_dezena(jogos, jogo, n, conn, cursor):
    for d in range(jogo[n-7] + 1, maior_dezena + 1):
        novo_jogo = copy.copy(jogo)
        novo_jogo[n-7] = d
        if n < quantidade_de_dezenas:
            novo_jogo[n-7+1] = d
            jogos = incrementar_a_partir_da_dezena(jogos, novo_jogo, n+1, conn, cursor)
        else:
            # jogos.append(novo_jogo)
            persistir_jogo(conn, cursor, novo_jogo)
            print(novo_jogo)
            jogos = incrementar_a_partir_da_dezena(jogos, novo_jogo, n, conn, cursor)
            return jogos
    return jogos


def do_jeito_bizarro():
    conn = connection()
    cursor = conn.cursor()
    jogos = [[1, 2, 3, 4, 5, 6]]
    print([1, 2, 3, 4, 5, 6])
    persistir_jogo(conn, cursor, [1, 2, 3, 4, 5, 6])
    for n in range(1, quantidade_de_dezenas+1):
        jogos = incrementar_a_partir_da_dezena(jogos, [1, 2, 3, 4, 5, 6], quantidade_de_dezenas+1-n, conn, cursor)
    cursor.close()
    conn.close()


def persistir_jogo(conn, cursor, jogo):
    sql = sql_base.format(jogo[0], jogo[1], jogo[2], jogo[3], jogo[4], jogo[5])
    cursor.execute(sql)
    conn.commit()


def connection():
    return psycopg2.connect(**get_db_params())


def get_db_params():
    return {
        'dbname': 'megasena',
        'user': 'postgres',
        'password': 'MiniPCP',
        'host': 'localhost',
        'port': '5432',
    }

do_jeito_bizarro()

# 5502 0910 2361 8383
# 284
# 07/21
