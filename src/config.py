##########################################################
#
# Copyright (C) 2024-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AUTH_TOKEN: str             = load_dotenv("AUTH_TOKEN")
SLEEP_TIME: int             = int(load_dotenv("SLEEP_TIME"))
TAB_COUNT: int              = int(load_dotenv("TAB_COUNT"))
AVAILABLE_TAB_COUNT: int    = int(load_dotenv("AVAILABLE_TAB_COUNT"))
