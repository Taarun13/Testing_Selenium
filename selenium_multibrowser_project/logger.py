from datetime import datetime

automation_logs = []
def log_step(module, step_description, status, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    automation_logs.append([timestamp, module, step_description, status, details])
