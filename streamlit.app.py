import streamlit as st

if "auth" not in st.session_state:
    st.session_state["auth"] = False

if not st.session_state["auth"]:
    st.title("🔒 Pro-Sync Private Access")
    pwd = st.text_input("Enter Key:", type="password")
    if st.button("Unlock"):
        if pwd == "LowePilot2026":
            st.session_state["auth"] = True
            st.rerun()
        else:
            st.error("Invalid Key")
else:
    # --- THE 7-FIGURE APP ---
    st.title("🚧 Lowe's Pro-Sync Pilot")
    st.sidebar.metric("Loss Prevented", "$4,200")
    
    with st.form("check"):
        job = st.text_input("Job ID (e.g. LW-101)")
        cam = st.camera_input("Scan Material")
        stat = st.radio("Status", ["Perfect", "Damaged"])
        if st.form_submit_button("Submit"):
            st.success("Report Sent to Pro Desk")
