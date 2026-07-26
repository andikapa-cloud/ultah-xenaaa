import streamlit as st
import os

# --- 1. KONFIGURASI HALAMAN UTAMA ---
st.set_page_config(
    page_title="Happy 20th Birthday, Xena! 🎂", 
    page_icon="🎉", 
    layout="centered"
)

# --- 2. JUDUL UTAMA & BADGE SELEBRASI ---
st.title("🎉 HAPPY BIRTHDAY XENA! 🎉")
st.subheader("Welcome to 20s Club! ✨")

# --- 3. FITUR MUSIK LATAR (.FEAST - NINA) ---
if os.path.exists("nina.mp3"):
    st.audio("nina.mp3", format="audio/mp3", autoplay=False)
    st.caption("🎵 *Sedang memutar: .Feast - Nina (Klik play jika browser Anda memblokirnya)*")
else:
    st.caption("💡 *Tips: Masukkan file 'nina.mp3' ke folder proyek agar lagu bisa diputar.*")

st.markdown("---")

# --- 4. TAMPILAN FOTO UTAMA XENA ---
if os.path.exists("sahabat.jpg"):
    st.image("sahabat.jpg", caption="Happy 20th Birthday Xena Ida Karunia! 🤩", use_container_width=True)
else:
    st.info("📸 [Info Foto]: Masukkan foto Xena ke folder proyek Anda dan beri nama 'sahabat.jpg'.")

# --- 5. VISUAL LILIN INTERAKTIF (STATE MANAGEMENT) ---
st.markdown("### 🎂 Lilin Ulang Tahun Virtual")

# Inisialisasi status lilin (Default: Menyala)
if 'lilin_menyala' not in st.session_state:
    st.session_state.lilin_menyala = True

# Tampilan visual lilin berdasarkan status menggunakan emoji (Sangat stabil & ringan)
if st.session_state.lilin_menyala:
    st.markdown("<h1 style='text-align: center; font-size: 80px; margin: 0;'>🔥<br>🕯️</h1>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>Status: Lilin sedang menyala. Buat harapan dan tiup di bawah! 👇</p>", unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center; font-size: 80px; margin: 0;'>💨<br>🕯️</h1>", unsafe_allow_html=True)
    st.success("🎉 Huffff... Lilin berhasil ditiup! Semoga semua harapanmu terkabul, Xena! ✨")

st.markdown("---")

# --- 6. KOTAK UCAPAN KHUSUS UNTUK XENA ---
st.markdown("### 💌 Pesan Spesial Buat Kamu:")

pesan_xena = """
WOIIIII THIS UR DAY😱🤩
hehehehehehe agaaa maleman yaawww😁🙏🏻
happy 20th birthday xenaaaa, kepala 2 btw woilahh, bener bener di fase dewasa yang sesungguhnya😱
🥳🥳🥳😼😱😱🤩🤩

selamat ulang tahun ke 20 xena ida karunia, suatu keberuntungan sendiri bisa kenal u selama ±7tahun ini, dan yapp sekarang udah 20 taonn padahal kek baru kemaren. 
😅😼🤩🤩🥳😎😜

di umur 20 ini semoga xena selalu di berikan kekuatan, kesehatan, kemudahan, kelancaran dalam hal apapun itu, keberhasilan buat dapetin apa yang xena impikan, selalu di jauhkan dari segala hal negatif yang ada di luar sana, menjadi pribadi yang lebih baik untuk kedepannya, semoga selalu di kelilingi sama orang orang baik,  selalu jadi kakak yang baik buat zaki sama novi yaww, nurut sama ayah sama mama jugaa. 

i proud of u, dengan segala upaya yang xena lakukan di hari hari kemarin akhirnya bener bener berbuahkan hasil, soon (dr). Xena Ida Karunia😼, semoga selalu di permudahkan urusan perkuliahan nya yaaaa, bisa lancar semua tugas yang xena emban selama kuliah nanti, dannnnnnnn semogaa xena lulus tepat waktu dengan hasil yang memuaskannn, aamiin.jangan lupa buat tetep jadi orang baik di tengah orang orang yang semrawut inii😭

jaga diri baik baik euyy selama di kampus buat kedepannya, tidak telat makan, tidak kurang tidur(ga yakin sih tapi nek iki), tidak kurang minum karna sby sangat amat allahuakbar panasnya, dan jangan lupa istirahat.tubuhmu juga perlu istirahat ditengah padat e jadwal kuliah kmu, jadii plisss jangan terlalu di paksain kalo bener bener udah lowbat.

wes ga tau neh meh ngomong opo, selamat bergabung di circle 20th dimana kejadian dewasa yang sebenarnya baru saja di mulai, terimakasih udah bertahan sejauh ini buat diri kamu, orang terdekatmu dan masa depanmu.semoga dunia selalu berbuat baik buat xena kapanpun dan dimanapun xena ada. 

once again, happy 20th  birthday xena ida karunia 🤩🤩🥳😼 u are an amazing person.
"""

st.info(pesan_xena)

# --- 7. FITUR INTERAKTIF: MAKE A WISH & TIUP LILIN ---
st.write("")
st.subheader("🔮 Make A Wish & Tiup Lilin")
wish_input = st.text_input("Apa pencapaian terbesar yang ingin kamu raih tahun ini?", placeholder="Tulis harapanmu di sini...")

if st.button("Tiup Lilin Virtual 🎂🚀"):
    if wish_input:
        st.session_state.lilin_menyala = False  # Mengubah status lilin menjadi mati
        st.balloons()  # Efek selebrasi balon udara
        st.success(f"Harapanmu: \"{wish_input}\" telah dikunci oleh semesta! ✨")
        st.rerun()  # Memperbarui halaman agar visual lilin langsung berubah mati
    else:
        st.warning("Tulis dulu harapanmu sebelum meniup lilinnya ya!")
