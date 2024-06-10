##########################################################
#
# Copyright (C) 2024-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import os
from dotenv import load_dotenv

load_dotenv()


AUTH_TOKEN: str             = os.getenv("AUTH_TOKEN")
SLEEP_TIME: int             = int(os.getenv("SLEEP_TIME"))
TAB_COUNT: int              = int(os.getenv("TAB_COUNT"))
AVAILABLE_TAB_COUNT: int    = int(os.getenv("AVAILABLE_TAB_COUNT"))
