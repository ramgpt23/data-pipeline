from functions import *
import datetime
import time

print("Starting data pipeline at ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("=========================================")

# step 1: extract video ids
t0=time.time()
getVideoIds()
t1=time.time()
print("step 1: Done")
print(f"Video IDs downloaded in {str(t1-t0)} seconds")

# step 2: extract transcripts for videos
t0=time.time()
getVideoTranscripts()
t1=time.time()
print("step 2: Done")
print(f"Transcripts downloaded in {str(t1-t0)} seconds")

# step 3: Transform data
t0=time.time()
transformData()
t1=time.time()
print("step 3: Done")
print(f"Data transformed in {str(t1-t0)} seconds")