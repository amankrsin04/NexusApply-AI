from openai import OpenAI

client = OpenAI(api_key="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")

def tailor_resume(job_description):

    prompt = f"""
    Optimize this resume for the following job:

    {job_description}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
