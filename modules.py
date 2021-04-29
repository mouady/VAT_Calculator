import os
import configparser as cf

build_version = "v5"

config = cf.ConfigParser()

if os.name == "posix":
    delete_msg = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    delete_msg = "cls"


long_msg = """
---------------------------------------------------------
You will have 2 options to perform
your calculations in this program.

1. CALCULATE (WITH PARAMETERS)
- This option allows you to make your
  calculations without having to put all the time
  the currency and the VAT percentage. It's used
  the parameters that you enter and save
  the settings for all the calculations you do.
  It can be useful if the calculations you require
  perform are in a single currency and VAT percentage

2. CALCULATE (WITHOUT PARAMETERS)
- This option allows you to perform the calculations but
  will ask you what currency and VAT percentage you want
  use right away. This can be useful if you calculate
  that you need to do are the currency and the
  VAT percentage all the time.

Regardless of which option you choose, below
it will ask you the parameters that you want, you can
change at any time in the "Parameters" section
-----------------------------------------------------------
"""
