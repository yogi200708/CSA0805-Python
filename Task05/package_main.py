import attendance.stats
from attendance import reader, report
if __name__ == "__main__":
    records = reader.read_records("attendance.csv")
    print("Example percentage:", attendance.stats.percentage(8, 10))
    report.write_report(records, "package_report.csv")
