import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    print("Stopwatch started!")
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            print(time_str, end="\r", flush=True)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nStopwatch stopped!")
        end_time = time.time()
        total_time = end_time - start_time
        hours = int(total_time // 3600)
        minutes = int((total_time % 3600) // 60)
        seconds = int(total_time % 60)
        print("Total time:", f"{hours:02d}:{minutes:02d}:{seconds:02d}")

stopwatch()
