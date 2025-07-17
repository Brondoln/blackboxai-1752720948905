# agent.py
import requests
from config import AGENT_API_URL

def send_message_to_agent(user_message):
    """
    Communicates with the intelligent agent using the provided endpoint.
    
    Args:
        user_message (str): The message from the user.
    
    Returns:
        dict: Parsed JSON containing the agent response or an error message.
    """
    payload = {"message": user_message}  # This may need adjustment per the agent API specs
    
    try:
        response = requests.post(AGENT_API_URL, json=payload, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        data = response.json()
        # Check if the expected 'reply' exists in the response
        if "reply" not in data:
            return {"reply": "Respuesta no definida por el agente."}
        
        return data
    except requests.exceptions.RequestException as e:
        # Return a structured error for UI processing
        return {"error": f"Error al comunicar con el agente: {str(e)}"}
