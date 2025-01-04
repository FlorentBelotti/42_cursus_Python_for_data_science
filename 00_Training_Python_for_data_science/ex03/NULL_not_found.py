# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbelotti <fbelotti@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 14:14:45 by fbelotti          #+#    #+#              #
#    Updated: 2025/01/03 14:59:59 by fbelotti         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Any
from math import isnan

def NULL_not_found(object: Any) -> int:
    if object is None:
        print(f"Nothing : {object} {type(object)}")
    elif isinstance(object, float) and isnan(object):
        print(f"Cheese : {object} {type(object)}")
    elif isinstance(object, bool) and object == False:
        print(f"Fake : {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero : {object} {type(object)}")
    elif object == "":
        print(f"Empty : {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0