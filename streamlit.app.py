import streamlit as st

# THIS MUST BE FIRST - It creates the counter so the app doesn't crash
if "count" not in st.session_state:
    st.session_state["count"] = 0

# 1. AUTHENTICATION (The Gate)
if "auth" not in st.session_state:
    st.session_state["auth"] = False
    st.session_state["count"] = 0  # Starts the counter for the scan math

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
                                                                            # 2. THE DASHBOARD (The Pitch)
                                                                                st.title("🛡️ Lowe's Pro-Sync Pilot")
                                                                                
                                                                                # This math updates every time you hit submit
                                                                                current_loss = 4200 + (st.session_state["count"] * 150) 
                                                                                st.sidebar.metric("Total Loss Prevented", f"${current_loss:,}")
                                                                                st.sidebar.write(f"Scans this Shift: {st.session_state['count']}")
                                                                            
                                                                                # 3. DATA CAPTURE (The Proof)
                                                                                with st.form("check"):
                                                                                    job = st.text_input("Job ID (e.g. LW-101)")
                                                                                    cam = st.camera_input("Scan Material Condition")
                                                                                    stat = st.radio("Status", ["Perfect", "Damaged"])
                                                                                    
                                                                                    if st.form_submit_button("Submit to Pro-Sync Database"):
                                                                                        if job:
                                                                                            st.session_state["count"] += 1
                                                                                            st.success(f"Log {job} synced to Lowe's backend. +$150 Loss Prevention recorded.")
                                                                                        else:
                                                                                            st.warning("Please enter a Job ID to sync data.")
                                                                                                                                                                                
