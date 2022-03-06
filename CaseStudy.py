import mysql.connector as mysql
from mysql.connector import Error
import sqlalchemy
from urllib.parse import quote_plus as urlquote
import matplotlib.pyplot as plt
import pandas as pd
import os

class StudiKasus2:
    """Kelas ini berguna untuk mengakses database yang berisi user
    """
    def __init__(self, host, port, user, password):
        """fungsi ini berguna sebagai constructor

        Args:
            host (String): biasanya berisi "localhost"
            port (String): biasanya isi "3306"
            user (String): login user untuk mysql
            password (String): password untuk mysql
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def create_db(self, db_name):
        """Untuk membuat database

        Args:
            db_name (String): nama dari database yang akan dibuat
        """
        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("CREATE DATABASE {}".format(db_name))
        except Error as e:
            print("Error while connecting to MySQL", e)
        # preparing a cursor object
        # creating database



    def create_table(self, db_name, table_name, df):
        """Membuat table dari data csv yang sudah di import

        Args:
            db_name (_type_): nama dari database yang akan dibuatkan table
            table_name (_type_): nama dari table yang akan dibuat
            df (_type_): data yang akan di import ke table
        """
        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("USE {}".format(db_name))
                cursor.execute("CREATE TABLE {}".format(table_name))
        except Error as e:
            print("Error while connecting to MySQL", e)

        engine_stmt = 'mysql+mysqldb://%s:%s@%s:%s/%s' % (self.user, urlquote(self.password),
                                                            self.host, self.port, db_name)
        engine = sqlalchemy.create_engine(engine_stmt)

        df.to_sql(name=table_name, con=engine,
                  if_exists='append', index=False, chunksize=1000)

    def load_data(self, db_name, table_name):
        """Fungsi ini berguna untuk mengakses dan menampilkan data dari table

        Args:
            db_name (String): nama dari database yang akan diakses
            table_name (String): nama dari table yang akan diakses

        Returns:
            String: hasil dari proses mengakses table
        """
        conn = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM {}.{}".format(db_name, table_name))
                result = cursor.fetchall()
                return result
        except Error as e:
            print("Error while connecting to MySQL", e)



    def import_csv(self, path):
        """Fungsi yang berguna untuk mengimport csv

        Args:
            path (String): File path dari file csv yang akan diimport

        Returns:
            DataFrame: data yang sudah diconvert dari bentuk csv ke dataframe
        """

        return pd.read_csv(path, index_col=False, delimiter=',')