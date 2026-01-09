from mem0 import MemoryClient

from cred import MEM0_API_KEY, USER_ID

# creating a memory client for the storing messages
memory = MemoryClient(
    api_key = MEM0_API_KEY
)

# function for the adding message to the memory
def add_memory(content:str) -> None:
    """
    Summary:
        Store content in persistent memory for the current user.

    Args:
        content (str): Text content to be added to memory.

    Returns:
        None: This function does not return a value.

    Raises:
        Exception: If storing content in memory fails.
    """
    try:
        memory.add(
            messages = content,
            user_id = USER_ID
        )
    
    except Exception as e:
        raise f"Mem0 add_memory error:{e}"

# function for the fetching message from the memory
def fetch_memory(query:str) -> list:
    """
    Summary:
        Retrieve relevant stored memories based on a search query.

    Args:
        query (str): Search query used to find related memories.

    Returns:
        list | str: Joined memory text if found, or a message indicating
        no relevant memory is available.

    Raises:
        Exception: If fetching memory from storage fails.
    """
    try:
        results = memory.search(
            query = query,
            filters = {"user_id": USER_ID},
            limit = 5
        )
        if not results:
            return "No relevant memory found."
        
        memories = [item["memory"] for item in results["results"]]
        return "\n".join(memories)
    
    except Exception as e:
        raise f"Mem0 fetch_memory error:{e}"