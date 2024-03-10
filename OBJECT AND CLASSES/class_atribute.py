class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1


first_comment = Comment("First comment")

print(Comment.total_comments)

second_comment = Comment("Second comment")

print(Comment.total_comments)

third_comment = Comment("Third comment")

print(Comment.total_comments)

fourth_comment = Comment("Fourth comments")
fourth_comment.total_comments = 11
print(Comment.total_comments)
print(fourth_comment.total_comments)
print(fourth_comment.__dict__)
print(Comment.__dict__)

Comment.total_comments = 20
