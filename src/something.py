#!/usr/bin/env python


import subprocess
# python script that plays mp3 file

subprocess.Popen(['mpg123', '-q',  '/home/gal/toibot_ws/src/ToiBot1/src/toi_bot_speakers/mp3_file_response/gTTS.mp3']).wait()

