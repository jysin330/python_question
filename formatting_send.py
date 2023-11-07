from formatting import format_msg
def send (name, website = None):
    msg = format_msg(my_name=name,my_website=website)
    print(msg)
    return msg


send("jyoti","cfe")