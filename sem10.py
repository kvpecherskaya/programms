
def readtext(file):
    with open(file, encoding = "utf-8") as f:
        text = f.read()
    return text

def split_text(text):
    text = text.lower().split()
    for i,word in enumerate(text):
        text[i] = word.strip('!?.,;-"":0123456789')  
    return tuple(text)

def main():
    print(split_text(readtext("book.txt")))
    
if __name__ == '__main__':
             main()
