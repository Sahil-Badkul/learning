from google import genai
from dotenv import load_dotenv
import json
from postgresdb import execute_query, get_schema

load_dotenv()

client = genai.Client()

schema = get_schema("orders")

print("Hello! Welcome to the SQL Query Generator. You can ask questions about the 'orders' table, and I will generate SQL queries for you based on your input. Type 'exit' to quit the program.")
while True:
    user_input = input("enter your question: ")
    if user_input == 'exit':
        break

    prompt = f"""
        You are a SQL assistant.
        Return only a JSON object with keys `sql` and `question`.
        Do not add any explanation or markdown formatting.

        Question: {user_input}

        Orders table schema:
        {schema}
    """

    try:
        res = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema={
                    "type": "object",
                    "properties": {
                        "sql": {"type": "string"},
                        "question": {"type": "string"}
                    },
                    "required": ["sql", "question"]
                }
            )
        )
    except Exception as e:
        print(f"API call failed: {e}")
        continue

    try:
        json_res = json.loads(res.text)
    except json.JSONDecodeError:
        print("Could not parse response as JSON:")
        print(res.text)
        continue

    final_sql = json_res.get('sql')
    if not final_sql:
        print('No SQL was returned.')
        print(json_res)
        continue

    final_result = execute_query(final_sql)
    print(final_result)