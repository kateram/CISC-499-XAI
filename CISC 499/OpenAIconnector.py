from openai import OpenAI

class OpenAIConnector:
    def __init__(self, api_key, model="gpt-4o", temperature=0.0):
        """
        Initialize the OpenAI connector.
        :param api_key: OpenAI API key.
        :param model: The model to use 
        :param temperature: The sampling temperature
        """
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.client = OpenAI(api_key=self.api_key)

    def explain_code(self, prompt):
        """
        This method should be used to asked GPT to EXPLAIN the code
        :param prompt: The prompt to send to the API.
        :return: The API's response as a string.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[ 
                    {"role": "system", "content": "Given a Python script that performs input-output operations, return a clear and concise paragraph describing its functionality, purpose, and core logic in English."},
                    {"role": "user", "content": prompt
                }],
                temperature=self.temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def generate_code(self, prompt):
        """
        This method should be used to asked GPT to GENERATE CODE based on explanation
        :param prompt: The prompt to send to the API.
        :return: The API's response as a string.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[ 
                    {"role": "system", "content": " Given a paragraph describing the logic and functionality of a Python input-output program, return a Python script that implements the described functionality. Include a sample input to demonstrate the script's execution"},
                    {"role": "user", "content": prompt
                }],
                temperature=self.temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None
