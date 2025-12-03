import streamlit as st
import random
import time

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Matematik Oyun Parkı", layout="wide", page_icon="🧮")

# --- CSS İLE RENKLENDİRME (Çocuklar için büyük yazılar) ---
st.markdown("""
<style>
    .big-font { font-size:30px !important; font-weight: bold; }
    .medium-font { font-size:20px !important; }
    .success { color: green; }
    .error { color: red; }
</style>
""", unsafe_allow_html=True)

st.title("🧮 Matematik Oyun Parkı")
st.markdown("Hoş geldin! Burada rakamlar yok, **meyveler, şekerler ve oyunlar** var!")

# --- SOL MENÜ (NAVİGASYON) ---
mod = st.sidebar.radio("Hangi Oyunu Oynayalım?", 
    ["🍎 Toplama Fabrikası", "🍪 Çıkarma Canavarı", "🥕 Çarpma Tarlası", "🍬 Bölme Paylaşımı", "🏆 Yarışma Zamanı"])

# ==========================================
# 🍎 1. TOPLAMA FABRİKASI
# ==========================================
if mod == "🍎 Toplama Fabrikası":
    st.header("🍎 Elma Toplama Zamanı")
    st.write("Sepetimizde kaç elma olacak?")
    
    col1, col2, col3 = st.columns([1, 0.2, 1])
    
    with col1:
        s1 = st.slider("Kırmızı Elmalar", 1, 10, 3)
        st.write("🍎" * s1)
        
    with col2:
        st.markdown("<h1 style='text-align: center;'>+</h1>", unsafe_allow_html=True)
        
    with col3:
        s2 = st.slider("Yeşil Elmalar", 1, 10, 2)
        st.write("🍏" * s2)
        
    st.markdown("---")
    toplam = s1 + s2
    st.subheader(f"Sonuç: {s1} + {s2} = {toplam} Elma")
    
    # Görsel Sonuç
    st.write("Sepetin İçi:")
    st.write("🍎" * s1 + "🍏" * s2)
    
    if toplam > 15:
        st.success("Waoow! Sepet doldu taştı! 🎉")

# ==========================================
# 🍪 2. ÇIKARMA CANAVARI
# ==========================================
elif mod == "🍪 Çıkarma Canavarı":
    st.header("🍪 Kurabiye Canavarı")
    st.write("Canavar acıktı! Kurabiyeleri yiyor.")
    
    baslangic = st.slider("Tabakta kaç kurabiye var?", 5, 20, 10)
    yenen = st.slider("Canavar kaç tane yesin?", 1, baslangic, 3)
    
    kalan = baslangic - yenen
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Başlangıçta:")
        # 5'li satırlar halinde göster
        st.write("🍪" * baslangic)
        
    with col2:
        st.warning(f"Canavar {yenen} tanesini yedi! (Hammm!)")
        st.write("😋" * yenen)
        
    st.markdown("---")
    st.subheader(f"Sonuç: {baslangic} - {yenen} = {kalan} Kurabiye Kaldı")
    st.write("🍪" * kalan)

# ==========================================
# 🥕 3. ÇARPMA TARLASI
# ==========================================
elif mod == "🥕 Çarpma Tarlası":
    st.header("🥕 Havuç Tarlası (Çarpım Tablosu)")
    st.write("Çarpma demek, **'Tane'** demektir. 3 tane 4 gibi.")
    
    col1, col2 = st.columns(2)
    with col1:
        satir = st.number_input("Kaç Sıra Olsun?", 1, 10, 3)
    with col2:
        sutun = st.number_input("Her Sırada Kaç Havuç Olsun?", 1, 10, 4)
        
    sonuc = satir * sutun
    
    st.markdown("---")
    st.subheader(f"İşlem: {satir} x {sutun} = {sonuc}")
    
    # Görsel Grid (Izgara)
    st.write("İşte Tarlamız:")
    for _ in range(satir):
        st.write("🥕 " * sutun)
        
    st.info(f"Bak! {satir} tane sıra var, her birinde {sutun} havuç var. Toplam {sonuc} havuç!")

# ==========================================
# 🍬 4. BÖLME PAYLAŞIMI
# ==========================================
elif mod == "🍬 Bölme Paylaşımı":
    st.header("🍬 Şekerleri Paylaşalım")
    st.write("Bölme demek, **'Eşit Paylaşmak'** demektir.")
    
    seker_sayisi = st.number_input("Kaç Şekerimiz Var?", 4, 30, 12, step=2)
    arkadas_sayisi = st.slider("Kaç Arkadaş Paylaşacak?", 1, 10, 3)
    
    # Kalanlı bölme kontrolü
    if seker_sayisi % arkadas_sayisi != 0:
        st.warning("⚠️ Eyvah! Şekerler tam bölünmüyor, bazıları artacak.")
    
    kisi_basi = seker_sayisi // arkadas_sayisi
    artan = seker_sayisi % arkadas_sayisi
    
    st.markdown("---")
    
    cols = st.columns(arkadas_sayisi)
    
    for i in range(arkadas_sayisi):
        with cols[i]:
            st.write(f"**{i+1}. Çocuk**")
            st.write("🧑")
            st.write("🍬" * kisi_basi)
            
    st.success(f"Her çocuğa **{kisi_basi}** şeker düştü!")
    
    if artan > 0:
        st.error(f"Sepette **{artan}** şeker arttı. Onları da sen ye! 😋")

# ==========================================
# 🏆 5. YARIŞMA ZAMANI
# ==========================================
elif mod == "🏆 Yarışma Zamanı":
    st.header("🏆 Büyük Ödüllü Yarışma")
    
    # Hafızada skor tutma
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
    if 'soru' not in st.session_state:
        # İlk soru üretimi
        op = random.choice(["+", "-", "x"])
        if op == "+":
            a, b = random.randint(1, 20), random.randint(1, 20)
            ans = a + b
        elif op == "-":
            a, b = random.randint(10, 30), random.randint(1, 10)
            ans = a - b
        else:
            a, b = random.randint(1, 10), random.randint(1, 10)
            ans = a * b
        st.session_state.soru = (a, op, b, ans)

    # Mevcut Skor
    st.metric("Mevcut Puanın", st.session_state.skor)
    
    # Soruyu Göster
    a, op, b, ans = st.session_state.soru
    sembol = "x" if op == "x" else op
    
    st.markdown(f"<h1 style='text-align: center;'>{a} {sembol} {b} = ?</h1>", unsafe_allow_html=True)
    
    cevap = st.number_input("Cevabı Yaz:", step=1, key="cevap_input")
    
    if st.button("Kontrol Et ✅"):
        if cevap == ans:
            st.balloons()
            st.success(f"TEBRİKLER! Doğru Cevap: {ans}")
            st.session_state.skor += 10
            # Yeni Soru Hazırla
            op = random.choice(["+", "-", "x"])
            if op == "+":
                a, b = random.randint(1, 20), random.randint(1, 20)
                new_ans = a + b
            elif op == "-":
                a, b = random.randint(10, 30), random.randint(1, 10)
                new_ans = a - b
            else:
                a, b = random.randint(1, 10), random.randint(1, 10)
                new_ans = a * b
            st.session_state.soru = (a, op, b, new_ans)
            time.sleep(1)
            st.rerun()
        else:
            st.error("Üzgünüm yanlış :( Tekrar dene!")