from auth import get_service
from fetch import fetch_top_5
from categorize import categorise
from actions import send_mail, delete_mail


def main():
    service = get_service()
    emails = fetch_top_5(service)

    results = []

    print("\n===== TOP 5 EMAILS =====")

    for i, email in enumerate(emails):
        category = categorise(email["subject"])

        results.append({
            "id": email["id"],
            "category": category
        })

        print(f"\n{i+1}. Sender: {email['sender']}")
        print(f"   Subject: {email['subject']}")
        print(f"   Category: {category}")

        # 🔎 Attachment Info
        if email["attachments"]:
            print("   Attachments Present:")
            for att in email["attachments"]:
                print(f"     - {att}")
        else:
            print("   No Attachments")

    # -------- MENU --------
    while True:
        print("\nOptions:")
        print("1. Send Mail")
        print("2. Delete a Mail")
        print("3. Bulk Delete by Category")
        print("4. Exit")

        choice = input("Choose option: ")

        # ---- SEND ----
        if choice == "1":
            to = input("To: ")
            subject = input("Subject: ")
            body = input("Message: ")
            send_mail(service, to, subject, body)

        # ---- SINGLE DELETE ----
        elif choice == "2":
            num = int(input("Enter mail number (1-5) to delete: "))
            confirm = input("Are you sure? (y/n): ")

            if confirm.lower() == 'y':
                delete_mail(service, emails[num-1]["id"])

        # ---- BULK DELETE ----
        elif choice == "3":
            cat = input("Enter category to delete (Security/Finance/Promotional/General): ")

            confirm = input(f"Delete all {cat} emails from top 5? (y/n): ")

            if confirm.lower() == 'y':
                for i, r in enumerate(results):
                    if r["category"].lower() == cat.lower():
                        delete_mail(service, emails[i]["id"])

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()