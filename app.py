import streamlit as st
import os

# Konfigurasi halaman web premium
st.set_page_config(
    page_title="Happy 20th Birthday, Xena! 🎂", 
    page_icon="👑", 
    layout="centered"
)

# --- CUSTOM CSS THEME ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #111116 0%, #1a1a24 100%); color: #f0f0f5; }
    .luxury-title { font-size: 42px !important; font-weight: 900; background: linear-gradient(45deg, #ff758c, #ff7eb3, #ffbe53); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin-bottom: 5px; }
    .luxury-badge { text-align: center; font-size: 18px; font-weight: 700; color: #111116; background: linear-gradient(45deg, #ffbe53, #ff758c); padding: 6px 20px; border-radius: 50px; width: fit-content; margin: 0 auto 25px auto; }
    .photo-frame { border-radius: 20px; overflow: hidden; border: 2px solid rgba(255, 255, 255, 0.1); box-shadow: 0px 10px 30px rgba(0,0,0,0.6); margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi status kado (Default: Belum dibuka)
if 'kado_terbuka' not in st.session_state:
    st.session_state.kado_terbuka = False

# --- HALAMAN DEPAN: TOMBOL KEJUTAN UNTUK MEMANCING AUTOPLAY BROWSER ---
if not st.session_state.kado_terbuka:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #ff758c;'>Haii Xena! Ada kado digital khusus buat kamu... 🎁</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa;'>Klik tombol di bawah ini untuk membuka kejutannya!</p>", unsafe_allow_html=True)
    
    st.write("")
    # Tombol besar di tengah halaman
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎉 BUKA KADO DIGITAL UTAMA 🎉", use_container_width=True):
            st.session_state.kado_terbuka = True
            st.rerun()

# --- HALAMAN UTAMA SETELAH KADO DIBUKA ---
else:
    st.markdown('<p class="luxury-title">✨ HAPPY BIRTHDAY, XENA ✨</p>', unsafe_allow_html=True)
    st.markdown('<div class="luxury-badge">Welcome to 20s Club! 👑</div>', unsafe_allow_html=True)

    # Efek Balon Otomatis
    if 'init_celebrate' not in st.session_state:
        st.balloons()
        st.session_state.init_celebrate = True

    # MEMUTAR MUSIK SECARA SEGERA (Browser mengizinkan karena tombol pembuka sudah diklik)
    if os.path.exists("nina.mp3"):
        try:
            with open("nina.mp3", "rb") as audio_file:
                audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", autoplay=True)
            st.caption("🎵 *Mengalun: .Feast - Nina (Browser Diizinkan Memutar)🔊*")
        except:
            st.audio("https://soundhelix.com", format="audio/mp3", autoplay=True)
    else:
        st.audio("https://soundhelix.com", format="audio/mp3", autoplay=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # TAMPILAN FOTO XENA
    if os.path.exists("sahabat.jpg"):
        st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
        st.image("sahabat.jpg", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("<p style='text-align: center; color: #aaa;'>Xena Ida Karunia • 20 Years of Awesomeness ✨</p>", unsafe_allow_html=True)

    st.markdown("---")

    # VISUAL LILIN INTERAKTIF
    st.markdown("<h4 style='text-align: center; color: #ffbe53;'>🎂 Tiup Lilin Ulang Tahun Virtualmu Di Sini</h4>", unsafe_allow_html=True)
    if 'lilin_aktif' not in st.session_state:
        st.session_state.lilin_aktif = True

    if st.session_state.lilin_aktif:
        st.markdown("<h1 style='text-align: center; font-size: 90px; margin: 0; text-shadow: 0 0 20px #ffbe53;'>🔥<br><span style='color: #eee;'>🕯️</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 14px; color: #ffbe53; font-style: italic;'>Make a wish, isi harapanmu di bawah, lalu klik tombol tiup! 👇</p>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; font-size: 90px; margin: 0; opacity: 0.6;'>💨<br><span style='color: #888;'>🕯️</span></h1>", unsafe_allow_html=True)
        st.success("🎉 Huffff... Lilin berhasil ditiup! Semoga seluruh mimpimu lekas dikabulkan oleh semesta, Xena! 🌟")

    st.markdown("---")

    # KOTAK UCAPAN STANDARD MARKDOWN (100% AMAN & RAPI)
    st.markdown("### 💌 Surat Terbuka Untuk Xena:")
    
    pesan_xena_fix = """
**WOIIIII THIS UR DAY 😱🤩**  
hehehehehehe agaaa maleman yaawww 😁🙏  
happy 20th birthday xenaaaa, kepala 2 btw woilahh, bener bener di fase dewasa yang sesungguhnya 😱 🥳🥳🥳😼😱😱🤩🤩  

selamat ulang tahun ke 20 xena ida karunia, suatu keberuntungan sendiri bisa kenal u selama ±7tahun ini, dan yapp sekarang udah 20 taonn padahal kek baru kemaren. 😅😼🤩🤩🥳😎😜  

di umur 20 ini semoga xena selalu di berikan kekuatan, kesehatan, kemudahan, kelancaran dalam hal apapun itu, keberhasilan buat dapetin apa yang xena impikan, selalu di jauhkan dari segala hal negatif yang ada di luar sana, menjadi pribadi yang lebih baik untuk kedepannya, semoga selalu di kelilingi sama orang orang baik, selalu jadi kakak yang baik buat zaki sama novi yaww, nurut sama ayah sama mama jugaa.  

i proud of u, dengan segala upaya yang xena lakukan di hari hari kemarin akhirnya bener bener berbuahkan hasil, soon (dr). Xena Ida Karunia 😼, semoga selalu di permudahkan urusan perkuliahan nya yaaaa, bisa lancar semua tugas yang xena emban selama kuliah nanti, dannnnnnnn semogaa xena lulus tepat waktu dengan hasil yang memuaskannn, aamiin. jangan lupa buat tetep jadi orang baik di tengah orang orang yang semrawut inii 😭  

jaga diri baik baik euyy selama di kampus buat kedepannya, tidak telat makan, tidak kurang tidur (ga yakin sih tapi nek iki), tidak kurang minum karna sby sangat amat allahuakbar panasnya, dan jangan lupa istirahat. tubuhmu juga perlu istirahat ditengah padat e jadwal kuliah kmu, jadii plisss jangan terlalu di paksain kalo bener bener udah lowbat.  

wes ga tau neh meh ngomong opo, selamat bergabung di circle 20th dimana kejadian dewasa yang sebenarnya baru saja di mulai, terimakasih udah bertahan sejauh ini buat diri kamu, orang terdekatmu dan masa depanmu. semoga dunia selalu berbuat baik buat xena kapanpun dan dimanapun xena ada.  

**once again, happy 20th birthday xena ida karunia 🤩🤩🥳😼 u are an amazing person.**
"""
    st.info(pesan_xena_fix)

    # BAGIAN INTERAKTIF: WISH INPUT & BLOW BUTTON
    wish_input = st.text_input("✨ Apa pencapaian terbesar yang ingin kamu raih tahun ini, Xen?", placeholder="Tulis satu impian terbesarmu di sini...")

    if st.button("Tiup Lilin & Kunci Harapan 🎂"):
        if wish_input:
            st.session_state.lilin_aktif = False
            st.balloons()
            st.toast("Harapanmu sudah terbang ke langit! 🪐")
            st.success(f"🔒 Selamat! Harapanmu: \"{wish_input}\" telah dikunci rapat. Semoga lekas terwujud nyata tahun ini! ✨")
            st.rerun()
        else:
            st.warning("Tulis dulu harapanmu sebelum meniup lilin virtualnya, Xena!")
