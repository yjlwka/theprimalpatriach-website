import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Header Button
content = content.replace('GET FULL BUNDLE', 'GET THE BLUEPRINT')
content = content.replace('https://buy.stripe.com/00wcN54Iv04w0nY7X21B600', 'https://buy.stripe.com/7sY28r0sf8B24Eea5a1B603')

# 2. Update Hero Text
content = content.replace('"Deploy 19th-century mechanical leverage to grow and preserve your own food off-the-grid, regardless of your age. Choose your structural blueprint below."', '"Deploy 19th-century mechanical leverage to grow and preserve your own food off-the-grid, regardless of your age. Get the complete structural blueprint below."')

# 3. Replace Pricing Section completely
pricing_section_start = content.find('<section id="pricing"')
pricing_section_end = content.find('</section>', pricing_section_start) + len('</section>')

new_pricing_section = """<section id="pricing" class="bg-[#1e1b18]/40 w-full py-24 backdrop-blur-md">
      <div class="max-w-4xl mx-auto px-6">
        <div class="bg-[#080706]/60 border-2 border-[#d88c51]/50 p-1 shadow-[0_0_40px_rgba(216,140,81,0.2)] relative rounded-sm transition-transform duration-300 hover:shadow-[0_0_50px_rgba(216,140,81,0.3)] backdrop-blur-lg">
          <div class="bg-red-600 text-white text-center py-2 font-bold text-[10px] sm:text-xs uppercase tracking-widest font-sans drop-shadow-sm">
            ★★★★★ INSTANT PDF DOWNLOAD
          </div>
          <div class="border border-[#c36934]/20 p-8 md:p-12 flex flex-col md:flex-row gap-10 items-center bg-[#080706]/30 backdrop-blur-md relative z-10">
            
            <!-- Left: Image -->
            <div class="w-full md:w-1/2">
              <img src="/assets/VOLUME1-COVER.jpg" alt="Volume I: The 1850 Maraîcher Soil Matrix" class="w-full h-auto object-cover rounded-sm drop-shadow-2xl">
            </div>
            
            <!-- Right: Content -->
            <div class="w-full md:w-1/2 flex flex-col">
              <h3 class="text-2xl md:text-3xl font-bold mb-3 text-white font-serif uppercase tracking-wider leading-tight">VOLUME I:<br/>THE 1850 MARAÎCHER SOIL MATRIX</h3>
              <p class="text-[#e3dfd8]/70 text-base md:text-lg italic font-serif mb-6">The Thermodynamic Blueprint for High-Yield Production</p>
              
              <div class="flex items-center gap-4 mb-8 font-serif border-b border-[#c36934]/20 pb-6">
                <span class="text-gray-500 line-through text-2xl decoration-red-600">$47</span>
                <span class="text-6xl font-bold text-[#d88c51] drop-shadow-md">$17</span>
                <span class="text-red-600 font-bold font-sans text-xs tracking-widest uppercase bg-red-600/10 px-2 py-1 rounded-sm border border-red-600/20">SAVE $30</span>
              </div>
              
              <ul class="space-y-4 mb-8 flex-grow font-sans text-[16px] text-[#e3dfd8] leading-snug">
                <li class="flex items-start gap-3">
                  <span class="text-green-500 font-bold text-lg leading-none drop-shadow-sm mt-0.5">✔</span> 
                  <span><strong class="text-[#d88c51] font-bold">25 forbidden methods</strong> for heating, cooling, pest control, water</span>
                </li>
                <li class="flex items-start gap-3">
                  <span class="text-green-500 font-bold text-lg leading-none drop-shadow-sm mt-0.5">✔</span> 
                  <span><strong class="text-[#d88c51] font-bold">The $300 earth tunnel</strong> system from Holmes County</span>
                </li>
                <li class="flex items-start gap-3">
                  <span class="text-green-500 font-bold text-lg leading-none drop-shadow-sm mt-0.5">✔</span> 
                  <span>Hexagonal, high-density grids to retain 90% moisture</span>
                </li>
                <li class="flex items-start gap-3">
                  <span class="text-green-500 font-bold text-lg leading-none drop-shadow-sm mt-0.5">✔</span> 
                  <span>100% free, localized organic inputs</span>
                </li>
              </ul>
              
              <a href="https://buy.stripe.com/7sY28r0sf8B24Eea5a1B603" target="_blank" class="block text-center bg-[#d88c51] hover:bg-[#e49b63] text-[#080706] font-bold py-5 px-4 uppercase tracking-widest transition-transform hover:scale-105 text-lg font-serif w-full shadow-[0_0_20px_rgba(216,140,81,0.4)] rounded-sm mt-auto">DOWNLOAD NOW →</a>
              <p class="text-center text-xs text-gray-500 mt-4 font-sans uppercase tracking-widest">Secure Stripe Checkout</p>
            </div>
            
          </div>
        </div>
      </div>
    </section>"""

content = content[:pricing_section_start] + new_pricing_section + content[pricing_section_end:]

# 4. Remove Exit Modal
modal_start = content.find('<!-- Exit-Intent Modal -->')
modal_end = content.find('</div>\n  </div>\n\n  <script type="module" src="/main.js"></script>', modal_start) + len('</div>\n  </div>')
if modal_start != -1:
    content = content[:modal_start] + content[modal_end:]

# Also remove modal JS logic
js_modal_start = content.find('// Exit-Intent Modal Logic')
js_modal_end = content.find('// FAQ Accordion Logic', js_modal_start)
if js_modal_start != -1:
    content = content[:js_modal_start] + content[js_modal_end:]

js_leave_start = content.find('// Trigger on mouse leave top window')
js_leave_end = content.find('});\n  </script>', js_leave_start)
if js_leave_start != -1:
    content = content[:js_leave_start] + content[js_leave_end:]


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Redesign complete.")
