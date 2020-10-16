from os import stat
import sqlite3
from sqlite3.dbapi2 import Connection

class db():

    @staticmethod
    def connectToDB(dbName : str = 'database.db') -> Connection:
        """Connect to the database
        Parameters
        ----------
        dbName : str, optional
            Name of the database to connect to, by default 'database.db'
        Returns
        -------
        sqlite3.Connection
            The connection to the database
        """
        connection: Connection = sqlite3.connect(dbName)

        return connection

    @staticmethod
    def setUp():
        connection : Connection = db.connectToDB()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE customEmotes(
            user TEXT NOT NULL,
            slot TEXT NOT NULL,
            url TEXT NOT NULL
        );
        """)

        connection.commit()
        connection.close()

    def getEmote(user: str, slot: str):
        connection: Connection = db.connectToDB()
        cursor = connection.cursor()

        data = (user, slot)
        cursor.execute('''SELECT url FROM customEmotes WHERE user = ? AND slot = ?;''', data)

        result = cursor.fetchall()

        connection.commit()
        connection.close()

        if len(result) == 0:
            return None
        return result[0][0]

    def setEmote(user: str, slot: str, url: str):
        connection = db.connectToDB()
        cursor = connection.cursor()

        data = (user, slot, url)
        cursor.execute('''
        REPLACE INTO customEmotes(user, slot, url)
            VALUES(?, ?, ?);
        ''', data)

        connection.commit()
        connection.close()