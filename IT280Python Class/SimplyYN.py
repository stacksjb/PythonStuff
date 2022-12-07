
def main():
    if confirm_prompt("Do you want to continue?"):
        print("Continuing...")
    else:
        print("Exiting...")

def confirm_prompt(question: str) -> bool:
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").casefold()
    return (reply == "y")


reply = confirm_prompt("Are you sure?")
print(reply)