# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbelotti <fbelotti@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 16:34:17 by fbelotti          #+#    #+#              #
#    Updated: 2025/01/03 16:55:41 by fbelotti         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 2:
    raise AssertionError("Error: invalid number of arguments")

if len(sys.argv) < 2:
    sys.exit()

try:
    number = int(sys.argv[1])
except ValueError:
    raise AssertionError("Error: argument is not an integer")
    sys.exit()

if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")