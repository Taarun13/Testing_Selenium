import threading
from amazon_automation import run_amazon_flow
from youtube_automation import run_youtube_flow

def main():
    t1 = threading.Thread(target=run_amazon_flow)
    t2 = threading.Thread(target=run_youtube_flow)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Both browser flows completed.")

if __name__ == "__main__":
    main()
