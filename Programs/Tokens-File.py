# Copyright (c) 2025 v4lkyr0/v4lkyr_
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import os
    import subprocess
except Exception as e:
    MissingModule(e)

Title("Tokens File")

try:
    file_path = os.path.join(tool_path, "Programs", "Extras", "DiscordTokens.txt")

    print(f"{INFO} Each token must be on a separate line", reset)
    print(f'{LOADING} Opening {red}"{white}DiscordTokens.txt{red}"{white}..', reset)

    try:
        if platform_pc == "Windows":
            os.startfile(file_path)
        else:
            subprocess.Popen(['xdg-open', file_path])
        print(f"{SUCCESS} File opened!", reset)
    except:
        print(f"{ERROR} Error while trying to open file!", reset)
        print(f"{INFO} Path:{red} {file_path}{reset}", reset)

    Continue()
    Reset()

except Exception as e:
    Error(e)