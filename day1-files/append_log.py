import datetime

def append_log(path, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} - {message}\n"
    with open(path, "a") as f:
        f.write(line)

append_log("day1-files/study_log.txt", "Finished word count exercise")
append_log("day1-files/study_log.txt", "Started append_log")