import threading
from amazon_automation import run_amazon_flow
from youtube_automation import run_youtube_flow
from rep_generation.excel import write_to_excel
from rep_generation.word import write_to_word
from logger import automation_logs

def main():
    def amazon_flow_wrapper():
        run_amazon_flow()
    def youtube_flow_wrapper():
        run_youtube_flow()
    t1 = threading.Thread(target=amazon_flow_wrapper)
    t2 = threading.Thread(target=youtube_flow_wrapper)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Both browser flows completed.")
    write_to_excel(automation_logs)
    modules = {}
    for log in automation_logs:
        timestamp, module, step_desc, status, details = log
        entry = f"{timestamp} - {step_desc} [{status}] {details}".strip()
        modules.setdefault(module, []).append(entry)
    for module_name, steps in modules.items():
        overall_status = "Fail" if any("[Fail]" in s for s in steps) else "Pass"
        write_to_word(module_name + " Automation", steps, overall_status, notes="")
if __name__ == "__main__":
    main()
