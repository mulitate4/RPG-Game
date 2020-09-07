'''class TableBorder:
    def __init__ (self, top_left, top_split, top_right,
        mid_left, mid_split, mid_right,
        low_left, low_split, low_right,
        horizontal, vertical):
        self.top_left = top_left
        self.top_split = top_split
        self.top_right = top_right
        self.mid_left = mid_left
        self.mid_split = mid_split
        self.mid_right = mid_right
        self.low_left = low_left
        self.low_split = low_split
        self.low_right = low_right
        self.horizontal = horizontal
        self.vertical = vertical

Borders0 = TableBorder ('+', '+', '+', '+', '+', '+', '+', '+', '+', '-', '|')
Borders1 = TableBorder (u'\u250c',u'\u252C',u'\u2510',u'\u251C',u'\u253C',u'\u2524',u'\u2514',u'\u2534',u'\u2518',u'\u2500',u'\u2502')
Borders2 = TableBorder (u'\u2554',u'\u2566',u'\u2557',u'\u2560',u'\u256C',u'\u2563',u'\u255a',u'\u2569',u'\u255d',u'\u2550',u'\u2551')

def draw_box (width, height, box):
    span = width-2
    line = box.horizontal * (span)
    print (box.top_left + line + box.top_right)
    body = box.vertical + (' '*span) + box.vertical
    for _ in range (height-1):
        print (body)
    print (box.low_left + line + box.low_right)

draw_box (20, 10, Borders0)'''

'''def ascii_print(codes:int):
    strlol = "\\u" + codes
    print (strlol)

while True:
    code = input("code: ")
    ascii_print(codes=code)'''

print("\u259B\u259c")
print("\u2599\u259F")