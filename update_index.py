import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove sticky timer
content = re.sub(r'  <!-- Countdown Timer Bottom Sticky Bar.*?\</div>\n', '', content, flags=re.DOTALL)

# 2. Insert timer after Pricing (around line 245-246)
new_timer = """    <!-- Inline Countdown Timer (Placed statically) -->
    <div class="w-full bg-[#2b0909] border-y border-red-600 shadow-[inset_0_0_50px_rgba(0,0,0,0.5),0_0_30px_rgba(220,38,38,0.2)] text-center py-10 z-10 relative">
      <div class="text-red-200 font-sans tracking-widest font-bold text-sm md:text-base uppercase mb-2 drop-shadow-sm flex items-center justify-center gap-2">
        <span class="text-[#d88c51]">⚠️</span> THIS PRICE EXPIRES IN
      </div>
      <div id="countdown-timer" class="text-[#d88c51] font-serif text-4xl md:text-5xl font-bold tracking-wider drop-shadow-[0_2px_10px_rgba(216,140,81,0.2)]">
        23 : 40 : 54
      </div>
    </div>
"""

content = content.replace('    <!-- Ligne Cuivrée -->\n    <div class="w-full border-b border-[#c36934]/40"></div>\n\n    <!-- The Biological Crisis',
                          new_timer + '\n    <!-- The Biological Crisis')

# 3. Extract FAQ section
faq_match = re.search(r'(    <!-- FAQ Section -->.*?</section>\n)', content, flags=re.DOTALL)
faq_section = faq_match.group(1) if faq_match else ""

# Remove FAQ section and its preceding line from original location
content = re.sub(r'    <!-- FAQ Section -->.*?</section>\n', '', content, flags=re.DOTALL)
content = re.sub(r'(    <!-- Ligne Cuivrée -->\n    <div class="w-full border-b border-\[\#c36934\]/40\"></div>\n\n){2,}', 
                 r'    <!-- Ligne Cuivrée -->\n    <div class="w-full border-b border-[#c36934]/40"></div>\n\n', content)

# 4. Insert FAQ and Footer after Testimonials
footer_section = """
    <!-- Ligne Cuivrée -->
    <div class="w-full border-b border-[#c36934]/40"></div>

""" + faq_section + """
    <!-- Footer -->
    <footer class="bg-[#0a0705] w-full py-16 border-t border-[#c36934]/20 text-center">
      <div class="max-w-4xl mx-auto px-6">
        <h2 class="text-2xl md:text-3xl font-serif text-[#d88c51] tracking-[0.2em] uppercase mb-4 drop-shadow-sm">THE PRIMAL PATRIARCH</h2>
        <p class="text-[#c36934] font-sans text-sm tracking-widest mb-8">THE COMPLETE THREE-VOLUME Ancestral Library - 2026</p>
        <p class="text-gray-500 font-sans text-xs leading-relaxed max-w-2xl mx-auto mb-6">
          Educational content based on documented traditional methods. Individual results vary based on climate, home characteristics, and implementation. Not financial or professional advice.
        </p>
        <p class="text-gray-400 font-sans text-sm">
          Questions? <a href="#" class="text-[#d88c51] hover:text-[#e49b63] transition-colors font-bold">contact us</a>
        </p>
      </div>
    </footer>
"""

content = content.replace('    </section>\n\n  </main>', '    </section>\n' + footer_section + '\n  </main>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("HTML updated successfully.")
