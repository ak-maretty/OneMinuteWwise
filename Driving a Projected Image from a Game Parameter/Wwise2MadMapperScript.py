# Copyright (c) <COPYRIGHTYEAR> Audiokinetic Inc.
 
#------- Commercial License Usage
# Licensees holding valid commercial licenses to the AUDIOKINETIC Wwise Technology
# may use this file in accordance with the end user license agreement provided
# with the software or, alternatively, in accordance with the terms contained in a
# written agreement between you and Audiokinetic Inc.
 
#------- Apache License Usage
# Alternatively, this file may be used under the Apache License, Version 2.0 (the
# "Apache License"); you may not use this file except in compliance with the
# Apache License. You may obtain a copy of the Apache License at
# http://www.apache.org/licenses/LICENSE-2.0.
 
# Unless required by applicable law or agreed to in writing, software distributed
# under the Apache License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, either express or implied. See the Apache License for
# the specific language governing permissions and limitations under the License.

#!/usr/bin/env python3
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

import threading
import mido
midiOutput = mido.open_output("Wwise2MadMapperPort 1")

try:
    client = WaapiClient()
    print("Connected MIDI device: '{}'".format(midiOutput))

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

else:
    #Start Profiler
    handler = client.call("ak.wwise.core.profiler.startCapture")

    def GetRTPCsLoop():
        threading.Timer(0.01, GetRTPCsLoop).start()
        arguments = {
            "time" : "capture"
        }
        result = client.call("ak.wwise.core.profiler.getRTPCs", arguments)

        for i in result.get("return"):
            if i.get("name") == "SomeGameParameter":
                msg = mido.Message('control_change', control=1, value=int(i.get("value")) + 48 )
                midiOutput.send(msg)
                print("Message: '{}'".format(msg))

    GetRTPCsLoop()
