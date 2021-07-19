import os, sys
import time
import subprocess


def speed(n):
    i = 0
    summary = []

    while i < n:
        print("\n\n Test # ",i+1)
        check = "speedtest"
        # check = os.system('cmd /c "speedtest"')
        output = str(subprocess.check_output(check,shell=True))
        serv = output.find('(id =')
        isp = output.find('ISP')
        dld = output.find('Download')
        upl = output.find('Upload')

        ookla_id = output[serv+5:serv+11].strip("' '()/\\")
        print(f"Server ID:{ookla_id}")
        print(f"ISP name:{output[isp+5:isp+15]}")
        isp_name = output[isp+5:isp+15]
        print(f"Download:{output[dld+11:dld+23]}")
        print(f"Upload:{output[upl+7:upl+22]}")

        dl = output[dld+11:dld+23].strip("' '()/\\").split()
        ul = output[upl+7:upl+22].strip("' '()/\\").split()
        Download = float(dl[0])
        Upload = float(ul[0])
        
        row = [i,isp_name, ookla_id, Download, Upload]
        summary.append(row)
        time.sleep(5)
        i+=1

    print("\n\n  Finished")
    print(summary)
    

    import csv

    headers = ["test_id","isp_name", "ookla_id", "Download", "Upload"]

    filename = 'isp_speedtest.csv'

    with open(filename, 'w+', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        if csvfile.readline() == None:
            csvwriter.writerow(headers)

        csvwriter.writerows(summary)
    print("\n CSV is created")

if __name__=="__main__":
   
    # n = int(sys.argv[1])
    n = 2
    speed(n)
