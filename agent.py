from rag import get_vector_database
from calculator import calculate_energy, calculate_potential_savings


# Load the RAG knowledge base
vectorstore = get_vector_database()


def energy_agent(
    room,
    students,
    ac_units,
    ac_temperature,
    computers,
    lights,
    duration
):

    # --------------------------------
    # CURRENT SITUATION
    # --------------------------------

    situation = f"""
    Room: {room}
    Students present: {students}
    AC units running: {ac_units}
    AC temperature: {ac_temperature}°C
    Computers running: {computers}
    Lights running: {lights}
    Duration: {duration} hours
    """


    # --------------------------------
    # ENERGY CALCULATION
    # --------------------------------

    energy = calculate_energy(
        ac_units,
        computers,
        lights,
        duration
    )


    # --------------------------------
    # RAG RETRIEVAL
    # --------------------------------

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    results = retriever.invoke(
        " ".join(situation.split())
        + " energy saving recommendations"
    )


    rag_knowledge = []

    for doc in results:
        rag_knowledge.append(doc.page_content)


    # --------------------------------
    # WASTE DETECTION
    # --------------------------------

    reasons = []
    recommendations = []


    if students == 0:

        waste_level = "HIGH"

        reasons.append(
            "The room is currently unoccupied while equipment is running."
        )

        recommendations.append(
            "Switch off unnecessary equipment when the room is unoccupied."
        )


    elif computers > students * 2:

        waste_level = "HIGH"

        reasons.append(
            f"{computers} computers are running for only {students} students."
        )

        unnecessary = computers - students

        recommendations.append(
            f"Check whether {unnecessary} computers can be switched off if they are not required."
        )


    elif ac_units >= 2 and students < 15:

        waste_level = "MEDIUM"

        reasons.append(
            f"{ac_units} AC units are running for a low occupancy of {students} students."
        )

        recommendations.append(
            "Check whether all running AC units are required for the current occupancy."
        )


    else:

        waste_level = "LOW"


    # --------------------------------
    # ADDITIONAL CONDITIONS
    # --------------------------------

    if ac_temperature <= 20:

        reasons.append(
            f"The AC temperature is set to {ac_temperature}°C."
        )

        recommendations.append(
            "Consider a reasonable AC temperature while maintaining occupant comfort."
        )


    if lights > students and students > 0:

        reasons.append(
            f"{lights} lights are running for {students} students."
        )

        recommendations.append(
            "Switch off unnecessary lights while maintaining adequate visibility and safety."
        )


    # --------------------------------
    # POTENTIAL SAVINGS
    # --------------------------------

    savings = calculate_potential_savings(
        students,
        ac_units,
        computers,
        lights,
        duration
    )


    # --------------------------------
    # STAFF ALERT
    # --------------------------------

    staff_alert = waste_level == "HIGH"


    # --------------------------------
    # RETURN ALL RESULTS
    # --------------------------------

    return {

        "room": room,

        "students": students,

        "ac_units": ac_units,

        "ac_temperature": ac_temperature,

        "computers": computers,

        "lights": lights,

        "duration": duration,

        "waste_level": waste_level,

        "reasons": reasons,

        "recommendations": recommendations,

        "energy": energy,

        "savings": savings,

        "staff_alert": staff_alert,

        "rag_knowledge": rag_knowledge
    }


# --------------------------------
# TERMINAL TESTING
# --------------------------------

if __name__ == "__main__":

    print("\n===== CAMPUS ENERGY SAVER =====")

    room = input("Enter room/lab name: ")

    students = int(
        input("Students currently present: ")
    )

    computers = int(
        input("Computers currently ON: ")
    )

    ac_units = int(
        input("AC units currently ON: ")
    )

    ac_temperature = int(
        input("AC temperature (°C): ")
    )

    lights = int(
        input("Lights currently ON: ")
    )

    duration = float(
        input("Hours running: ")
    )


    result = energy_agent(
        room,
        students,
        ac_units,
        ac_temperature,
        computers,
        lights,
        duration
    )


    print("\n===== RESULT =====")

    print(
        "Waste Level:",
        result["waste_level"]
    )

    print(
        "Total Energy:",
        result["energy"]["Total"],
        "kWh"
    )

    print(
        "Potential Savings:",
        result["savings"]["Total"],
        "kWh"
    )