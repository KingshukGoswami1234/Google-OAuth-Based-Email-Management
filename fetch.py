def fetch_top_5(service):
    results = service.users().messages().list(
        userId="me",
        maxResults=5
    ).execute()

    messages = results.get("messages", [])
    emails = []

    for msg in messages:
        full_msg = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        sender = subject = ""
        attachment_types = []

        headers = full_msg.get("payload", {}).get("headers", [])
        for h in headers:
            if h["name"] == "From":
                sender = h["value"]
            if h["name"] == "Subject":
                subject = h["value"]

        # 🔎 Attachment detection
        parts = full_msg.get("payload", {}).get("parts", [])
        for part in parts:
            filename = part.get("filename")
            mime_type = part.get("mimeType")

            if filename:
                attachment_types.append(mime_type)

        emails.append({
            "id": msg["id"],
            "sender": sender,
            "subject": subject,
            "attachments": attachment_types
        })

    return emails