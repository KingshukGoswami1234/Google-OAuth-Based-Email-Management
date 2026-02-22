def categorise(subject):
    s = subject.lower()

    if "otp" in s or "verification" in s:
        return "Security"
    if "invoice" in s or "payment" in s:
        return "Finance"
    if "offer" in s or "sale" in s:
        return "Promotional"

    return "General"