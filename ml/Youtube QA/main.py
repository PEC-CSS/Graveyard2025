import os
import anthropic
import dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

dotenv.load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
SAVE_LOCATION = r"N:\Graveyard Projects\Youtube QA\Transcripts"
os.makedirs(SAVE_LOCATION, exist_ok=True)
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def save_transcript(video_id):
    transcript_file = os.path.join(SAVE_LOCATION, f"{video_id}_transcript.txt")
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        formatted_transcript = "".join(
            f"[{int(entry['start'] // 60):02d}:{int(entry['start'] % 60):02d}] {entry['text']}\n"
            for entry in transcript_list
        )
        with open(transcript_file, 'w', encoding='utf-8') as f:
            f.write(formatted_transcript)
        return formatted_transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def create_vector_database(transcript_text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(transcript_text)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embeddings)

def get_answer(query, database, video_id):
    similar_docs = database.similarity_search(query, k=3)
    context = " ".join(doc.page_content for doc in similar_docs)
    prompt = f"""
You are a helpful assistant that answers questions based on YouTube video transcripts.
Use ONLY the following transcript excerpts to answer the question.
If the answer cannot be found in the transcript, say "I cannot find information about that in the video."

TRANSCRIPT EXCERPTS (from video ID {video_id}):
{context}

USER QUESTION: {query}

Answer the question based only on the information provided in the transcript excerpts.
Include relevant timestamps from the transcript when possible, formatted as [MM:SS].
"""
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception:
        try:
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text
        except Exception as e:
            print(f"Error: {e}")
            return "Error: Could not get a response from Claude API."

def main():
    print("YouTube Transcript Q&A Bot")
    while True:
        video_id = input("Enter YouTube video ID (or 'exit' to quit): ")
        print("WAIT PLEASE GETTING TRANSCRIPTS...........")
        if video_id.lower() == 'exit':
            print("Goodbye!")
            break
        if "youtube.com" in video_id or "youtu.be" in video_id:
            if "v=" in video_id:
                video_id = video_id.split("v=")[1].split("&")[0]
            elif "youtu.be/" in video_id:
                video_id = video_id.split("youtu.be/")[1].split("?")[0]
        transcript = save_transcript(video_id)
        if not transcript:
            print("Could not fetch transcript. Please try another video.")
            continue
        database = create_vector_database(transcript)
        print("Transcript loaded! Ask questions about this video (or type 'new' for a new video, 'exit' to quit)")
        while True:
            user_input = input("Your question: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                return
            elif user_input.lower() == 'new':
                break
            print("Answer:", get_answer(user_input, database, video_id))

main()