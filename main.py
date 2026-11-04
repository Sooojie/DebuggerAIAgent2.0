
import logging
from debugger import debug_code


# ---------------------------------------
# Logging Configuration
# ---------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# ---------------------------------------
# Display Results
# ---------------------------------------

def display_results(result):
    """
    Display the debugging results in the terminal.
    """

    print("\n" + "=" * 60)
    print("CODE ANALYSIS RESULTS")
    print("=" * 60)

    # Display summary
    print("\nSUMMARY:")
    print(result["summary"])

    # Display identified bugs
    print("\nIDENTIFIED BUGS:")

    if result["bugs"]:
        for index, bug in enumerate(result["bugs"], start=1):
            print(f"\nBug {index}: {bug['type']}")
            print(f"Location: {bug['location']}")
            print(f"Description: {bug['description']}")
            print(f"Reason: {bug['reason']}")
            print(f"Suggested Fix: {bug['fix']}")
    else:
        print("No obvious bugs identified.")

    # Display corrected code
    print("\nCORRECTED CODE:")
    print("-" * 60)
    print(result["corrected_code"])
    print("-" * 60)

    # Display explanation
    print("\nEXPLANATION:")
    print(result["explanation"])

    # Display suggestions
    print("\nSUGGESTIONS:")

    if result["suggestions"]:
        for suggestion in result["suggestions"]:
            print(f"- {suggestion}")
    else:
        print("No additional suggestions.")

    # Display test cases
    print("\nSUGGESTED TESTS:")

    if result["tests"]:
        for test in result["tests"]:
            print(f"- {test}")
    else:
        print("No test cases suggested.")

    print("\n" + "=" * 60)


# ---------------------------------------
# Main Application
# ---------------------------------------

def main():

    print("=" * 60)
    print("AI CODE DEBUGGING ASSISTANT")
    print("=" * 60)

    print("\nWelcome! I can help you analyze and debug your code.")

    while True:

        print("\n" + "-" * 60)
        print("NEW DEBUGGING SESSION")
        print("-" * 60)

        # Get programming language
        language = input(
            "\nEnter programming language (e.g. Python, Java, C++): "
        ).strip()

        if not language:
            print("Please enter a programming language.")
            continue

        # Get source code
        print("\nPaste your source code below.")
        print("Enter a line containing only END when finished:")

        code_lines = []

        while True:
            line = input()

            if line.strip() == "END":
                break

            code_lines.append(line)

        code = "\n".join(code_lines)

        if not code.strip():
            print("No code was provided. Please try again.")
            continue

        # Get optional error message
        print("\nEnter the error message or additional context.")
        print("Press Enter without typing anything to skip:")

        error_message = input("> ").strip()

        # Submit code to debugging agent
        print("\nAnalyzing your code with Llama 3.2...")
        result = debug_code(
            code=code,
            language=language,
            error_message=error_message
        )

        # Display response
        if result:
            display_results(result)
        else:
            print("\nUnable to analyze the submitted code.")
            print("Check that Ollama is running and Llama 3.2 is available.")

        # Ask whether to continue
        choice = input(
            "\nWould you like to debug another piece of code? (y/n): "
        ).strip().lower()

        if choice != "y":
            print("\nThank you for using the AI Code Debugging Assistant!")
            break


# ---------------------------------------
# Program Entry Point
# ---------------------------------------

if __name__ == "__main__":
    main()
