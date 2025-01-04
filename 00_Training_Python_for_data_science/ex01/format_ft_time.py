# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbelotti <fbelotti@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 11:06:12 by fbelotti          #+#    #+#              #
#    Updated: 2025/01/03 11:26:19 by fbelotti         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
import time

seconds_since_unix = time.time()
scientific_notation = f"{seconds_since_unix :.2e}"
current_date = datetime.datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {seconds_since_unix:.4f} or {scientific_notation} in scientific notation")
print(current_date)