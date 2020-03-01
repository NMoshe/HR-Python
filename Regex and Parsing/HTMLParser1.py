from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for elem in attrs:
            print('->', elem[0], '>', elem[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for elem in attrs:
            print('->', elem[0], '>', elem[1])


if __name__ == '__main__':
    parser = MyHTMLParser()
    for x in range(int(input())):
        parser.feed(input())
    parser.close()
