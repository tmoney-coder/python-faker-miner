#!/usr/bin/env python3

# Initial inspiration for the script came from: https://qxf2.com/blog/generate-cpu-load/

import time, math, multiprocessing

def fake_miner(util=80):
  start_time = time.time()
  while True:
    while time.time()-start_time < util/100.0:
      x = math.sqrt(64*64*64*64*64*64)
      time.sleep(1-util/100.0)

if __name__ == "__main__":
  print("Starting up the fake miner, to exit, you must kill the process")

  theThreads = []
  for x in range(multiprocessing.cpu_count()):
    theProcess = multiprocessing.Process(target=fake_miner)
    theProcess.name = f"miner_thread_{x}"
    theProcess.start()
    theThreads.append(theProcess)

  print("Threads have started, now just pausing the main thread")
  for theProc in theThreads:
    theProc.join()
