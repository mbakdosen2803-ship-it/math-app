import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi Halaman Aplikasi
st.set_page_config(page_title="MathFunc: Media Digital Fungsi Linear", layout="wide")

# Sidebar Navigasi Menu
st.sidebar.title("🎮 Navigasi Aplikasi")
menu = st.sidebar.radio("Pilih Menu Pembelajaran:", ["1. Materi Pembelajaran", "2. Simulator Keseimbangan Pasar", "3. Kuis Numerasi Interaktif", "4. Profil Pengembang"])

# ==================== MENU 1: MATERI ====================
if menu == "1. Materi Pembelajaran":
    st.title("📚 Materi: Fungsi Linear dalam Ekonomi")
    st.write("Selamat datang di modul digital matematika fungsional!")
    
    tab1, tab2, tab3 = st.tabs(["Fungsi Permintaan", "Fungsi Penawaran", "Keseimbangan Pasar"])
    
    with tab1:
        st.subheader("📉 Fungsi Permintaan (Qd)")
        st.write("Menunjukkan hubungan antara harga barang ($P$) dengan jumlah barang yang diminta konsumen. Hukumnya: Jika harga NAIK, permintaan TURUN. Rumus: $Q_d = a - bP$.")
        
    with tab2:
        st.subheader("📈 Fungsi Penawaran (Qs)")
        st.write("Menunjukkan hubungan antara harga barang ($P$) dengan jumlah barang yang ditawarkan penjual. Hukumnya: Jika harga NAIK, penawaran NAIK. Rumus: $Q_s = -c + dP$.")
        
    with tab3:
        st.subheader("⚖️ Keseimbangan Pasar (Ekuilibrium)")
        st.write("Terjadi ketika jumlah barang yang diminta konsumen SAMA PERSIS dengan jumlah yang ditawarkan produsen ($Q_d = Q_s$).")

# ==================== MENU 2: SIMULATOR ====================
elif menu == "2. Simulator Keseimbangan Pasar":
    st.title("📊 Simulator Kurva Matematika Ekonomi")
    st.write("Geser angka di sidebar sebelah kiri untuk melihat perubahan kurva secara langsung!")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Atur Parameter Fungsi")
    a = st.sidebar.slider("Konstanta Permintaan (a)", 50, 150, 100)
    b = st.sidebar.slider("Koefisien Permintaan (b)", 1, 5, 2)
    c = st.sidebar.slider("Konstanta Penawaran (c)", 10, 50, 20)
    d = st.sidebar.slider("Koefisien Penawaran (d)", 1, 5, 2)
    
    # Hitung Titik Keseimbangan
    P_eq = (a + c) / (b + d)
    Q_eq = a - (b * P_eq)
    
    st.info(f"✨ **Titik Keseimbangan Pasar:** Harga ($P$) = **{P_eq:.2f}** dan Kuantitas ($Q$) = **{Q_eq:.2f}**")
    
    # Membuat Grafik
    P_vals = np.linspace(0, (a/b)+10, 100)
    Q_d = a - b * P_vals
    Q_s = -c + d * P_vals
    
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(P_vals, Q_d, label="Permintaan (Qd)", color="red", linewidth=2)
    ax.plot(P_vals, Q_s, label="Penawaran (Qs)", color="blue", linewidth=2)
    if P_eq > 0 and Q_eq > 0:
        ax.scatter(P_eq, Q_eq, color="black", s=100, zorder=5, label=f"Ekuilibrium ({P_eq:.1f}, {Q_eq:.1f})")
        ax.axhline(Q_eq, color='gray', linestyle='--')
        ax.axvline(P_eq, color='gray', linestyle='--')
    
    ax.set_xlabel("Harga (P)")
    ax.set_ylabel("Kuantitas (Q)")
    ax.set_ylim(0, a+20)
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# ==================== MENU 3: KUIS ====================
elif menu == "3. Kuis Numerasi Interaktif":
    st.title("📝 Kuis Evaluasi Mandiri")
    
    q1 = st.radio("1. Jika fungsi permintaan masker adalah Qd = 50 - 2P. Jika harga masker (P) adalah 10, berapakah jumlah yang diminta?", ["20", "30", "40", "50"])
    if st.button("Cek Jawaban Soal 1"):
        if q1 == "30":
            st.success("Benar! Pembahasan: Qd = 50 - 2(10) = 30.")
        else:
            st.error("Salah. Coba hitung kembali menggunakan rumus Qd.")

# ==================== MENU 4: PROFIL ====================
elif menu == "4. Profil Pengembang":
    st.title("👤 Profil Pengembang")
    st.write("**Nama:** Marchinia Rakhmi Pradani Putri")
    st.write("**Program Studi:** Magister Pendidikan Matematika")
    st.write("**Mata Kuliah:** Teknologi Pembelajaran Digital")