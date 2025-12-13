msg = "###!!@mocleW EPGTQ!!!6789"

msg = msg.replace("#", "")
msg = msg.replace("!", "")
msg = msg.replace("@", "")
msg = msg.replace("6", "")
msg = msg.replace("7", "")
msg = msg.replace("8", "")
msg = msg.replace("9", "")

first_word, second_word = msg.split()

first_word = first_word[::-1]

print(first_word + " " + second_word)
