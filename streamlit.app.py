import streamlit as st

# INITIALIZE TRACKING AT ZERO
if "total_saved" not in st.session_state:
    st.session_state["total_saved"] = 0.0  # Starts at $0 [cite: 2026-02-18]
    if "auth" not in st.session_state:
        st.session_state["auth"] = False

        import streamlit as st


        def init_state():
                if "total_saved" not in st.session_state:
                        st.session_state["total_saved"] = 0.0
                if "auth" not in st.session_state:
                        st.session_state["auth"] = False


        def login_flow():
                st.title("🔒 Pro-Sync Private Access")
                pwd = st.text_input("Enter Key:", type="password")
                if st.button("Unlock"):
                        if pwd == "LowePilot2026":
                                st.session_state["auth"] = True
                                st.experimental_rerun()
                        else:
                                st.error("Invalid key.")


        def dashboard():
                st.title("🛡️ Lowe's Pro-Sync Pilot")
                st.sidebar.metric("Verified Asset Value", f"${st.session_state['total_saved']:,.2f}")

                st.header("Live Data Input")
                with st.form("scan_form"):
                        job = st.text_input("Job ID (e.g. LW-101)")
                        price = st.number_input("Item Retail Value ($)", min_value=0.0, step=0.01, format="%.2f")
                        cam = st.camera_input("Scan Material Condition")
                        stat = st.radio("Status", ["Perfect", "Damaged"])
                        submitted = st.form_submit_button("Sync to Lowe's System")

                if submitted:
                        if job and price > 0:
                                st.session_state["total_saved"] += float(price)
                                st.success(f"Log {job} synced. ${price:,.2f} in value protected.")
                                st.experimental_rerun()
                        else:
                                st.warning("Please enter Job ID and Item Value.")


        def main():
                init_state()
                if not st.session_state["auth"]:
                        login_flow()
                else:
                        dashboard()


        if __name__ == "__main__":
                main()
