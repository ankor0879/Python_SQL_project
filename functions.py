#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import Dict, List, Any
import queries
from db_mod import QueryExecutor
from utils import safe_execute

# Search Functions

@safe_execute
def categories(query_executor: QueryExecutor, db_name: str):
    """
    Fetches all movie categories.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.

    Returns:
        List[tuple]: A list of tuples with category IDs and names.
    """
    query = queries.category_list
    return query_executor.execute_select(db_name, query)

@safe_execute
def movies_by_category(query_executor: QueryExecutor, db_name: str, category_id: int):
    """
    Fetches movies from the specified category by ID.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.
        category_id (int): The ID of the category to search for.

    Returns:
        List[tuple]: A list of tuples with movie details.
    """
    query = queries.search_by_category
    params = (category_id,)
    return query_executor.execute_select(db_name, query, params)    

@safe_execute
def movies_by_year(query_executor: QueryExecutor, db_name: str, year: int):
    """
    Fetches movies released in the specified year.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.
        year (int): The year to search for.

    Returns:
        List[tuple]: A list of tuples with movie details.
    """
    query = queries.search_by_year
    params = (year,)
    return query_executor.execute_select(db_name, query, params)

@safe_execute
def movies_by_category_and_year(query_executor: QueryExecutor, db_name: str, category_name: str, year: int):
    """
    Fetches movies from the specified category released in the specified year.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.
        category_name (str): The name of the category to search for.
        year (int): The year to search for.

    Returns:
        List[tuple]: A list of tuples with movie details.
    """
    query = queries.search_by_category_and_year
    params = (category_name, year)
    return query_executor.execute_select(db_name, query, params)

@safe_execute    
def movies_by_title(query_executor: QueryExecutor, db_name: str, title: str):
    """
    Fetches movies matching the specified title.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.
        title (str): The title or part of the title of the movie.

    Returns:
        List[tuple]: A list of tuples with movie details.
    """
    query = queries.search_by_title
    params = (f"%{title}%",)
    return query_executor.execute_select(db_name, query, params)

@safe_execute
def movies_by_actor(query_executor: QueryExecutor, db_name: str, actor_name: str):
    """
    Fetches movies with the specified actor.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.
        actor_name (str): The name of the actor to search for.

    Returns:
        List[tuple]: A list of tuples with movie details and actor names.
    """
    query = queries.search_by_actor
    params = (f"%{actor_name}%",)
    return query_executor.execute_select(db_name, query, params)

@safe_execute
def movies_by_keyword(query_executor: QueryExecutor, db_name: str, keyword: str):
    """
    Fetches movies that match the given keyword in title, actor name, or description.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.
        keyword (str): The keyword to search for.

    Returns:
        List[tuple]: A list of tuples with movie details (title, actor, description).
    """
    query = queries.search_by_keyword
    params = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
    return query_executor.execute_select(db_name, query, params)


# Analytics Functions
@safe_execute
def popular_search_types(query_executor: QueryExecutor, db_name: str):
    """
    Fetches the most popular search types and their usage counts.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.

    Returns:
        List[tuple]: A list of tuples with search types and their usage counts.
    """
    query = queries.popular_searches_by_type
    return query_executor.execute_select(db_name, query)

@safe_execute
def popular_search_terms(query_executor: QueryExecutor, db_name: str):
    """
    Fetches the most popular search terms and their usage counts.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.

    Returns:
        List[tuple]: A list of tuples with search terms and their usage counts.
    """
    query = queries.popular_searches_by_term
    return query_executor.execute_select(db_name, query)
    
@safe_execute
def popular_searches_today(query_executor: QueryExecutor, db_name: str):
    """
    Fetches the most popular search terms for today and their usage counts.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.

    Returns:
        List[tuple]: A list of tuples with search terms and their usage counts for today.
    """
    query = queries.popular_searches_today
    return query_executor.execute_select(db_name, query)

@safe_execute
def popular_searches_month(query_executor: QueryExecutor, db_name: str):
    """
    Fetches the most popular search terms for the current month and their usage counts.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        db_name (str): The name of the database to query.

    Returns:
        List[tuple]: A list of tuples with search terms and their usage counts for the current month.
    """
    query = queries.popular_searches_month
    return query_executor.execute_select(db_name, query)


# log Functions

@safe_execute
def log_query(query_executor: QueryExecutor, search_type: str, search_term: str):
    """
    Logs a query into the 'queries' database.

    Args:
        query_executor (QueryExecutor): The query executor instance.
        search_type (str): The type of the search (e.g., 'category_search').
        search_term (str): The term used in the search.
    """
    query = queries.insert_query_log
    params = (search_type, search_term)
    query_executor.execute_non_select("queries", query, params)

