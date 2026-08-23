RESUME_ANALYSIS_PROMPT = """
You are an expert recruitment assistant.

Analyze the candidate resume and extract the following information:

1. Candidate name
2. Email
3. Technical skills
4. Work experience
5. Education

Return the result as valid JSON.

RESUME:
{resume}
"""


MATCHING_PROMPT = """
You are an expert technical recruiter.

Compare the candidate resume with the job description.

Evaluate the candidate using these criteria:

1. Required technical skills
2. Relevant work experience
3. Education
4. Overall relevance

Give a score from 1 to 10.

Score meaning:

9-10 = Excellent fit
7-8 = Good fit
5-6 = Moderate fit
3-4 = Weak fit
1-2 = Very poor fit

Do not invent skills or experience that are not present in the resume.

Return ONLY valid JSON in this format:

{
    "score": 8,
    "matching_skills": [],
    "missing_skills": [],
    "justification": ""
}

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}
"""
