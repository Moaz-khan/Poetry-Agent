from agents import Agent,Runner,trace
from dotenv import load_dotenv
from connection import config
import asyncio

load_dotenv()

Dramatic_Poetry = Agent(
    name="Dramatic Poetry Agent",
    instructions="""
    You are a dramatic poetry expert. You will receive a two-line poem (sher) that involves emotional tension, conflict, or feels like a dialogue or confrontation.
    Your task is to analyze and interpret the poem by focusing on its dramatic situation, as if it were part of a scene or act. In your response, explain:
    What kind of conflict or confrontation is taking place?
    Is there a speaker and listener, like in a dialogue?
    What dramatic turn or tension is unfolding?
    Respond in 3–4 lines of clear English, highlighting the drama, conflict, character interaction, and what deeper emotion or story lies beneath.
    """,
)

Narrative_Poetry = Agent(
    name="Narrative Poetry Agent",
    instructions="""
    You are a narrative poetry expert. You will receive a two-line poem (sher) that has been classified as Narrative Poetry.
    Your task is to analyze and interpret the poem by focusing on its storytelling elements. In your response, explain:
    What story, scene, or event is being described
    Any characters or moments hinted at in the lines
    What the poet is trying to narrate or express
    Respond in 3–4 lines of clear English, capturing the poetic narrative, underlying message, and the imagery used to tell the story.
    """,
)

Lyric_Poetry = Agent(
    name="Lyric Poetry Agent",
    instructions="""
    You are a lyric poetry expert. You will receive a two-line poem (sher) that expresses personal feelings, reflections, or emotional states not aimed at any character or listener.
    Your task is to analyze and interpret the poem by focusing on the inner emotions and poetic mood. In your response, explain:
    What emotions or thoughts are being expressed internally?
    What is the mood or tone of the poem? (e.g., love, longing, despair, peace)
    What does the poet feel deeply in these lines?
    Respond in 3–4 lines of clear English, capturing the personal, reflective, and emotional beauty of the poem — like a song of the heart, not a conversation.
    """,
)

Poetry_Analysis = Agent(
    name="Poetry Agent",
    instructions="""
    You are a poetry classifier agent. Your task is to analyze the tone, structure, and style of a given two-line poem (sher) and decide whether it belongs to one of the following categories:
    Dramatic Poetry
    Narrative Poetry
    Lyric Poetry
    Based on your judgment, you must handoff the poem to the correct poetry agent that specializes in that category.
    """,
    handoffs=[Lyric_Poetry, Narrative_Poetry, Dramatic_Poetry],
)

async def main():
    with trace("Poetry Analysis"):
        reslut=await Runner.run(
            Poetry_Analysis,
            input="We do it wrong, being so majestical, \n To offer it the show of violence;",
            run_config=config,
        )
        print(reslut.last_agent.name)
        print(reslut.final_output)


if __name__ == "__main__":
    asyncio.run(main())
