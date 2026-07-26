import streamlit as st
import os

# Konfigurasi halaman web premium
st.set_page_config(
    page_title="Happy 20th Birthday, Xena! 🎂", 
    page_icon="👑", 
    layout="centered"
)

# --- CUSTOM CSS THEME: LUXURY, ANIMASI, & SMOOTH SCROLL ---
st.markdown("""
    <style>
    /* Mengaktifkan efek scroll yang halus saat halaman otomatis naik ke atas */
    html {
        scroll-behavior: smooth;
    }
    .stApp { 
        background: linear-gradient(135deg, #16111e 0%, #111116 100%); 
        color: #f0f0f5; 
    }
    .luxury-title { 
        font-size: 45px !important; 
        font-weight: 900; 
        background: linear-gradient(45deg, #ff4b4b, #ff8533, #ffeb3b, #e91e63); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        text-align: center; 
        margin-bottom: 5px;
    }
    .pesta-banner {
        text-align: center;
        font-size: 24px;
        letter-spacing: 5px;
        margin-bottom: 10px;
    }
    .luxury-badge { 
        text-align: center; 
        font-size: 18px; 
        font-weight: 700; 
        color: #111116; 
        background: linear-gradient(45deg, #ffbe53, #ff758c); 
        padding: 6px 20px; 
        border-radius: 50px; 
        width: fit-content; 
        margin: 0 auto 25px auto; 
    }
    .photo-frame { 
        border-radius: 20px; 
        overflow: hidden; 
        border: 3px solid #ff758c; 
        box-shadow: 0px 0px 25px rgba(255, 117, 140, 0.6); 
        margin-bottom: 20px; 
    }
    /* Gaya Wadah Lilin Animasi */
    .candle-container {
        text-align: center;
        margin: 20px auto;
        width: 150px;
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi status kado
if 'kado_terbuka' not in st.session_state:
    st.session_state.kado_terbuka = False

# --- HALAMAN DEPAN: TOMBOL KEJUTAN ---
if not st.session_state.kado_terbuka:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>🥳🥳🥳</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #ff758c;'>Haii Xena! Ada kado digital khusus buat kamu... 🎁</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa;'>Klik tombol di bawah ini untuk membuka keseruannya!</p>", unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🎉 BUKA KADO DIGITAL 🎉", use_container_width=True):
            st.session_state.kado_terbuka = True
            st.rerun()

# --- HALAMAN UTAMA SETELAH KADO DIBUKA ---
else:
    st.snow() 
    st.markdown('<p class="pesta-banner">🎈🎁✨🎈🎁✨🎈🎁✨🎈</p>', unsafe_allow_html=True)
    st.markdown('<p class="luxury-title">✨ HAPPY BIRTHDAY, XENA ✨</p>', unsafe_allow_html=True)
    st.markdown('<div class="luxury-badge">Welcome to 20s Club! 👑</div>', unsafe_allow_html=True)

    if 'init_celebrate' not in st.session_state:
        st.balloons()
        st.session_state.init_celebrate = True

    # MUSIK LATAR (.FEAST - NINA)
    if os.path.exists("nina.mp3"):
        try:
            with open("nina.mp3", "rb") as audio_file:
                audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", autoplay=True)
            st.caption("🎵 *Mengalun: .Feast - Nina 🔊*")
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
        st.caption("<p style='text-align: center; color: #ffba53; font-weight: bold;'>✨ Xena Ida Karunia • 20 Years of Awesomeness ✨</p>", unsafe_allow_html=True)

    st.markdown("---")

    # --- TITIK JANGKAR UNTUK AUTO-SCROLL (AREA LILIN) ---
    st.markdown('<div id="area-lilin"></div>', unsafe_allow_html=True)

    # VISUAL LILIN INTERAKTIF BERGERAK (GIF ANIMASI)
    st.markdown("<h4 style='text-align: center; color: #ffbe53;'>🎂 Lilin Ulang Tahun Virtual</h4>", unsafe_allow_html=True)
    
    if 'lilin_aktif' not in st.session_state:
        st.session_state.lilin_aktif = True

    if st.session_state.lilin_aktif:
        # Menampilkan Gambar Animasi Api Lilin Bergerak (GIF)
        st.markdown("""
            <div class="candle-container">
                <img src="https://giphy.com" width="120">
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 14px; color: #ffbe53; font-style: italic;'>Make a wish, isi harapanmu di bawah, lalu tiup lilinnya! 👇</p>", unsafe_allow_html=True)
    else:
        # Menampilkan Gambar Animasi Api Padam Menjadi Asap Bergerak (GIF)
        st.markdown("""
            <div class="candle-container">
                <img src="https://giphy.com" width="120">
            </div>
        """, unsafe_allow_html=True)
        st.success("🎉 Huffff... Lilin berhasil ditiup! Semoga seluruh mimpimu lekas dikabulkan oleh semesta, Xena! 🌟")

    st.markdown("---")

    # KOTAK SURAT
    st.markdown("### 💌 Surat Terbuka Untuk Xena:")
    
    pesan_xena_fix = """
🥳 **WOIIIII THIS UR DAY 😱🤩**  
hehehehehehe agaaa maleman yaawww 😁🙏  
happy 20th birthday xenaaaa, kepala 2 btw woilahh, bener bener di fase dewasa yang sesungguhnya 😱 🥳🥳🥳😼😱😱🤩🤩  
  
selamat ulang tahun ke 20 xena ida karunia, suatu keberuntungan sendiri bisa kenal u selama ±7tahun ini, dan yapp sekarang udah 20 taonn padahal kek baru kemaren. 😅😼🤩🤩🥳😎😜  
  
di umur 20 ini semoga xena selalu di berikan kekuatan, kesehatan, kemudahan, kelancaran dalam hal apapun itu, keberhasilan buat dapetin apa yang xena impikan, selalu di jauhkan dari segala hal negatif yang ada di luar sana, menjadi pribadi yang lebih baik untuk kedepannya, semoga selalu di kelilingi sama orang orang baik, selalu jadi kakak yang baik buat zaki sama novi yaww, nurut sama ayah sama mama jugaa.  
 
i proud of u, dengan segala upaya yang xena lakukan di hari hari kemarin akhirnya bener bener berbuahkan hasil, soon (dr). Xena Ida Karunia 😼, semoga selalu di permudahan urusan perkuliahan nya yaaaa, bisa lancar semua tugas yang xena emban selama kuliah nanti, dannnnnnnn semogaa xena lulus tepat waktu dengan hasil yang memuaskannn, aamiin. jangan lupa buat tetep jadi orang baik di tengah orang orang yang semrawut inii 😭  
  
jaga diri baik baik euyy selama di kampus buat kedepannya, tidak telat makan, tidak kurang tidur (ga yakin sih tapi nek iki), tidak kurang minum karna sby sangat amat allahuakbar panasnya, dan jangan lupa istirahat. tubuhmu juga perlu istirahat ditengah padat e jadwal kuliah kmu, jadii plisss jangan terlalu di paksain kalo bener bener udah lowbat.  
  
wes ga tau neh meh ngomong opo, selamat bergabung di circle 20th dimana kejadian dewasa yang sebenarnya baru saja di mulai, terimakasih udah bertahan sejauh ini buat diri kamu, orang terdekatmu and masa depanmu. semoga dunia selalu berbuat baik buat xena kapanpun dan dimanapun xena ada.  

✨ **once again, happy 20th birthday xena ida karunia 🤩🤩🥳😼 u are an amazing person.**
"""
    st.info(pesan_xena_fix)

    # BAGIAN INTERAKTIF: WISH INPUT & BLOW BUTTON
    st.markdown('<p class="pesta-banner">🎈🎁✨🎈🎁✨🎈🎁✨🎈</p>', unsafe_allow_html=True)
    wish_input = st.text_input("✨ Apa pencapaian terbesar yang ingin kamu raih tahun ini, Xen?", placeholder="Tulis satu impian terbesarmu di sini...")

    # Tombol menggunakan trik JavaScript bawaan HTML untuk otomatis loncat ke atas (#area-lilin) saat diklik
    if st.button("Tiup Lilin & Kunci Harapan 🎂"):
        if wish_input:
            st.session_state.lilin_aktif = False
            st.balloons()
            st.toast("Harapanmu sudah terbang ke langit! 🪐")
            st.success(f"🔒 Selamat! Harapanmu: \"{wish_input}\" telah dikunci rapat. Semoga lekas terwujud nyata tahun ini! ✨")
            
            # Trik JavaScript untuk menarik layar otomatis naik ke area lilin
            st.markdown('<script>window.location.href = "#area-lilin";</script>', unsafe_allow_html=True)
            st.rerun()
        else:
            st.warning("Tulis dulu harapanmu sebelum meniup lilin virtualnya, Xena!")
