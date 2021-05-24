import re
import requests
import streamlit as st

from contextlib import contextmanager
from pathlib import Path

_filter_share = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)


@contextmanager
def readme(project, usage=None, source=None):
    content = requests.get(f"https://raw.githubusercontent.com/okld/{project}/main/README.md").text
    st.markdown(_filter_share.sub("", content))

    demo = st.beta_container()

    if usage or source:
        st.write("---")

    if usage:
        with st.beta_expander("USAGE"):
            st.help(usage)
    
    if source:
        with st.beta_expander("SOURCE"):
            st.code(Path(source).read_text())

    with demo:
        yield
