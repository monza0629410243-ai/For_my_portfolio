# --- Basic Symptom Checker (Console) ---
# Educational tool only — NOT a medical diagnosis.
# Gives general symptom groupings and general self-care tips.
# Always advises seeing a doctor/pharmacist for real diagnosis or medication.

SYMPTOMS = {
    "1": "Fever / High body temperature",
    "2": "Cough",
    "3": "Sore throat",
    "4": "Runny nose / Nasal congestion",
    "5": "Headache",
    "6": "Abdominal pain",
    "7": "Diarrhea",
    "8": "Nausea / Vomiting",
    "9": "Body aches / Muscle pain",
    "10": "Shortness of breath / Breathing difficulty",
    "11": "Itchy rash / Red rash",
    "12": "Red eyes",
    "13": "Loss of taste or smell",
    "14": "Painful or burning urination",
    "15": "Earache",
}

GROUPS = [
    {
        "name": "Potential condition: Common Cold",
        "keys": {"1", "2", "3", "4", "5"},
        "min_match": 2,
        "advices": [
            "Get plenty of rest and drink plenty of water.",
            "If you have a fever, use a damp cloth to cool down and take antipyretic medication according to product label instructions.",
            "Avoid close contact with others to reduce spreading infections; wear a face mask.",
            "Consume warm meals, herbal teas (such as ginger), and high-vitamin-C foods to help your body recover faster.",
            "For fever or body aches, you can take paracetamol according to your body weight and label guidelines.",
            "If coughing heavily, consider taking cough suppressants or expectorants based on your symptoms.",
            "For nasal congestion or a runny nose, decongestants can help ease breathing."
        ]
    },
    {
        "name": "Potential condition: Influenza (Flu)",
        "keys": {"1", "2", "3", "5", "9"},
        "min_match": 2,
        "advices": [
            "Get plenty of rest and stay well-hydrated.",
            "If you have a fever, cool down your body and take fever-reducing medication as directed on the label.",
            "Avoid close contact with others and wear a face mask to prevent transmission.",
            "Consume warm soups, ginger tea, and high-vitamin-C foods to boost recovery.",
            "Take paracetamol for fever and aches following package instructions.",
            "Manage severe coughs with appropriate cough syrup or expectorants.",
            "Use decongestants if nasal congestion makes breathing difficult."
        ]
    },
    {
        "name": "Potential condition: COVID-19",
        "keys": {"1", "2", "5", "9", "13"},
        "min_match": 2,
        "advices": [
            "Recommended to take an ATK test to confirm results and self-isolate from others while waiting.",
            "Get adequate rest, drink plenty of water, and keep your body warm.",
            "Wear a face mask at all times around others and separate your personal items.",
            "Take paracetamol for fever and body aches following label instructions.",
            "Monitor symptoms closely; seek immediate medical attention if you experience shortness of breath, chest tightness, bluish lips, or lethargy.",
            "High-risk individuals (elderly, chronic conditions, pregnant) should contact a healthcare provider promptly regarding antiviral treatment.",
            "Boost your immune system with warm foods, ginger, and high-vitamin-C items (avoid if you have liver disease or take blood thinners)."
        ]
    },
    {
        "name": "Potential condition: Pharyngitis / Tonsillitis",
        "keys": {"3", "5", "1"},
        "min_match": 2,
        "advices": [
            "Sip warm water or honey with lemon frequently to soothe throat irritation.",
            "Gargle with warm salt water 2-3 times a day to reduce inflammation.",
            "Avoid spicy, fried, hard, and very cold foods and drinks.",
            "Rest your voice and speak softly to minimize throat irritation.",
            "Combine warm honey, lemon, or ginger tea with appropriate medication to enhance soothing effects.",
            "Take paracetamol or throat lozenges for severe pain following package directions.",
            "If you experience severe pain, difficulty swallowing, white pus spots on tonsils, or high fever lasting over 2-3 days, see a doctor for antibiotics if necessary."
        ]
    },
    {
        "name": "Potential condition: Bronchitis",
        "keys": {"2", "10", "1", "9"},
        "min_match": 2,
        "advices": [
            "Get adequate rest and drink plenty of warm water to help loosen mucus.",
            "Avoid cigarette smoke, dust, and cold air, which can trigger more coughing.",
            "Inhale warm steam (such as during a warm shower) to help clear airways.",
            "Sip warm honey lemon or ginger tea alongside treatments to ease irritation.",
            "For productive coughs, take expectorants or cough medicines according to label guidelines.",
            "If coughing lasts longer than 2-3 weeks, contains blood, or if you experience wheezing or worsening shortness of breath, see a doctor immediately."
        ]
    },
    {
        "name": "Potential condition: Pneumonia",
        "keys": {"1", "2", "9", "10"},
        "min_match": 3,
        "advices": [
            "⚠️ This condition requires professional medical diagnosis. Please visit a hospital promptly for an examination or chest X-ray.",
            "Rest fully and drink plenty of warm fluids to help loosen phlegm.",
            "Sip warm honey, lemon, or ginger tea alongside prescribed medication to ease throat irritation.",
            "If you experience high fever, rapid breathing, shortness of breath, chest tightness, bluish lips, or confusion, go to the emergency room immediately.",
            "Do not purchase or take antibiotics without a doctor's prescription."
        ]
    },
    {
        "name": "Potential condition: Food Poisoning",
        "keys": {"6", "7", "8"},
        "min_match": 2,
        "advices": [
            "Sip oral rehydration salts (ORS) frequently to prevent dehydration from diarrhea or vomiting.",
            "Eat soft, easily digestible foods like rice soup or congee; avoid oily, spicy foods and dairy.",
            "Sip warm ginger tea to help reduce nausea and relieve gas.",
            "Rest sufficiently and avoid heavy physical exertion.",
            "If severe diarrhea/vomiting occurs, blood appears in stool, high fever develops, or dehydration signs show (dry mouth, low urine, dizziness), seek medical care immediately."
        ]
    },
    {
        "name": "Potential condition: Gastroenteritis (Intestinal Inflammation)",
        "keys": {"6", "7", "1"},
        "min_match": 2,
        "advices": [
            "Sip oral rehydration salts (ORS) regularly to prevent dehydration.",
            "Eat soft, bland foods; avoid greasy items, spicy food, dairy, and fermented foods.",
            "Sip warm ginger tea or boiled green bananas to help relieve stomach cramps and aid digestion.",
            "Get plenty of rest and avoid stress, which can worsen symptoms.",
            "If severe abdominal pain, bloody/mucus stools, high fever occur, or symptoms do not improve within 2-3 days, consult a physician to find the exact cause."
        ]
    },
    {
        "name": "Potential condition: Urinary Tract Infection (UTI)",
        "keys": {"14", "1", "6"},
        "min_match": 2,
        "advices": [
            "Drink plenty of clean water to help flush bacteria out of your urinary tract.",
            "Avoid holding your urine; go to the bathroom as soon as you feel the urge.",
            "Drink unsweetened cranberry juice or lemon water to help balance urinary tract conditions.",
            "Avoid tea, coffee, alcohol, and spicy foods that can irritate the bladder.",
            "If you develop a high fever, back pain, blood in urine, or symptoms do not improve within 1-2 days, consult a doctor."
        ]
    },
    {
        "name": "Potential condition: Dengue Fever",
        "keys": {"1", "5", "9", "11"},
        "min_match": 3,
        "advices": [
            "⚠️ This condition requires a doctor's consultation and blood tests to confirm. Do not self-diagnose or self-treat.",
            "❌ Strictly avoid aspirin or ibuprofen, as they increase the risk of bleeding. Use only paracetamol for fever if advised.",
            "Drink plenty of water or oral rehydration solutions to prevent dehydration.",
            "Sip coconut water or fresh fruit juices to help maintain fluid and electrolyte balance.",
            "If you notice skin petechiae/bleeding spots, nosebleeds, vomiting/passing bloody stool, severe abdominal pain, or extreme lethargy, go to the hospital immediately."
        ]
    },
]

URGENT_SYMPTOMS = {"10"}


def ask_confirmation():
    while True:
        answer = input("Would you like to run this assessment tool? (y/n) >>> ").strip().lower()
        if answer in ("y", "yes", "ใช่"):
            return True
        elif answer in ("n", "no", "ไม่"):
            return False
        else:
            print("Please type 'y' (yes) or 'n' (no) only.")


def show_menu():
    print("\n" + "=" * 50)
    print("     Basic Symptom Checker (Console)")
    print("=" * 50)
    print("*** For educational purposes only — NOT a medical diagnosis ***")
    print("-" * 50)
    for key, label in SYMPTOMS.items():
        print(f"  {key:>2}. {label}")
    print("-" * 50)
    print("Enter symptom numbers separated by commas, e.g., 1,3,5")
    print("Type 'menu' to view the symptom list again, or 'exit' to quit.")
    print("=" * 50)


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

    print("\n--- Preliminary Assessment Results ---")

    if not matched_groups:
        print("No exact matching symptom groupings found for standard conditions in this system.")
    else:
        for group in matched_groups:
            print(f"\n• {group['name']}")
            print("  General Self-Care & Dietary Guidance:")
            for tip in group["advices"]:
                print(f"    - {tip}")

    if selected_keys & URGENT_SYMPTOMS:
        print("\n⚠️  Warning: The symptom selected (e.g., breathing difficulty) requires immediate medical attention.")
        print("    If symptoms are acute or severe, visit an emergency room or call emergency services.")

    print(
        "\nDisclaimer: This program provides general information only and cannot diagnose medical "
        "conditions or prescribe medications. If symptoms persist for 2-3 days, high fever continues, "
        "or conditions worsen/become chronic, please consult a doctor or pharmacist directly."
    )


def main():
    if not ask_confirmation():
        print("\nThank you. Have a healthy day!")
        return

    show_menu()
    while True:
        user_input = input("\nSelect symptoms >>> ").strip()

        if user_input.lower() == "exit":
            print("Thank you for using the program. Stay healthy!")
            break
        elif user_input.lower() == "menu":
            show_menu()
            continue
        elif not user_input:
            continue

        selected, invalid = parse_selection(user_input)

        if invalid:
            print(f"Invalid number(s): {', '.join(invalid)} (Type 'menu' to view symptom list)")

        if selected:
            analyze(selected)


if __name__ == "__main__":
    main()