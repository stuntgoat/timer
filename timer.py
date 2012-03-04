#!/usr/bin/python

# TODO: 
# - add animations at the prompt. 
# - pass a file to play( ie. either .wav, .aiff or ChucK file ).
# - default audio player functions( Mac, Linux, Windows )

if __name__ == "__main__":
    from time import sleep
    import subprocess
    import argparse
    parser = argparse.ArgumentParser(description='''Set an audible timer for -m minutes 
and/or -s seconds.\n$python timer.py -m 5 # after 5 minutes execute a subprocess
to play some audio.\nThe function or method of generating audio must be configured
within this script.''')
    parser.add_argument('--s', type=int, help='number of seconds',
                        required=False)
    parser.add_argument('minutes', help='number of minutes', type=int)
    
    parser.set_defaults(minutes=5, s=0)
    args = parser.parse_args()

    total_seconds = (args.minutes * 60) + args.s
    sleep(total_seconds)

    # how I generate sound
    subprocess.call('chuck moe.ck', shell=True)
