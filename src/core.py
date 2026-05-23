import instaloader
from colorama import Fore, Style
from src.banner import print_status
from src.utils import anti_block_delay

class InstagramOSINT:
    def __init__(self):
        self.loader = instaloader.Instaloader(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        self.context = self.loader.context

    def attempt_login(self, username, password):
        """Melakukan otentikasi sesi ke server Instagram."""
        try:
            print_status("Mencoba melakukan otentikasi ke Instagram...", "info")
            self.loader.login(username, password)
            print_status("Sesi login berhasil diamankan!", "success")
            return True
        except instaloader.exceptions.BadCredentialsException:
            print_status("Username atau password salah.", "error")
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            print_status("Akun mengaktifkan 2FA. Diperlukan penanganan manual via session file.", "warning")
        except instaloader.exceptions.ConnectionException as ce:
            print_status(f"Gagal terhubung ke server: {ce}", "error")
        except Exception as e:
            print_status(f"Kegagalan otentikasi tidak dikenal: {e}", "error")
        return False

    def fetch_profile_data(self, target_username):
        """Menarik seluruh metadata profil yang tersedia pada target."""
        try:
            print_status(f"Mengunduh metadata untuk objek target: @{target_username}", "info")
            profile = instaloader.Profile.from_username(self.context, target_username)
            
            # Ekstraksi informasi dasar ke dalam dictionary struktur data
            data = {
                "Username": profile.username,
                "ID Kategori": profile.userid,
                "Nama Lengkap": profile.full_name,
                "Centang Biru": "Ya" if profile.is_verified else "Tidak",
                "Akun Privat": "Ya" if profile.is_private else "Tidak",
                "Akun Bisnis": "Ya" if profile.is_business_account else "Tidak",
                "Kategori Bisnis": profile.business_category_name if profile.business_category_name else "-",
                "Biografi": profile.biography if profile.biography else "-",
                "Total Pengikut": profile.followers,
                "Total Mengikuti": profile.followees,
                "URL Foto Profil": profile.profile_pic_url,
                "Tautan Eksternal": profile.external_url if profile.external_url else "-",
                "Jumlah Publikasi Post": profile.mediacount,
                "Ada Story Aktif": "Ya" if profile.has_viewable_story else "Tidak",
                "Ada Sorotan/Highlight": "Ya" if profile.has_highlight_reels else "Tidak",
                "Diikuti Oleh Anda": "Ya" if profile.followed_by_viewer else "Tidak",
                "Mengikuti Anda": "Ya" if profile.follows_viewer else "Tidak",
                "Diblokir Oleh Anda": "Ya" if profile.blocked_by_viewer else "Tidak",
                "Memblokir Anda": "Ya" if profile.has_blocked_viewer else "Tidak"
            }
            return profile, data
        except instaloader.exceptions.ProfileNotExistsException:
            print_status(f"Target dengan username @{target_username} tidak ditemukan di database Instagram.", "error")
        except Exception as e:
            print_status(f"Gagal menarik data profil: {e}", "error")
        return None, None

    def dump_relations(self, profile, limit=50):
        """Mengekstrak data relasi (Followers/Following) secara aman."""
        # Menangani pembatasan jika akun target bersifat privat dan kita tidak mengikutinya
        if profile.is_private and not profile.followed_by_viewer:
            print_status("Akun target bersifat privat! Tidak dapat mengekstrak daftar pengikut.", "warning")
            return

        print_status(f"Memulai proses penarikan daftar pengikut (Limit: {limit})...", "info")
        try:
            print(f"\n{Fore.CYAN}[ Daftar Followers @{profile.username} ]")
            count = 0
            for follower in profile.get_followers():
                if count >= limit:
                    break
                print(f" -> {Fore.GREEN}{follower.username} {Fore.WHITE}(ID: {follower.userid})")
                count += 1
                anti_block_delay(1, 3) # Jeda ringan antarnama
                
            print(f"\n{Fore.CYAN}[ Daftar Following @{profile.username} ]")
            count = 0
            for followee in profile.get_followees():
                if count >= limit:
                    break
                print(f" -> {Fore.YELLOW}{followee.username} {Fore.WHITE}(ID: {followee.userid})")
                count += 1
                anti_block_delay(1, 3)
        except instaloader.exceptions.QueryReturnedBadRequestException:
            print_status("Permintaan ditolak oleh Instagram. Terindikasi limit batas query rate.", "error")
        except Exception as e:
            print_status(f"Terjadi kesalahan saat memproses iterasi relasi: {e}", "error")
