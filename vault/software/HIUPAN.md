---
aliases: 
    - S1230
    
mitre-attack: https://attack.mitre.org/software/S1230
---

## S1230

[HIUPAN](https://attack.mitre.org/software/S1230) (aka U2DiskWatch) is a is a worm that propagates through removable drives known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2024. [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [HIUPAN](https://attack.mitre.org/software/S1230) has periodically checked for removable and hot-plugged drives connected to the infected machine, should one be found [HIUPAN](https://attack.mitre.org/software/S1230) will propagate to the removeable drives by copying itself and accompanying malware components to a directory to the new drive in a hidden subdirectory `<Drive_Letter>:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\` and hides any other existing files to ensure UsbConfig.exe is the only visible file on the device.[^1] [^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [HIUPAN](https://attack.mitre.org/software/S1230) has modified registry keys to ensure hidden files and extensions are not visible through the modification of `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced`.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [HIUPAN](https://attack.mitre.org/software/S1230) has conducted process discovery to identify the [PUBLOAD](https://attack.mitre.org/software/S1228) malware under the process WCBrowserWatcher.exe and will launch it from an install directory if it is not found.[^2]  |
| [[Delay Execution\|T1678]] | Delay Execution | [HIUPAN](https://attack.mitre.org/software/S1230) has used a config file “$.ini” to store a sleep multiplier to execute at a set interval value prior to initiating a watcher function that checks for a specific running process, that checks for removable drives and installs itself and supporting files if one is available.[^1] [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [HIUPAN](https://attack.mitre.org/software/S1230) has added Registry Run keys to achieve persistence using `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.[^1] [^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [HIUPAN](https://attack.mitre.org/software/S1230) has lured victims into executing malicious files from USBs including the use of files such as USBconfig.exe.[^1] [^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [HIUPAN](https://attack.mitre.org/software/S1230) has modified registry keys to ensure hidden files and extensions are not visible through the modification of `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced`.[^1] [^2]  |
| [[DLL\|T1574.001]] | DLL | [HIUPAN](https://attack.mitre.org/software/S1230) has abused legitimate executables to side-load malicious DLLs to include the legitimate exe UsbConfig.exe.[^1] [^2]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [HIUPAN](https://attack.mitre.org/software/S1230) has checked periodically for removable drives and installs itself when a drive is detected.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^2]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


