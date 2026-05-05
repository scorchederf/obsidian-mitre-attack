---
aliases: 
    - Mofang
mitre-attack: https://attack.mitre.org/groups/G0103
---

## G0103

[Mofang](https://attack.mitre.org/groups/G0103) is a likely China-based cyber espionage group, named for its frequent practice of imitating a victim's infrastructure. This adversary has been observed since at least May 2012 conducting focused attacks against government and critical infrastructure in Myanmar, as well as several other countries and sectors including military, automobile, and weapons industries.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Mofang](https://attack.mitre.org/groups/G0103) delivered spearphishing emails with malicious links included.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Mofang](https://attack.mitre.org/groups/G0103)'s spearphishing emails required a user to click the link to connect to a compromised website.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Mofang](https://attack.mitre.org/groups/G0103) delivered spearphishing emails with malicious documents, PDFs, or Excel files attached.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Mofang](https://attack.mitre.org/groups/G0103) has encrypted payloads before they are downloaded to victims.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Mofang](https://attack.mitre.org/groups/G0103)'s malicious spearphishing attachments required a user to open the file after receiving.[^1]  |
| [[Compression\|T1027.015]] | Compression | [Mofang](https://attack.mitre.org/groups/G0103) has compressed the [ShimRat](https://attack.mitre.org/software/S0444) executable within malicious email attachments.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ShimRatReporter\|S0445]] | ShimRatReporter |  |
| [[ShimRat\|S0444]] | ShimRat |  |



## References

[^1]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


