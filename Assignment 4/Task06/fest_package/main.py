from fest.processor import run
if __name__ == "__main__":
    students, events, errors = run("input", "output")
    print("Unique students:", len(students))
    print("Events:", len(events))
    print("Errors:", len(errors))
