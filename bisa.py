import streamlit as st 

def konfigurasi_elektron(atomic_number):
    
    electron_config = {'1': '1s¹', '2': '1s²', '3': '1s² 2s¹', '4': '1s² 2s²', '5': '1s² 2s² 2p¹',
                       '6': '1s² 2s² 2p²', '7': '1s² 2s² 2p³', '8': '1s² 2s² 2p⁴', '9': '1s² 2s² 2p⁵',
                       '10': '1s² 2s² 2p⁶', '11': '1s² 2s² 2p⁶ 3s¹', '12': '1s² 2s² 2p⁶ 3s²',
                       '13': '1s² 2s² 2p⁶ 3s² 3p¹', '14': '1s² 2s² 2p⁶ 3s² 3p²', '15': '1s² 2s² 2p⁶ 3s² 3p³',
                       '16': '1s² 2s² 2p⁶ 3s² 3p⁴', '17': '1s² 2s² 2p⁶ 3s² 3p⁵', '18': '1s² 2s² 2p⁶ 3s² 3p⁶',
                       '19':'1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹', '20':'1s² 2s² 2p⁶ 3s² 3p⁶ 4s²', '21':'1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹'}

  
    if atomic_number not in electron_config:
        return "Nomor atom tidak valid. Masukkan nomor atom antara 1 hingga 18."

    return electron_config[atomic_number]

def main():
    st.title("Aplikasi Konfigurasi Elektron")
    st.write("Aplikasi ini menghasilkan konfigurasi elektron untuk atom dengan nomor atom tertentu.")

    
    atomic_number = st.text_input("Masukkan nomor atom (1-18):")

    
    if st.button("Tampilkan Konfigurasi Elektron"):
        result = konfigurasi_elektron(atomic_number)
        st.write("Konfigurasi elektron untuk atom dengan nomor atom", atomic_number, "adalah:", result)

if name == "main":
    main()