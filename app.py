# Tomato Disease Diagnostic Agent

def diagnose_tomato_disease(symptom):
    symptom = symptom.lower()

    if "brown spots" in symptom:
        return "Early Blight"
    elif "yellow leaves" in symptom:
        return "Leaf Mold"
    elif "black spots" in symptom:
        return "Bacterial Spot"
    elif "mosaic pattern" in symptom:
        return "Mosaic Virus"
    elif "gray spots" in symptom:
        return "Septoria Leaf Spot"
    else:
        return "Disease Not Identified"

# User Input
symptom = input("Enter tomato plant symptoms: ")

# Diagnosis
disease = diagnose_tomato_disease(symptom)

print("\nTomato Disease Diagnostic Report")
print("--------------------------------")
print("Symptoms:", symptom)
print("Detected Disease:", disease)

# Treatment Suggestion
if disease == "Early Blight":
    print("Treatment: Remove infected leaves and apply fungicide.")
elif disease == "Leaf Mold":
    print("Treatment: Improve air circulation and use fungicide.")
elif disease == "Bacterial Spot":
    print("Treatment: Use copper-based spray.")
elif disease == "Mosaic Virus":
    print("Treatment: Remove infected plants.")
elif disease == "Septoria Leaf Spot":
    print("Treatment: Remove affected leaves and apply fungicide.")
else:
    print("Treatment: Consult an agricultural expert.")
