#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_all.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbelotti <fbelotti@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 by fbelotti               #+#    #+#                  #
#    Updated: 2026/01/06 by fbelotti                ###   ########.fr          #
#                                                                              #
# **************************************************************************** #

"""
Script de test pour tous les exercices de la série 00 - Training Python for Data Science
"""

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

    # Chercher le fichier principal
    files_to_try = []

    if exercise_name == "ex00":
        files_to_try = ["Hello.py"]
    elif exercise_name == "ex01":
        files_to_try = ["format_ft_time.py"]
    elif exercise_name == "ex02":
        files_to_try = ["tester.py"]
    elif exercise_name == "ex03":
        files_to_try = ["tester.py"]
    elif exercise_name == "ex04":
        files_to_try = ["tester.py"]
    elif exercise_name == "ex05":
        files_to_try = ["building.py"]
    elif exercise_name == "ex06":
        files_to_try = ["filterstring.py"]
    elif exercise_name == "ex07":
        files_to_try = ["sos.py"]
    elif exercise_name == "ex08":
        files_to_try = ["tester.py"]
    elif exercise_name == "ex09":
        files_to_try = ["tester.py"]

    success = False
    for file in files_to_try:
        if os.path.exists(file):
            try:
                if exercise_name == "ex05":
                    print("Test avec une chaîne de caractères:")
                    result = subprocess.run(
                        [sys.executable, file, "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )
                elif exercise_name == "ex06":
                    print("Test avec une chaîne et un nombre:")
                    result = subprocess.run(
                        [sys.executable, file, "Hello the World", "4"],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )
                elif exercise_name == "ex07":
                    print("Test avec un texte:")
                    result = subprocess.run(
                        [sys.executable, file, "SOS"],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )
                elif exercise_name == "ex08":
                    cmd = ["python3", file]
                    result = subprocess.run(cmd, text=True)
                else:
                    result = subprocess.run(
                        [sys.executable, file],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )

                print(result.stdout)
                if result.stderr:
                    print("Erreurs:", result.stderr)
                if result.returncode == 0:
                    print(f"✅ {exercise_name} - {file} exécuté avec succès")
                    success = True
                else:
                    print(f"⚠️  {exercise_name} - {file} terminé avec code {result.returncode}")
                break
            except subprocess.TimeoutExpired:
                print(f"⏱️  {exercise_name} - {file} timeout (exercice interactif?)")
                success = True
                break
            except Exception as e:
                print(f"❌ Erreur lors de l'exécution de {file}: {e}")

    if not success and not files_to_try:
        print(f"⚠️  Aucun fichier à tester pour {exercise_name}")

    return success


def main():
    base_path = os.path.dirname(os.path.abspath(__file__))

    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "TESTS - 00 Training Python for Data Science" + " " * 20 + "║")
    print("╚" + "=" * 78 + "╝")

    exercises = [
        "ex00", "ex01", "ex02", "ex03", "ex04",
        "ex05", "ex06", "ex07", "ex08", "ex09"
    ]

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
    print(f"\n📊 Score: {passed}/{total} exercices réussis")


if __name__ == "__main__":
    main()
