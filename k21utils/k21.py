import os
import requests
from google.colab import userdata

try:
    # Load key from Colab Secrets into environment
    api_key = userdata.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in Colab Secrets")

    os.environ["OPENAI_API_KEY"] = api_key
    print("API key loaded ✔")

    # Call OpenAI identity endpoint
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    resp = requests.get("https://api.openai.com/v1/me", headers=headers)
    resp.raise_for_status()   # catches 401 / 403 / etc.

    me = resp.json()
    name = me.get("name", "N/A")
    email = me.get("email", "N/A")

    print(f"Logged in as {name} {email}")

except Exception as e:
    print("❌ OpenAI credential check failed")
    print("Reason:", str(e))





def CreateVectorStore(corpus1, corpus2):
    from openai import OpenAI

    client = OpenAI()

    # Create our permanent Khawna knowledge base
    vector_store = client.vector_stores.create(
        name="Khana21_0"
    )

    VECTOR_STORE_ID = vector_store.id

    print("Vector Store:", VECTOR_STORE_ID)

    # Upload Braha and Harihar
    with open(corpus1, "rb") as f1, \
         open(corpus2, "rb") as f2:

        result = client.vector_stores.file_batches.upload_and_poll(
            vector_store_id = VECTOR_STORE_ID,
            files=[f1, f2]
        )

    print(result)
    return(client, VECTOR_STORE_ID)
    
def TestRetrieval(client, vsID, cquery):
    # Pure retrieval test — NO LLM

    results = client.vector_stores.search(
        #vector_store_id="vs_6ab4bd1cfbe081919a3876771cfd3271",
        vector_store_id = vsID,
        query=cquery
    )

    for i, item in enumerate(results.data, 1):
        print(f"\n{'='*70}")
        print(f"RESULT {i}")
        print(f"File:  {item.filename}")
        print(f"Score: {item.score:.4f}")

        for content in item.content:
            if content.type == "text":
                print(content.text)



