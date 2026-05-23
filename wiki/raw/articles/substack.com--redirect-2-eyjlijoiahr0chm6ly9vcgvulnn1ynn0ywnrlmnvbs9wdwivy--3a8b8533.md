---
title: "Inside TSMC’s Three Extreme Capacity Plays - and How It Helped Shape Cerebras"
url: "https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvY3duZXdzcm9vbS9wL2luc2lkZS10c21jLXRocmVlLWV4dHJlbWUtY2FwYWNpdHktcGxheXMtYW5kLWhvdy1pdC1oZWxwZWQtc2hhcGUtY2VyZWJyYXM_dXRtX3NvdXJjZT1zdWJzdGFjayZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1yZXN0YWNrLWNvbW1lbnQmYWN0aW9uPXJlc3RhY2stY29tbWVudCZyPTJmbHg2JnRva2VuPWV5SjFjMlZ5WDJsa0lqbzBNRGczTkRneUxDSndiM04wWDJsa0lqb3hPVGc0TVRRMU5EWXNJbWxoZENJNk1UYzNPVFF6T1RNNU9Dd2laWGh3SWpveE56Z3lNRE14TXprNExDSnBjM01pT2lKd2RXSXRNelF5TXpRd09DSXNJbk4xWWlJNkluQnZjM1F0Y21WaFkzUnBiMjRpZlEuQUtUNzIyWXA2RXhvZGNBOUVscURQdU8yQUhBOG1tbERScTdXS3AwYWtZUSIsInAiOjE5ODgxNDU0NiwicyI6MzQyMzQwOCwiZiI6dHJ1ZSwidSI6NDA4NzQ4MiwiaWF0IjoxNzc5NDM5Mzk4LCJleHAiOjIwOTUwMTUzOTgsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.rf3vs0vUshGJEN-4cIHVp8Qb4UbQKiIHAHksg2nL7SU?&utm_source=substack&utm_medium=email"
fetched_at: 2026-05-23T04:00:44.454045+00:00
source_date: 2026-05-22
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Inside TSMC’s Three Extreme Capacity Plays - and How It Helped Shape Cerebras

Source: https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvY3duZXdzcm9vbS9wL2luc2lkZS10c21jLXRocmVlLWV4dHJlbWUtY2FwYWNpdHktcGxheXMtYW5kLWhvdy1pdC1oZWxwZWQtc2hhcGUtY2VyZWJyYXM_dXRtX3NvdXJjZT1zdWJzdGFjayZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1yZXN0YWNrLWNvbW1lbnQmYWN0aW9uPXJlc3RhY2stY29tbWVudCZyPTJmbHg2JnRva2VuPWV5SjFjMlZ5WDJsa0lqbzBNRGczTkRneUxDSndiM04wWDJsa0lqb3hPVGc0TVRRMU5EWXNJbWxoZENJNk1UYzNPVFF6T1RNNU9Dd2laWGh3SWpveE56Z3lNRE14TXprNExDSnBjM01pT2lKd2RXSXRNelF5TXpRd09DSXNJbk4xWWlJNkluQnZjM1F0Y21WaFkzUnBiMjRpZlEuQUtUNzIyWXA2RXhvZGNBOUVscURQdU8yQUhBOG1tbERScTdXS3AwYWtZUSIsInAiOjE5ODgxNDU0NiwicyI6MzQyMzQwOCwiZiI6dHJ1ZSwidSI6NDA4NzQ4MiwiaWF0IjoxNzc5NDM5Mzk4LCJleHAiOjIwOTUwMTUzOTgsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.rf3vs0vUshGJEN-4cIHVp8Qb4UbQKiIHAHksg2nL7SU?&utm_source=substack&utm_medium=email

The prospectus has just been filed for what could become the largest IPO in human history: SpaceX.
But what I want to talk about today is another newly filed prospectus — this one from Chinese DRAM maker CXMT (長鑫存儲) in Hefei, which is preparing to list on Shanghai’s STAR Market.
The filing revealed staggering numbers. After posting losses during the same period last year, CXMT reported net profit of RMB 33 billion in the first quarter of this year — more than five times the profit of its Taiwanese rival, Nanya Technology.
The company’s founder and chairman is Yiming Zhu（朱一明）, the founder of NOR Flash maker GigaDevice（兆易創新）, whom I wrote about four years ago as a major threat to Macronix（旺宏）. At the time, the article’s headline was: “Which Chinese Semiconductor Company Should Taiwan Be Most Concerned About?”
That headline still holds true today — and the threat posed by China’s red supply chain has only expanded further.
A senior executive at a major memory company recently told me that another Chinese memory giant, YMTC（長江存儲）, which specializes in NAND Flash, is expected to become the world’s largest flash manufacturer by 2030.
After being placed on the U.S. Entity List, YMTC has been working aggressively to replace all equipment on its new production lines with domestically sourced Chinese tools. The company expects the buildout of these fully localized production lines to be completed by 2030.
The executive also shared a story with me. In 2022, when the U.S. announced sanctions on YMTC and required all engineers from U.S. equipment vendors supporting the company to withdraw immediately, those foreign engineers reportedly went to hotels in downtown Wuhan that same afternoon to apply for jobs at YMTC. They were all hired on the spot, reissued access badges by HR, and continued maintaining the same U.S.-made equipment they had previously supported.
These two companies — YMTC and CXMT — have effectively become China’s national champions in memory, and may emerge as the biggest beneficiaries of the current memory supercycle.
Originally, amid the increasingly tense atmosphere of “one world, two systems,” many companies led by the United States had approached Chinese memory suppliers with extreme caution.
But under the pressure of today’s severe shortages, some PC brands have quietly begun adopting Chinese memory products.
As Phison（群聯） CEO K.S. Pua（潘健成） once said: “In a famine, do you really care where the rice was grown?”
Back to this issue of the newsletter.
This edition takes a deep dive into the recently concluded TSMC Technology Symposium in Hsinchu.
From presentations delivered by executives led by TSMC Senior Vice President of Business Development and Global Sales and Deputy Co-Chief Operating Officer Kevin Zhang（張曉強）, I realized the event revealed not only why Cerebras — an IC startup long nurtured by TSMC and what could become one of the largest semiconductor IPOs in history — has suddenly exploded into prominence, but also what may determine the winners of the next wave of AI hardware.
Please enjoy this issue of the newsletter.
