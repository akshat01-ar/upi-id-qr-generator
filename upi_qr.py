import qrcode as qr
print("only valid for upi_id not for mob number ")
upi = input("enter your upi id : ")
js = f"upi://pay?pa={upi}&pn=Recipient%20Name&mc=1234"
img = qr.make(js)
img.save(f"QR_{upi}.png")
img.show()
    
