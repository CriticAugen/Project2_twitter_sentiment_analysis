import twitter_bot
c_key='yoIwFkjZGYDa49aO16XqSNqcN'
c_secret='gl4LQOItV7Z1aFwNrlvaiKJ3t8o8h99blMIAmnmdHxYjzjRAxO'
a_token='624310916-E7fDF2IE8P6bfY1oVFglASf6F8RnxMd3vgSXFqnZ'
a_secret='ID9JcoXHsDcKtvNcnmBGcCQhUlO0wmwAxBJ6lCesiUAas'

bot=twitter_bot.bot(c_key,c_secret,a_token,a_secret)
total_neg,total_pos,neg,pos=bot.analyse("facebook",100)
print("TOTAL NEG: "+str(total_neg))
print("TOTAL POS: "+str(total_pos))


