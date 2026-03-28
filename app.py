from debate import run_debate

SAMPLE_TOPICS = [
    "AI will replace software engineers within 10 years",
    "Remote work is better than office work",
    "Social media does more harm than good",
    "Python is better than JavaScript for AI development",
    "Open source AI models are safer than closed source",
]

def main():
    print("\n=== Multi-Agent Debate System ===")
    print("3 AI agents. 3 rounds. 1 winner.\n")
    print("Sample topics:")
    for i, topic in enumerate(SAMPLE_TOPICS):
        print(f"  {i+1}. {topic}")

    choice = input("\nEnter topic number or type your own topic: ").strip()

    try:
        idx = int(choice) - 1
        topic = SAMPLE_TOPICS[idx]
    except:
        topic = choice

    if not topic:
        print("No topic entered.")
        return

    run_debate(topic)

    another = input("\nRun another debate? (y/n): ")
    if another.lower() == "y":
        main()

if __name__ == "__main__":
    main()