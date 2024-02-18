m = ["madam", "fire", "tomato", "book", "kiosk", "mom"]
print(list(filter(lambda x: x in [i[::-1] for i in m], m)))
