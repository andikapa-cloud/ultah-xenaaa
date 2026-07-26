import streamlit as st
import os

# Konfigurasi halaman web premium
st.set_page_config(
    page_title="Happy 20th Birthday, Xena! 🎂", 
    page_icon="🎉", 
    layout="centered"
)

# --- CUSTOM CSS UNTUK TAMPILAN ELEGAN ---
st.markdown("""
    <style>
    .main-title { 
        font-size: 50px !important; 
        font-weight: 800; 
        background: linear-gradient(45deg, #FF4B4B, #FF8533);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; 
        margin-bottom: 10px;
    }
    .age-badge {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #FFFFFF;
        background-color: #FF4B4B;
        padding: 5px 15px;
        border-radius: 20px;
        width: fit-content;
        margin: 0 auto 30px auto;
    }
    .premium-card { 
        background-color: #FFFFFF; 
        padding: 30px; 
        border-radius: 15px; 
        box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.1);
        border-top: 5px solid #FF4B4B;
        margin-top: 20px;
        margin-bottom: 20px;
        line-height: 1.6;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# --- KONFIGURASI ---
AGE = 20
NAMA_SAHABAT = "Xena"

# Tampilkan Judul Utama & Badge Umur
st.markdown('<p class="main-title">🎉 HAPPY BIRTHDAY! 🎉</p>', unsafe_allow_html=True)
st.markdown(f'<div class="age-badge">Welcome to {AGE}s Club! ✨</div>', unsafe_allow_html=True)

# Efek Balon Selebrasi Otomatis saat Halaman Dibuka
st.balloons()

# Fitur Musik Latar Otomatis
audio_url = "https://soundhelix.com"
st.audio(audio_url, format="audio/mp3", autoplay=True)
st.caption("🎵 *Musik latar otomatis diputar (Klik tombol play jika browser Anda memblokirnya)*")

st.success("🔓 KADO DIGITAL UTAMA BERHASIL DIBUKA!")

# --- TAMPILAN FOTO UTAMA SAHABAT ---
if os.path.exists("sahabat.jpg"):
    st.image("sahabat.jpg", caption=f"Selamat Ulang Tahun yang ke-{AGE}, {NAMA_SAHABAT}! ✨", use_container_width=True)
else:
    st.warning("📸 File 'sahabat.jpg' tidak ditemukan di repositori GitHub Anda. Tolong pastikan nama filenya sudah huruf kecil semua.")

# --- KOTAK UCAPAN CUSTOM ---
st.markdown(f"""
    <div class="premium-card">
        <p><b>WOIIIII THIS UR DAY😱🤩</b><br>
        hehehehehehe agaaa maleman yaawww😁🙏🏻<br>
        happy 20th birthday xenaaaa, kepala 2 btw woilahh, bener bener di fase dewasa yang sesungguhnya😱 🥳🥳🥳😼😱😱🤩🤩</p>
        
        <p>selamat ulang tahun ke 20 xena ida karunia, suatu keberuntungan sendiri bisa kenal u selama ±7tahun ini, dan yapp sekarang udah 20 taonn padahal kek baru kemaren. 😅😼🤩🤩🥳😎😜</p>
        
        <p>di umur 20 ini semoga xena selalu di berikan kekuatan, kesehatan, kemudahan, kelancaran dalam hal apapun itu, keberhasilan buat dapetin apa yang xena impikan, selalu di jauhkan dari segala hal negatif yang ada di luar sana, menjadi pribadi yang lebih baik untuk kedepannya, semoga selalu di kelilingi sama orang orang baik, selalu jadi kakak yang baik buat zaki sama novi yaww, nurut sama ayah sama mama jugaa.</p>
        
        <p>i proud of u, dengan segala upaya yang xena lakukan di hari hari kemarin akhirnya bener bener berbuahkan hasil, soon (dr). Xena Ida Karunia😼, semoga selalu di permudahkan urusan perkuliahan nya yaaaa, bisa lancar semua tugas yang xena emban selama kuliah nanti, dannnnnnnn semogaa xena lulus tepat waktu dengan hasil yang memuaskannn, aamiin. jangan lupa buat tetep jadi orang baik di tengah orang orang yang semrawut inii😭</p>
        
        <p>jaga diri baik baik euyy selama di kampus buat kedepannya, tidak telat makan, tidak kurang tidur(ga yakin sih tapi nek iki), tidak kurang minum karna sby sangat amat allahuakbar panasnya, dan jangan lupa istirahat. tubuhmu juga perlu istirahat ditengah padat e jadwal kuliah kmu, jadii plisss jangan terlalu di paksain kalo bener bener udah lowbat.</p>
        
        <p>wes ga tau neh meh ngomong opo, selamat bergabung di circle 20th dimana kejadian dewasa yang sebenarnya baru saja di mulai, terimakasih udah bertahan sejauh ini buat diri kamu, orang terdekatmu dan masa depanmu. semoga dunia selalu berbuat baik buat xena kapanpun dan dimanapun xena ada.</p>
        
        <p style="font-weight: bold; color: #FF4B4B; font-size: 18px; margin-top: 25px;">once again, happy 20th birthday xena ida karunia 🤩🤩🥳😼 u are an amazing person.</p>
    </div>
""", unsafe_allow_html=True)

# Fitur Make A Wish Box
st.write("")
st.subheader("🔮 Tulis Harapanmu di Usia 20 Tahun Ini")
wish_input = st.text_input("Apa pencapaian terbesar yang ingin kamu raih tahun ini?", placeholder="Contoh: Sukses kuliah kedokteran / Bahagia selalu...")

if st.button("Tiup Lilin & Kirim Harapan 🎂🚀"):
    if wish_input:
        st.toast("Harapanmu sudah tercatat di semesta! 💫")
        st.balloons()
        st.success(f"Selamat! Harapanmu: \"{wish_input}\" telah dikunci. Semoga segera terwujud nyata tahun ini! ✨")
    else:
        st.warning("Tulis dulu harapanmu sebelum meniup lilin virtual!")

