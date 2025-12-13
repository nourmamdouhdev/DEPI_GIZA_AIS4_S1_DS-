msg = "##$$$@!yalpstcejorp EPUVT****9887"

msg = msg.replace("#", "")
msg = msg.replace("$", "")
msg = msg.replace("@", "")
msg = msg.replace("!", "")
msg = msg.replace("*", "")
msg = msg.replace("9", "")
msg = msg.replace("8", "")
msg = msg.replace("7", "")

first_word, second_word = msg.split()

first_word = first_word[::-1]

second_word = second_word.replace("E", "A")
second_word = second_word.replace("U", "O")

print(first_word + " " + second_word)
