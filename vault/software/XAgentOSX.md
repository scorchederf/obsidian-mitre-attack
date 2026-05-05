---
aliases: 
    - S0161
    
mitre-attack: https://attack.mitre.org/software/S0161
---

## S0161

[XAgentOSX](https://attack.mitre.org/software/S0161) is a trojan that has been used by [APT28](https://attack.mitre.org/groups/G0007)  on OS X and appears to be a port of their standard [CHOPSTICK](https://attack.mitre.org/software/S0023) or XAgent trojan. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [XAgentOSX](https://attack.mitre.org/software/S0161) contains keylogging functionality that will monitor for active application windows and write them to the log, it can handle special characters, and it will buffer by default 50 characters before sending them out over the C2 infrastructure.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the getInfoOSX function to return the OS X version as well as the current user.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the readFiles function to return a detailed listing (sometimes recursive) of a specified directory.[^2]  [XAgentOSX](https://attack.mitre.org/software/S0161) contains the showBackupIosFolder function to check for IOS device backups by running `ls -la ~/Library/Application\ Support/MobileSync/Backup/`.[^2]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the ftpUpload function to use the FTPManager:uploadFile method to upload files from the target system.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the getFirefoxPassword function to attempt to locate Firefox passwords.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the getProcessList function to run `ps aux` to get running processes.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the takeScreenShot (along with startTakeScreenShot and stopTakeScreenShot) functions to take screenshots using the CGGetActiveDisplayList, CGDisplayCreateImage, and NSImage:initWithCGImage methods.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the getInstalledAPP function to run `ls -la /Applications` to gather what applications are installed.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the deletFileFromPath function to delete a specified file using the NSFileManager:removeFileAtPath method.[^2]  |
| [[Native API\|T1106]] | Native API | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the execFile function to execute a specified file on the system using the NSTask:launch method.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [US District Court Indictment GRU Oct 2018](https://www.justice.gov/opa/page/file/1098481/download)


[^2]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)


[^3]: XAgentOSX


[^4]: [Symantec APT28 Oct 2018](https://www.symantec.com/blogs/election-security/apt28-espionage-military-government)


[^5]: OSX.Sofacy


