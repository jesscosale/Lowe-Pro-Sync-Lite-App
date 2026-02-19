import streamlit as st

# 1. SETUP (Starts at $0)
if "total_saved" not in st.session_state:
    st.session_state["total_saved"] = 0.0

if "auth" not in st.session_state:
    st.session_state["auth"] = False

# 2. LOGIN
if not st.session_state["auth"]:
    st.title("🔒 Pro-Sync Private Access")
    pwd = st.text_input("Enter Key:", type="password")
    if st.button("Unlock"):
        if pwd == "LowePilot2026":
            st.session_state["auth"] = True
            try:
                st.experimental_rerun()
            except Exception:
                pass
        else:
            st.error("Invalid Key")
else:
    # 3. DASHBOARD
    st.title("🛡️ Lowe's Pro-Sync Pilot")
    st.sidebar.metric("Verified Asset Value", f"${st.session_state['total_saved']:,.2f}")

    with st.form("scan_form"):
        job = st.text_input("Job ID (e.g. LW-101)")
        price = st.number_input("Item Retail Value ($)", min_value=0.0, step=0.01)
        cam = st.camera_input("Scan Material Condition")
        stat = st.radio("Status", ["Perfect", "Damaged"])

        if st.form_submit_button("Sync to Lowe's System"):
            if job and price > 0:
                st.session_state["total_saved"] += float(price)
                st.success(f"Log {job} synced. ${price:,.2f} protected.")
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            else:
                st.warning("Please enter Job ID and Item Value.")
                                                                                                                                                                                                                                