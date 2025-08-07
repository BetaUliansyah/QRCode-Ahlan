import streamlit as st
import segno
from PIL import Image
    
APP_TITLE = 'QR Code Generator - Penerbit Ahlan'
APP_SUB_TITLE = 'Membuat QR Code dengan logo Ahlan'

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

def make_qrcode_ahlan(URL):
    LOGO = 'logo-ahlan-bg-putih.png'
    OUTPUT = 'qrcode.png'

    # Make QR code
    qr = segno.make_qr(URL, error='H')
    qr.save(OUTPUT, scale=100)
    
    # Now open that png image to put the logo
    img = Image.open(OUTPUT).convert("RGBA")
    
    width, height = img.size
    
    # How big the logo we want to put in the qr code png
    logo_size = 1100
    
    # Open the logo image
    logo = Image.open(LOGO).convert("RGBA")
    
    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))
    
    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))
    
    # put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))
    
    #img.show()
    img.save(OUTPUT)



if __name__ == "__main__":
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    text_input = st.text_input("Masukkan URL di sini", 
                               "https://www.ahlan.id/shop/dzikir-pagi-petang-for-kids-warna-coklat-3039",
                              label_visibility=st.session_state.visibility,
                              disabled=st.session_state.disabled,
#                              placeholder=st.session_state.placeholder,
                              )
    if text_input:
        make_qrcode_ahlan(text_input)
        st.warning("Jangan lupa untuk cek lagi apakah QR Code sudah benar!")
        st.image("qrcode.png", caption=f"{text_input}")
        
