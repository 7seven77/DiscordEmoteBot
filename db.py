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
            url TEXT NOT NULL,
        );
        """)

        connection.commit()
        connection.close()
