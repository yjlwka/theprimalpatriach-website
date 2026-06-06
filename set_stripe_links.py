import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace all #checkout links with the appropriate stripe links based on context

# VOLUME 1: https://buy.stripe.com/7sY28r0sf8B24Eea5a1B603
v1_link = "https://buy.stripe.com/7sY28r0sf8B24Eea5a1B603"

# VOLUME 2: https://buy.stripe.com/eVqaEX5Mz2cEgmW4KQ1B602
v2_link = "https://buy.stripe.com/eVqaEX5Mz2cEgmW4KQ1B602"

# BUNDLE / VOLUME 3: https://buy.stripe.com/00wcN54Iv04w0nY7X21B600
bundle_link = "https://buy.stripe.com/00wcN54Iv04w0nY7X21B600"

# Card 1 (Volume 1) Image
content = content.replace(
    '<a href="#checkout" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME1-COVER.jpg"',
    f'<a href="{v1_link}" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME1-COVER.jpg"'
)
# Card 1 (Volume 1) Button
content = content.replace(
    '<a href="#checkout" target="_blank" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 1 ONLY — $27</a>',
    f'<a href="{v1_link}" target="_blank" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 1 ONLY — $27</a>'
)

# Card 2 (Volume 2) Image
content = content.replace(
    '<a href="#checkout" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME2-COVER.jpg"',
    f'<a href="{v2_link}" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME2-COVER.jpg"'
)
# Card 2 (Volume 2) Button
content = content.replace(
    '<a href="#checkout" target="_blank" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 2 ONLY — $27</a>',
    f'<a href="{v2_link}" target="_blank" class="block text-center bg-[#1e1b18] hover:bg-[#2a2622] text-[#e3dfd8] border border-[#c36934]/30 font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif mt-auto">GET VOLUME 2 ONLY — $27</a>'
)

# Card 3 (Bundle) Image
content = content.replace(
    '<a href="#checkout" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME3-COVER.png"',
    f'<a href="{bundle_link}" target="_blank" class="block overflow-hidden rounded-sm mb-6 drop-shadow-md">\n              <img src="/assets/VOLUME3-COVER.png"'
)
# Card 3 (Bundle) Button
content = content.replace(
    '<a href="#checkout" target="_blank" class="block text-center bg-[#d88c51] hover:bg-[#e49b63] text-[#080706] font-bold py-5 px-2 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif w-full shadow-lg shadow-[#d88c51]/40 rounded-sm mt-auto">GET THE FULL SYSTEM →</a>',
    f'<a href="{bundle_link}" target="_blank" class="block text-center bg-[#d88c51] hover:bg-[#e49b63] text-[#080706] font-bold py-5 px-2 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif w-full shadow-lg shadow-[#d88c51]/40 rounded-sm mt-auto">GET THE FULL SYSTEM →</a>'
)

# Exit modal button (Volume 1)
content = content.replace(
    '<a href="#checkout" target="_blank" class="w-full block text-center bg-[#3a5340] hover:bg-[#46634d] text-white font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif shadow-lg cursor-pointer rounded-sm">\n          GET VOLUME 1 ONLY — $27\n        </a>',
    f'<a href="{v1_link}" target="_blank" class="w-full block text-center bg-[#3a5340] hover:bg-[#46634d] text-white font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif shadow-lg cursor-pointer rounded-sm">\n          GET VOLUME 1 ONLY — $27\n        </a>'
)

# Now, any remaining `#checkout` (e.g. the Header Top Nav) is the Bundle link
# But wait, earlier I might not have changed the header link to `#checkout`. Let's just do a regex replace to catch any `#checkout`
content = content.replace('href="#checkout"', f'href="{bundle_link}" target="_blank"')
# Also if the header nav still has href="#pricing", let's update it to the bundle link so it's a direct buy button.
content = content.replace('href="#pricing"', f'href="{bundle_link}" target="_blank"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Stripe links applied successfully")
