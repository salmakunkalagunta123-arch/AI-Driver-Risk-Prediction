import streamlit as st

st.set_page_config(
    page_title="AI Driver Safety Assistant",
    page_icon="🚗"
)

st.title("🚗 AI Driver Risk Prediction & Safety Assistant")
st.write("Analyze driver conditions and identify the current safety risk.")

st.subheader("Enter Driver Details")

speed = st.slider("Driving Speed (km/h)", 0, 160, 60)
alcohol = st.slider("Alcohol Level", 0.0, 0.10, 0.0, 0.01)
drowsiness = st.checkbox("😴 Drowsiness Detected")
rash_driving = st.checkbox("⚠️ Rash Driving Detected")
heart_risk = st.checkbox("❤️ Health Risk Indication")

if st.button("🔍 Analyze Driver Risk"):

    risk_score = 0

    # Speed analysis
    if speed > 100:
        risk_score += 2
    elif speed > 80:
        risk_score += 1

    # Alcohol analysis
    if alcohol > 0.03:
        risk_score += 3
    elif alcohol > 0:
        risk_score += 1

    # Other risk factors
    if drowsiness:
        risk_score += 3

    if rash_driving:
        risk_score += 2

    if heart_risk:
        risk_score += 2

    # Risk prediction
    if risk_score >= 6:
        risk = "HIGH RISK 🚨"
        message = "Immediate safety action is recommended."
        st.error(risk)

    elif risk_score >= 3:
        risk = "MEDIUM RISK ⚠️"
        message = "Driver should slow down and remain alert."
        st.warning(risk)

    else:
        risk = "LOW RISK ✅"
        message = "Current driving conditions appear relatively safe."
        st.success(risk)

    st.write("### 📊 Safety Analysis")
    st.write("Risk Score:", risk_score)
    st.write("Recommendation:", message)

    if risk_score >= 6:
        st.info("🚑 Emergency assistance may be required if the situation is critical.")
    elif drowsiness:
        st.info("😴 Please take a break and avoid continuing while drowsy.")
    elif rash_driving:
        st.info("⚠️ Reduce speed and drive carefully.")
    else:
        st.info("✅ Continue following safe driving practices.")
