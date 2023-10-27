from sync_ftp import SyncFtp
import os
import time
# from user_name import user_name
#get the local folder location.
home_path = os.path.expanduser("~")
dir_list = os.listdir(home_path)
if "zlogger" in dir_list:
    source_path = os.path.join(home_path, "zlogger")
    target_path = "/var/www/html/"

SYNC = SyncFtp("20.124.217.64", "zlogger", "zlogger")
while True:
    SYNC.send_to_ftp(source_path, target_path)
    time.sleep(60)
