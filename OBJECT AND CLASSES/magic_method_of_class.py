class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        return (f"{self.text} {other.text}",
                self.votes_qty + other.votes_qty)

    def __bool__(self, also):
        return


f_com = Comment("First")
f_com.upvote()

s_com = Comment("Second")
s_com.upvote()
print(f_com + s_com)

print(type(f_com == s_com))
