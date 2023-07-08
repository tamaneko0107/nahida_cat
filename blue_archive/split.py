
def read(category):
    with open(f"./blue_archive/{category}.txt", 'r', encoding="utf-8") as f:
        t = f.read()

    t = t.split('\n ')
    return part(t)

def fetch(part, symbol):
    start = part.find(symbol)
    part = part.replace(symbol, '', 1)
    # if symbol == '$':
    #     rgb_start = part.find('rgb', start)
    #     rgb_end = part.find('))', start) + 1
    #     rgb = part[rgb_start:rgb_end]

    #     part = part.replace(f'({rgb})', '', 1)

        
    #     end = part.find(symbol)
    #     part = part.replace(symbol, '', 1)

    #     return (part, part[start:end], rgb)
    
    end = part.find(symbol)
    part = part.replace(symbol, '', 1)

    return (part, part[start:end])
    

#區分color and strong
def part(tlist):
    strong_list = []
    # color_list = []
    for index, t in enumerate(tlist):
        text = t

        # while True:
        #     if('$' in text):
        #         result = fetch(text, '$')
        #         color_list.extend(result[1:])
        #         text = result[0]
        #     else:
        #         break

        while True:
            if('_' in text):
                result = fetch(text, '_')
                strong_list.extend(result[1:])
                text = result[0]
            else:
                break

        tlist[index] = text
             
    # return tlist, color_list, strong_list
    return tlist, strong_list