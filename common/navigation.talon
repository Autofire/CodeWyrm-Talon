tag: user.wyrm_vim
-

[<number>] (care|cares) right: user.command("{number}" or "1", "l")
[<number>] (care|cares)  left: user.command("{number}" or "1", "h")

[<number>] (term|terms) right: user.command("{number}" or "1", "w")
[<number>] (term|terms)  left: user.command("{number}" or "1", "b")
[<number>] (tail|tails) right: user.command("{number}" or "1", "e")
[<number>] (tail|tails)  left: user.command("{number}" or "1", "ge")

[<number>] (word|words) right: user.command("{number}" or "1", "W")
[<number>] (word|words)  left: user.command("{number}" or "1", "B")
[<number>] (end|ends)   right: user.command("{number}" or "1", "E")
[<number>] (end|ends)    left: user.command("{number}" or "1", "gE")


[<number>] (line|lines)    up: user.command("{number}" or "1", "k")
[<number>] (line|lines)  down: user.command("{number}" or "1", "j")
<number>   (line)        jump: user.command("{number}", "gg")
line end:                      user.command("$")
line start:                    user.command("^")
line awake:                    user.command("0")
line first:                    user.command("gg")
line last:                     user.command("G")

bracket match: user.command("%")
