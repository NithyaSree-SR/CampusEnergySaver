<<<<<<< HEAD
import streamlit as st
import pandas as pd
import altair as alt

from agent import energy_agent


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Campus Energy Saver",
    page_icon="⚡",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("⚡ Campus Energy Saver")

st.subheader(
    "AI-Powered Energy Waste Detection & Savings Assistant"
)

st.write(
    "Enter the current conditions of a classroom or laboratory. "
    "The system analyzes energy usage, identifies potential wastage, "
    "retrieves relevant energy-saving knowledge using RAG, "
    "and provides actionable recommendations."
)

st.divider()


# =========================================================
# INPUT SECTION
# =========================================================

st.header("🏫 Current Room Conditions")

col1, col2 = st.columns(2)


with col1:

    room = st.text_input(
        "🏫 Room / Lab Name",
        value="CSE Lab"
    )

    students = st.number_input(
        "👥 Students currently present",
        min_value=0,
        max_value=200,
        value=8,
        step=1
    )

    computers = st.number_input(
        "💻 Computers currently ON",
        min_value=0,
        max_value=200,
        value=30,
        step=1
    )


with col2:

    ac_units = st.number_input(
        "❄️ AC units currently ON",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )

    ac_temperature = st.number_input(
        "🌡️ AC temperature (°C)",
        min_value=16,
        max_value=30,
        value=20,
        step=1
    )

    lights = st.number_input(
        "💡 Lights currently ON",
        min_value=0,
        max_value=100,
        value=10,
        step=1
    )


duration = st.number_input(
    "⏱️ Duration of operation (hours)",
    min_value=0.5,
    max_value=24.0,
    value=2.0,
    step=0.5
)


st.write("")


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze = st.button(
    "⚡ ANALYZE ENERGY USAGE",
    type="primary",
    use_container_width=True
)


# =========================================================
# RUN ANALYSIS
# =========================================================

if analyze:

    result = energy_agent(
        room,
        students,
        ac_units,
        ac_temperature,
        computers,
        lights,
        duration
    )


    # -----------------------------------------------------
    # GET RESULTS
    # -----------------------------------------------------

    level = result["waste_level"]

    energy = result["energy"]

    savings = result["savings"]


    st.divider()


    # =====================================================
    # ENERGY INTELLIGENCE
    # =====================================================

    st.header("📊 Energy Intelligence")


    if level == "HIGH":

        st.error(
            "🔴 HIGH ENERGY WASTE DETECTED"
        )

    elif level == "MEDIUM":

        st.warning(
            "🟡 MODERATE ENERGY WASTE DETECTED"
        )

    else:

        st.success(
            "🟢 LOW ENERGY WASTE"
        )


    # =====================================================
    # KPI CARDS
    # =====================================================

    st.subheader("📌 Key Metrics")

    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            label="🔴 Waste Level",
            value=level
        )


    with c2:

        st.metric(
            label="⚡ Estimated Energy",
            value=f"{energy['Total']:.2f} kWh"
        )


    with c3:

        st.metric(
            label="💰 Potential Savings",
            value=f"{savings['Total']:.2f} kWh"
        )


    with c4:

        st.metric(
            label="👥 Occupancy",
            value=students
        )


    st.divider()


    # =====================================================
    # GRAPHS
    # =====================================================

    st.header("📊 Energy Insights")


    chart_col1, chart_col2 = st.columns(2)


    # =====================================================
    # ENERGY CONSUMPTION GRAPH
    # =====================================================

    with chart_col1:

        st.subheader("⚡ Energy Consumption")


        energy_data = pd.DataFrame(
            {
                "Equipment": [
                    "Air Conditioners",
                    "Computers",
                    "Lighting"
                ],

                "Energy (kWh)": [
                    energy["AC"],
                    energy["Computers"],
                    energy["Lights"]
                ]
            }
        )


        energy_chart = (
            alt.Chart(energy_data)
            .mark_bar(
                color="#42A5F5",
                cornerRadiusTopLeft=5,
                cornerRadiusTopRight=5
            )
            .encode(
                x=alt.X(
                    "Equipment:N",
                    title="Equipment",
                    axis=alt.Axis(
                        labelAngle=0
                    )
                ),

                y=alt.Y(
                    "Energy (kWh):Q",
                    title="Energy (kWh)"
                ),

                tooltip=[
                    alt.Tooltip(
                        "Equipment:N",
                        title="Equipment"
                    ),

                    alt.Tooltip(
                        "Energy (kWh):Q",
                        title="Energy",
                        format=".2f"
                    )
                ]
            )
            .properties(
                height=300
            )
        )


        st.altair_chart(
            energy_chart,
            use_container_width=True
        )


        st.caption(
            f"❄️ AC: {energy['AC']:.2f} kWh   |   "
            f"💻 Computers: {energy['Computers']:.2f} kWh   |   "
            f"💡 Lighting: {energy['Lights']:.2f} kWh"
        )


        st.success(
            f"⚡ Total consumption: "
            f"**{energy['Total']:.2f} kWh**"
        )


    # =====================================================
    # POTENTIAL SAVINGS GRAPH
    # =====================================================

    with chart_col2:

        st.subheader("💰 Potential Savings")


        savings_data = pd.DataFrame(
            {
                "Equipment": [
                    "Computers",
                    "AC",
                    "Lighting"
                ],

                "Potential Savings (kWh)": [
                    savings["Computers"],
                    savings["AC"],
                    savings["Lights"]
                ]
            }
        )


        savings_chart = (
            alt.Chart(savings_data)
            .mark_bar(
                color="#26C281",
                cornerRadiusTopLeft=5,
                cornerRadiusTopRight=5
            )
            .encode(
                x=alt.X(
                    "Equipment:N",
                    title="Equipment",
                    axis=alt.Axis(
                        labelAngle=0
                    )
                ),

                y=alt.Y(
                    "Potential Savings (kWh):Q",
                    title="Savings (kWh)"
                ),

                tooltip=[
                    alt.Tooltip(
                        "Equipment:N",
                        title="Equipment"
                    ),

                    alt.Tooltip(
                        "Potential Savings (kWh):Q",
                        title="Savings",
                        format=".2f"
                    )
                ]
            )
            .properties(
                height=300
            )
        )


        st.altair_chart(
            savings_chart,
            use_container_width=True
        )


        st.caption(
            f"💻 Computers: {savings['Computers']:.2f} kWh   |   "
            f"❄️ AC: {savings['AC']:.2f} kWh   |   "
            f"💡 Lighting: {savings['Lights']:.2f} kWh"
        )


        st.success(
            f"💰 Total potential savings: "
            f"**{savings['Total']:.2f} kWh**"
        )


    st.divider()


    # =====================================================
    # REASONS + RECOMMENDATIONS
    # =====================================================

    left, right = st.columns(2)


    # -----------------------------------------------------
    # REASONS
    # -----------------------------------------------------

    with left:

        st.header("🔍 Why was this detected?")


        if result["reasons"]:

            for reason in result["reasons"]:

                st.warning(
                    f"🔎 {reason}"
                )

        else:

            st.success(
                "No major energy-waste indicators detected."
            )


    # -----------------------------------------------------
    # RECOMMENDATIONS
    # -----------------------------------------------------

    with right:

        st.header("💡 Recommended Actions")


        if result["recommendations"]:

            for recommendation in result["recommendations"]:

                st.success(
                    f"✓ {recommendation}"
                )

        else:

            st.success(
                "Current usage appears reasonable."
            )


    st.divider()


    # =====================================================
    # STAFF ALERT
    # =====================================================

    if result["staff_alert"]:

        st.error(
            f"""
🚨 **STAFF ALERT**

Potential energy wastage detected in **{room}**.

Current status: **{level}**

Suggested action: Review unnecessary equipment usage.
"""
        )

    else:

        st.success(
            "✅ No high-priority staff alert generated."
        )


    st.divider()


    # =====================================================
    # CURRENT ROOM SUMMARY
    # =====================================================

    st.header("🏫 Current Room Summary")


    summary_col1, summary_col2 = st.columns(2)


    with summary_col1:

        st.write(
            f"**Room:** {room}"
        )

        st.write(
            f"**Students present:** {students}"
        )

        st.write(
            f"**Computers ON:** {computers}"
        )

        st.write(
            f"**Lights ON:** {lights}"
        )


    with summary_col2:

        st.write(
            f"**AC units ON:** {ac_units}"
        )

        st.write(
            f"**AC temperature:** {ac_temperature}°C"
        )

        st.write(
            f"**Duration:** {duration} hours"
        )

        st.write(
            f"**Waste status:** {level}"
        )


    st.divider()


    # =====================================================
    # RAG KNOWLEDGE
    # =====================================================

    st.header("🤖 AI Knowledge Retrieved")


    st.write(
        "The system uses Retrieval-Augmented Generation (RAG) "
        "to retrieve relevant energy-saving guidelines from "
        "the sustainability knowledge base."
    )


    with st.expander("🔎 View Retrieved Knowledge"):

        for knowledge in result["rag_knowledge"]:

            st.write(knowledge)

            st.divider()


    # =====================================================
    # RESPONSIBLE AI
    # =====================================================

    st.header("🛡️ Responsible AI Considerations")


    st.info(
        """
**Approximate estimates**

Energy values are calculated using assumed appliance
power ratings.

**User-provided conditions**

The prototype analyzes conditions entered by the user
rather than real physical IoT or sensor measurements.

**Human decision-making**

The system provides recommendations. It does not
automatically control ACs, computers or lights.

**Safety and comfort**

Energy-saving actions should not compromise visibility,
productivity, safety or occupant comfort.

**Equipment variation**

Actual energy consumption may vary depending on appliance
model, power rating, operating conditions and duration.
"""
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()


st.caption(
    "⚡ Campus Energy Saver | "
    "AI for Sustainable Campus Energy Management | "
    "SDG 7 • SDG 12"
=======
import streamlit as st
import pandas as pd
import altair as alt

from agent import energy_agent


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Campus Energy Saver",
    page_icon="⚡",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("⚡ Campus Energy Saver")

st.subheader(
    "AI-Powered Energy Waste Detection & Savings Assistant"
)

st.write(
    "Enter the current conditions of a classroom or laboratory. "
    "The system analyzes energy usage, identifies potential wastage, "
    "retrieves relevant energy-saving knowledge using RAG, "
    "and provides actionable recommendations."
)

st.divider()


# =========================================================
# INPUT SECTION
# =========================================================

st.header("🏫 Current Room Conditions")

col1, col2 = st.columns(2)


with col1:

    room = st.text_input(
        "🏫 Room / Lab Name",
        value="CSE Lab"
    )

    students = st.number_input(
        "👥 Students currently present",
        min_value=0,
        max_value=200,
        value=8,
        step=1
    )

    computers = st.number_input(
        "💻 Computers currently ON",
        min_value=0,
        max_value=200,
        value=30,
        step=1
    )


with col2:

    ac_units = st.number_input(
        "❄️ AC units currently ON",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )

    ac_temperature = st.number_input(
        "🌡️ AC temperature (°C)",
        min_value=16,
        max_value=30,
        value=20,
        step=1
    )

    lights = st.number_input(
        "💡 Lights currently ON",
        min_value=0,
        max_value=100,
        value=10,
        step=1
    )


duration = st.number_input(
    "⏱️ Duration of operation (hours)",
    min_value=0.5,
    max_value=24.0,
    value=2.0,
    step=0.5
)


st.write("")


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze = st.button(
    "⚡ ANALYZE ENERGY USAGE",
    type="primary",
    use_container_width=True
)


# =========================================================
# RUN ANALYSIS
# =========================================================

if analyze:

    result = energy_agent(
        room,
        students,
        ac_units,
        ac_temperature,
        computers,
        lights,
        duration
    )


    # -----------------------------------------------------
    # GET RESULTS
    # -----------------------------------------------------

    level = result["waste_level"]

    energy = result["energy"]

    savings = result["savings"]


    st.divider()


    # =====================================================
    # ENERGY INTELLIGENCE
    # =====================================================

    st.header("📊 Energy Intelligence")


    if level == "HIGH":

        st.error(
            "🔴 HIGH ENERGY WASTE DETECTED"
        )

    elif level == "MEDIUM":

        st.warning(
            "🟡 MODERATE ENERGY WASTE DETECTED"
        )

    else:

        st.success(
            "🟢 LOW ENERGY WASTE"
        )


    # =====================================================
    # KPI CARDS
    # =====================================================

    st.subheader("📌 Key Metrics")

    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            label="🔴 Waste Level",
            value=level
        )


    with c2:

        st.metric(
            label="⚡ Estimated Energy",
            value=f"{energy['Total']:.2f} kWh"
        )


    with c3:

        st.metric(
            label="💰 Potential Savings",
            value=f"{savings['Total']:.2f} kWh"
        )


    with c4:

        st.metric(
            label="👥 Occupancy",
            value=students
        )


    st.divider()


    # =====================================================
    # GRAPHS
    # =====================================================

    st.header("📊 Energy Insights")


    chart_col1, chart_col2 = st.columns(2)


    # =====================================================
    # ENERGY CONSUMPTION GRAPH
    # =====================================================

    with chart_col1:

        st.subheader("⚡ Energy Consumption")


        energy_data = pd.DataFrame(
            {
                "Equipment": [
                    "Air Conditioners",
                    "Computers",
                    "Lighting"
                ],

                "Energy (kWh)": [
                    energy["AC"],
                    energy["Computers"],
                    energy["Lights"]
                ]
            }
        )


        energy_chart = (
            alt.Chart(energy_data)
            .mark_bar(
                color="#42A5F5",
                cornerRadiusTopLeft=5,
                cornerRadiusTopRight=5
            )
            .encode(
                x=alt.X(
                    "Equipment:N",
                    title="Equipment",
                    axis=alt.Axis(
                        labelAngle=0
                    )
                ),

                y=alt.Y(
                    "Energy (kWh):Q",
                    title="Energy (kWh)"
                ),

                tooltip=[
                    alt.Tooltip(
                        "Equipment:N",
                        title="Equipment"
                    ),

                    alt.Tooltip(
                        "Energy (kWh):Q",
                        title="Energy",
                        format=".2f"
                    )
                ]
            )
            .properties(
                height=300
            )
        )


        st.altair_chart(
            energy_chart,
            use_container_width=True
        )


        st.caption(
            f"❄️ AC: {energy['AC']:.2f} kWh   |   "
            f"💻 Computers: {energy['Computers']:.2f} kWh   |   "
            f"💡 Lighting: {energy['Lights']:.2f} kWh"
        )


        st.success(
            f"⚡ Total consumption: "
            f"**{energy['Total']:.2f} kWh**"
        )


    # =====================================================
    # POTENTIAL SAVINGS GRAPH
    # =====================================================

    with chart_col2:

        st.subheader("💰 Potential Savings")


        savings_data = pd.DataFrame(
            {
                "Equipment": [
                    "Computers",
                    "AC",
                    "Lighting"
                ],

                "Potential Savings (kWh)": [
                    savings["Computers"],
                    savings["AC"],
                    savings["Lights"]
                ]
            }
        )


        savings_chart = (
            alt.Chart(savings_data)
            .mark_bar(
                color="#26C281",
                cornerRadiusTopLeft=5,
                cornerRadiusTopRight=5
            )
            .encode(
                x=alt.X(
                    "Equipment:N",
                    title="Equipment",
                    axis=alt.Axis(
                        labelAngle=0
                    )
                ),

                y=alt.Y(
                    "Potential Savings (kWh):Q",
                    title="Savings (kWh)"
                ),

                tooltip=[
                    alt.Tooltip(
                        "Equipment:N",
                        title="Equipment"
                    ),

                    alt.Tooltip(
                        "Potential Savings (kWh):Q",
                        title="Savings",
                        format=".2f"
                    )
                ]
            )
            .properties(
                height=300
            )
        )


        st.altair_chart(
            savings_chart,
            use_container_width=True
        )


        st.caption(
            f"💻 Computers: {savings['Computers']:.2f} kWh   |   "
            f"❄️ AC: {savings['AC']:.2f} kWh   |   "
            f"💡 Lighting: {savings['Lights']:.2f} kWh"
        )


        st.success(
            f"💰 Total potential savings: "
            f"**{savings['Total']:.2f} kWh**"
        )


    st.divider()


    # =====================================================
    # REASONS + RECOMMENDATIONS
    # =====================================================

    left, right = st.columns(2)


    # -----------------------------------------------------
    # REASONS
    # -----------------------------------------------------

    with left:

        st.header("🔍 Why was this detected?")


        if result["reasons"]:

            for reason in result["reasons"]:

                st.warning(
                    f"🔎 {reason}"
                )

        else:

            st.success(
                "No major energy-waste indicators detected."
            )


    # -----------------------------------------------------
    # RECOMMENDATIONS
    # -----------------------------------------------------

    with right:

        st.header("💡 Recommended Actions")


        if result["recommendations"]:

            for recommendation in result["recommendations"]:

                st.success(
                    f"✓ {recommendation}"
                )

        else:

            st.success(
                "Current usage appears reasonable."
            )


    st.divider()


    # =====================================================
    # STAFF ALERT
    # =====================================================

    if result["staff_alert"]:

        st.error(
            f"""
🚨 **STAFF ALERT**

Potential energy wastage detected in **{room}**.

Current status: **{level}**

Suggested action: Review unnecessary equipment usage.
"""
        )

    else:

        st.success(
            "✅ No high-priority staff alert generated."
        )


    st.divider()


    # =====================================================
    # CURRENT ROOM SUMMARY
    # =====================================================

    st.header("🏫 Current Room Summary")


    summary_col1, summary_col2 = st.columns(2)


    with summary_col1:

        st.write(
            f"**Room:** {room}"
        )

        st.write(
            f"**Students present:** {students}"
        )

        st.write(
            f"**Computers ON:** {computers}"
        )

        st.write(
            f"**Lights ON:** {lights}"
        )


    with summary_col2:

        st.write(
            f"**AC units ON:** {ac_units}"
        )

        st.write(
            f"**AC temperature:** {ac_temperature}°C"
        )

        st.write(
            f"**Duration:** {duration} hours"
        )

        st.write(
            f"**Waste status:** {level}"
        )


    st.divider()


    # =====================================================
    # RAG KNOWLEDGE
    # =====================================================

    st.header("🤖 AI Knowledge Retrieved")


    st.write(
        "The system uses Retrieval-Augmented Generation (RAG) "
        "to retrieve relevant energy-saving guidelines from "
        "the sustainability knowledge base."
    )


    with st.expander("🔎 View Retrieved Knowledge"):

        for knowledge in result["rag_knowledge"]:

            st.write(knowledge)

            st.divider()


    # =====================================================
    # RESPONSIBLE AI
    # =====================================================

    st.header("🛡️ Responsible AI Considerations")


    st.info(
        """
**Approximate estimates**

Energy values are calculated using assumed appliance
power ratings.

**User-provided conditions**

The prototype analyzes conditions entered by the user
rather than real physical IoT or sensor measurements.

**Human decision-making**

The system provides recommendations. It does not
automatically control ACs, computers or lights.

**Safety and comfort**

Energy-saving actions should not compromise visibility,
productivity, safety or occupant comfort.

**Equipment variation**

Actual energy consumption may vary depending on appliance
model, power rating, operating conditions and duration.
"""
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()


st.caption(
    "⚡ Campus Energy Saver | "
    "AI for Sustainable Campus Energy Management | "
    "SDG 7 • SDG 12"
>>>>>>> a11ca4af62bd57625a554b4b60f23b3f9379e30b
)