msg = "&&&**$gnirtS PLIO!!@1234"

msg = msg.replace("&", "")
msg = msg.replace("*", "")
msg = msg.replace("$", "")
msg = msg.replace("!", "")
msg = msg.replace("@", "")
msg = msg.replace("1", "")
msg = msg.replace("2", "")
msg = msg.replace("3", "")
msg = msg.replace("4", "")

first_word, second_word = msg.split()

first_word = first_word[::-1]

second_word = second_word.replace("I", "E")
second_word = second_word.replace("O", "U")

print(first_word + " " + second_word)
