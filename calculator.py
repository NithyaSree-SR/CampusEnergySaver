<<<<<<< HEAD
def calculate_energy(ac_units, computers, lights, duration):

    # Approximate power consumption
    AC_POWER = 1.5          # kW per AC
    COMPUTER_POWER = 0.1    # kW per computer
    LIGHT_POWER = 0.04      # kW per light

    ac_energy = ac_units * AC_POWER * duration
    computer_energy = computers * COMPUTER_POWER * duration
    light_energy = lights * LIGHT_POWER * duration

    total_energy = ac_energy + computer_energy + light_energy

    return {
        "AC": ac_energy,
        "Computers": computer_energy,
        "Lights": light_energy,
        "Total": total_energy
    }


def calculate_potential_savings(
    students,
    ac_units,
    computers,
    lights,
    duration
):

    # Approximate power consumption
    AC_POWER = 1.5
    COMPUTER_POWER = 0.1
    LIGHT_POWER = 0.04

    savings = 0

    # Assume computers above the number of students
    # may be unnecessary
    unnecessary_computers = max(computers - students, 0)

    computer_savings = (
        unnecessary_computers
        * COMPUTER_POWER
        * duration
    )

    savings += computer_savings

    # If there are 2 or more ACs with low occupancy,
    # estimate one AC could potentially be avoided
    if ac_units >= 2 and students < 15:
        ac_savings = AC_POWER * duration
    else:
        ac_savings = 0

    savings += ac_savings

    # Estimate one light per student as sufficient for
    # this simple prototype
    unnecessary_lights = max(lights - students, 0)

    light_savings = (
        unnecessary_lights
        * LIGHT_POWER
        * duration
    )

    savings += light_savings

    return {
        "Computers": computer_savings,
        "AC": ac_savings,
        "Lights": light_savings,
        "Total": savings
    }


if __name__ == "__main__":

    result = calculate_energy(
        ac_units=2,
        computers=30,
        lights=10,
        duration=2
    )

    print("===== ENERGY ESTIMATE =====")
    print("AC Energy:", result["AC"], "kWh")
    print("Computer Energy:", result["Computers"], "kWh")
    print("Lighting Energy:", result["Lights"], "kWh")
    print("Total Energy:", result["Total"], "kWh")

    savings = calculate_potential_savings(
        students=8,
        ac_units=2,
        computers=30,
        lights=10,
        duration=2
    )

    print("\n===== POTENTIAL SAVINGS =====")
    print("Computer Savings:", savings["Computers"], "kWh")
    print("AC Savings:", savings["AC"], "kWh")
    print("Light Savings:", savings["Lights"], "kWh")
=======
def calculate_energy(ac_units, computers, lights, duration):

    # Approximate power consumption
    AC_POWER = 1.5          # kW per AC
    COMPUTER_POWER = 0.1    # kW per computer
    LIGHT_POWER = 0.04      # kW per light

    ac_energy = ac_units * AC_POWER * duration
    computer_energy = computers * COMPUTER_POWER * duration
    light_energy = lights * LIGHT_POWER * duration

    total_energy = ac_energy + computer_energy + light_energy

    return {
        "AC": ac_energy,
        "Computers": computer_energy,
        "Lights": light_energy,
        "Total": total_energy
    }


def calculate_potential_savings(
    students,
    ac_units,
    computers,
    lights,
    duration
):

    # Approximate power consumption
    AC_POWER = 1.5
    COMPUTER_POWER = 0.1
    LIGHT_POWER = 0.04

    savings = 0

    # Assume computers above the number of students
    # may be unnecessary
    unnecessary_computers = max(computers - students, 0)

    computer_savings = (
        unnecessary_computers
        * COMPUTER_POWER
        * duration
    )

    savings += computer_savings

    # If there are 2 or more ACs with low occupancy,
    # estimate one AC could potentially be avoided
    if ac_units >= 2 and students < 15:
        ac_savings = AC_POWER * duration
    else:
        ac_savings = 0

    savings += ac_savings

    # Estimate one light per student as sufficient for
    # this simple prototype
    unnecessary_lights = max(lights - students, 0)

    light_savings = (
        unnecessary_lights
        * LIGHT_POWER
        * duration
    )

    savings += light_savings

    return {
        "Computers": computer_savings,
        "AC": ac_savings,
        "Lights": light_savings,
        "Total": savings
    }


if __name__ == "__main__":

    result = calculate_energy(
        ac_units=2,
        computers=30,
        lights=10,
        duration=2
    )

    print("===== ENERGY ESTIMATE =====")
    print("AC Energy:", result["AC"], "kWh")
    print("Computer Energy:", result["Computers"], "kWh")
    print("Lighting Energy:", result["Lights"], "kWh")
    print("Total Energy:", result["Total"], "kWh")

    savings = calculate_potential_savings(
        students=8,
        ac_units=2,
        computers=30,
        lights=10,
        duration=2
    )

    print("\n===== POTENTIAL SAVINGS =====")
    print("Computer Savings:", savings["Computers"], "kWh")
    print("AC Savings:", savings["AC"], "kWh")
    print("Light Savings:", savings["Lights"], "kWh")
>>>>>>> a11ca4af62bd57625a554b4b60f23b3f9379e30b
    print("Total Potential Savings:", savings["Total"], "kWh")