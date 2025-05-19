import os
import google.generativeai as genai

def get_gemini_response(prompt):
    """
    Get response from Gemini API

    Args:
        prompt (str): Prompt to send to Gemini API
    Returns:
        str: Response from Gemini API or error message
    """
    try:
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        # gemini-2.5-flash-preview-04-17
        # gemini-2.0-flash
        gemini_model = os.getenv('GEMINI_MODEL')
    
        model = genai.GenerativeModel(gemini_model)
        response = model.generate_content(prompt)

        # Check if response has text attribute
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            print(f"Unexpected response format from Gemini API: {response}")
            return "Failed to get a valid response from AI, try again later..."

    except Exception as e:
        print(f"Error occurred while fetching Gemini API: {e}")
        return "Failed while processing AI response, try again later..."
    
