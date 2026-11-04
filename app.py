
import streamlit as st
import logging

from debugger import debug_code


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Code Debugging Assistant",
    page_icon="🐛",
    layout="wide"
)


# ---------------------------------------
# Logging Configuration
# ---------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ---------------------------------------
# Session State
# ---------------------------------------

if "debug_result" not in st.session_state:
    st.session_state.debug_result = None

if "last_code" not in st.session_state:
    st.session_state.last_code = ""


# ---------------------------------------
# Application Header
# ---------------------------------------

st.title("🐛 AI Code Debugging Assistant")

st.markdown(
    "Analyze, debug, and improve your code using "
    "artificial intelligence powered by Ollama and Llama 3.2."
)

st.divider()


# ---------------------------------------
# Sidebar
# ---------------------------------------

with st.sidebar:

    st.header("About the Assistant")

    st.write(
        "This AI agent helps developers identify bugs, "
        "understand errors, and improve their source code."
    )

    st.divider()

    st.subheader("Model Information")

    st.write("**LLM:** Llama 3.2")
    st.write("**Runtime:** Ollama")
    st.write("**Framework:** Streamlit")

    st.divider()

    st.subheader("Supported Languages")

    st.write(
        "- Python\n"
        "- Java\n"
        "- C++\n"
        "- C\n"
        "- JavaScript\n"
        "- C#\n"
        "- SQL\n"
        "- Other languages"
    )

    st.divider()

    if st.button("Clear Results", use_container_width=True):
        st.session_state.debug_result = None
        st.session_state.last_code = ""
        st.rerun()


# ---------------------------------------
# Code Input Section
# ---------------------------------------

st.header("Code Analysis")

col1, col2 = st.columns([1, 1])

with col1:

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "Java",
            "C++",
            "C",
            "JavaScript",
            "C#",
            "SQL",
            "Other"
        ]
    )

with col2:

    st.markdown("#### Debugging Engine")
    st.info("Ollama | Llama 3.2")


code = st.text_area(
    "Enter your source code",
    height=350,
    placeholder="Paste your source code here..."
)

error_message = st.text_area(
    "Error Message / Additional Context (Optional)",
    height=120,
    placeholder="Paste an error message or describe what is going wrong..."
)


# ---------------------------------------
# Debug Button
# ---------------------------------------

if st.button(
    "🐛 Debug My Code",
    type="primary",
    use_container_width=True
):

    if not code.strip():

        st.warning("Please enter some source code before debugging.")

    else:

        with st.spinner("Llama 3.2 is analyzing your code..."):

            try:

                result = debug_code(
                    code=code,
                    language=language,
                    error_message=error_message
                )

                if result:

                    st.session_state.debug_result = result
                    st.session_state.last_code = code

                    logger.info("Code analysis completed.")

                else:

                    st.error(
                        "Unable to analyze your code. "
                        "Please check that Ollama is running "
                        "and Llama 3.2 is installed."
                    )

            except Exception as error:

                logger.exception("An error occurred during debugging.")

                st.error(f"An error occurred: {error}")


# ---------------------------------------
# Display Analysis Results
# ---------------------------------------

if st.session_state.debug_result:

    result = st.session_state.debug_result

    st.divider()

    st.header("Analysis Results")

    # Summary
    st.subheader("Summary")

    st.write(result["summary"])

    # Tabs for organized results
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🐛 Bug Diagnosis",
            "💻 Corrected Code",
            "💡 Suggestions",
            "🧪 Test Cases"
        ]
    )

    # -----------------------------------
    # Bug Diagnosis
    # -----------------------------------

    with tab1:

        st.subheader("Identified Bugs")

        if result["bugs"]:

            for index, bug in enumerate(result["bugs"], start=1):

                with st.expander(
                    f"Bug {index}: {bug['type']}",
                    expanded=True
                ):

                    st.write(f"**Location:** {bug['location']}")

                    st.write("**Description:**")
                    st.write(bug["description"])

                    st.write("**Reason:**")
                    st.write(bug["reason"])

                    st.write("**Suggested Fix:**")
                    st.write(bug["fix"])

        else:

            st.success("No obvious bugs were identified.")

    # -----------------------------------
    # Corrected Code
    # -----------------------------------

    with tab2:

        st.subheader("Proposed Corrected Code")

        st.caption(
            "Review the generated code before using it. "
            "It has not been executed or verified."
        )

        st.code(
            result["corrected_code"],
            language=language.lower() if language != "Other" else "text"
        )

        file_extensions = {
            "Python": "py",
            "Java": "java",
            "C++": "cpp",
            "C": "c",
            "JavaScript": "js",
            "C#": "cs",
            "SQL": "sql"
        }

        st.download_button(
            label="Download Corrected Code",
            data=result["corrected_code"],
            file_name=f"corrected_code.{file_extensions.get(language, 'txt')}",
            mime="text/plain"
        )

        st.subheader("Explanation")

        st.write(result["explanation"])

    # -----------------------------------
    # Suggestions
    # -----------------------------------

    with tab3:

        st.subheader("Code Improvement Suggestions")

        if result["suggestions"]:

            for suggestion in result["suggestions"]:
                st.markdown(f"- {suggestion}")

        else:

            st.info("No additional suggestions.")

    # -----------------------------------
    # Test Cases
    # -----------------------------------

    with tab4:

        st.subheader("Suggested Test Cases")

        if result["tests"]:

            for index, test in enumerate(result["tests"], start=1):
                st.markdown(f"**Test {index}:** {test}")

        else:

            st.info("No test cases were suggested.")

    st.divider()

    st.caption(
        "AI-generated results may contain mistakes. "
        "Always review corrections before using them."
    )
