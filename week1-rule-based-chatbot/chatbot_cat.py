"""
Project 1: Rule-Based AI Chatbot (Cat Lover Edition 🐾)
DecodeLabs - AI Internship (Batch 2026)

A rule-based chatbot with a cat-obsessed personality. Uses a dictionary
(hash map) for instant O(1) lookups instead of a long if-elif ladder,
plus one nested-condition example for a slightly "smarter" reply.
"""

responses = {
    "hello": "Meow! Hi there, human. 🐱",
    "hi": "Hiii! I was just napping, but for you I'll wake up.",
    "how are you": "Purring happily! Just had a nap and a treat, life is good.",
    "what is your name": "I'm Whiskers the ChatBot — half AI, half cat.",
    "what can you do": "I can chat, drop cat facts, and judge you silently. Try 'help'!",
    "help": "Try: hello, how are you, cat fact, my cat, i love cats, are you a cat, thank you, bye.",
    "thank you": "You're welcome! Now scratch my chin as payment.",
    "thanks": "Meow-lcome!",
    "cat fact": "Fun fact: cats spend around 70% of their life sleeping!",
    "are you a cat": "I identify as 99% cat, 1% code.",
    "i love cats": "Excellent taste! We should be best friends.",
}

exit_commands = {"bye", "exit", "quit"}
cat_mention_keywords = {"my cat", "i have a cat", "our cat"}


def get_response(user_input: str) -> str:
    if user_input in responses:
        return responses[user_input]
    else:
        for keyword in cat_mention_keywords:
            if keyword in user_input:
                if "no" in user_input or "not" in user_input:
                    return "Aww, no cat? We can fix that. 😼"
                else:
                    return "Ooh, tell me more about your cat! I bet they're adorable."
        return "Meow? I do not understand that. Type 'help' to see what I know."


def chatbot():
    print("Whiskers: Meow! I'm Whiskers, a rule-based cat chatbot. Type 'bye' to exit.")
    while True:
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()
        if clean_input in exit_commands:
            print("Whiskers: Goodbye! *purrs and walks away* 🐾")
            break
        if clean_input == "":
            continue
        reply = get_response(clean_input)
        print(f"Whiskers: {reply}")


if __name__ == "__main__":
    chatbot()
