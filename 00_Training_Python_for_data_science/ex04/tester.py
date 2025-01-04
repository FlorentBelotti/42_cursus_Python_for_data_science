# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbelotti <fbelotti@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 17:00:10 by fbelotti          #+#    #+#              #
#    Updated: 2025/01/03 18:04:48 by fbelotti         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess

def run_test(args):
    result = subprocess.run(['python3', 'whatis.py'] + args, capture_output=True, text=True)
    print(f"Args: {args} -> Output: {result.stdout.strip()}{result.stderr.strip()}")

def main():
    tests = [
        ["14"],
        ["-5"],
        ["0"],
        ["Hi!"],
        ["13", "5"],
        [],
    ]

    for args in tests:
        run_test(args)

if __name__ == "__main__":
    main()