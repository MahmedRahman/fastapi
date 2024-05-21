from youtube_transcript_api import YouTubeTranscriptApi 
import google.generativeai as genai
from fastapi import FastAPI

genai.configure(api_key="AIzaSyDkK0IlWO1wLMkYsH_1yFiHsAZidOuAkzc")
model = genai.GenerativeModel('gemini-pro')

app = FastAPI()
#GZbeL5AcTgw
@app.get("/Video/{video_id}")
async def root(video_id):
    text = YouTubeTranscriptApi.get_transcript(video_id)
    YtString = ""
    for item in text:
      YtString = YtString + " " + item ["text"]

    promote = """
    Could you please provide a concise and comprehensive summary of the given text?
    given text """ + YtString +  """  The summary should capture the main points and key details of the text while conveying the author's intended meaning accurately. 
    Please ensure that the summary is well-organized and easy to read, with clear headings and subheadings to guide the reader through each section.
    The length of the summary should be appropriate to capture the main points and key details of the text, without including unnecessary information or becoming overly long.
    """
    response = model.generate_content(promote)
    return {"contant": response.text}

