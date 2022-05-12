class ChatMsg:
    def __init__(self, contents, to=None, frm=None, attach=None):
        self.contents = contents
        self.to = to
        self.frm = frm
        self.attach = attach
        
#     def __str__(self):
#         return "contents={}, frm={}, to={}, attach={}"
#     .format(self.contents, self.frm, self.to, True if self.attach else False)
    
#     def __str__(self):
#         return "contents={}, frm={}, to={}".format(self.contents, self.frm, self.to)
    def __str__(self):
        return "contents={}, to={}, frm={}, attach={}".format(self.contents, self.to, self.frm, True if self.attach else False)