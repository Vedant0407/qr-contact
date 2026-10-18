import argparse
import urllib.parse
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate(url, output_path="contact_qr.png", label="Scan to Connect"):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="#0b0f19", back_color="#ffffff").convert('RGB')
    
    # Create high-res branded card frame
    qr_w, qr_h = img_qr.size
    card_w = qr_w + 60
    card_h = qr_h + 120

    card = Image.new('RGB', (card_w, card_h), '#ffffff')
    draw = ImageDraw.Draw(card)

    # Draw rounded rectangle border
    draw.rounded_rectangle([(10, 10), (card_w - 10, card_h - 10)], radius=20, outline='#e2e8f0', width=2)
    
    # Paste QR code
    card.paste(img_qr, (30, 30))

    # Add text label below QR
    try:
        # Default font
        font = ImageFont.load_default()
    except Exception:
        font = None

    text = label
    # Draw centered text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    draw.text(((card_w - text_w) / 2, qr_h + 50), text, fill='#1e293b', font=font)

    sub_text = "Call  •  WhatsApp  •  Instagram"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font)
    sub_w = bbox_sub[2] - bbox_sub[0]
    draw.text(((card_w - sub_w) / 2, qr_h + 75), sub_text, fill='#64748b', font=font)

    card.save(output_path, 'PNG', quality=100)
    print(f"[SUCCESS] QR Code saved to: {os.path.abspath(output_path)}")
    print(f"[URL] Target URL: {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 3-in-1 Contact QR Code")
    parser.add_argument("--base-url", default="http://172.17.48.79:8000/index.html", help="Hosted base URL of index.html")
    parser.add_argument("--name", default="Apex Care", help="Brand/Person Name")
    parser.add_argument("--phone", default="+15551234567", help="Phone number to call")
    parser.add_argument("--wa", default="15551234567", help="WhatsApp number (digits only)")
    parser.add_argument("--insta", default="instagram", help="Instagram handle")
    parser.add_argument("--msg", default="Hi! I scanned your QR code and wanted to connect.", help="WhatsApp initial greeting")
    parser.add_argument("--output", default="contact_qr.png", help="Output filename")

    args = parser.parse_args()

    params = {
        "name": args.name,
        "phone": args.phone,
        "whatsapp": args.wa,
        "insta": args.insta,
        "msg": args.msg
    }

    full_url = f"{args.base_url}?{urllib.parse.urlencode(params)}"
    generate(full_url, args.output, label=f"Scan to Connect with {args.name}")
