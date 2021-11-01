import subprocess
Output = subprocess.check_output(f'nslookup  {domain}', shell=True, encoding=‘UTF-8’)
