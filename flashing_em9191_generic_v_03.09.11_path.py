#Julius Kaplan 08.05.2023 Flashing 03.09.11.00-001_GENERIC:
import subprocess
from subprocess import call
from subprocess import check_call
from datetime import datetime


modems = [
    ["1-4.4.2", "mbim1.log"],
    ["1-4.2", "mbim2.log"],
    ["1-4.1.4", "mbim3.log"],
    ["1-4.4.4", "mbim4.log"],
    ["1-4.4.1", "mbim5.log"],
    ["1-4.1.3", "mbim6.log"],
    ["1-4.3.2", "mbim7.log"],
    ["1-4.3.4", "mbim8.log"],
    ["1-4.1.1", "mbim9.log"],
    ["1-4.3.1", "mbim10.log"],
    ["1-4.3.3", "mbim11.log"],
    ["1-4.1.2", "mbim12.log"],
    ["1-4.4.3", "mbim13.log"],
    ["1-4.4.3.2", "mbim14.log"],
    ["1-4.4.3.3", "mbim15.log"],
    ["1-4.4.3.4.1", "mbim16.log"],
]

fw_dir = "/home/jade/em91/EM91_All_FW_PRI_03.09.11.00"
firmware = "SWIX55C_03.09.11.00-001.cwe"
nvu = "SWIX55C_03.09.11.00-001_GENERIC_030.044_000.nvu"

rc = call("./modems_detection.sh")	

#remove current FW

for modem in modems:
    port = modem[0]
    log_file = modem[1]

    print(f"Working on {port}...")

    subprocess.run([
        "./fwdwl-litehostx86_64",
        "-P", port,
        "-l", f"/home/jade/em91/logs/{log_file}",
        "-c", "MBIM",
        "-m", "4",
        "-x", "255"
    ])
    print("Finish remove")

for modem in modems:
    port = modem[0]
    log_file = modem[1]

    print(f"Working on {port}...")

    subprocess.run([
        "./fwdwl-litehostx86_64",
        "-P", port,
        "-l", f"/home/jade/em91/logs/{log_file}",
        "-c", "MBIM",
        "-m", "4",
        "-f", fw_dir,
        "-t", "1",
        "-w", f"{firmware}",
        "-n", f"{nvu}",
        "--nsc"
    ])



    print("Done.")
    print()
