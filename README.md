# Kadence Lead Agent

An AI agent for Kadence Lab (My business) that finds, scores and drafts outreach to sales leads. You ask it something in plain English, like "find fast food leads in Birmingham and score them", and Claude decides which Python tools to call to answer it.

This is just an example. It runs on a small set of sample leads while I build out the real data side.

## What it can do

- **Search leads** by city, industry and company size
- **Look up a company** and return everything we have on it
- **Score a lead** out of 10 against my ideal customer, with the reasons for the score
- **Draft a cold email** to a lead and save it as a text file. It never sends anything.

It can chain these together. One question like "find fast food leads in Birmingham, score them, and draft an email to the best one" makes it search, then score each result, then write the email.

## How it works

The agent uses Claude's tool calling. Claude never runs code itself. It asks for a tool, my code runs it and sends the result back, and that repeats until Claude has enough to answer.

```
1. Send the question to Claude, along with descriptions of the 4 tools
2. Claude replies with either an answer, or a request to run a tool
3. If it's a tool request, run the matching Python function
4. Send the results back to Claude
5. Repeat until Claude stops asking for tools, then print its answer
```

A system prompt (`kadence_prompt.txt`) tells Claude what Kadence does, who we sell to, and how our emails should sound.

## Design decisions

**Rules live in the code.** Scoring is done in Python with fixed rules (company size, MRR, market cap), so the same lead always gets the same score. Claude's job is to explain and rank the scores, not invent them. I learned this on my last project, where asking an LLM to follow strict rules gave inconsistent results.

**Drafts only.** The email tool saves a draft to the `draft email/` folder. Nothing gets sent without a person reading it first.

**Forgiving inputs.** Searches ignore capital letters, so "Birmingham" and "birmingham" both work. City and industry are optional, so "companies in Leeds" works without naming an industry.

**Handles more than one tool at once.** If Claude asks for several tools in one go, all the results go back in a single message, which is the format the API expects.

**Doesn't crash on a normal reply.** If Claude just answers without needing a tool (e.g. "hi"), the loop is skipped and it prints the answer.

## Project structure

```
main.py              # the lead data and the 4 tool functions
LLM.py               # tool definitions for Claude and the agent loop
kadence_prompt.txt   # system prompt describing Kadence Lab
draft email/         # where drafted emails are saved
README.md            # This doc
```

## Run it locally

```bash
git clone https://github.com/Scotty212/<kadence-agent>.git
cd <kadence-agent>
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic python-dotenv
```

Create a `.env` file with your Anthropic API key:

```
ANTHROPIC_API_KEY=your-key-here
```

Put your question in the `messages` line in `LLM.py`, then run:

```bash
python LLM.py
```

## Example

Question: `companies in brum`

```
I found 2 companies in Birmingham (I took "brum" to mean Birmingham):

1. Dominoes: fast food, about 200 staff. Contact: mo (mo@gmail.com)
2. JD: retailer, about 200 staff. Contact: mo (mo@gmail.com)

Both entries list the same contact email, so it may be worth checking
it before reaching out.
```

Claude worked out that "brum" means Birmingham, the code did the filtering, and it even spotted a duplicate contact in the sample data.

## Roadmap

- [ ] Real leads from the Apollo API instead of sample data
- [ ] SQLite database to store leads, scores, drafts and who's been contacted
- [ ] Streamlit chat interface instead of editing the question in the code
- [ ] Scoring rules set per client instead of hard-coded
- [ ] Save drafts straight into Gmail as drafts
- [ ] Tests that check the agent gives the right answers

## Tech

- Python
- Anthropic API (Claude, tool calling)
- python-dotenv for keeping the API key out of the code
