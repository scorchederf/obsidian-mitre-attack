---
aliases: 
    - S0194
    
mitre-attack: https://attack.mitre.org/software/S0194
---

## S0194

[PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. [^15]  [^5]  [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Path Interception by PATH Environment Variable\|T1574.007]] | Path Interception by PATH Environment Variable | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit path interception opportunities in the PATH environment variable.[^15] [^4]  |
| [[Keylogging\|T1056.001]] | Keylogging | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Get-Keystrokes` Exfiltration module can log keystrokes.[^15] [^4]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [PowerSploit](https://attack.mitre.org/software/S0194) reflectively loads a Windows PE file into a process.[^15] [^4]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [PowerSploit](https://attack.mitre.org/software/S0194) has several modules that search the Windows Registry for stored credentials: `Get-UnattendedInstallFile`, `Get-Webconfig`, `Get-ApplicationHost`, `Get-SiteListPassword`, `Get-CachedGPPPassword`, and `Get-RegistryAutoLogon`.[^14]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Find-AVSignature` AntivirusBypass module can be used to locate single byte anti-virus signatures.[^15] [^4]  |
| [[Audio Capture\|T1123]] | Audio Capture | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Get-MicrophoneAudio` Exfiltration module can record system microphone audio.[^15] [^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Invoke-WmiCommand` CodeExecution module uses WMI to execute and retrieve the output from a [PowerShell](https://attack.mitre.org/techniques/T1086) payload.[^15] [^4]  |
| [[Path Interception by Unquoted Path\|T1574.009]] | Path Interception by Unquoted Path | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit unquoted path vulnerabilities.[^15] [^4]  |
| [[Query Registry\|T1012]] | Query Registry | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.[^15] [^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.[^15] [^4]  |
| [[Group Policy Preferences\|T1552.006]] | Group Policy Preferences | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials from Group Policy Preferences.[^15] [^4]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of CodeExecution modules that inject code (DLL, shellcode) into a process.[^15] [^4]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of ScriptModification modules that compress and encode scripts and payloads.[^15] [^4]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Invoke-TokenManipulation` Exfiltration module can be used to manipulate tokens.[^15] [^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and replace/modify service binaries, paths, and configs.[^15] [^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Get-TimedScreenshot` Exfiltration module can take screenshots at regular intervals.[^15] [^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PowerSploit](https://attack.mitre.org/software/S0194)'s `New-UserPersistenceOption` Persistence argument can be used to establish via the `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` Registry key.[^15] [^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [PowerSploit](https://attack.mitre.org/software/S0194)'s `New-UserPersistenceOption` Persistence argument can be used to establish via a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053).[^15] [^4]  |
| [[DLL\|T1574.001]] | DLL | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit DLL hijacking opportunities in services and processes.[^15] [^4]  |
| [[Path Interception by Search Order Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit search order hijacking vulnerabilities.[^15] [^4]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Invoke-Kerberoast` module can request service tickets and return crackable ticket hashes.[^11] [^3]  |
| [[Local Account\|T1087.001]] | Local Account | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Get-ProcessTokenGroup` Privesc-PowerUp module can enumerate all SIDs associated with its current token.[^15] [^4]  |
| [[Security Support Provider\|T1547.005]] | Security Support Provider | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Install-SSP` Persistence module can be used to establish by installing a SSP DLL.[^15] [^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Get-ProcessTokenPrivilege` Privesc-PowerUp module can enumerate privileges for a given process.[^15] [^4]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials from Windows vault credential objects.[^15] [^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PowerSploit](https://attack.mitre.org/software/S0194) modules are written in and executed via [PowerShell](https://attack.mitre.org/techniques/T1086).[^15] [^4]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [PowerSploit](https://attack.mitre.org/software/S0194) has modules such as `Get-NetDomainTrust` and `Get-NetForestTrust` to enumerate domain and forest trusts.[^15] [^4]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials using [Mimikatz](https://attack.mitre.org/software/S0002).[^15] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[APT41\|G0096]] | APT41 |
| [[MuddyWater\|G0069]] | MuddyWater |
| [[FIN7\|G0046]] | FIN7 |
| [[menuPass\|G0045]] | menuPass |
| [[Leviathan\|G0065]] | Leviathan |
| [[TA505\|G0092]] | TA505 |
| [[Patchwork\|G0040]] | Patchwork |



## References

[^1]: [NCC Group TA505](https://research.nccgroup.com/2020/11/18/ta505-a-brief-history-of-their-time/)


[^2]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^3]: [Harmj0y Kerberoast Nov 2016](https://blog.harmj0y.net/powershell/kerberoasting-without-mimikatz/)


[^4]: [PowerSploit Documentation](http://powersploit.readthedocs.io)


[^5]: [PowerShellMagazine PowerSploit July 2014](http://www.powershellmagazine.com/2014/07/08/powersploit/)


[^6]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^7]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^8]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^9]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^10]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^11]: [PowerSploit Invoke Kerberoast](https://powersploit.readthedocs.io/en/latest/Recon/Invoke-Kerberoast/)


[^12]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^13]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^14]: [Pentestlab Stored Credentials](https://pentestlab.blog/2017/04/19/stored-credentials/)


[^15]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


[^16]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


