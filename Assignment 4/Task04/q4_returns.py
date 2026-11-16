from pathlib import Path

def save_returns(books, log_file="returns.log"):
    with open(log_file, "a", encoding="utf-8") as log:
        for book in books:
            log.write(book.rstrip("\\n") + "\\n")

def process(day_file, log_file="returns.log", error_file="errors.log"):
    try:
        with open(day_file, encoding="utf-8") as file:
            books = file.read().splitlines()
        save_returns(books, log_file)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
        with open(error_file, "a", encoding="utf-8") as log:
            log.write(f"{day_file}: {type(error).__name__}: {error}\\n")
        print("Could not process", day_file, "-", error)

if __name__ == "__main__":
    for day in ("day1.txt", "day2.txt", "day3.txt"):
        process(day, "returns.log")
    print(Path("returns.log").read_text(encoding="utf-8"))
