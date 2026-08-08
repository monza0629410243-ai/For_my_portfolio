# --- Automotive Diagnostic & Repair Assistant (Post-2000 Vehicles) ---
# Diagnostic guide for technicians — Not a formal automotive certification.
# Consult certified repair manuals and professionals for complex repairs.

SYMPTOMS = {
    "1": "Check Engine Light (MIL) Illuminated",
    "2": "Difficult Starting / Cranking But No Start",
    "3": "Rough Idle / Engine Vibration / Hesitation on Acceleration",
    "4": "Sluggish Acceleration / Lack of Power",
    "5": "Excessive Fuel Consumption",
    "6": "Abnormal Exhaust Smoke (Black / White / Blue Smoke)",
    "7": "Engine Overheating",
    "8": "Unusual Noises from Engine Bay or Suspension",
    "9": "Transmission Shifting Harshness / Delay / Failure to Shift",
    "10": "Steering Wheel Vibration During Braking / Brake Fade / Squealing",
    "11": "Heavy Steering / Noise When Turning / Misaligned Steering",
    "12": "AC Not Cooling / Musty Odor",
    "13": "Electrical System Faults / Rapid Battery Drain / Alternator Not Charging",
    "14": "Engine Oil or Fluid Leaks Under Vehicle",
    "15": "ABS / Traction Control Warning Light Illuminated",
}

GROUPS = [
    {
        "name": "Engine and Sensor Group (Diagnose with OBD-II Scanner)",
        "keys": {"1", "3", "4", "5"},
        "min_match": 2,
        "advices": [
            "Connect an OBD-II diagnostic scanner to the under-dash port (standard on all post-2000 vehicles).",
            "Read Diagnostic Trouble Codes (DTCs) and review Freeze Frame data from when the fault occurred.",
            "Check live data on the scanner display, such as fuel rail pressure and O2 sensor values.",
            "Remove and clean the throttle body, then perform an Idle Learn procedure via the scan tool.",
            "Inspect the air filter, fuel filter, and spark plugs; replace them if worn beyond service intervals.",
            "If codes indicate a faulty sensor (e.g., MAF Sensor), inspect wiring harnesses and clean connectors before replacing parts."
        ]
    },
    {
        "name": "Ignition and Fuel System Group (Engine Vibration / Lack of Power)",
        "keys": {"2", "3", "4", "6"},
        "min_match": 2,
        "advices": [
            "Check Misfire history in the scanner data to identify which cylinder is failing to fire.",
            "Swap ignition coils or spark plugs across cylinders to verify if the component is truly defective.",
            "Check fuel pressure using a mechanical fuel pressure gauge or scan tool live data.",
            "Clean fuel injectors using an ultrasonic bath or quality fuel injector cleaning additives.",
            "Inspect the fuel filter and fuel lines for any signs of leakage or restriction."
        ]
    },
    {
        "name": "Turbocharger and Exhaust System Group (Abnormal Smoke / Poor Acceleration)",
        "keys": {"4", "6", "8"},
        "min_match": 2,
        "advices": [
            "For common-rail diesel or turbocharged gasoline engines, check Boost Pressure via the OBD-II scanner.",
            "Inspect the intercooler and turbocharger boost hoses for cracks or leaks.",
            "Remove and clean carbon buildup from the EGR valve and intake manifold.",
            "For diesel vehicles equipped with a Diesel Particulate Filter (DPF), initiate a forced DPF Regeneration using the scan tool.",
            "Inspect the turbocharger shaft for excessive play or oil leakage into the intake tract."
        ]
    },
    {
        "name": "Engine Cooling System Group (Engine Overheating)",
        "keys": {"1", "7"},
        "min_match": 2,
        "advices": [
            "Verify actual coolant temperature via live scan data against the dashboard temperature gauge.",
            "Inspect the thermostat to ensure proper opening and closing operation.",
            "Check if electric radiator fans operate at all speeds (inspect cooling fan relays or motor wear).",
            "Inspect hose connections, radiator core, and water pump for leaks; refill with quality coolant.",
            "Do not continue driving if the engine is overheating to prevent severe cylinder head warping."
        ]
    },
    {
        "name": "Automatic Transmission System Group",
        "keys": {"1", "9"},
        "min_match": 2,
        "advices": [
            "Connect the scanner to the Transmission Control Module (TCM) to read transmission-specific DTCs.",
            "Check transmission fluid level, color, and odor; replace fluid and filter if dark or burnt.",
            "Perform an Actuator Test via the scan tool to verify transmission solenoid operation.",
            "Inspect engine and transmission mounts for wear or collapse, which causes harsh shifting engagement."
        ]
    },
    {
        "name": "Brake and ABS System Group",
        "keys": {"1", "10", "15"},
        "min_match": 2,
        "advices": [
            "Scan the ABS and traction control modules for diagnostic trouble codes.",
            "Inspect brake pad thickness and check brake rotors for warping or scoring.",
            "Check brake calipers to ensure pistons are not sticking and slide pins move freely.",
            "Bleed the brake system or use the scan tool's automated ABS Bleeding function if required.",
            "Inspect wheel speed sensors at each hub and check wiring harnesses for damage or debris."
        ]
    },
    {
        "name": "Steering and Suspension System Group",
        "keys": {"8", "11"},
        "min_match": 2,
        "advices": [
            "Inspect ball joints, tie rod ends, and steering rack bellows for looseness or wear.",
            "Check shock absorbers and strut mounts for fluid leaks or abnormal play.",
            "For Electronic Power Steering (EPS) systems, perform a Steering Angle Sensor calibration via scan tool.",
            "Perform a wheel alignment and balancing service if the vehicle pulls to one side or vibrates at speed."
        ]
    },
    {
        "name": "Electrical System and Charging Group",
        "keys": {"1", "13"},
        "min_match": 2,
        "advices": [
            "Test battery voltage: should read approximately 12.4–12.6V with engine off, and 13.5–14.5V with engine running.",
            "Check alternator output to ensure proper battery charging capability.",
            "Inspect fuses and relays in the engine bay and cabin fuse boxes for continuity and damage.",
            "Check battery terminals for corrosion, clean with warm water if necessary, and secure connections."
        ]
    },
    {
        "name": "AC and Fluid Leak Group",
        "keys": {"12", "14"},
        "min_match": 2,
        "advices": [
            "Check refrigerant level and system operating pressures using an AC manifold gauge set.",
            "Inspect the AC compressor, magnetic clutch, and evaporator core for refrigerant leaks.",
            "Clean or replace the cabin air filter and service the evaporator core if odors or low airflow occur.",
            "Inspect underbody fluid leaks (e.g., rear main seal, oil pan); clean oil residue and apply chalk to locate the source."
        ]
    },
]

URGENT_SYMPTOMS = {"7"}

def ask_confirmation():
    while True:
        answer = input("Would you like to launch the Automotive Diagnostic Assistant (OBD-II / Tech Guide)? (y/n) >>> ").strip().lower()
        if answer in ("y", "yes", "true"):
            return True
        elif answer in ("n", "no", "false"):
            return False
        else:
            print("Please type 'y' (yes) or 'n' (no).")


def show_menu():
    print("\n" + "=" * 65)
    print("     Technician Assistant: Vehicle Diagnostics (Post-2000)")
    print("=" * 65)
    print("*** Designed for use with OBD-II diagnostic scanners & hands-on expertise ***")
    print("-" * 65)
    for key, label in SYMPTOMS.items():
        print(f"  {key:>2}. {label}")
    print("-" * 65)
    print("Enter symptom numbers separated by commas (e.g., 1,3,4)")
    print("Type 'menu' to view the list again, or 'exit' to quit.")
    print("=" * 65)


def parse_selection(user_input):
    parts = [p.strip() for p in user_input.split(",") if p.strip()]
    valid = set()
    invalid = []
    for p in parts:
        if p in SYMPTOMS:
            valid.add(p)
        else:
            invalid.append(p)
    return valid, invalid


def analyze(selected_keys):
    matched_groups = []
    for group in GROUPS:
        overlap = selected_keys & group["keys"]
        if len(overlap) >= group["min_match"]:
            matched_groups.append(group)

    print("\n--- Diagnostic Analysis & Repair Guidelines ---")

    if not matched_groups:
        print("No primary symptom groups matched your selection. Please try again.")
    else:
        for group in matched_groups:
            print(f"\n• {group['name']}")
            print("  Inspection & Repair Procedures:")
            for tip in group["advices"]:
                print(f"    - {tip}")

    if selected_keys & URGENT_SYMPTOMS:
        print("\n⚠️  URGENT WARNING: Engine Overheating Detected!")
        print("    Advise immediate vehicle shutdown to prevent catastrophic engine damage (warped cylinder head).")

    print(
        "\nNote: This tool provides general guidance for OBD-II era vehicles (2000+). "
        "Always combine live data scanning with professional mechanical inspection."
    )


def main():
    if not ask_confirmation():
        print("\nExiting program. Have a great day and safe repairs!")
        return

    show_menu()
    while True:
        user_input = input("\nEnter vehicle symptom(s) >>> ").strip()

        if user_input.lower() == "exit":
            print("Exiting program. Good luck with your repairs!")
            break
        elif user_input.lower() == "menu":
            show_menu()
            continue
        elif not user_input:
            continue

        selected, invalid = parse_selection(user_input)

        if invalid:
            print(f"Invalid code(s): {', '.join(invalid)} (Type 'menu' to view symptom options)")

        if selected:
            analyze(selected)


if __name__ == "__main__":
    main()