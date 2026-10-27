from google import genai
import logging

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(name)s (line %(lineno)d): %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("ai_service")
client = genai.Client()

def ask_ai_service(client, query):
    logger.info(f"Query: {query}")
    

    try:
        res = client.models.generate_content(model="gemini-flash-lite-latest",
         contents=query)

        logger.info("Jawab generate ho gaya")
        return res.text

    except Exception as e:
        logger.error(f"AI call fail hui: {e}")
        return "Service temporarily unavailable" 


if __name__ == "__main__":
    reply = ask_ai_service(client, "Python kya hai? Ek line mein batao.")
    print("Final Output:", reply)
