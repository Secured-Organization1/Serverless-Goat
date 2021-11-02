import subprocess
output = subprocess.check_output(f"nslookup2 {domain}", shell=True, encoding='UTF-8')
