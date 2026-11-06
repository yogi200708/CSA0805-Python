from reader import read_records
from stats import percentage
from report import write_report
if __name__ == "__main__":
    records = read_records("attendance.csv")
    print("Example percentage:", percentage(8, 10))
    write_report(records, "report.csv")
