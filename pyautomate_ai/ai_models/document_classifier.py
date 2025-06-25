def classify_document(text):
    text = text.lower()
    if any(word in text for word in ["invoice", "amount", "due", "total"]):
        return "invoice"
    elif any(word in text for word in ["resume", "cv", "education", "experience"]):
        return "resume"
    else:
        return "unknown" 