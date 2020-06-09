#!/usr/bin/env python3
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        
        result = client.call("ak.wwise.core.remote.connect", {"host":"127.0.0.1"})

except CannotConnectToWaapiException:

    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")