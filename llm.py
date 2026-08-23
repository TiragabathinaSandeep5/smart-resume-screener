import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from .prompts import RESUME_ANALYSIS_PROMPT, MATCHING_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_resume(resume_text: str):

    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume=resume_text
    )

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL"),
        input=prompt
    )

    return json.loads(response.output_text)


def match_resume(resume_text: str, job_description: str):

    prompt = MATCHING_PROMPT.format(
        resume=resume_text,
        job_description=job_description
    )

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL"),
        input=prompt
    )

    return json.loads(response.output_text)
