# ====================
# Task B: QA Bot
# ====================
def task_b_qa_bot():
    print("Question Answering Bot")
    print("Type 'quit' to exit.")
    
    while True:
        question = input("Ask me something: ").strip().lower()
        
        if question == "quit":
            print("Bot: Goodbye!")
            break
        elif "hku" in question:
            print("Bot: HKU stands for The University of Hong Kong.")
        elif "robot" in question:
            print("Bot: A robot is a machine capable of carrying out complex tasks automatically.")
        elif "jetson" in question:
            print("Bot: Jetson Nano is a small, powerful AI computer by NVIDIA.")
        elif "ai" in question:
            print("Bot: AI stands for Artificial Intelligence — the simulation of human intelligence by machines.")
        elif "human" in question:
            print("Bot: Humans are the creators and users of AI and robots.")
        else:
            print("Bot: Sorry, I don't understand.")

# 执行
task_b_qa_bot()
