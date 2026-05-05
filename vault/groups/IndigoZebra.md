---
aliases: 
    - IndigoZebra
mitre-attack: https://attack.mitre.org/groups/G0136
---

## G0136

[IndigoZebra](https://attack.mitre.org/groups/G0136) is a suspected Chinese cyber espionage group that has been targeting Central Asian governments since at least 2014.[^4] [^1] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Domains\|T1583.001]] | Domains | [IndigoZebra](https://attack.mitre.org/groups/G0136) has established domains, some of which were designed to look like official government domains, for their operations.[^1]  |
| [[Tool\|T1588.002]] | Tool | [IndigoZebra](https://attack.mitre.org/groups/G0136) has acquired open source tools such as [NBTscan](https://attack.mitre.org/software/S0590) and Meterpreter for their operations.[^1] [^2]   |
| [[Web Services\|T1583.006]] | Web Services | [IndigoZebra](https://attack.mitre.org/groups/G0136) created Dropbox accounts for their operations.[^4] [^1]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [IndigoZebra](https://attack.mitre.org/groups/G0136) has compromised legitimate email accounts to use in their spearphishing operations.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [IndigoZebra](https://attack.mitre.org/groups/G0136) sent spearphishing emails containing malicious password-protected RAR attachments.[^4] [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [IndigoZebra](https://attack.mitre.org/groups/G0136) sent spearphishing emails containing malicious attachments that urged recipients to review modifications in the file which would trigger the attack.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [IndigoZebra](https://attack.mitre.org/groups/G0136) has downloaded additional files and tools from its C2 server.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[xCaon\|S0653]] | xCaon | [^1]  |
| [[BoxCaon\|S0651]] | BoxCaon | [^1]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^2]  |



## References

[^1]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^2]: [Securelist APT Trends Q2 2017](https://securelist.com/apt-trends-report-q2-2017/79332/)


[^3]: IndigoZebra


[^4]: [HackerNews IndigoZebra July 2021](https://thehackernews.com/2021/07/indigozebra-apt-hacking-campaign.html)


