Set a countdown timer, then execute a subprocess to play some audio. 
The function or method of generating audio must be configured within this script.

Usage:

    $ python timer.py 5           # 5 minute timer 
    $ python timer.py 0 -s 30     # 30 second timer
    $ python timer.py -s 999 0    # 999 second timer

** Cancel timer with Ctrl-c

positional arguments:
  minutes     <the number of minutes to countdown>

optional arguments:
  -h, --help  show this help message and exit
  -s seconds  <the number of seconds to countdown>
