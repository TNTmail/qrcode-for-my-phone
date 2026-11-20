from pathlib import Path
import qrcode

output_path = Path(r"C:\Users\InstallationsBruger\Desktop") / "phone_qr.png"

img = qrcode.make("tel:44429282")
img.save(output_path)
print(f"Saved to {output_path}")