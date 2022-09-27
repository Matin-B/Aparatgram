import requests


MAIN_URL = "https://www.aparat.com"

def download(video_url: str) -> dict:
    video_id = video_url.split("/v/")[1].split("/")[0].split("?")[0]
    url = f"{MAIN_URL}/api/fa/v1/video/video/show/videohash/{video_id}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        publisher_data = data["included"][0]["attributes"]
        publisher_username = publisher_data["username"]
        publisher_avatar = publisher_data["avatar"]
        publisher_display_name = publisher_data["displayName"]
        publisher_link = publisher_data["link"]
        data = data["data"]["attributes"]
        title = data["title"]
        description = data["description"]
        thumbnail = data["big_poster"]
        duration = data["duration"]
        date = data["mdate"]
        tags = data["tags"]
        links = data["file_link_all"]
        download_links = [
            {link["profile"]:link["urls"][0]} for link in links
        ]
        for link in links:
            resolution = link["profile"]
            download_url = link["urls"][0]
            download_links[resolution] = download_url
        return {
            "publisher_data": {
                "publisher_username": publisher_username,
                "publisher_display_name": publisher_display_name,
                "publisher_avatar": publisher_avatar,
                "publisher_link": publisher_link,
            },
            "title": title,
            "description": description,
            "thumbnail": thumbnail,
            "duration": duration,
            "date": date,
            "tags": tags,
            "links": download_links
        }
