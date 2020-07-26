import youtube

def main():
    songList = youtube.getSongList('PL0m_RB_7CwlAU66D3XDZpVquBgt7psmoi')
    for song in songList:
        print(song)

if __name__ == "__main__":
    main()