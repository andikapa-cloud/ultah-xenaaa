import streamlit as st
import os

# --- 1. SET KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Happy 20th Birthday, Xena! 🎂", 
    page_icon="👑", 
    layout="centered"
)

# --- 2. CUSTOM CSS: THEMA LUXURY DARK MODE & GLASSMORPHISM ---
st.markdown("""
    <style>
    /* Mengubah background utama menjadi dark mode elegan */
    .stApp {
        background: linear-gradient(135deg, #111116 0%, #1a1a24 100%);
        color: #f0f0f5;
    }
    
    /* Judul Utama dengan Efek Glow Emas/Pink */
    .luxury-title { 
        font-size: 42px !important; 
        font-weight: 900; 
        background: linear-gradient(45deg, #ff758c, #ff7eb3, #ffbe53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; 
        margin-bottom: 5px;
        letter-spacing: 2px;
        text-shadow: 0px 0px 20px rgba(255, 117, 140, 0.2);
    }
    
    /* Badge Usia */
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
        box-shadow: 0px 4px 15px rgba(255, 117, 140, 0.4);
    }
    
    /* Kartu Ucapan Efek Kaca Transparan (Glassmorphism) */
    .luxury-card { 
        background: rgba(255, 255, 255, 0.03); 
        padding: 30px; 
        border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0px 15px 35px rgba(0, 0, 0, 0.5);
        margin-top: 25px;
        margin-bottom: 25px;
        line-height: 1.8;
        font-size: 16px;
        color: #e2e2ec;
        text-align: justify;
    }
    
    /* Bingkai Foto */
    .photo-frame {
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.6);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. TAMPILAN HEADER ---
st.markdown('<p class="luxury-title">✨ HAPPY BIRTHDAY, XENA ✨</p>', unsafe_allow_html=True)
st.markdown('<div class="luxury-badge">Welcome to 20s Club! 👑</div>', unsafe_allow_html=True)

# Efek Balon Otomatis saat Halaman Dimuat Pertama Kali
if 'init_celebrate' not in st.session_state:
    st.balloons()
    st.session_state.init_celebrate = True

# --- 4. PLAYER MUSIK LATAR (.FEAST - NINA) ---
if os.path.exists("nina.mp3"):
    try:
        with open("nina.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        st.caption("🎵 *Mengalun: .Feast - Nina*")
    except:
        st.audio("https://soundhelix.com", format="audio/mp3", autoplay=True)
else:
    st.audio("https://soundhelix.com", format="audio/mp3", autoplay=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 5. TAMPILAN FOTO UTAMA DENGAN FRAME ELEGAN ---
if os.path.exists("sahabat.jpg"):
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    st.image("sahabat.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.caption("<p style='text-align: center; color: #aaa;'>Xena Ida Karunia • 20 Years of Awesomeness ✨</p>", unsafe_allow_html=True)
else:
    st.info("📸 Masukkan foto 'sahabat.jpg' ke dalam folder proyek Anda.")

st.markdown("---")

# --- 6. VISUAL LILIN INTERAKTIF YANG LEBIH HIDUP ---
st.markdown("<h4 style='text-align: center; color: #ffbe53;'>🎂 Tiup Lilin Ulang Tahun Virtualmu Di Sini</h4>", unsafe_allow_html=True)

if 'lilin_aktif' not in st.session_state:
    st.session_state.lilin_aktif = True

if st.session_state.lilin_aktif:
    # Lilin menyala dengan animasi glow teks sederhana
    st.markdown("<h1 style='text-align: center; font-size: 90px; margin: 0; text-shadow: 0 0 20px #ffbe53;'>🔥<br><span style='color: #eee;'>🕯️</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; color: #ffbe53; font-style: italic;'>Make a wish, isi harapanmu di bawah, lalu klik tombol tiup! 👇</p>", unsafe_allow_html=True)
else:
    # Lilin padam berganti asap tiupan
    st.markdown("<h1 style='text-align: center; font-size: 90px; margin: 0; opacity: 0.6;'>💨<br><span style='color: #888;'>🕯️</span></h1>", unsafe_allow_html=True)
    st.success("🎉 Huffff... Lilin berhasil ditiup! Semoga seluruh mimpimu lekas dikabulkan oleh semesta, Xena! 🌟")

st.markdown("---")

# --- 7. KOTAK UCAPAN DENGAN DESAIN TEXT LUXURY ---
st.markdown("<h4 style='color: #ff758c;'>💌 Surat Terbuka Untuk Xena:</h4>", unsafe_allow_html=True)

# Menggunakan markdown murni agar teks otomatis turun ke bawah (responsive) dan tag HTML terbaca sempurna
st.markdown(f"""
<div class="luxury-card">
    <b>WOIIIII THIS UR DAY 😱🤩</b><br>
    hehehehehehe agaaa maleman yaawww 😁🙏<br>
    happy 20th birthday xenaaaa, kepala 2 btw woilahh, bener bener di fase dewasa yang sesungguhnya 😱 🥳🥳🥳😼😱😱🤩🤩<br><br>
    
    selamat ulang tahun ke 20 xena ida karunia, suatu keberuntungan sendiri bisa kenal u selama ±7tahun ini, dan yapp sekarang udah 20 taonn padahal kek baru kemaren. 😅😼🤩🤩🥳😎😜<br><br>
    
    di umur 20 ini semoga xena selalu di berikan kekuatan, kesehatan, kemudahan, kelancaran dalam hal apapun itu, keberhasilan buat dapetin apa yang xena impikan, selalu di jauhkan dari segala hal negatif yang ada di luar sana, menjadi pribadi yang lebih baik untuk kedepannya, semoga selalu di kelilingi sama orang orang baik, selalu jadi kakak yang baik buat zaki sama novi yaww, nurut sama ayah sama mama jugaa.<br><br>
    
    i proud of u, dengan segala upaya yang xena lakukan di hari hari kemarin akhirnya bener bener berbuahkan hasil, soon (dr). Xena Ida Karunia 😼, semoga selalu di permudahkan urusan perkuliahan nya yaaaa, bisa lancar semua tugas yang xena emban selama kuliah nanti, dannnnnnnn semogaa xena lulus tepat waktu dengan hasil yang memuaskannn, aamiin. jangan lupa buat tetep jadi orang baik di tengah orang orang yang semrawut inii 😭<br><br>
    
    jaga diri baik baik euyy selama di kampus buat kedepannya, tidak telat makan, tidak kurang tidur (ga yakin sih tapi nek iki), tidak kurang minum karna sby sangat amat allahuakbar panasnya, dan jangan lupa istirahat. tubuhmu juga perlu istirahat ditengah padat e jadwal kuliah kmu, jadii plisss jangan terlalu di paksain kalo bener bener udah lowbat.<br><br>
    
    wes ga tau neh meh ngomong opo, selamat bergabung di circle 20th dimana kejadian dewasa yang sebenarnya baru saja di mulai, terimakasih udah bertahan sejauh ini buat diri kamu, orang terdekatmu dan masa depanmu. semoga dunia selalu berbuat baik buat xena kapanpun dan dimanapun xena ada.<br><br>
    
    <span style="font-weight: bold; color: #ff758c; font-size: 17px;">once again, happy 20th birthday xena ida karunia 🤩🤩🥳😼 u are an amazing person.</span>
</div>
""", unsafe_allow_html=True) # <-- Bagian ini wajib diakhiri dengan unsafe_allow_html=True agar kodenya aktif!

# --- 8. BAGIAN INTERAKTIF: WISH INPUT & BLOW BUTTON ---
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
