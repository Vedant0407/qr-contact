# 📲 3-in-1 Contact QR Hub (Call, Chat, Instagram)

A lightweight, modern web landing page and QR code generation suite designed for business cards, storefronts, table tents, and event badges. When scanned, it presents three instant touchpoints:

1. 📞 **Call Us**: Opens the visitor's native phone dialer with your number pre-filled.
2. 💬 **Chat on WhatsApp**: Launches WhatsApp directly with an optional pre-typed greeting message.
3. 📸 **Instagram Profile**: Opens your Instagram profile in the Instagram app or browser.

---

## 📁 Project Structure

- [**`index.html`**](index.html): The mobile-optimized visitor landing page. Clean dark-mode glassmorphism theme, fast loading, zero external framework dependencies.
- [**`generator.html`**](generator.html): The interactive Studio tool where you can configure your contact information, customize branding, preview in real time, and download high-resolution QR codes.
- [**`generate_qr.py`**](generate_qr.py): A Python script to generate branded, high-res printable QR cards with custom labels.

---

## 🚀 Quick Local Testing

### Option 1: Open in Browser
Double-click [`generator.html`](generator.html) or open it in any web browser to customize your details and test the buttons.

### Option 2: Test on Your Actual Smartphone (Same Wi-Fi)
1. Run a local server from this folder:
   ```bash
   python -m http.server 8000
   ```
2. Find your computer's local IP address (`ipconfig` on Windows).
3. Open `http://<YOUR_IP>:8000/generator.html` in your browser.
4. Set the Base URL to `http://<YOUR_IP>:8000/index.html`.
5. Point your phone camera at the screen and scan the QR code!

---

## 🌐 Free Hosting (So Anyone Can Scan from Anywhere)

To make your QR code permanent and scannable by anyone on cellular data or outside your Wi-Fi, host `index.html` on any free static hosting service:

### Method A: GitHub Pages (Recommended - 2 Minutes)
1. Create a free repository on [GitHub](https://github.com).
2. Upload `index.html`.
3. Go to **Settings > Pages > Branch: main / root** and click **Save**.
4. GitHub provides you with a free link like `https://yourusername.github.io/qr-card`.
5. In [`generator.html`](generator.html), paste that link as the **Hosting Base URL** and download your permanent QR code!

### Method B: Netlify Drop / Vercel
- Drag and drop the folder into [Netlify Drop](https://app.netlify.com/drop) or deploy via Vercel to get an instant `https://...` URL.

---

## ⚙️ Customization via Query Parameters

You don't even need to edit the code to change details. You can pass parameters in the URL:
```
index.html?name=Apex+Care&phone=+15551234567&whatsapp=15551234567&insta=apexfitness&msg=Hi!
```
- `name`: Display name or company name
- `bio`: Subtitle or short tagline
- `phone`: Dialing phone number
- `whatsapp`: WhatsApp phone digits (international format without `+` or spaces)
- `msg`: Pre-filled message for WhatsApp chat
- `insta`: Instagram username handle
