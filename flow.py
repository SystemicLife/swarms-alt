from swarms.models import OpenAIChat
from swarms.structs import Flow
from swarms.tools.interpreter_tool import compile

api_key = ""

# Initialize the language model, this model can be swapped out with Anthropic, ETC, Huggingface Models like Mistral, ETC
llm = OpenAIChat(
    openai_api_key=api_key,
    temperature=0.5,
    max_tokens=3000,
)

# Initialize the flow
flow = Flow(llm=llm, max_loops=5, dashboard=True, tools=[compile])

# flow = Flow(
#     llm=llm,
#     max_loops=5,
#     dashboard=True,
#     # stopping_condition=None,  # You can define a stopping condition as needed.
#     # loop_interval=1,
#     # retry_attempts=3,
#     # retry_interval=1,
#     # interactive=False,  # Set to 'True' for interactive mode.
#     # dynamic_temperature=False,  # Set to 'True' for dynamic temperature handling.
# )


out = flow.run("Use your open interpreter tool to print hello world to the terminal")

print(out)
