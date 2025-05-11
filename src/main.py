from textnode import *

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK_TEXT.value, "https://www.boot.dev")
    print(text_node)

main()