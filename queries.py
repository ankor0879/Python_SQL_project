#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Insert Queries

insert_query_log = """
INSERT INTO queries (search_type, search_term) 
VALUES (%s, %s);
"""

# Search Queries

category_list = "SELECT category_id, name FROM category;"

search_by_category = """
SELECT f.title, f.release_year, f.description
FROM film AS f
JOIN film_category AS fc ON f.film_id = fc.film_id
WHERE fc.category_id = %s;
"""

category_name_query = """
SELECT name FROM category WHERE category_id = %s;
"""

search_by_year = """
SELECT title, release_year, description
FROM film
WHERE release_year = %s;
"""

search_by_category_and_year = """
SELECT f.title, f.release_year, c.name AS category, f.description
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = %s AND f.release_year = %s;
"""

search_by_title = """
SELECT title, description
FROM film
WHERE title LIKE %s;
"""

search_by_actor = """
SELECT f.title, CONCAT(a.first_name, ' ', a.last_name) AS actor
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE CONCAT(a.first_name, ' ', a.last_name) LIKE %s;
"""

search_by_keyword = """
SELECT 
    f.title,
    GROUP_CONCAT(DISTINCT CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors,
    f.description
FROM film f
LEFT JOIN film_actor fa ON f.film_id = fa.film_id
LEFT JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.title LIKE %s
   OR CONCAT(a.first_name, ' ', a.last_name) LIKE %s
   OR f.description LIKE %s
GROUP BY f.film_id, f.title, f.description;
"""

# Analytics Queries

popular_searches_by_type = """
SELECT search_type, COUNT(*) AS usage_count
FROM queries
GROUP BY search_type
ORDER BY usage_count DESC
LIMIT 5;
"""

popular_searches_by_term = """
SELECT search_term, COUNT(*) AS usage_count
FROM queries
GROUP BY search_term
ORDER BY usage_count DESC
LIMIT 5;
"""

popular_searches_today = """
SELECT search_term, COUNT(*) AS usage_count
FROM queries
WHERE DATE(timestamp) = CURRENT_DATE
GROUP BY search_term
ORDER BY usage_count DESC
LIMIT 5;
"""

popular_searches_month = """
SELECT search_term, COUNT(*) AS usage_count
FROM queries
WHERE MONTH(timestamp) = MONTH(CURRENT_DATE) AND YEAR(timestamp) = YEAR(CURRENT_DATE)
GROUP BY search_term
ORDER BY usage_count DESC
LIMIT 5;
"""

