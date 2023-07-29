def write_string_to_file(text, filename):
    """
    This is a generic function that allows us to write a string (recipe) to a file
    """
    with open(f'Recipes/{filename}.txt', "w") as file:
        file.write(text)
    # file automatically closes at this point


def get_title_of_recipe(gpt_text):
    """
    This function extracts the recipe's title from the response given by ChatGPT
    We know the response's beginning will contain
        TITLE: [TITLE OF RECIPE]
        ...
    """
    # Use split() to get the part after "TITLE:"
    after_title = gpt_text.split("TITLE:", 1)[-1]

    # Use split() again to extract the text before the newline character
    extracted_text = after_title.split("\n", 1)[0]

    return extracted_text.strip()  # get rid of leading space

