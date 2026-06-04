import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace links for Card 1 (Volume 1)
# 1. The image link
content = content.replace(
    '<a href="thank-you.html" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME1-COVER.jpg"',
    '<a href="https://pay.hotmart.com/I105608889O" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME1-COVER.jpg"'
)
# 2. The button link
content = content.replace(
    '<a href="thank-you.html" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 1 ONLY — $27</a>',
    '<a href="https://pay.hotmart.com/I105608889O" target="_blank" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 1 ONLY — $27</a>'
)


# Replace links for Card 2 (Volume 2)
# 1. The image link
content = content.replace(
    '<a href="thank-you.html" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME2-COVER.jpg"',
    '<a href="https://pay.hotmart.com/A105829385U" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME2-COVER.jpg"'
)
# 2. The button link
content = content.replace(
    '<a href="thank-you.html" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 2 ONLY — $27</a>',
    '<a href="https://pay.hotmart.com/A105829385U" target="_blank" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 2 ONLY — $27</a>'
)


# Replace links for Card 3 (Bundle)
# 1. The image link
content = content.replace(
    '<a href="thank-you.html" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME3-COVER.png"',
    '<a href="https://pay.hotmart.com/V105833643T" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME3-COVER.png"'
)
# 2. The button link
content = content.replace(
    '<a href="thank-you.html" class="block text-center bg-[#d88c51] hover:bg-[#e49b63] text-[#080706] font-bold py-5 px-2 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif w-full shadow-lg shadow-[#d88c51]/40 rounded-sm mt-auto">GET THE FULL SYSTEM →</a>',
    '<a href="https://pay.hotmart.com/V105833643T" target="_blank" class="block text-center bg-[#d88c51] hover:bg-[#e49b63] text-[#080706] font-bold py-5 px-2 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif w-full shadow-lg shadow-[#d88c51]/40 rounded-sm mt-auto">GET THE FULL SYSTEM →</a>'
)

# Also replace the exit intent modal link
content = content.replace(
    '<a href="thank-you.html" class="w-full block text-center bg-[#3a5340] hover:bg-[#46634d] text-white font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif shadow-lg cursor-pointer rounded-sm">\n          GET VOLUME 1 ONLY — $27\n        </a>',
    '<a href="https://pay.hotmart.com/I105608889O" target="_blank" class="w-full block text-center bg-[#3a5340] hover:bg-[#46634d] text-white font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif shadow-lg cursor-pointer rounded-sm">\n          GET VOLUME 1 ONLY — $27\n        </a>'
)

# And any remaining thank-you.html just in case (like top nav if any)
content = content.replace('href="thank-you.html"', 'href="https://pay.hotmart.com/V105833643T" target="_blank"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Links updated")
