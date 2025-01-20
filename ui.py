#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
from typing import List, Tuple


def display_main_menu():
    """
    Displays the main menu for the application.
    """
    print("\nMain Menu:")
    print("1. Search Queries")
    print("2. Analytical Queries")
    print("3. Exit")


def display_search_menu():
    """
    Displays the submenu for search queries.
    """
    print("\nSearch Queries:")
    print("1. Search by Category")
    print("2. Search by Actor")
    print("3. Search by Title")
    print("4. Search by Year")
    print("5. Search by Category and Year")
    print("6. Search by Keyword")
    print("7. Back to Main Menu")


def display_analytics_menu():
    """
    Displays the submenu for analytical queries.
    """
    print("\nAnalytical Queries:")
    print("1. Popular Search Types")
    print("2. Popular Search Terms")
    print("3. Popular Searches Today")
    print("4. Popular Searches This Month")
    print("5. Back to Main Menu")


def user_choice(prompt: str, valid_choices: List[int]) -> int:
    """
    Prompts the user to select an option and ensures it's valid.

    Args:
        prompt (str): The message to display to the user.
        valid_choices (List[int]): A list of valid numeric choices.

    Returns:
        int: The valid choice entered by the user.
    """
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            print(f"Please choose a valid option")
        except ValueError:
            print("Invalid input. Please enter a number.")
            

def input_process(prompt: str) -> str:
    """
    Prompts the user to input a string.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        str: The user input stripped of leading and trailing spaces.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")
    

def display_results(results: List[Tuple], headers: List[str]) -> None:
    """
    Displays query results in a formatted way.

    Args:
        results (List[Tuple]): The list of results to display.
        headers (List[str]): The headers for the columns.
    """
    if not results:
        print("No results found.")
        return

    print("\n" + " | ".join(headers))
    print("-" * (len(headers) * 15))

    for row in results:
        print(" | ".join(str(item) for item in row))


def display_with_limit(results: list, headers: list, limit: int = 10):
    """
    Displays the first `limit` results and provides an option to display all remaining.

    Args:
        results (list): List of results to display.
        headers (list): List of column headers.
        limit (int): Number of results to display initially.
    """
    total_results = len(results)

    print("\n" + "-" * 50)
    print(f"Showing the first {min(limit, total_results)} of {total_results} results")
    print("-" * 50)
    display_results(results[:limit], headers)

    if total_results > limit:
        show_all = input("\nDo you want to see all remaining results? (y/n): ").strip().lower()
        if show_all == 'y':
            print("\n" + "-" * 50)
            print(f"Showing all {total_results - limit} remaining results")
            print("-" * 50)
            display_results(results[limit:], headers)


def exit_application():
    """
    Displays a goodbye message and exits the application.
    """
    print("\nThank you for using the Movie Database. Goodbye!")
    sys.exit(0)


# In[ ]:




