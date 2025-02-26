from baixar_musicas import BaixarMusicas
from playlist import Playlist

playlist = Playlist('O link da sua playlist vai aqui')
list_of_urls = playlist.pegar_links_playlist()
bm = BaixarMusicas(list_of_urls)
bm.baixar_todos_videos()