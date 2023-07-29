from get_database_entries import get_items_in_notion_db


def filter_response(response_dict):
    """
    This function will take in response obtained from notion and return a list of ingredients AVAILABLE
    """
    result = []
    for key, value in response_dict.items():
        if value:
            result.append(key)
    
    return result


def generate_gpt_query():
    """
    This function will take in a list of AVAILABLE items and generate a query to gpt as such:
        Can you give me a tasty recipe using the following ingredients: {INSERT LIST HERE}
    """
    notion_response = get_items_in_notion_db()
    list_of_items = filter_response(notion_response)

    ingredients = ", ".join(list_of_items)
    query = f"Can you give me a tasty recipe using the following ingredients: {ingredients}? Begin your response with saying TITLE: [INSERT RECIPE's TITLE]"
    return query

