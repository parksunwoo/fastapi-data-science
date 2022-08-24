def retrieve_page(page):
    if page > 3:
        return {"next_page": None, "items": []}
    return {"next_page": page + 1, "items": ["A", "B", "C"]}
items = []
page = 1

while page is not None:
    page_reuslt = retrieve_page(page)
    items += page_reuslt["items"]
    page = page_reuslt["next_page"]
print(items)
