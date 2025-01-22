#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from typing import Any, Dict, List, Optional
import logging
import queries
from utils import safe_execute

logging.basicConfig(
    filename='db_manager.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

load_dotenv()

class ConnectionManager:
    """
    Manages database connections for multiple databases.

    Attributes:
        connections (Dict[str, mysql.connector.MySQLConnection]):
            A dictionary of database connections identified by database names.
    """
    def __init__(self):
        """
        Initializes the ConnectionManager and connects to the databases.
        """
        self.connections: Dict[str, mysql.connector.MySQLConnection] = {}
        self.initialize_connections()
        self.main_db = "sakila"  # Main database name
        self.log_db = "queries"  # Logging database name


    @safe_execute
    def initialize_connections(self):
        """
        Initializes database connections using the _connect_to_databases method.
        """
        self._connect_to_databases()

    def _connect_to_databases(self) -> None:
        """
        Establishes connections to the required databases using credentials
        from environment variables.

        Raises:
            Error: If a connection to any database fails.
        """
        try:
            self.connections['sakila'] = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.connections['queries'] = mysql.connector.connect(
                host=os.getenv("DBQ_HOST"),
                user=os.getenv("DBQ_USER"),
                password=os.getenv("DBQ_PASSWORD"),
                database=os.getenv("DBQ_NAME")
            )
        except Error as e:
            logging.error(f"Database connection error: {e}")
            raise ConnectionError("Sorry! Failed to connect to one or more databases. Please, try next time") from e 

    @safe_execute
    def get_connection(self, db_name: str) -> mysql.connector.MySQLConnection:
        """
        Retrieves a connection to the specified database.

        Args:
            db_name (str): The name of the database.

        Returns:
            mysql.connector.MySQLConnection: The connection object for the specified database.

        Raises:
            ValueError: If no connection exists for the specified database.
        """
        connection = self.connections.get(db_name)
        if not connection:
            raise ConnectionError(f"No connection to database: {db_name}")
        return connection

    def close_connections(self) -> None:
        """
        Closes all active database connections.
        """
        for name, connection in self.connections.items():
            if connection.is_connected():
                connection.close()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_connections()

                
class QueryExecutor:
    """
    Executes SQL queries on specified databases.

    Attributes:
        connection_manager (ConnectionManager):
            The manager responsible for providing database connections.
    """
    def __init__(self, connection_manager: ConnectionManager):
        """
        Initializes the QueryExecutor with a ConnectionManager instance.

        Args:
            connection_manager (ConnectionManager):
                The manager responsible for managing database connections.
        """
        self.connection_manager = connection_manager
    
    @safe_execute
    def execute_select(self, db_name: str, query: str, params: Optional[tuple] = None) -> List[Any]:
        """
        Executes a SELECT query on the specified database.

        Args:
            db_name (str): The name of the database.
            query (str): The SQL SELECT query to execute.
            params (Optional[tuple]): Parameters for the SQL query.

        Returns:
            List[Any]: The results of the SELECT query.

        Raises:
            Error: If the query execution fails.
        """
        try:
            connection = self.connection_manager.get_connection(db_name)
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Error as e:
            logging.error(f"Query execution error (SELECT): {e}")
            raise RuntimeError from e

    @safe_execute
    def execute_non_select(self, db_name: str, query: str, params: Optional[tuple] = None) -> None:
        """
        Executes an INSERT, UPDATE, or DELETE query on the specified database.

        Args:
            db_name (str): The name of the database.
            query (str): The Non-Select SQL query to execute .
            params (Optional[tuple]): Parameters for the SQL query.

        Raises:
            Error: If the query execution fails.
        """
        try:
            connection = self.connection_manager.get_connection(db_name)
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()
        except Error as e:
            logging.error(f"Query execution error (Non-SELECT): {e}")
            raise RuntimeError from e


# In[ ]:




