#!/usr/bin/python

from flask import Flask
import psutil
import pandas as pd
import time
import os
import argparse
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def main():


    processes = []
    for process in psutil.process_iter():
      if(process.pid!=os.getpid()):
           pid = process.pid
           if pid == 0:
                # System Idle Process for Windows NT, useless to see anyways
               continue
           name = process.name()
           p = psutil.Process(pid)
           cpu_usage = process.cpu_percent()
           mem_usage=p.memory_percent()
           status = process.status()
           #cwd=p.cwd()
           # get the time the process was spawned
           try:
               create_time = datetime.fromtimestamp(process.create_time())
           except OSError:
                # system processes, using boot time instead
               create_time = datetime.fromtimestamp(psutil.boot_time())
           except OSError:
                # system processes, using boot time instead
               create_time = datetime.fromtimestamp(psutil.boot_time())

           uptime=time.time() - process.create_time()
           #uptime=time.strftime('%H:%M:%S', time.gmtime(uptime))
           if (uptime<60):
               uptime=round((uptime/60),2)
           #try:
           #    username = process.username()
           #except psutil.AccessDenied:
           #    username = "N/A"
           #try:
           #    exe = process.exe()
           #except psutil.AccessDenied:
           #    exe = "Access to full path denied"
           processes.append({
                 'pid': pid, 'name': name,'status': status,'cpu_usage':cpu_usage,'memory_usage':mem_usage,'found_ratio':uptime
           })
    df = pd.DataFrame(processes)
    df2 = pd.DataFrame(processes)
    df3 = pd.DataFrame(processes)
    df4 = pd.DataFrame(processes)
    df5 = pd.DataFrame(processes)
    df6 = pd.DataFrame(processes)
    df7 = pd.DataFrame(processes)
    df8 = pd.DataFrame(processes)
    total_memory_percent=round(df['memory_usage'].sum(),1)
    total_cpu_percent=round(df['cpu_usage'].sum(),1)
    max_cpu = df['cpu_usage'].max()
    max_mem=round(df['memory_usage'].max(),1)
    df = df[['pid', 'name','status','found_ratio','cpu_usage','memory_usage']]
    df = df[df['found_ratio']<1]
    #df.sort_values(by=['found_ratio'], inplace=True)
    #df=df.iloc[:30]
    #os.system("clear")
    data=[]
    data.append({
             '  Max CPU(%) : ' : max_cpu , ' Max Memory(%) : ' : max_mem , ' Total Processes : ' : len(processes), ' Total CPU(%) : ': total_cpu_percent, ' Total Memory(%) : ' : total_memory_percent
    })
    return """
    <meta http-equiv="refresh" content={} /> 
    System Resources<br><br>: {} .""".format(args.refresh,data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("server", help="specify address and port")
    parser.add_argument("refresh", help="specify refresh rate",
                        type=int)
    args = parser.parse_args()
    app.config.update (
        SERVER_NAME=args.server)
    app.run()
