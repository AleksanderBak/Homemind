import sys

import streamlit.web.cli as stcli


def main():
    sys.argv = ["streamlit", "run", "homemind/app.py"]  # Path to your Streamlit app
    sys.exit(stcli.main())
