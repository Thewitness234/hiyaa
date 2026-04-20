p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("enter the comment:")
if(p1 in message) or(p2 in message) or (p3 in message) or(p4 in message):
    print("the comment is a spam")
else:
    print("the comment is not a spam") 