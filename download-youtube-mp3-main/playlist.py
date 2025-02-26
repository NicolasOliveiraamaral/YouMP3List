import yt_dlp

class Playlist:

    def __init__(self, playlist_url):
        # URL da playlist do YouTube
        self._playlist_url = playlist_url

    # Função para pegar os links de uma playlist
    def pegar_links_playlist(self):
        try:
            ydl_opts = {
                'quiet': True,  # Não mostrar o output completo do yt-dlp
                'extract_flat': True,  # Não baixar os vídeos, apenas extrair os links
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Obtém informações da playlist
                result = ydl.extract_info(self._playlist_url, download=False)
                
                # Verifica se a URL é uma playlist
                if 'entries' in result:
                    # Cria uma lista com os links de cada vídeo
                    links = [entry['url'] for entry in result['entries']]
                    return links
                else:
                    print("A URL fornecida não é uma playlist válida.")
                    return []
        
        except Exception as e:
            print(f"Erro ao pegar os links da playlist: {e}")
            return []
