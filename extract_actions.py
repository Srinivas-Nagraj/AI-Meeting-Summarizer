import spacy

nlp = spacy.load("en_core_web_sm")

def extract_action_items(text):
    doc = nlp(text)
    action_items = []

    for sent in doc.sents:
        if "must" in sent.text or "should" in sent.text or "deadline" in sent.text:
            action_items.append(sent.text)

    return action_items

if __name__ == "__main__":
    text = open("data/transcript.txt").read()
    actions = extract_action_items(text)
    print("Extracted Action Items:\n", actions)
