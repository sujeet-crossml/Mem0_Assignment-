
"""
Run all examples from one file.
"""
from logs import setup_logger

from agents.multi_tools import multi_tool_agent
from agents.memory import add_memory

if __name__ == "__main__":
    logger = setup_logger()

    logger.info("🚀 Logging initialized successfully")

    add_memory("User prefers DD-MM-YYYY date format for any queries.")
    add_memory("User prefers solving equations with step by step and also likes explanation for every step.")
    add_memory("User is located in Chandigarh.")
    add_memory("User prefer text sentiment answer in one line with small reasons.")
    
    # Invoking the agent for the response of content for real api tool
    while True:
        print(".....running")
        print("Press s for start chat \nPress q for quiting")
        user_input = input("Enter your preference:")
        if user_input == "s":
            while True:
                print("-------start your chat-------")
                chat = input("You:")
                if chat == "q":
                    break
                api_response = multi_tool_agent.invoke({
                    "messages": [
                        {"role": "user",
                        "content": chat}
                    ]}
                )
                print("\n--- Real API Tool Example ---")
                print(f"AI: {api_response['messages'][-1].content}")
                print("Enter q for quiting chat.")
                
        
        elif user_input == "q":
            break
        
        else:
            print("Enter a valid input(either s or q )")
