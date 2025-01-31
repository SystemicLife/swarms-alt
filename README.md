![Swarming banner icon](images/swarmslogobanner.png)

<div align="center">

Swarms is a modular framework that enables reliable and useful multi-agent collaboration at scale to automate real-world tasks.


[![GitHub issues](https://img.shields.io/github/issues/kyegomez/swarms)](https://github.com/kyegomez/swarms/issues) [![GitHub forks](https://img.shields.io/github/forks/kyegomez/swarms)](https://github.com/kyegomez/swarms/network) [![GitHub stars](https://img.shields.io/github/stars/kyegomez/swarms)](https://github.com/kyegomez/swarms/stargazers) [![GitHub license](https://img.shields.io/github/license/kyegomez/swarms)](https://github.com/kyegomez/swarms/blob/main/LICENSE)[![GitHub star chart](https://img.shields.io/github/stars/kyegomez/swarms?style=social)](https://star-history.com/#kyegomez/swarms)[![Dependency Status](https://img.shields.io/librariesio/github/kyegomez/swarms)](https://libraries.io/github/kyegomez/swarms) [![Downloads](https://static.pepy.tech/badge/swarms/month)](https://pepy.tech/project/swarms)


### Share on Social Media

[![Join the Agora discord](https://img.shields.io/discord/1110910277110743103?label=Discord&logo=discord&logoColor=white&style=plastic&color=d7b023)![Share on Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Share%20%40kyegomez/swarms)](https://twitter.com/intent/tweet?text=Check%20out%20this%20amazing%20AI%20project:%20&url=https%3A%2F%2Fgithub.com%2Fkyegomez%2Fswarms) [![Share on Facebook](https://img.shields.io/badge/Share-%20facebook-blue)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fgithub.com%2Fkyegomez%2Fswarms) [![Share on LinkedIn](https://img.shields.io/badge/Share-%20linkedin-blue)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fgithub.com%2Fkyegomez%2Fswarms&title=&summary=&source=)

[![Share on Reddit](https://img.shields.io/badge/-Share%20on%20Reddit-orange)](https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2Fkyegomez%2Fswarms&title=Swarms%20-%20the%20future%20of%20AI) [![Share on Hacker News](https://img.shields.io/badge/-Share%20on%20Hacker%20News-orange)](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2Fkyegomez%2Fswarms&t=Swarms%20-%20the%20future%20of%20AI) [![Share on Pinterest](https://img.shields.io/badge/-Share%20on%20Pinterest-red)](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fgithub.com%2Fkyegomez%2Fswarms&media=https%3A%2F%2Fexample.com%2Fimage.jpg&description=Swarms%20-%20the%20future%20of%20AI) [![Share on WhatsApp](https://img.shields.io/badge/-Share%20on%20WhatsApp-green)](https://api.whatsapp.com/send?text=Check%20out%20Swarms%20-%20the%20future%20of%20AI%20%23swarms%20%23AI%0A%0Ahttps%3A%2F%2Fgithub.com%2Fkyegomez%2Fswarms)

</div>

[![Swarm Fest](images/swarmfest.png)](https://github.com/users/kyegomez/projects/1)

## Vision
At Swarms, we're transforming the landscape of AI from siloed AI agents to a unified 'swarm' of intelligence. Through relentless iteration and the power of collective insight from our 1500+ Agora researchers, we're developing a groundbreaking framework for AI collaboration. Our mission is to catalyze a paradigm shift, advancing Humanity with the power of unified autonomous AI agent swarms.

-----

## 🤝 Schedule a 1-on-1 Session

Book a [1-on-1 Session with Kye](https://calendly.com/swarm-corp/30min), the Creator, to discuss any issues, provide feedback, or explore how we can improve Swarms for you.


----------

## Installation
`pip3 install --upgrade swarms`

---

## Usage
We have a small gallery of examples to run here, [for more check out the docs to build your own agent and or swarms!](https://docs.apac.ai)

### `Flow` Example
- The `Flow` is a superior iteratioin of the `LLMChain` from Langchain, our intent with `Flow` is to create the most reliable loop structure that gives the agents their "autonomy" through 3 main methods of interaction, one through user specified loops, then dynamic where the agent parses a <DONE> token, and or an interactive human input verison, or a mix of all 3. 
```python

from swarms.models import OpenAIChat
from swarms.structs import Flow

api_key = ""


# Initialize the language model,
# This model can be swapped out with Anthropic, ETC, Huggingface Models like Mistral, ETC
llm = OpenAIChat(
    openai_api_key=api_key,
    temperature=0.5,
)

# Initialize the flow
flow = Flow(
    llm=llm,
    max_loops=5,
)

out = flow.run("Generate a 10,000 word blog, say Stop when done")
print(out)


```


## `GodMode`
- A powerful tool for concurrent execution of tasks using multiple Language Model (LLM) instances.

```python
from swarms.swarms import GodMode
from swarms.models import OpenAIChat

api_key = ""

llm = OpenAIChat(
    openai_api_key=api_key
)


llms = [
    llm,
    llm,
    llm
]

god_mode = GodMode(llms)

task = 'Generate a 10,000 word blog on health and wellness.'

out = god_mode.run(task)
god_mode.print_responses(task)
```

------

### `OmniModalAgent`
- OmniModal Agent is an LLM that access to 10+ multi-modal encoders and diffusers! It can generate images, videos, speech, music and so much more, get started with:

```python
from swarms.models import OpenAIChat
from swarms.agents import OmniModalAgent

api_key = "SK-"

llm = OpenAIChat(model_name="gpt-4", openai_api_key=api_key)

agent = OmniModalAgent(llm)

agent.run("Create a video of a swarm of fish")

```

---

## Documentation

- For documentation, go here, [swarms.apac.ai](https://swarms.apac.ai)


## Contribute

We're always looking for contributors to help us improve and expand this project. If you're interested, please check out our [Contributing Guidelines](CONTRIBUTING.md).

# License

MIT
