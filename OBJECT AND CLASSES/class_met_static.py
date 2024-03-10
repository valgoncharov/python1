class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

    @staticmethod
    def qty_comments(qty):
        return qty


my_comment = Comment("Me comment")

m_1 = Comment.merge_comments("Thanks!", "Excellent.")
print(m_1)

m_2 = my_comment.merge_comments("Great", "OK")
print(m_2)

m_3 = Comment.qty_comments(2)
print(m_3)

m_4 = my_comment.qty_comments(4)
print(m_4)
