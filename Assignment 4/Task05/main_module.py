# Organisation B: utility module + main script
from attendance_utils import percentage, read_records
if __name__ == "__main__":
    records = read_records("attendance.csv")
    print("Records:", records)
    print("Example percentage:", percentage(8, 10))
