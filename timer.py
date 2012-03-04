#!/usr/bin/python

# TODO: 
# - add animations at the prompt. 
# - pass a file to play( ie. either .wav, .aiff or ChucK file ).
# - default audio player functions( Mac, Linux, Windows )

if __name__ == "__main__":
    from time import sleep
    from subprocess import call
    from argparse import ArgumentParser, RawDescriptionHelpFormatter

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                                     description=
'''
Set a countdown timer, then execute a subprocess to play some audio. 
The function or method of generating audio must be configured within this script.

Usage:

    $ python timer.py 5           # 5 minute timer 
    $ python timer.py 0 -s 30     # 30 second timer
    $ python timer.py -s 999 0    # 999 second timer

** Cancel timer or subprocess with ctrl-c

''')

    parser.add_argument('-s', type=int, help='<the number of seconds to countdown>',
                        required=False, metavar='seconds')
    parser.add_argument('minutes', help='<the number of minutes to countdown>', type=int)

    parser.set_defaults(s=0)
    args = parser.parse_args()
    total_seconds = (args.minutes * 60) + args.s

    try:
        # comment next line after configuring audio playback
        print("Configure audio playback inside timer.py!!!")

        sleep(total_seconds)

        # how I personally generate sound. Edit to your preference
        call('/Users/me/bin/chuck /Users/me/chuck/alarms/moe.ck', shell=True)
    except KeyboardInterrupt:
        print
        
        
