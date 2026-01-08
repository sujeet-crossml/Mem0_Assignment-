from mem0 import MemoryClient

from cred import MEM0_API_KEY, USER_ID

# creating a memory client for the storing messages
memory = MemoryClient(
    api_key = MEM0_API_KEY
)

# function for the adding message to the memory
def add_memory(content:str|list|dict) -> None:
    try:
        memory.add(
            messages=content,
            user_id = USER_ID
        )
    
    except Exception as e:
        raise f"Mem0 add_memory error:{e}"

# function for the fetching message from the memory
def fetch_memory(query:str) -> dict:
    try:
        result = memory.search(
            query=query,
            filters = {"user_id": "USER_ID"},
            limit = 5
        )
    except Exception as e:
        raise f"Mem0 fetch_memory error:{e}"