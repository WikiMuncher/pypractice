word = "Neat"
words = "Simple name"

say = "henlo {name}, let me {line}, {name}{name}"
ws = say.format(name="icecream", line="lick you up")

print(ws + " plz ")

# maketrans and translate test git hub iz bast
temp = ws.maketrans("elo", "zxq")

print(temp, ws.translate(temp))