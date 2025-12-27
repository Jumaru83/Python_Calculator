# Αυτό είναι ένα απλό πρόγραμμα αριθμομηχανής

# Ορισμός συναρτήσεων για τις πράξεις
def add(x, y):
    """Προσθέτει δύο αριθμούς."""
    return x + y


def subtract(x, y):
    """Αφαιρεί τον y από τον x."""
    return x - y


def multiply(x, y):
    """Πολλαπλασιάζει δύο αριθμούς."""
    return x * y


def divide(x, y):
    """Διαιρεί τον x με τον y. Χειρίζεται τη διαίρεση με το μηδέν."""
    if y == 0:
        return "Σφάλμα: Δεν επιτρέπεται η διαίρεση με το μηδέν!"
    return x / y


# Το κυρίως μέρος του προγράμματος
if __name__ == "__main__":
    print("=== Python Calculator ===")
    print("Επίλεξε πράξη:")
    print("1. Πρόσθεση (+)")
    print("2. Αφαίρεση (-)")
    print("3. Πολλαπλασιασμός (*)")
    print("4. Διαίρεση (/)")

    while True:
        # Ζητάμε από τον χρήστη να επιλέξει
        choice = input("Δώσε την επιλογή σου (1/2/3/4) ή 'q' για έξοδο: ")

        # Έλεγχος αν ο χρήστης θέλει να βγει
        if choice.lower() == 'q':
            print("Έξοδος από την αριθμομηχανή.")
            break

        # Έλεγχος αν η επιλογή είναι έγκυρη
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Δώσε τον πρώτο αριθμό: "))
                num2 = float(input("Δώσε τον δεύτερο αριθμό: "))
            except ValueError:
                print("Σφάλμα: Παρακαλώ εισάγετε μόνο αριθμούς.")
                continue

            if choice == '1':
                print(f"Αποτέλεσμα: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Αποτέλεσμα: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Αποτέλεσμα: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str) and result.startswith("Σφάλμα"):
                    print(result)
                else:
                    print(f"Αποτέλεσμα: {num1} / {num2} = {result}")

            print("-" * 20)  # Διαχωριστική γραμμή

        else:
            print("Μη έγκυρη επιλογή. Προσπάθησε ξανά.")