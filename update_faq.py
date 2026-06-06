import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- FAQ Section -->'
end_marker = '</section>'
start_idx = content.find(start_marker)
# Find the first </section> after the start_marker
end_idx = content.find(end_marker, start_idx) + len(end_marker)

new_faq_section = """<!-- FAQ Section -->
    <section class="bg-[#110d0b]/40 w-full py-24 backdrop-blur-md">
      <div class="max-w-4xl mx-auto px-6">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-white mb-6 font-serif drop-shadow-md">Common Questions</h2>
          <div class="w-16 h-1 bg-red-600 mx-auto rounded-full"></div>
        </div>

        <div class="space-y-4">
          
          <!-- FAQ 1 -->
          <div class="faq-item bg-black/40 backdrop-blur-sm border border-[#c36934]/20 hover:border-[#c36934]/40 transition-colors rounded-sm">
            <button class="w-full text-left px-6 py-5 flex justify-between items-center focus:outline-none">
              <h4 class="text-xl font-bold text-white font-serif">Do I need to buy expensive new tools to use this system?</h4>
              <span class="faq-icon text-red-600 text-2xl font-bold leading-none">+</span>
            </button>
            <div class="faq-content hidden px-6 pb-6 pt-0">
              <div class="w-full h-px bg-[#c36934]/20 mb-4"></div>
              <p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">No. You do not need to discard your entire shed of standard tools. The blueprint provides exact, DIY clinical steps to modify your existing straight-handled shovels and rakes using a simple aftermarket D-grip attachment. You will upgrade their geometry to achieve the required 70° leverage angle.</p>
            </div>
          </div>

          <!-- FAQ 2 -->
          <div class="faq-item bg-black/40 backdrop-blur-sm border border-[#c36934]/20 hover:border-[#c36934]/40 transition-colors rounded-sm">
            <button class="w-full text-left px-6 py-5 flex justify-between items-center focus:outline-none">
              <h4 class="text-xl font-bold text-white font-serif">I'm in my 60s or 70s and already have back pain. Can I still do this?</h4>
              <span class="faq-icon text-red-600 text-2xl font-bold leading-none">+</span>
            </button>
            <div class="faq-content hidden px-6 pb-6 pt-0">
              <div class="w-full h-px bg-[#c36934]/20 mb-4"></div>
              <p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">Yes, this system was engineered specifically for you. We do not ask you to rely on muscle. You will learn the 70° tool modification angles and the Spartan Kinetic-Pendulum Protocol to work the land using pure leverage and momentum. If you suffer from sciatica, arthritis, or lower back degradation, this is the safest way to maintain physical autonomy and bypass the devastating shear force placed on your L4-L5 vertebrae.</p>
            </div>
          </div>

          <!-- FAQ 3 -->
          <div class="faq-item bg-black/40 backdrop-blur-sm border border-[#c36934]/20 hover:border-[#c36934]/40 transition-colors rounded-sm">
            <button class="w-full text-left px-6 py-5 flex justify-between items-center focus:outline-none">
              <h4 class="text-xl font-bold text-white font-serif">Do I need special equipment for the recovery protocol?</h4>
              <span class="faq-icon text-red-600 text-2xl font-bold leading-none">+</span>
            </button>
            <div class="faq-content hidden px-6 pb-6 pt-0">
              <div class="w-full h-px bg-[#c36934]/20 mb-4"></div>
              <p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">Structural decompression does not require a gym membership, foam rollers, or expensive inversion tables. The manual teaches you how to utilize gravity-assisted passive postures using only a firm floor, a standard chair, or a sturdy fence post to create a micro-vacuum effect and draw hydration back into your spinal discs.</p>
            </div>
          </div>

          <!-- FAQ 4 -->
          <div class="faq-item bg-black/40 backdrop-blur-sm border border-[#c36934]/20 hover:border-[#c36934]/40 transition-colors rounded-sm">
            <button class="w-full text-left px-6 py-5 flex justify-between items-center focus:outline-none">
              <h4 class="text-xl font-bold text-white font-serif">What format is the book in? How do I access it?</h4>
              <span class="faq-icon text-red-600 text-2xl font-bold leading-none">+</span>
            </button>
            <div class="faq-content hidden px-6 pb-6 pt-0">
              <div class="w-full h-px bg-[#c36934]/20 mb-4"></div>
              <p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">This is a digital field manual (PDF format). The moment your order is securely processed, you will receive an instant download link directly to your email. You can read it on your smartphone, tablet, computer, or print out the blueprints to take directly into the garage or out on the field.</p>
            </div>
          </div>

        </div>
      </div>
    </section>"""

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_faq_section + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("FAQ replaced successfully.")
else:
    print("Could not find FAQ section.")
