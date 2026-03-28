from agents import pro_agent, con_agent, judge_agent

def run_debate(topic: str) -> dict:
    print(f"\n{'='*60}")
    print(f"DEBATE TOPIC: {topic}")
    print(f"{'='*60}\n")

    pro_args = []
    con_args = []

    # Round 1 — Opening arguments
    print("ROUND 1 — Opening Arguments")
    print("-"*40)

    print("\nAgent PRO:")
    pro_r1 = pro_agent(topic, 1)
    print(pro_r1)
    pro_args.append(pro_r1)

    print("\nAgent CON:")
    con_r1 = con_agent(topic, 1)
    print(con_r1)
    con_args.append(con_r1)

    # Round 2 — Rebuttals
    print("\nROUND 2 — Rebuttals")
    print("-"*40)

    print("\nAgent PRO (rebutting CON):")
    pro_r2 = pro_agent(topic, 2, con_r1)
    print(pro_r2)
    pro_args.append(pro_r2)

    print("\nAgent CON (rebutting PRO):")
    con_r2 = con_agent(topic, 2, pro_r1)
    print(con_r2)
    con_args.append(con_r2)

    # Round 3 — Closing arguments
    print("\nROUND 3 — Closing Arguments")
    print("-"*40)

    print("\nAgent PRO:")
    pro_r3 = pro_agent(topic, 3)
    print(pro_r3)
    pro_args.append(pro_r3)

    print("\nAgent CON:")
    con_r3 = con_agent(topic, 3)
    print(con_r3)
    con_args.append(con_r3)

    # Judge decides
    print("\nJUDGE DELIBERATING...")
    judgment = judge_agent(topic, pro_args, con_args)

    print(f"\n{'='*60}")
    print("FINAL JUDGMENT")
    print(f"{'='*60}")
    print(f"PRO Score:  {judgment['pro_score']}/30")
    print(f"CON Score:  {judgment['con_score']}/30")
    print(f"WINNER:     {judgment['winner']}")
    print(f"VERDICT:    {judgment['verdict']}")
    print(f"{'='*60}\n")

    return judgment