---
title: "ChinAI #367: Claude Code's Future in China?"
url: "https://open.substack.com/pub/chinai/p/chinai-367-claude-codes-future-in?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&action=restack-comment&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc3MTc0MTIsImlhdCI6MTc4NDU0Njc2MiwiZXhwIjoxNzg3MTM4NzYyLCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.rF15SXOE3NFyq_3OhLlU6VpFIytg8v_5QN3PYtHoL-s&utm_source=substack&utm_medium=email"
fetched_at: 2026-07-23T04:01:08.389385+00:00
source_date: 2026-07-20
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# ChinAI #367: Claude Code's Future in China?

Source: https://open.substack.com/pub/chinai/p/chinai-367-claude-codes-future-in?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&action=restack-comment&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDc3MTc0MTIsImlhdCI6MTc4NDU0Njc2MiwiZXhwIjoxNzg3MTM4NzYyLCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.rF15SXOE3NFyq_3OhLlU6VpFIytg8v_5QN3PYtHoL-s&utm_source=substack&utm_medium=email

Greetings from a world where…
North American league of legends is not closing the gap
…As always, the searchable archive of all past issues is
here
. Please please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).
When scanning for Around the Horn articles a few weeks back, one story dominated the Chinese tech media landscape:
In the April 2026 release of Claude Code, Anthropic quietly added some code aimed at identifying Chinese users. After people figured out what was happening, Anthropic framed the move as an effort to guard against distillation and announced a rollback. In the wake of this revelation, Alibaba has issued an
internal mandate
to remove all Claude software from employee computers.
Additionally, on July 8, China’s National Vulnerability Database warned about a security backdoor risk in Claude Code. In this week’s issue, I wanted to get deeper into this story and try to understand the future of Claude Code in China.
To start, however, we need to understand the past and present of Claude Code in China. Afra Wang, who writes the excellent
Concurrent newsletter
, provided a
temperature check
in January 2026 when she visited Shanghai:
I’ve been deep in the tech scene across hangzhou, liangzhu, and shanghai, meeting a few dozens of devs who are working on ai. a big revelation is…so far, probably due to some confirmation bias, not a single one is using Chinese coding tools.
they’re all on Claude Code/Antigravity/Codex/Cursor
.
Of these tools, Claude was the most frequently mentioned model.
Okay, so six months later, now, there’s this firestorm over a tracker that secretly monitors Claude Code users in China. By the way, the ClaudeAI subreddit
consensus
sees this as a “reasonable, if sneaky, way for Anthropic to combat the rampant unauthorized resale and model distillation by Chinese labs.” Remember, Anthropic’s
terms and conditions
technically prohibit the use of its services in China. In any case, Anthropic engineer
Thariq Shihipar
stated that this was an experiment that would be fully rolled back in the next release.
So, Alibaba issues this internal Claude ban. What about all other coders who use Claude? To conduct a vibe check, I turned to a Zhihu thread on this topic: “Alibaba is set to completely ban Claude Code due to backdoor security risks;
what kind of ripple effects might this trigger
?” This thread has generated 1.6 million views and 315 responses. Let’s go through the top three responses:
gingercat (784 upvotes) gives a typical technonationalist responses: “Claude is going overboard. It is essentially the U.S. company that is second most unfriendly to China. That’s right, TikTok is number one…”
On July 3, Morgan [程墨] (1472 upvotes) penned a fascinating take, seemingly based on a lot of insider industry knowledge:
Alibaba has set a precedent.
CTOs at major tech companies across China will be grappling with this issue over the weekend. Because on Monday morning, someone is bound to ask at the staff meeting: “Alibaba has banned it, should we?”
For a long time, the attitude of big tech firms toward Claude Code was essentially “secretly use it.” While they paid lip service to security and compliance, actions don’t lie. Who doesn’t know that Claude Code is touted as the world’s most powerful coding assistant? Who wouldn’t want to double their programmers’ productivity? Yet, these companies couldn’t officially procure Claude Code; Anthropic is hostile toward China; plus, Chinese firms simply cannot purchase it directly.
In actual practice, the procedure is: The company stays out of it, leaving employees to handle it themselves, using personal subscriptions, intermediaries, having friends pay on their behalf — each finding their own creative solution.
Companies would turn a blind eye, or even reimburse the costs. Now, Anthropic has blown the lid off this arrangement.
In truth, Chinese big tech firms knew all along that Anthropic had ways to detect Chinese users—how else could they ban accounts with such pinpoint accuracy…Who could have imagined that Anthropic had actually embedded a backdoor directly into the client?…Now, major tech firms can no longer afford to do nothing.
I predict that, by next Monday, all mainstream tech companies in China will issue a ban on Claude Code
…the landscape has shifted, however, as domestic models are now making significant strides in coding capabilities…Alibaba has promoted its in-house “Qoder” as an alternative; ByteDance has MarsCode; Tencent has Code Buddy; and Baidu has Comate…Yet, these tools have long faced an awkward reality: the companies’ own programmers rarely use them…the situation has changed—Claude Code is banned, so you have no choice but to use the internal tools. Any tool will inevitably improve if it has a sufficient user base and receives continuous feedback.
This move represents a decoupling from Anthropic by China’s major tech firms; in the future, they will no longer hope for Claude Code.
Everyone is striking out on their own, leaving the market to ultimately decide the winners and losers.
Zhihu user [anonymous] (691 upvotes):
Here is a story illustrating the reverse scenario: Alibaba’s component library, Ant Design, once inserted a Christmas “Easter egg” without notifying users. When the system detected the date as December 25th, it would change the default button style to a snow-covered look, and the alt text (which primarily affects assistive screen readers) would change to the sound of Santa Claus laughing. This incident drew a storm of fierce criticism against Ant Design and Alibaba; many users labeled it a “backdoor,” and some major tech companies even required their employees to migrate to other frameworks. It would be truly bizarre if a company were to tolerate the kind of approach Anthropic is taking here.
I thought Morgan’s response was the most interesting but also overblown. Contrary to that poster’s prediction, Chinese tech firms have not all internally banned Claude Code. Notably, if you read the aforementioned Chinese government’s National Vulnerability Database warning, it even advises users to “uninstall the affected versions
or upgrade to the latest secure version in which the relevant backdoor code has been removed
.”
This vulnerability database recognizes that developers might not be so willing to give up on Claude Code.
Ultimately, the answer to this week’s big question will depend on the capabilities of Chinese AI coding assistants. By one metric, Alibaba’s Qoder appears to be leading the way. According to a recent IDC report, it holds
47.6%
of the Chinese AI coding market. The linked
Leiphone analysis
provides more details about why Alibaba has captured so much of the market. However, though I haven’t been able to find the methodology of the full IDC report, I would guess that they get their data from company surveys, which reflects on-paper adoption, not necessarily actual usage (individual employees just use Claude Code instead of the company-provided tool).
After all that, I conclude that the Claude Code’s future in China is…cloudy. A swift decoupling always sounds easy — it’ll always happen by next Monday! — but it’s never that easy to let go.
These are Jeff Ding’s (sometimes) weekly translations of Chinese-language musings on AI and related topics. Jeff is an Assistant Professor of Political Science at George Washington University.
Check out the archive of all past issues
here
& please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay for a subscription will support access for all).
Any suggestions or feedback? Let me know at chinainewsletter@gmail.com or on Twitter at
@jjding99
