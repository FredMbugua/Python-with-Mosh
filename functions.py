# def greetings():
#     print("Hi")
#
#
# greetings()

message = input(">")
def emoji_converter(string):
    words= message.split(' ')
    emojis = {
        ":)": "smiley face",
        ":(": "Sad face"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter(message))