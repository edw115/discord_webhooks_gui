import os
import re
from dhooks import Webhook, Embed, File
import validators
import requests
from datetime import datetime

def webhook_pattern(url):
    pattern = re.compile(r'^https:\/\/discord\.com\/api\/webhooks\/\d+\/[A-Za-z0-9_-]{68}$')
    return bool(pattern.match(url))

def webhook_validator(text:str):
    
    if (validators.url(text) and 
        # text.startswith("https://discord.com/api/webhooks/") and
        webhook_pattern(text)):
        response = requests.get(text)
        if response.status_code == 200:
            r_json = response.json()
            return {
                'status_code':response.status_code,
                'avatar': f'https://cdn.discordapp.com/avatars/{r_json["id"]}/{r_json["avatar"]}.png?size=1024',
                'username': r_json["name"]
            }
        return {'status_code':response.status_code}
    return 'Invalid webhook url'


def send(url, avatar, username, content, embeds, file_str):
    hook = Webhook(url)
    # print(url, avatar, username, content, embeds, file_str)
    if len(content) > 0 or len(embeds) > 0 or len(file_str) > 0:
        if len(file_str) > 0:
            if (
                os.path.isfile(file_str)
                and os.path.getsize(file_str) / (1024 * 1024) <= 8
            ):
                file = File(fp=file_str)
        else:
            file = None
        hook.send(
            content=content,
            embeds=embeds,
            avatar_url=avatar,
            username=username,
            file=file,
        )
    else:
        raise Exception("There must be a content, a embed or a file at least")


def field_dict_creation(name,value,inline):
    name = name if len(name)> 0 else None
    value = value if len(value)> 0 else None
    return {
        'name':name,
        'value':value,
        'inline':inline
    }

def embed_dict_creation(
    author,
    authorUrl,
    authorIconUrl,
    title,
    description,
    bodyUrl,
    color,
    fields,
    image,
    thumbnail,
    footer,
    timestamp,
    footerIconUrl,
):  
    embed_dict = {}
    embed_dict["author"] = author
    embed_dict["authorUrl"] = authorUrl if validators.url(authorUrl) else None 
    embed_dict["authorIconUrl"] = authorIconUrl if validators.url(authorIconUrl) else None
    embed_dict["title"] = title
    embed_dict["description"] = description
    embed_dict["bodyUrl"] = bodyUrl if validators.url(bodyUrl) else None
    embed_dict["color"] = int(color[1:], 16) if len(color)>1 else None
    embed_dict["fields"] = fields
    embed_dict["image"] = image if os.path.isfile(image) or validators.url(image) else None
    embed_dict["thumbnail"] = thumbnail if os.path.isfile(thumbnail) or validators.url(thumbnail) else None
    embed_dict["footer"] = footer
    embed_dict["timestamp"] = timestamp
    embed_dict["footerIconUrl"] = footerIconUrl if os.path.isfile(footerIconUrl) or validators.url(footerIconUrl) else None
    return embed_dict

def embed_creation(embed_dict):
    embed = Embed(
        description=embed_dict["description"],
        color=embed_dict["color"],
    )
    # print(embed_dict['timestamp'], type(embed_dict['timestamp']))
    if embed_dict['timestamp']:
        embed.set_timestamp(now=embed_dict['timestamp'])
    embed.set_title(embed_dict["title"], url=embed_dict["bodyUrl"])
    embed.set_author(
        name=embed_dict["author"],
        icon_url=embed_dict["authorIconUrl"],
        url=embed_dict["authorUrl"],
    )
    for field in embed_dict["fields"]:
        embed.add_field(field["name"], field["value"], inline=field["inline"])
    embed.set_image(url=embed_dict["image"])
    embed.set_thumbnail(url=embed_dict["thumbnail"])
    embed.set_footer(text=f"{embed_dict['footer']}", icon_url = embed_dict["footerIconUrl"])

    return embed

def timestamp_fixer(timestamp):
    utcnow = datetime.utcnow()
    now = datetime.fromisoformat(timestamp)
    if utcnow > now:
        diff = utcnow - now
        def_datetime = utcnow - diff
    elif now > utcnow:
        diff = now - utcnow 
        def_datetime = now + diff
    return def_datetime.isoformat().replace('T', ' ')
        
def datetime_valid(dt_str):
    try:
        timestamp = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
    except:
        # raise Exception('Invalid Timestamp ')
        return [False, None]
    return [True, timestamp]
