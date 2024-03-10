class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self, qty):
        # self.votes_qty += 1
        self.votes_qty = qty


vote = Comment("This is comment")

print(vote)

print(vote.text)
print(vote.upvote)
print(vote.votes_qty)

print(vote.__dict__)

print(dir(vote))

vote.upvote(5)
print(vote.votes_qty)

vote.upvote = 10
print(vote.__dict__)
# vote.upvote()

sec_vote = Comment("My comment")

sec_vote.upvote(2)
print(sec_vote.votes_qty)
