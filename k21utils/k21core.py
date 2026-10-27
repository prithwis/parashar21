import os
from google.colab import userdata

# ---------------------------------------------------------------------------------------

def authenticateLLM(provider="openai"):

    from google.colab import userdata

    provider = provider.lower()

    secrets = {
        "openai": "OPENAI_API_KEY",
        "claude": "ANTHROPIC_API_KEY",
        "gemini": "GEMINI_API_KEY"
    }

    if provider not in secrets:
        raise ValueError(f"Unsupported provider: {provider}")

    api_key = userdata.get(secrets[provider])

    if not api_key:
        raise ValueError(f"Missing Colab Secret: {secrets[provider]}")

    if provider == "openai":

        import requests
        from openai import OpenAI

        response = requests.get(
            "https://api.openai.com/v1/me",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=15
        )
        response.raise_for_status()

        user = response.json()

        print(
            f"OPENAI | "
            f"User: {user.get('name', 'N/A')} | "
            f"Email: {user.get('email', 'N/A')} | "
            f"ID: {user.get('id', 'N/A')}"
        )

        client = OpenAI(api_key=api_key)

    elif provider == "claude":

        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)
        print("CLAUDE | Client initialized | Identity not verified")

    elif provider == "gemini":

        from google import genai
        client = genai.Client(api_key=api_key)
        print("GEMINI | Client initialized | Identity not verified")

    return client
	
# ---------------------------------------------------------------------------------------	

import time

def callLLM(client, role, query, model=None,
            provider="openai", effort="medium"):

    provider = provider.lower()
    model = model or DEFAULT_MODELS[provider]

    start = time.perf_counter()

    if provider == "openai":

        response = client.responses.create(
            model=model,
            instructions=role,
            input=query,
            reasoning={"effort": effort}
        )

        answer = response.output_text
        usage = response.usage

        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens

        input_details = getattr(usage, "input_tokens_details", None)
        output_details = getattr(usage, "output_tokens_details", None)

        cached_tokens = (
            getattr(input_details, "cached_tokens", 0)
            if input_details else 0
        )

        reasoning_tokens = (
            getattr(output_details, "reasoning_tokens", 0)
            if output_details else 0
        )

    elif provider == "claude":

        response = client.messages.create(
            model=model,
            system=role,
            max_tokens=8192,
            messages=[
                {"role": "user", "content": query}
            ]
        )

        answer = "\n".join(
            block.text for block in response.content
            if block.type == "text"
        )

        usage = response.usage

        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens

        cached_tokens = (
            getattr(usage, "cache_read_input_tokens", 0) or 0
        )

        reasoning_tokens = 0  # Not separately reported here

    elif provider == "gemini":

        from google.genai import types

        response = client.models.generate_content(
            model=model,
            contents=query,
            config=types.GenerateContentConfig(
                system_instruction=role
            )
        )

        answer = response.text
        usage = response.usage_metadata

        input_tokens = usage.prompt_token_count or 0
        output_tokens = usage.candidates_token_count or 0

        cached_tokens = (
            getattr(usage, "cached_content_token_count", 0) or 0
        )

        reasoning_tokens = (
            getattr(usage, "thoughts_token_count", 0) or 0
        )

    else:
        raise ValueError(f"Unsupported provider: {provider}")

    elapsed = time.perf_counter() - start

    print(
    f"{provider.upper()} | {getattr(response, 'model', model)} | "
    f"Effort: {effort if provider == 'openai' else 'Default'} | "
    f"In: {input_tokens:,} | Cached: {cached_tokens:,} | "
    f"Out: {output_tokens:,} | Reasoning: {reasoning_tokens:,} | "
    f"Time: {elapsed:.1f}s"
)

    return answer

# ---------------------------------------------------------------------------------------
def readText(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"{path} | {len(content):,} characters")
        return content

# ---------------------------------------------------------------------------------------

def buildContext(brahaPath, hariharPath, chartPath,
                 navamsaPath, dashaPath):
    ''' 
    def readText(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"{path} | {len(content):,} characters")
        return content
     '''
    sections = {
        "BRAHA": readText(brahaPath),
        "HARIHAR": readText(hariharPath),
        "RASHI CHART": readText(chartPath),
        "NAVAMSA": readText(navamsaPath),
        "VIMSHOTTARI DASHA": readText(dashaPath)
    }

    return "\n\n".join(
        f"{'=' * 20} {name} {'=' * 20}\n{content}"
        for name, content in sections.items()
    )

# ---------------------------------------------------------------------------------------
def buildQuery(context, question):
    return (
        f"{context}\n\n"
        f"{'=' * 20} QUESTION {'=' * 20}\n"
        f"{question}"
    )
# ---------------------------------------------------------------------------------------
def getContext(**files):
    sections = []

    for name, path in files.items():
        if path:
            with open(path, "r", encoding="utf-8") as f:
                sections.append(f"<{name}>\n{f.read()}\n</{name}>")

    return "\n\n".join(sections)

# ---------------------------------------------------------------------------------------
def augContext(context, **texts):
    sections = [context]

    for name, content in texts.items():
        if content:
            sections.append(f"<{name}>\n{content}\n</{name}>")

    return "\n\n".join(sections)