# sierra_flashing_by_path
Flasher machine to flash automatically by USB paths
This script make to updates multiple Sierra Wireless EM9191 modems one by one by using the `-P` flag of USB path, and solves the issue that unit change the ttyUSB ports after reboot in Linux system.

# usage

Download the binary fwfwdl from [source.sierrawireless](https://source.sierrawireless.com/resources/airprime/software/mbpl/mbpl-software-latest/)

1. update the USB path by using with `find /sys/bus/usb/devices/usb*/ -name dev |sort` Linux command and update the `modems` list in the first item of each line  per the result.
2. update the `fw_dir`, `firmware`, `nvu` paths if needed.
3. omit `rc = call("./modems_detection.sh")` if not in used
4. run the py file by `python3.8 flashing_em9191_generic_v_03.09.11_path.py`
5. firt it will remove by using the

# license
This program is free software.
It is licensed under the GNU GPL version 3 or later.
That means you are free to use this program for any purpose;
free to study and modify this program to suit your needs;
and free to share this program or your modifications with anyone.
If you share this program or your modifications
you must grant the recipients the same freedoms.
To be more specific: you must share the source code under the same license.
For details see https://www.gnu.org/licenses/gpl-3.0.html
