import os
import time
import html
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from utils import load_model_and_labels, prepare_image

# === KONFIGURASI API ===
TELEGRAM_API = "ubah api token telegram di sini"
GEMINI_API_KEY = "ubah api gemini di sini"  

# === SETUP Gemini ===
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel("gemini-1.5-flash")

# === LOAD CNN & LABEL ENCODER ===
model, le = load_model_and_labels()

# === PEMBAGI TEKS PANJANG UNTUK TELEGRAM ===
def split_text(text, max_length=4000):
    lines = text.split('\n')
    chunks = []
    current = ""
    for line in lines:
        if len(current) + len(line) + 1 > max_length:
            chunks.append(current)
            current = ""
        current += line + "\n"
    if current:
        chunks.append(current)
    return chunks

# === FUNGSI REQUEST GEMINI DENGAN RETRY & HANDLING ===
def ask_gemini(prompt: str, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = model_gemini.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            if attempt < retries - 1:
                print(f"[Retry {attempt + 1}] Gemini error: {e}")
                time.sleep(delay)
            else:
                return f"⚠️ Terjadi error saat menghubungi Gemini:\n{str(e)}"

# === COMMAND /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 Kirim gambar simbol hieroglif Mesir kuno.")

# === HANDLER GAMBAR ===
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Simpan gambar dari pengguna
        file = await update.message.photo[-1].get_file()
        path = "temp.jpg"
        await file.download_to_drive(path)

        # Prediksi simbol dengan CNN
        img = prepare_image(path)
        pred = model.predict(img)
        label = le.inverse_transform([pred.argmax()])[0]

        # Kirim hasil deteksi
        await update.message.reply_text(
            f"✅ <b>Simbol terdeteksi:</b> {html.escape(label)}",
            parse_mode="HTML"
        )

        # Buat prompt Gemini
        prompt = (
            f"Jelaskan secara ringkas simbol hieroglif Mesir kuno '{label}', "
            f"termasuk sejarah, makna, dan konteks penggunaannya. "
            f"Jawaban maksimal 3 paragraf dan tidak lebih dari 4000 karakter."
        )
        desc = ask_gemini(prompt)

        # Kirim penjelasan dari Gemini
        await update.message.reply_text("📚 <b>Penjelasan Historis:</b>", parse_mode="HTML")
        for part in split_text(desc):
            safe_text = html.escape(part)
            await update.message.reply_text(safe_text, parse_mode="HTML")

    except Exception as e:
        await update.message.reply_text(
            f"❌ Terjadi error saat memproses gambar:\n<code>{html.escape(str(e))}</code>",
            parse_mode="HTML"
        )

# === MAIN ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_API).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("🤖 Bot hieroglif aktif dan terhubung ke Gemini.")
    app.run_polling()
