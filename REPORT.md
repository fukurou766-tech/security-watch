# 🛡️ 脆弱性情報ダッシュボード

**最終取得：2026-10-22 22:58 JST**

**取得件数：35件**（CISA KEVの直近35件とJVNの直近40件を上限）

> ⚠️ CISAの英語本文は翻訳APIを使用していないため、英語原文です。Android Chromeの「翻訳」で日本語表示できます。

## 取得時の注意
- JVN: HTTP Error 503: Service Unavailable
- JVN: HTTP Error 503: Service Unavailable
- JVN: RSSを取得できませんでした

## 🎯 業務に関係しそうな情報

### Microsoft Windows — CVE-2026-96951
**緊急（悪用確認）** · CISA KEV · 2026-10-13

Microsoft Windows Shell contains a command injection vulnerability that allows an unauthorized attacker to bypass a security feature over a network.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### ONLYOFFICE Docs — CVE-2021-3199
**緊急（悪用確認）** · CISA KEV · 2026-10-08

ONLYOFFICE Docs contains a path traversal vulnerability that can occur when JWT is used, via a /.. sequence in an image upload parameter and could allow for remote code execution.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Microsoft SharePoint — CVE-2026-65660
**緊急（悪用確認）** · CISA KEV · 2026-09-25

Microsoft SharePoint contains a code injection vulnerability which could allow an authorized attacker to execute code over a network.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

## 🆕 その他の新着情報

### EG Secure Solutions SiteGuard Server Edition — CVE-2026-106931
**緊急（悪用確認）** · CISA KEV · 2026-10-20

EG Secure Solutions SiteGuard Server Edition contains an OS command injection vulnerability which may allow an attacker to execute arbitrary OS commands with root or SYSTEM privileges on the system running the affected product.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Plex Media Server — CVE-2026-96656
**緊急（悪用確認）** · CISA KEV · 2026-10-20

Plex Media Server contains an external control of file name or path vulnerability which can allow an admin user to write arbitrary files that may be executed on load. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96654, and CVE-2026-96655.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Plex Media Server — CVE-2026-96655
**緊急（悪用確認）** · CISA KEV · 2026-10-20

Plex Media Server contains a server-side request forgery (SSRF) vulnerability that could allow an authenticated user to request arbitrary internal or external addresses via the '/video/:/transcode/universal' path parameter. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96654, and CVE-2026-96656.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Plex Media Server — CVE-2026-96654
**緊急（悪用確認）** · CISA KEV · 2026-10-20

Plex Media Server contains an improper neutralization of encoded URI schemes in a web page vulnerability that could allow an attacker to call other plugins' functions and supply their own parameters. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96655, and CVE-2026-96656.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Plex Media Server — CVE-2026-96652
**緊急（悪用確認）** · CISA KEV · 2026-10-20

Plex Media Server contains a server-side request forgery (SSRF) vulnerability which could allow an attacker using any X-Plex-Token value to include a full URL in the 'protocol' parameter and force the Plex server to POST to the attacker's chosen destination. This vulnerability can be chained with CVE-2026-96654, CVE-2026-96655, and CVE-2026-96656.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Siemens Software Center — CVE-2026-110936
**緊急（悪用確認）** · CISA KEV · 2026-10-20

Siemens Software Center contains an uncontrolled search path element vulnerability that could allow an authenticated local attacker to place a specially crafted DLL in a directory that the application searches, leading to arbitrary code execution with the privileges of the affected application.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### BeyondTrust Remote Support — CVE-2026-102764
**緊急（悪用確認）** · CISA KEV · 2026-10-16

BeyondTrust Remote Support contains an authentication bypass by spoofing vulnerability that could allow a remote attacker to perform file operations on the appliance.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Fortinet Multiple Products — CVE-2025-61624
**緊急（悪用確認）** · CISA KEV · 2026-10-16

FortiOS, FortiPAM, FortiProxy, and FortiSwitchManager contain a path traversal vulnerability that may allow an authenticated attacker with admin profile and at least read-write permissions to write or delete arbitrary files via specific CLI commands.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Atlassian Multiple Products — CVE-2026-21589
**緊急（悪用確認）** · CISA KEV · 2026-10-15

Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an unauthenticated attacker to access specific files within the web application root directory in affected versions.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Ahsay AhsayCBS — CVE-2026-105134
**緊急（悪用確認）** · CISA KEV · 2026-10-14

Ahsay AhsayCBS contains a command injection vulnerability that could allow a remote attacker to execute operating system commands via manipulation of the random parameter in the Replication Receiver component’s /rps/api/json/UpdateReceivers.do endpoint. This vulnerability can be chained with CVE-2026-105133.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Cisco Secure Email Gateway — CVE-2026-76519
**緊急（悪用確認）** · CISA KEV · 2026-10-14

Cisco Secure Email Gateway contains a relative path traversal vulnerability that could allow an unauthenticated, remote attacker to write arbitrary files on the underlying operating system.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Ahsay AhsayCBS — CVE-2026-105133
**緊急（悪用確認）** · CISA KEV · 2026-10-14

Ahsay AhsayCBS contains an improper authentication vulnerability that could allow a remote attacker to bypass authentication via manipulation of the random parameter in the API component’s checkSysPwd function. This vulnerability can be chained with CVE-2026-105134.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Palo Alto Networks PAN-OS — CVE-2026-0322
**緊急（悪用確認）** · CISA KEV · 2026-10-14

Palo Alto Networks PAN-OS contains a code injection vulnerability that could allow an authenticated attacker with network access to execute arbitrary code with root privileges on the firewall.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Ivanti Connect Secure — CVE-2026-104935
**緊急（悪用確認）** · CISA KEV · 2026-10-13

Ivanti Connect Secure contains an authentication bypass by spoofing vulnerability that allows a remote unauthenticated attacker to execute arbitrary commands.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### ISC BIND — CVE-2015-5477
**緊急（悪用確認）** · CISA KEV · 2026-10-08

ISC BIND contains a data processing errors vulnerability that could allow remote attackers to cause a denial of service via TKEY queries.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Apache Struts — CVE-2016-3081
**緊急（悪用確認）** · CISA KEV · 2026-10-08

Apache Struts contains a command injection vulnerability that could allow remote attackers to execute arbitrary code via method:prefix when Dynamic Method Invocation is enabled.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Strapi Strapi — CVE-2023-22894
**緊急（悪用確認）** · CISA KEV · 2026-10-08

Strapi contains a cleartext storage of sensitive information vulnerability that could allow attackers with access to the admin panel to discover sensitive user details via the query filter. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version. This vulnerability can be chained with CVE-2023-22621 to achieve remote code execution.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### ProFTPD ProFTPD — CVE-2015-3306
**緊急（悪用確認）** · CISA KEV · 2026-10-08

ProFTPD contains an improper access control vulnerability that could allow remote attackers to read and write to arbitrary files via the site cpfr and site cpto commands.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Citrix NetScaler — CVE-2026-88779
**緊急（悪用確認）** · CISA KEV · 2026-10-04

Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway) contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for a denial of service.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Zammad GmbH Zammad — CVE-2026-102490
**緊急（悪用確認）** · CISA KEV · 2026-10-02

Zammad GmbH Zammad contains an improper privilege management vulnerability that can allow the local zammad user to escalate privileges to root. This vulnerability can be chained with CVE-2026-102489.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Zammad GmbH Zammad — CVE-2026-102489
**緊急（悪用確認）** · CISA KEV · 2026-10-02

Zammad GmbH Zammad contains a session fixation vulnerability that can lead to remote code execution as the zammad user. This vulnerability can be chained with CVE-2026-102490.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Fortinet FortiMail — CVE-2026-104286
**緊急（悪用確認）** · CISA KEV · 2026-10-01

Fortinet FortiMail contains a path traversal and an improper neutralization of NULL byte or NULL character vulnerability that may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Cisco Catalyst SD-WAN Manager — CVE-2026-76504
**緊急（悪用確認）** · CISA KEV · 2026-09-30

Cisco Catalyst SD-WAN Manager contains a hex encoding vulnerability that could allow an unauthenticated, remote attacker to access an affected system with privileges of the admin user due to improper handling of URI encoding in an HTTP request.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Apple Multiple Products — CVE-2026-86950
**緊急（悪用確認）** · CISA KEV · 2026-09-29

Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Citrix NetScaler — CVE-2026-88772
**緊急（悪用確認）** · CISA KEV · 2026-09-27

Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Citrix NetScaler — CVE-2026-88771
**緊急（悪用確認）** · CISA KEV · 2026-09-27

Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### MikroTik RouterOS — CVE-2026-67279
**緊急（悪用確認）** · CISA KEV · 2026-09-25

Mikrotik RouterOS contains an improper enforcement of behavioral workflow vulnerability that could allow an unauthenticated client to open a session channel and send an exec request. This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### WordPress Core — CVE-2026-87902
**緊急（悪用確認）** · CISA KEV · 2026-09-25

WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### WSO2 Multiple Products — CVE-2026-5430
**緊急（悪用確認）** · CISA KEV · 2026-09-24

WSO2 API Control Plane, API Manager, Traffic Manager & Universal Gateway contain a path traversal vulnerability that could allow for unrestricted file upload and lead to remote code execution.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Adobe Commerce and Magento — CVE-2026-71362
**緊急（悪用確認）** · CISA KEV · 2026-09-24

Adobe Commerce and Magento contains an incorrect authorization vulnerability that could allow an attacker to leverage this vulnerability to gain elevated access to sensitive resources without any user interaction.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### Arista VeloCloud Orchestrator — CVE-2026-93952
**緊急（悪用確認）** · CISA KEV · 2026-09-22

Arista VeloCloud Orchestrator (VCO) on-prem contains an improper input validation vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---

### F5 BIG-IP APM — CVE-2026-94127
**緊急（悪用確認）** · CISA KEV · 2026-09-22

F5 BIG-IP APM contains a heap-based buffer overflow vulnerability when access policy and an OAuth profile are configured on a virtual server. This vulnerability could allow an unauthenticated attacker to perform remote code execution.

**対策：** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[公式情報を見る](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

---
