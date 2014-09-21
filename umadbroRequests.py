#!/usr/bin/env python
import urllib, sys
__author__ = 'jared'


class Request:
    ''' Requests class handles receiving information from umadbro website'''

    def __init__(self):
        print("Successfully created object!")

    # Name: make_request
    # Param: self, user command
    # Purpose: Making request to "umadbro" server based on user args.
    # Return: Nothing.
    def make_request(self, command):

        tool_list= self.check_args(command)

        for tool in tool_list:

            req = urllib.urlopen('http://umadbro.pw/'+str(command))

            if req.getcode() != 200: # File doesn't exist
                print("Error! that page doesn't exist! (yet!)\n")
            else:
                print(req)

    # Name: check_args
    # Param: self, command line arguments
    # Purpose: Checking the user passed in tools to search.
    #          Script exits if nothing is found.
    # Return: Array of searchable items
    def check_args(self, usr_arg):
        arg_len = len(usr_arg)

        if arg_len == 0:
            print("Error! please enter an tool!/n Ex: umadbro 'toolname' ")
            sys.exit()
        else:
            usr_arg.pop(0)  # removing the 0 element of argument (the script name)

        return usr_arg