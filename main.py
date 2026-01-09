
"""
Run all examples from one file.
"""
from logs import setup_logger

from agents.multi_tools import multi_tool_agent
from agents.memory import add_memory

# Driver code
if __name__ == "__main__":
    logger = setup_logger()

    logger.info("Logging initialized successfully")

    # Adding memory
    add_memory("User prefers DD-MM-YYYY date format for any queries.")
    add_memory("User name is sujeet")
    add_memory("User is located in Chandigarh.")
    add_memory("I love to play cricket, badminton and vollyball.")
    
    # Invoking the agent for the response of content for real api tool
    print(".....running", end="\n")
    while True:
        # Asking users preferences
        print("Press s for start chat \nPress q for quiting")
        user_input = input("Enter your preference:")
        if user_input == "s":
            while True:
                # Starting chat with agents
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
                # Agent response
                response_data = api_response['messages'][-1].content
                print(f"AI: {response_data[0]['text']}\n\n")
                print("Enter q for quiting chat.")
                
        
        elif user_input == "q":
            break

        else:
            print("Enter a valid input(either s or q )")
