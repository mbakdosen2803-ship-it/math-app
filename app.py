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
    st.title("📝 Kuis Asesmen Numerasi Fungsional")
    st.write("Silakan jawab 10 pertanyaan di bawah ini secara mandiri!")
    
    # Soal 1
    st.markdown("---")
    q1 = st.radio("1. Jika fungsi permintaan masker adalah Qd = 50 - 2P. Jika harga masker (P) adalah 10, berapakah jumlah yang diminta?", ["20", "30", "40", "50"], key="soal1")
    if st.button("Cek Jawaban Soal 1"):
        if q1 == "30": st.success("Benar! ✨ Pembahasan: Qd = 50 - 2(10) = 30.")
        else: st.error("Salah. ❌ Periksa kembali perhitungan perkaliannya.")

    # Soal 2
    st.markdown("---")
    q2 = st.radio("2. Jika fungsi penawaran kemeja adalah Qs = -20 + 3P. Jika harga kemeja (P) adalah 20, berapakah kuantitas yang ditawarkan?", ["20", "30", "40", "50"], key="soal2")
    if st.button("Cek Jawaban Soal 2"):
        if q2 == "40": st.success("Benar! ✨ Pembahasan: Qs = -20 + 3(20) = 40.")
        else: st.error("Salah. ❌ Ingat bahwa konstanta bernilai negatif.")

    # Soal 3
    st.markdown("---")
    q3 = st.radio("3. Diketahui fungsi permintaan Qd = 100 - 2P dan penawaran Qs = -20 + 4P. Berapakah harga (P) keseimbangan pasarnya?", ["10", "20", "30", "40"], key="soal3")
    if st.button("Cek Jawaban Soal 3"):
        if q3 == "20": st.success("Benar! ✨ Pembahasan: Qd = Qs -> 100 - 2P = -20 + 4P -> 120 = 6P -> P = 20.")
        else: st.error("Salah. ❌ Cari nilai P saat Qd sama dengan Qs.")

    # Soal 4
    st.markdown("---")
    q4 = st.radio("4. Berdasarkan Soal 3, berapakah jumlah kuantitas (Q) keseimbangan pasar yang terjadi?", ["40", "50", "60", "70"], key="soal4")
    if st.button("Cek Jawaban Soal 4"):
        if q4 == "60": st.success("Benar! ✨ Pembahasan: Masukkan P = 20 ke rumus Qd. Qd = 100 - 2(20) = 60.")
        else: st.error("Salah. ❌ Substitusikan nilai P keseimbangan ke salah satu fungsi.")

    # Soal 5
    st.markdown("---")
    q5 = st.radio("5. Jika harga suatu barang naik, maka jumlah barang yang ditawarkan oleh produsen cenderung akan...", ["Turun", "Tetap", "Naik", "Tidak menentu"], key="soal5")
    if st.button("Cek Jawaban Soal 5"):
        if q5 == "Naik": st.success("Benar! ✨ Sesuai dengan Hukum Penawaran, harga sebanding dengan jumlah penawaran.")
        else: st.error("Salah. ❌ Ingat kembali perilaku produsen saat harga pasar naik.")

    # Soal 6
    st.markdown("---")
    q6 = st.radio("6. Fungsi permintaan barang dinyatakan dengan P = 80 - 4Q. Jika jumlah barang yang diminta (Q) adalah 5, berapakah harganya (P)?", ["50", "60", "70", "80"], key="soal6")
    if st.button("Cek Jawaban Soal 6"):
        if q6 == "60": st.success("Benar! ✨ Pembahasan: P = 80 - 4(5) = 80 - 20 = 60.")
        else: st.error("Salah. ❌ Kurangi konstanta dengan hasil perkaliannya.")

    # Soal 7
    st.markdown("---")
    q7 = st.radio("7. Jika suatu produk diberikan subsidi oleh pemerintah, pengaruh yang terjadi pada kurva penawaran adalah...", ["Kurva bergeser ke kiri bawah", "Kurva bergeser ke kanan bawah", "Kurva tetap", "Kurva menjadi vertikal"], key="soal7")
    if st.button("Cek Jawaban Soal 7"):
        if q7 == "Kurva bergeser ke kanan bawah": st.success("Benar! ✨ Subsidi menurunkan biaya produksi produsen, sehingga penawaran bertambah.")
        else: st.error("Salah. ❌ Subsidi meringankan beban produsen, periksa arah pergeserannya.")

    # Soal 8
    st.markdown("---")
    q8 = st.radio("8. Pada harga P = 50, jumlah permintaan barang adalah 10 unit. Ketika harga turun menjadi P = 40, jumlah permintaan naik menjadi 15 unit. Gradien (b) fungsi permintaan Qd = a - bP adalah...", ["0.5", "1.0", "1.5", "2.0"], key="soal8")
    if st.button("Cek Jawaban Soal 8"):
        if q8 == "0.5": st.success("Benar! ✨ Pembahasan: b = delta_Q / delta_P = (15 - 10) / (50 - 40) = 5 / 10 = 0.5.")
        else: st.error("Salah. ❌ Rumus gradien kemiringan kuantitas terhadap harga adalah delta_Q dibagi delta_P.")

    # Soal 9
    st.markdown("---")
    q9 = st.radio("9. Kondisi pasar di mana jumlah barang yang diminta konsumen lebih besar daripada jumlah yang ditawarkan produsen dinamakan...", ["Equilibrium", "Shortage (Kelangkaan)", "Surplus", "Monopoli"], key="soal9")
    if st.button("Cek Jawaban Soal 9"):
        if q9 == "Shortage (Kelangkaan)": st.success("Benar! ✨ Excess Demand atau kelebihan permintaan memicu kelangkaan barang di pasar.")
        else: st.error("Salah. ❌ Jumlah permintaan lebih melimpah dibanding pasokan, sebutannya adalah kelangkaan.")

    # Soal 10
    st.markdown("---")
    q10 = st.radio("10. Jika fungsi penawaran adalah Qs = 2P - 10, pada tingkat harga berapakah produsen mulai enggan menawarkan barangnya sama sekali (Qs = 0)?", ["P = 2", "P = 5", "P = 10", "P = 0"], key="soal10")
    if st.button("Cek Jawaban Soal 10"):
        if q10 == "P = 5": st.success("Benar! ✨ Pembahasan: 0 = 2P - 10 -> 2P = 10 -> P = 5
