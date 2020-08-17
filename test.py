from Kurumi.kurumi import Kurumi
import asyncio

async def main():
    client = Kurumi()
    res = await client.search("date")
    anime = res[2]
    print(anime.title)
    episodes = await anime.get_episodes()
    episode = episodes.get_episode_by_number(1)
    kwikdata = await episode.get_kwik_data()
    print(await kwikdata[0].get_m3u8())
    await client.close()

asyncio.run(main())