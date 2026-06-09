from openai import OpenAI

client = OpenAI(api_key="API_KEY")

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
