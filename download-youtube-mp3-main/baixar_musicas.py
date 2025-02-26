import subprocess

class BaixarMusicas:

    def __init__(self, list_of_video_links : list[str]):
        # Lista de links dos vídeos do YouTube
        self._list_of_video_links = list_of_video_links

        # Caminho para o yt-dlp.exe
        self._yt_dlp_path = r"yt-dlp.exe"  # Substitua pelo caminho do seu yt-dlp.exe

        # Caminho para o arquivo de cookies
        self._cookies_path = r"cookies.txt"  # Substitua pelo caminho do seu arquivo de cookies

    def baixar_todos_videos(self):
        # Baixar todos os vídeos da lista
        i = 1
        for link in self._list_of_video_links:
            print(f'Baixando vídeo {i} de {len(self._list_of_video_links)}')
            self.baixar_video(link)   
            i += 1

    # Função para baixar o vídeo
    def baixar_video(self, video_link):
        try:
            # Comando para baixar o vídeo em MP3 usando o arquivo de cookies
            command = [
                self._yt_dlp_path,
                '--cookies', self._cookies_path,          # Adiciona o arquivo de cookies
                '-x',                               # Extrair áudio
                '--audio-format', 'mp3',             # Converter para MP3
                '--audio-quality', '0',              # Melhor qualidade
                '--output', 'musics/%(title)s.%(ext)s',     # Nome do arquivo baseado no título, salva em /musics
                video_link
            ]
            
            # Executa o comando
            subprocess.run(command, check=True)
            print(f"Vídeo {video_link} baixado com sucesso!")
        
        except subprocess.CalledProcessError as e:
            print(f"Erro ao baixar {video_link}: {e}")

    
