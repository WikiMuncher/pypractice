word = "Neat"
words = "Simple name"

say = "henlo {name}, let me {line}, {name}{name}"
ws = say.format(name="icecream", line="lick you up")

print(ws + " plz ")

# maketrans test 2021 03 24
temp = ws.maketrans("elo", "zxq")

print(temp, ws.translate(temp))