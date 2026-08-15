---
title: "kvcache-ai/AgentENV: AgentENV (AENV) is a distributed platform for running agent environments at scale. · GitHub"
url: "https://substack.com/redirect/82817be0-aa56-4d92-a39d-d2bc62a2e0b7?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-08-04T04:00:36.465281+00:00
source_date: 2026-08-03
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# kvcache-ai/AgentENV: AgentENV (AENV) is a distributed platform for running agent environments at scale. · GitHub

Source: https://substack.com/redirect/82817be0-aa56-4d92-a39d-d2bc62a2e0b7?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Running agent environments at scale
📖
Full documentation
AgentENV (AENV) is a platform for running agent environments at scale, powering agentic RL training for
Kimi K3
.
Scale across diverse environments
: AENV runs massive numbers of Firecracker environments across machines and diverse OCI-compatible images, loaded on demand via
overlaybd
. Local disk acts as a bounded cache, retaining hot data and evicting cold, so images can exceed disk capacity while startup stays fast cluster-wide, without pre-warming every host.
Make idle environments inexpensive
: Snapshot-backed environments boot or resume in under 50 ms and pause in under 100 ms. Idle environments can quickly release CPU and memory, then return when new work arrives.
Native snapshot and fork support
: AENV snapshots memory and filesystem changes incrementally, completing in under 100 ms even under heavy disk modification. A running environment can fork into multiple independent sandboxes for parallel agent workflows. Snapshots persist to S3-compatible object storage or a shared distributed filesystem to prevent data loss.
Preserve performance and density over time
: AENV delivers high-performance I/O via ublk while sharing the host page cache across storage and memory-snapshot data. Memory ballooning returns reclaimable guest memory to the host, sustaining high overcommit as environments run longer and diverge.
Linux kernel 6.8+
; the install script additionally requires
Ubuntu 24.04
(see
Quick Start
below for installation options)
/dev/kvm
access for Firecracker microVM execution
If your server does not support standard KVM, see the
PVM deployment guide
before installing.
⚡ Quick Start (Single Node)
Warning
AgentENV currently does not support authorization.
Do not expose the AgentENV
API to the public network. Run it only on a trusted network or behind an
authorization proxy with appropriate network controls.
1. Install and start the server
Option A — install script (Ubuntu 24.04)
Install both the server and the
aenv
CLI, then start the server as a systemd service:
curl -fsSL https://raw.githubusercontent.com/kvcache-ai/AgentENV/main/scripts/install.sh
|
sudo bash
sudo systemctl start aenv
If this installation fails because standard KVM is unavailable, follow the
PVM deployment guide
instead.
Option B — Docker
Set up the server:
curl -fsSL https://raw.githubusercontent.com/kvcache-ai/AgentENV/main/scripts/docker-setup.sh
|
sudo bash
docker pull ghcr.io/kvcache-ai/aenv-server:latest
docker run -d --privileged -v /dev:/dev -p 8000:8000 ghcr.io/kvcache-ai/aenv-server:latest
The server is accessible at
http://127.0.0.1:8000
by default.
2. Install the aenv CLI
(skip if you used Option A in step 1)
Install separately if you used the Docker method above, or if you are running
the CLI on a different machine from the server. Supports Linux and macOS on
x86_64 and arm64:
curl -fsSL https://raw.githubusercontent.com/kvcache-ai/AgentENV/main/scripts/install-cli.sh
|
bash
3. Authenticate
aenv auth
#
AENV server URL [http://localhost:8000]: http://127.0.0.1:8000
#
API key: dummy
4. Pull a template and run a sandbox
aenv pull ubuntu:22.04 --name ubuntu
aenv start ubuntu
#
starts a sandbox and attaches an interactive shell
For Docker Compose / Kubernetes cluster deployment and build-from-source instructions,
see 📖
Deployment
.
AgentENV exposes an E2B-compatible HTTP API. Point
E2B_API_URL
at your
server and use the standard E2B Python / TypeScript SDK without any code
changes. See 📖
E2B integration
for setup details.
#
Templates
aenv pull docker.io/library/ubuntu:latest --name ubuntu
#
FROM <image> → template
aenv template list
#
alias: aenv template ls
#
Sandboxes
aenv start ubuntu
#
start + attach interactive shell
aenv start ubuntu --detach
#
start, print sandbox ID, don't attach
aenv cn
<
sandbox-id
>
#
reattach a shell
aenv
exec
<
sandbox-id
>
ls -la /
#
one-shot command
aenv ls

aenv pause
<
sandbox-id
>
aenv resume
<
sandbox-id
>
aenv timeout
<
sandbox-id
>
600
#
extend TTL to 600 s from now
aenv delete
<
sandbox-id
>
#
alias: aenv rm
aenv start
accepts a template UUID or human-readable name/alias.
aenv list
outputs a table on TTY and JSON when piped; override with
--output table|json
.
Bug reports, feature proposals, documentation fixes, and pull requests are welcome. Please read
CONTRIBUTING.md
before opening an issue or submitting a change.
Follow
SECURITY.md
to report security vulnerabilities privately; do not disclose them in a public issue.
