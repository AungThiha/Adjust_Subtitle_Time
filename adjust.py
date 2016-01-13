"""
NAME
     adjust -- adjust time in subtitle

SYNOPSIS
    python adjust.py [-i | -d] <hh:mm:ss> <input> <output>

DESCRIPTION
    The adjust utility edit the input subtitle file
    to increase or decrease time.

    It needs python to be able to run.

    The options are as follows:

    -i          increase time
    -d          decrease time
    input       name of original subtitle file to edit
    output      [Optional] name of edited file that like to be printed out

Example
    python adjust.py -i 00:00:20 FlashS01E02.srt output.srt
"""

from datetime import datetime, timedelta
import re
import sys

__author__ = 'aungthiha'

arrow = ' --> '
dot_pat = r'(\d\d:\d\d:\d\d\.\d\d\d) --> (\d\d:\d\d:\d\d\.\d\d\d)'
comma_pat = r'(\d\d:\d\d:\d\d\,\d\d\d) --> (\d\d:\d\d:\d\d\,\d\d\d)'


def change_time(t_str):
    t = datetime.strptime(t_str[:8], '%H:%M:%S')
    if is_decrease:
        output = t - adjustment
    else:
        output = t + adjustment
    return str(output.time()) + t_str[8:]


def repl(t_range):
    start = change_time(t_range.group(1))
    end = change_time(t_range.group(2))
    return start + arrow + end


def adjust_time(hours, minutes, seconds, is_decrease_str, content):
    global is_decrease, adjustment
    is_decrease = is_decrease_str == '-d'
    adjustment = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    content = re.sub(dot_pat, repl, content)
    content = re.sub(comma_pat, repl, content)
    return content


def main(hours, minutes, seconds, is_decrease_str, input_f, output_f):
    with open(input_f, 'r') as f:
        content = adjust_time(hours,
                              minutes,
                              seconds, is_decrease_str, f.read())
    with open(output_f, 'w') as f:
        f.write(content)


if __name__ == '__main__':

    if len(sys.argv) > 3:

        # decrease or increase
        is_decrease_str = sys.argv[1]

        # adjustment time
        str_adjust = sys.argv[2].split(":")

        # output and input files
        input_f = sys.argv[3]
        if len(sys.argv) > 4:
            output_f = sys.argv[4]
        else:
            output_f = 'output.srt'

        main(int(str_adjust[0]),
             int(str_adjust[1]),
             int(str_adjust[2]),
             is_decrease_str,
             input_f, output_f)

    else:

        print __doc__
