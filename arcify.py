from config import Config
from slack import Notifier
import subprocess


class Archify:
    @staticmethod
    def backup():
        config = Config.get()
        server = config['remote']['server_address']
        remote_dir = config['remote']['directory']
        for directory in config['directories']:
            command = f"rsync -arvz --progress {directory} {server}:{remote_dir}"
            result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            exitcode = result.communicate()[0]
            if result.returncode == 0:
                last_line = exitcode.decode()
                last_line = last_line[last_line.find('total size'):-2]
                Notifier.notify(f"[~OK~] Backup {directory} to {server}:{remote_dir} {last_line}")
            else:
                Notifier.notify(f"[*ERROR*] Backup {directory} to {server}:{remote_dir} {exitcode}")
