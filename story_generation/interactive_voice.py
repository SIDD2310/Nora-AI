from elevenlabs import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ClientTools

def log_message(parameters):
    message = parameters.get("message")
    print(message)

client_tools = ClientTools()
client_tools.register("logMessage", log_message)

conversation = Conversation(
    client=ElevenLabs(),
    agent_id="W3HZWJljPMmSxbtsFoAD",
    client_tools=client_tools,
    # ...
)

conversation.start_session()
