# Defect demonstration: w overwrites and no newline joins entries.
def bad_save(books):
    log = open("bad_returns.log", "w")
    for book in books:
        log.write(book)
    log.close()

bad_save(["Book A", "Book B"])
bad_save(["Book C"])
print(open("bad_returns.log").read())  # only Book C; entries are joined
