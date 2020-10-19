#!/usr/bin/env python
# -*- coding: utf-8 -*-
###coding: utf-8 の部分は、書類のコーディングに依存する
###ファイル(F)->保存オプションの詳細設定(V)...
###で書類のコーディングが変更可能
###この場合「Unicode(UTF-8シグネチャなし)-コードページ65001」
###SHIFT-JISの場合はcp932
import pypyodbc

def pypy():
    cnn = pypyodbc.connect('DRIVER={FileMaker ODBC};SERVER=192.168.0.171;PORT=2399;UID=kanyama;PWD=soumu2049;DATABASE=退勤管理test01.fmp12')
    # cnn = pypyodbc.connect("DSN=SoumuHost;UID=kanyama;PWD=soumu2049;DATABASE=退勤管理test01.fmp12")
    cur = cnn.cursor()
    #日本語フィールドの場合、かならずダブルクォーテーションで囲む必要があります。
    cur.execute("SELECT \"職員名\",\"その日の所定時間\" from \"出退勤一覧\" WHERE (\"職員番号\" = '2049' AND \"日付\" = DATE '2020-03-02') ")
    rows = cur.fetchall()
    n = len(rows)
    print(n)
    for row in rows:

        print(row[0],row[1])
    cur.close()
    cnn.close()

if __name__ == "__main__":
    pypy()