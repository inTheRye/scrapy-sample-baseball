# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.exceptions import DropItem


class SpaceObjectPipeline(object):

    CREATE_TABLE_TLE = """
    CREATE TABLE tle (
    soname text,
    satnum integer,
    jdsatepoch text,
    epoch text,
    bstar text,
    inclo real,
    nodeo real,
    ecco real,
    argpo real,
    mo real,
    no real,
    sma real,
    apogee real,
    perigee real,
    altitude real,
    create_date date,
    update_date date,
    primary key(satnum, jdsatepoch)
    )
    """

    INSERT_TLE = """
    insert into tle(
    soname,
    satnum,
    jdsatepoch,
    epoch,
    bstar,
    inclo,
    nodeo,
    ecco,
    argpo,
    mo,
    no,
    sma,
    apogee,
    perigee,
    altitude,
    create_date,
    update_date
    )
    values(
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
    datetime('now', 'localtime'),
    datetime('now', 'localtime')
    )
    """

    DATABASE_NAME = 'space_object.db'
    conn = None

    def __init__(self):
        """
        Tableの有無をチェック,無ければ作る
        """
        conn = sqlite3.connect(self.DATABASE_NAME)
        if conn.execute("select count(*) from sqlite_master where name='tle'").fetchone()[0] == 0:
            conn.execute(self.CREATE_TABLE_TLE)
        conn.close()

    def open_spider(self, spider):
        """
        初期処理(DBを開く)
        :param spider: ScrapyのSpiderオブジェクト
        """
        self.conn = sqlite3.connect(self.DATABASE_NAME)

    def process_item(self, item, spider):
        """
        ItemをSQLite3に保存
        :param item: Itemの名前
        :param spider: ScrapyのSpiderオブジェクト
        :return: Item
        """
        # Spiderの名前で投入先のテーブルを判断
        if spider.name == 'tle':
            # 打者成績
            self.conn.execute(self.INSERT_TLE, (
                item['soname'], item['satnum'], item['jdsatepoch'],
                item['epoch'], item['bstar'], item['inclo'], item['nodeo'],
                item['ecco'], item['argpo'], item['mo'], item['no'],
                item['sma'], item['perigee'], item['apogee'], item['altitude'],
            ))
        else:
            raise DropItem('spider not found')
        self.conn.commit()
        return item

    def close_spider(self, spider):
        """
        終了処理(DBを閉じる)
        :param spider: ScrapyのSpiderオブジェクト
        """
        self.conn.close()
