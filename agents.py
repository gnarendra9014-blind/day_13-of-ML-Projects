import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def pro_agent(topic: str, round_num: int, opponent_arg: str = "") -> str:
    if round_num == 1:
        prompt = f"""You are a skilled debate champion arguing FOR this topic.
Topic: {topic}
Give a powerful opening argument in 3-4 sentences.
Use specific facts, logic, and compelling examples.
Be confident and persuasive."""
    elif round_num == 2:
        prompt = f"""You are a skilled debate champion arguing FOR: {topic}
Your opponent just said: {opponent_arg}
Rebuttal: Directly counter their argument in 3-4 sentences.
Then reinforce your position with a new strong point."""
    else:
        prompt = f"""You are a skilled debate champion arguing FOR: {topic}
Give a powerful closing argument in 2-3 sentences.
Summarize why your position wins. End with impact."""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    return res.choices[0].message.content

def con_agent(topic: str, round_num: int, opponent_arg: str = "") -> str:
    if round_num == 1:
        prompt = f"""You are a skilled debate champion arguing AGAINST this topic.
Topic: {topic}
Give a powerful opening argument in 3-4 sentences.
Use specific facts, logic, and compelling examples.
Be confident and persuasive."""
    elif round_num == 2:
        prompt = f"""You are a skilled debate champion arguing AGAINST: {topic}
Your opponent just said: {opponent_arg}
Rebuttal: Directly counter their argument in 3-4 sentences.
Then reinforce your position with a new strong point."""
    else:
        prompt = f"""You are a skilled debate champion arguing AGAINST: {topic}
Give a powerful closing argument in 2-3 sentences.
Summarize why your position wins. End with impact."""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    return res.choices[0].message.content

def judge_agent(topic: str, pro_args: list, con_args: list) -> dict:
    pro_full = "\n\n".join([f"Round {i+1}: {a}" for i, a in enumerate(pro_args)])
    con_full = "\n\n".join([f"Round {i+1}: {a}" for i, a in enumerate(con_args)])

    prompt = f"""You are an impartial debate judge. Score this debate fairly.

Topic: {topic}

PRO ARGUMENTS:
{pro_full}

CON ARGUMENTS:
{con_full}

Score each side on: Logic (1-10), Evidence (1-10), Persuasion (1-10)
Reply in EXACTLY this format:
PRO_LOGIC: X
PRO_EVIDENCE: X
PRO_PERSUASION: X
CON_LOGIC: X
CON_EVIDENCE: X
CON_PERSUASION: X
WINNER: PRO or CON
VERDICT: two sentence explanation of why this side won"""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
    )
    return parse_judgment(res.choices[0].message.content)

def parse_judgment(text: str) -> dict:
    result = {
        "raw": text,
        "winner": "UNKNOWN",
        "pro_score": 0,
        "con_score": 0,
        "verdict": ""
    }
    pro_total, con_total = 0, 0
    for line in text.split("\n"):
        if "PRO_" in line and ":" in line:
            try: pro_total += int(line.split(":")[-1].strip())
            except: pass
        elif "CON_" in line and ":" in line and "WINNER" not in line:
            try: con_total += int(line.split(":")[-1].strip())
            except: pass
        elif "WINNER:" in line:
            result["winner"] = "PRO" if "PRO" in line.split(":")[-1] else "CON"
        elif "VERDICT:" in line:
            result["verdict"] = line.split("VERDICT:", 1)[-1].strip()
    result["pro_score"] = pro_total
    result["con_score"] = con_total
    return result