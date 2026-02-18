#!/usr/bin/env python3


import os
import sys
import subprocess


def print_header(exercise_name):
    """Affiche un en-tête pour chaque exercice"""
    print("\n" + "=" * 80)
    print(f"  {exercise_name}")
    print("=" * 80 + "\n")


def run_exercise(ex_path, exercise_name):
    """Exécute un exercice donné"""
    print_header(exercise_name)

    if not os.path.exists(ex_path):
        print(f"❌ Le dossier {ex_path} n'existe pas")
        return False

    os.chdir(ex_path)

    # Chercher le fichier tester.py
    tester_file = "tester.py"

    if os.path.exists(tester_file):
        try:
            result = subprocess.run(
                [sys.executable, tester_file],
                capture_output=True,
                text=True,
                timeout=30
            )

            print(result.stdout)
            if result.stderr:
                print("Erreurs:", result.stderr)

            if result.returncode == 0:
                print(f"✅ {exercise_name} - OK")
                return True
            else:
                print(f"{exercise_name} - NOPE")
                return False

        except subprocess.TimeoutExpired:
            print(f"⏱️  {exercise_name} - {tester_file} timeout")
            return False
        except Exception as e:
            print(f"❌ Erreur lors de l'exécution de {tester_file}: {e}")
            return False
    else:
        print(f"⚠️  Aucun fichier tester.py trouvé pour {exercise_name}")
        return False


def main():
    """Fonction principale"""
    base_path = os.path.dirname(os.path.abspath(__file__))

    exercises = ["ex00", "ex01", "ex02", "ex03", "ex04"]

    results = {}

    for ex in exercises:
        ex_path = os.path.join(base_path, ex)
        results[ex] = run_exercise(ex_path, ex)
        os.chdir(base_path)

    # Résumé final
    print("\n" + "=" * 80)
    print("  RÉSUMÉ DES TESTS")
    print("=" * 80)

    for ex, success in results.items():
        status = "✅" if success else "❌"
        print(f"{status} {ex}")

    total = len(results)
    passed = sum(1 for v in results.values() if v)
    print(f"\nScore: {passed}/{total} exercices réussis")


if __name__ == "__main__":
    main()
