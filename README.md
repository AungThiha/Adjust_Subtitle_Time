# Adjust Subtitle Time
A script to Adjust time in subtitle


### Requirements

* Python 2.7
* Git (optional)
* Terminal or command prompt


### How to download

Open up your terminal or command prompt and enter the following command to download
* $ git clone https://github.com/AungThiha/Adjust_Subtitle_Time.git
Alternatively, you can download by clicking **Download Zip** button.


### How to use

Open up your terminal or command prompt.
Make sure your working directory is where adjust.py exists
which means cd to your folder you've downloaded.

#### Manual
```
NAME
     adjust -- adjust time in subtitle
     
SYNOPSIS
    python adjust.py [-i | -d] <hh:mm:ss> <input> <output>
    
DESCRIPTION
    The adjust utility edit the input subtitle file to increase or decrease time.

    It needs python to be able to run.

    The options are as follows:
    -i          increase time
	-d          decrease time
	input       name of original subtitle file to edit
	output      [Optional] name of edited file that like to be printed out
```

### Example
* $ python adjust.py -i 00:00:20 FlashS01E02.srt output.srt

