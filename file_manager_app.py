import streamlit as st
from pathlib import Path
import time

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="FileVault | File Handling System",
    page_icon="🗂️",
    layout="centered",
)

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
    <style>
        .main-title {
            font-size: 2.4rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0px;
            background: -webkit-linear-gradient(45deg, #4F8BF9, #1DE9B6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .sub-title {
            text-align: center;
            color: #888;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }
        .stButton>button {
            border-radius: 10px;
            font-weight: 600;
            padding: 0.5rem 1.2rem;
            transition: 0.2s;
        }
        .stButton>button:hover {
            transform: scale(1.02);
        }
        .footer-note {
            text-align: center;
            color: #aaa;
            font-size: 0.8rem;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# All files created/managed by this app live inside a sandbox folder
BASE_DIR = Path("filevault_storage")
BASE_DIR.mkdir(exist_ok=True)

# ---------------------- HEADER ----------------------
st.markdown('<div class="main-title">🗂️ FileVault</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">A simple Create • Read • Update • Delete file manager built with Python & Streamlit</div>', unsafe_allow_html=True)

# ---------------------- SIDEBAR NAVIGATION ----------------------
st.sidebar.title("⚙️ Operations")
menu = st.sidebar.radio(
    "Choose an action",
    ["📄 Create File", "📖 Read File", "✏️ Update File", "🗑️ Delete File", "📂 View All Files"],
)

st.sidebar.markdown("---")
existing_files = sorted([f.name for f in BASE_DIR.iterdir() if f.is_file()])
st.sidebar.metric("Total Files", len(existing_files))

# ---------------------- CREATE FILE ----------------------
if menu == "📄 Create File":
    st.header("📄 Create a New File")

    with st.form("create_form", clear_on_submit=True):
        filename = st.text_input("File name (e.g. notes.txt)")
        content = st.text_area("File content", height=150)
        submitted = st.form_submit_button("🚀 Create File")

    if submitted:
        if not filename.strip():
            st.error("⚠️ Please enter a file name.")
        else:
            path = BASE_DIR / filename
            if path.exists():
                st.error(f"❌ A file named **{filename}** already exists.")
            else:
                path.write_text(content)
                st.success(f"✅ File **{filename}** created successfully!")
                st.balloons()

# ---------------------- READ FILE ----------------------
elif menu == "📖 Read File":
    st.header("📖 Read a File")

    if not existing_files:
        st.info("No files available yet. Create one first!")
    else:
        selected = st.selectbox("Select a file to read", existing_files)
        if st.button("🔍 Show Content"):
            path = BASE_DIR / selected
            if path.exists():
                content = path.read_text()
                st.code(content or "(This file is empty)", language="text")
            else:
                st.error("❌ File not found.")

# ---------------------- UPDATE FILE ----------------------
elif menu == "✏️ Update File":
    st.header("✏️ Update a File")

    if not existing_files:
        st.info("No files available yet. Create one first!")
    else:
        selected = st.selectbox("Select a file to update", existing_files)
        path = BASE_DIR / selected

        action = st.radio("Choose an operation", ["Rename", "Append content", "Overwrite content"])

        if action == "Rename":
            new_name = st.text_input("Enter new file name")
            if st.button("✅ Rename"):
                new_path = BASE_DIR / new_name
                if not new_name.strip():
                    st.error("⚠️ Please enter a valid name.")
                elif new_path.exists():
                    st.error(f"❌ A file named **{new_name}** already exists.")
                else:
                    path.rename(new_path)
                    st.success(f"✅ Renamed to **{new_name}** successfully!")
                    time.sleep(0.8)
                    st.rerun()

        elif action == "Append content":
            extra = st.text_area("Content to append", height=100)
            if st.button("➕ Append"):
                with open(path, "a") as f:
                    f.write("\n" + extra)
                st.success("✅ Content appended successfully!")

        elif action == "Overwrite content":
            new_content = st.text_area("New content (replaces everything)", height=150)
            if st.button("♻️ Overwrite"):
                path.write_text(new_content)
                st.success("✅ File overwritten successfully!")

# ---------------------- DELETE FILE ----------------------
elif menu == "🗑️ Delete File":
    st.header("🗑️ Delete a File")

    if not existing_files:
        st.info("No files available yet. Create one first!")
    else:
        selected = st.selectbox("Select a file to delete", existing_files)
        confirm = st.checkbox(f"I confirm I want to permanently delete **{selected}**")
        if st.button("🗑️ Delete", disabled=not confirm):
            path = BASE_DIR / selected
            if path.exists():
                path.unlink()
                st.success(f"✅ **{selected}** deleted successfully!")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("❌ File not found.")

# ---------------------- VIEW ALL FILES ----------------------
elif menu == "📂 View All Files":
    st.header("📂 All Files in Vault")

    if not existing_files:
        st.info("No files created yet. Start by creating one!")
    else:
        for f in existing_files:
            fpath = BASE_DIR / f
            size = fpath.stat().st_size
            with st.expander(f"📄 {f}  —  {size} bytes"):
                st.code(fpath.read_text() or "(empty file)", language="text")

# ---------------------- FOOTER ----------------------
st.markdown(
    '<div class="footer-note">Built with 🐍 Python + Streamlit — a beginner project demonstrating file handling (CRUD) operations.</div>',
    unsafe_allow_html=True,
)
