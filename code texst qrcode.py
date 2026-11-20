from pathlib import Path
import qrcode


def build_qr_matrix(
    data: str,
    version: int = 3,
    mask_pattern: int = 0,
    output_path: str | Path = r"C:\Users\InstallationsBruger\Desktop\mary_qr.png"
):
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        mask_pattern=mask_pattern,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    # fit=True allows qrcode to automatically adjust the version if the text is too long for Version 3
    qr.make(fit=True)

    matrix = qr.get_matrix()
    print(f"Matrix size: {len(matrix)}x{len(matrix[0])}")

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_file)
    return matrix


if __name__ == "__main__":
    # Pass any plain text message here
    text_message = "Hello, world! This is a plain text QR code."

    grid = build_qr_matrix(
        data=text_message,
        version=3,
        mask_pattern=0,
        output_path=r"C:\Users\InstallationsBruger\Desktop\mary_qr.png",
    )

    for row in grid:
        print("".join("##" if cell else "  " for cell in row))