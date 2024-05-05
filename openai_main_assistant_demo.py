from openai import OpenAI
client = OpenAI()

# Create an assistant instance
assistant = client.beta.assistants.create(
  name="agi_hack_tutor",
  instructions="You are a mentor trying to explain concepts to a student. Answer their questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-3.5-turbo-16k-0613",
)

# Create a thread
thread = client.beta.threads.create()

# Add a message to the thread
prompt = 'break this subject into subcomponents: ' + 'quantum'
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content=prompt
)

# Run the assistant on the thread
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

# Get the messages from the thread
if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    messages_dict = messages.to_dict()
    #print(type(messages_dict))
    #assert False
    for message in messages_dict['data']:
        print(message['content'][0]['text']['value'])
else:
  print(run.status)