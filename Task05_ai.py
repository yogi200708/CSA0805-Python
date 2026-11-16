# Task A5/B4: Simple sentiment, summary and rule-based chatbot
POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}

def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0
    previous = ""
    for word in words:
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if previous in NEGATORS:
            value = -value
        total += value
        previous = word
    return total

def label(text):
    s = score(text)
    if s > 0:
        return "positive"
    if s < 0:
        return "negative"
    return "neutral"

complaints = [
    "Roads are clean and the bus was fast.",
    "Smoke from factory, air is bad.",
    "The staff were not helpful.",
    "Not bad, service improved."
]
for c in complaints:
    print(label(c), "|", c)

def simple_summary(text, count=1):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    return ". ".join(sentences[:count]) + ("." if sentences else "")

print("Summary:", simple_summary("Air is bad. Roads are dirty. Buses are slow.", 2))

def chatbot(question):
    q = question.lower()
    if "pm2.5" in q and "adyar" in q:
        return "Sample response: Adyar PM2.5 is 48."
    if "pm2.5" in q and "guindy" in q:
        return "Sample response: Guindy PM2.5 is 95."
    return "Sorry, I do not understand. Ask about PM2.5 and a station."

print(chatbot("What is PM2.5 in Adyar today?"))
