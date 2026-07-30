# ---------------------------------------------------------
# KNOWLEDGE BASE: dictionary of known inputs -> responses
# (Requirement: 5+ intents) — expanded vocabulary, cat themed
# ---------------------------------------------------------
responses = {
    "hello": "Meow! Hi there, human.",
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
 
# Words that should end the conversation
exit_commands = {"bye", "exit", "quit"}
 
# Keywords that count as "mentioning their own cat"
cat_mention_keywords = {"my cat", "i have a cat", "our cat"}
 
 
def get_response(user_input: str) -> str:
    """
    Looks up the cleaned user input in the responses dictionary.
    Uses .get() so lookup + fallback happen in a single step.
    """
    # Nested condition example: if they mention their own cat,
    # give a more personal reply instead of the generic fallback.
    if user_input in responses:
        return responses[user_input]
    else:
        for keyword in cat_mention_keywords:
            if keyword in user_input:
                if "no" in user_input or "not" in user_input:
                    return "Aww, no cat? We can fix that."
                else:
                    return "Ooh, tell me more about your cat! I bet they're adorable."
        return "Meow? I do not understand that. Type 'help' to see what I know."
 
 
def chatbot():
    print("Whiskers: Meow! I'm Whiskers, a rule-based cat chatbot. Type 'bye' to exit.")
 
    # ---------------------------------------------------------
    # THE HEARTBEAT: continuous loop until exit command
    # ---------------------------------------------------------
    while True:
        raw_input_text = input("You: ")
 
        # PHASE 1: Sanitization & Normalization (handle case + whitespace)
        clean_input = raw_input_text.lower().strip()
 
        # Exit condition (kill command)
        if clean_input in exit_commands:
            print("Whiskers: Goodbye! *purrs and walks away* ")
            break
 
        # Skip empty input
        if clean_input == "":
            continue
 
        # Process input through the knowledge base
        reply = get_response(clean_input)
        print(f"Whiskers: {reply}")
 
 
if __name__ == "__main__":
    chatbot()
 