from pathlib import Path
import qrcode

output_path = Path(r"C:\Users\InstallationsBruger\Desktop") / "qrcode.png"

url = "https://exfigure.com/da/products/vocaloid-hatsune-miku-desktop-cute-nekomimi-t-shirt-ver-taito-2023-07-28-15-00-00"
img = qrcode.make(url)
img.save(output_path)
print(f"Saved to {output_path}")