#!/usr/bin/python
import subprocess
import cfworker
import time

worker = cfworker.cfworker()
worker.start()

while True:
        proc = subprocess.Popen("./cplusplus", stdout=subprocess.PIPE, shell=True)
        out, err = proc.communicate()
        print out
	time.sleep(5)

worker.stop()

