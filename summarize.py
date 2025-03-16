from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="t5-small")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    transcript = open("data/transcript.txt").read()
    summary = summarize_text(transcript)
    print("Meeting Summary:\n", summary)
