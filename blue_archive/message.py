import discord
import blue_archive.fetch as fetch

def Embed():
    content, strong_list, url, colors = fetch.fetch()
    content = '\n'.join(content)
    content = content.strip(' \n')

    img_start = content.find('https://')
    img_end = content.find('.png') + 4
    img = content[img_start:img_end]
    while True:
        if 'https://' in content:
            img_start = content.find('https://')
            img_end = content.find('.png') + 4
            content = content.replace(content[img_start:img_end] + '\n', '', 1)
        else:
            break
    
    end = 0
    for strong_text in strong_list:
        content = content[:end] + content[end:].replace(strong_text, f'**{strong_text}**', 1)
        end = end + content[end:].find(f'**{strong_text}**') + len(strong_text) + 4
    content = content.replace('****', '')

    content_list = content.split('\n')

    title = content_list[0]

    time_stamp = content_list[1][:-3]

    footer = "ブルアカ" + '・' + time_stamp

    content = '\n'.join(content_list[2:])

    colors = [i for i in colors if i != 'rgb(0, 0, 0)']
    if colors:
        # color_list = color_list[1::2]
        rgb = colors[0]
        colors = [i for i in colors if i != 'rgb(255, 0, 0)']
        if colors:
            rgb = colors[0]

        # 移除 "rgb(" 和 ")"，並將剩餘部分拆分為三個部分
        r, g, b = map(int, rgb[4:-1].split(","))
        # 將 r、g、b 值轉換為十六進制並組合成一個整數
        hex_int = r << 16 | g << 8 | b

        color = hex_int
    else:
        color = 0x00FFFF

    embed = discord.Embed(title=title, description=content, 
                          color=color, url=url)
    embed.set_image(url=img)
    embed.set_footer(text=footer, 
                     icon_url="https://pbs.twimg.com/profile_images/1509908445054443527/ObBk7aEE_400x400.png")
    
    return embed, url

    
    
    