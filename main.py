#!/usr/bin/env python
# coding: utf-8

# In[1]:


import functions
import db_mod
import ui
import queries

def main():
    with db_mod.ConnectionManager() as connection_manager:
        query_executor = db_mod.QueryExecutor(connection_manager)


        while True:
            ui.display_main_menu()
            main_choice = ui.user_choice("Select an option: ", [1, 2, 3])

            if main_choice == 1:  # Search Queries
                while True:
                    ui.display_search_menu()
                    search_choice = ui.user_choice("Select a search option: ", list(range(1, 8)))

                    if search_choice == 1:  # Search by Category
                        categories = functions.categories(query_executor, connection_manager.main_db)
                        ui.display_results(categories, ["Category ID", "Name"])
                        category_id = ui.user_choice("Enter the category ID: ", [c[0] for c in categories])
                        results = functions.movies_by_category(query_executor, connection_manager.main_db, category_id)
                        ui.display_with_limit(results, ["Title", "Release Year", "Description"])
                        category_name = query_executor.execute_select(connection_manager.main_db, queries.category_name_query, (category_id,))
                        if category_name:
                            functions.log_query(query_executor, "category_search", category_name[0][0])

                    elif search_choice == 2:  # Search by Actor
                        actor_name = ui.input_process("Enter the actor's name: ")
                        results = functions.movies_by_actor(query_executor, connection_manager.main_db, actor_name)
                        ui.display_with_limit(results, ["Title", "Actor"])
                        functions.log_query(query_executor, "actor_search", actor_name)

                    elif search_choice == 3:  # Search by Title
                        title = ui.input_process("Enter the movie title: ")
                        results = functions.movies_by_title(query_executor, connection_manager.main_db, title)
                        ui.display_with_limit(results, ["Title", "Description"])
                        functions.log_query(query_executor, "title_search", title)

                    elif search_choice == 4:  # Search by Year
                        year = ui.user_choice("Enter the release year: ", list(range(1980, 2024)))
                        results = functions.movies_by_year(query_executor, connection_manager.main_db, year)
                        ui.display_with_limit(results, ["Title", "Release Year", "Description"])
                        functions.log_query(query_executor, "year_search", str(year))

                    elif search_choice == 5:  # Search by Category and Year
                        categories = functions.categories(query_executor, connection_manager.main_db)
                        ui.display_results(categories, ["Category ID", "Name"])
                        category_name = ui.input_process("Enter the category name: ")
                        year = ui.user_choice("Enter the release year: ", list(range(1980, 2024)))
                        results = functions.movies_by_category_and_year(query_executor, connection_manager.main_db, category_name, year)
                        ui.display_with_limit(results, ["Title", "Release Year", "Category", "Description"])
                        functions.log_query(query_executor, "category_year_search", f"{category_name}, {year}")

                    elif search_choice == 6:  # Search by Keyword
                        keyword = ui.input_process("Enter a keyword to search: ")
                        results = functions.movies_by_keyword(query_executor, connection_manager.main_db, keyword)
                        ui.display_with_limit(results, ["Title", "Actor", "Description"])
                        functions.log_query(query_executor, "keyword_search", keyword)

                    elif search_choice == 7:  # Back to Main Menu
                        break

            elif main_choice == 2:  # Analytical Queries
                while True:
                    ui.display_analytics_menu()
                    analytics_choice = ui.user_choice("Select an analytical option: ", list(range(1, 6)))

                    if analytics_choice == 1:  # Popular Search Types
                        results = functions.popular_search_types(query_executor, connection_manager.log_db)
                        ui.display_results(results, ["Search Type", "Usage Count"])

                    elif analytics_choice == 2:  # Popular Search Terms
                        results = functions.popular_search_terms(query_executor, connection_manager.log_db)
                        ui.display_results(results, ["Search Term", "Usage Count"])

                    elif analytics_choice == 3:  # Popular Searches Today
                        results = functions.popular_searches_today(query_executor, connection_manager.log_db)
                        ui.display_results(results, ["Search Term", "Usage Count"])

                    elif analytics_choice == 4:  # Popular Searches This Month
                        results = functions.popular_searches_month(query_executor, connection_manager.log_db)
                        ui.display_results(results, ["Search Term", "Usage Count"])

                    elif analytics_choice == 5:  # Back to Main Menu
                        break

            elif main_choice == 3:  # Exit
                ui.exit_application()




if __name__ == "__main__":
    main()


# In[ ]:
