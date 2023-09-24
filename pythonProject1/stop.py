import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    start_time = time.time()
    input("press Enter to run the stopwatch.")
    run_time = time.time()
    input("Press Enter to stop the stopwatch.")
    end_time = time.time()
    run_time = run_time - start_time
    print(f"run time: {run_time:.2f} minutes")

stopwatch()
