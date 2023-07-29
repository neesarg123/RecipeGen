import os
import requests
import json

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

TEXT_COLUMN_NAME = "Item"
CHECKBOX_COLUMN_NAME = "Have it?"


def get_pages(num_pages=None):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results


def get_items_in_notion_db():
    pages = get_pages()
    item_to_availability_map = {}

    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        item = props[TEXT_COLUMN_NAME]["title"][0]["text"]["content"]
        availability = props[CHECKBOX_COLUMN_NAME]["checkbox"]
        
        item_to_availability_map[item] = availability

    # ------------- THE FOLLOWING IS THE LIST OF ITEMS ON NOTION DATABASE ----------------- #
    return item_to_availability_map

