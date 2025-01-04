# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbelotti <fbelotti@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 10:58:05 by fbelotti          #+#    #+#              #
#    Updated: 2025/01/03 11:01:07 by fbelotti         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

ft_tuple = (ft_tuple[0], "France!")

ft_set.remove("tutu!")
ft_set.add("Perpignan!")

ft_dict["Hello"] = "42Perpignan!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)