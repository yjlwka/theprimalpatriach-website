import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Meta Title
content = content.replace(
    '<title>The Sovereign Soil System | The Ground Remembers</title>',
    '<title>The Joint-Safe Homestead Mechanics | The Primal Patriarch</title>'
)

# 2. Hero Section
content = content.replace(
    'THE ANCESTRAL OFF-GRID BLUEPRINTS',
    'THE ANCESTRAL BIOMECHANICS BLUEPRINT'
)
content = content.replace(
    '<span class="text-white">Secure Your Food Supply.<br/>Protect Your </span><span class="text-red-600 drop-shadow-[0_0_15px_rgba(220,38,38,0.4)]">Joints.</span>',
    '<span class="text-white">Silence the Alarm.<br/>Protect Your </span><span class="text-red-600 drop-shadow-[0_0_15px_rgba(220,38,38,0.4)]">Joints.</span>'
)
content = content.replace(
    '"Deploy 19th-century mechanical leverage to grow and preserve your own food off-the-grid, regardless of your age. Get the complete structural blueprint below."',
    '"Deploy 19th-century mechanical leverage to eliminate lumbar pain and preserve your joints, regardless of your age. Get the complete structural blueprint below."'
)

# 3. Pricing Grid Bullets
content = content.replace(
    '<span>Authentic Alpine infrastructure independent of the grid</span>',
    '<span>Structural Decompression protocols to end the day without pain</span>'
)
content = content.replace(
    '<span>The $12 DIY mechanical lifts that replace $300 equipment</span>',
    '<span>The Spartan Kinetic-Pendulum Protocol to lift heavy loads</span>'
)

# 4. Rewrite "The Biological Crisis"
# Find the section and replace it entirely
crisis_start = content.find('<!-- The Biological Crisis (Gradient Depth) -->')
crisis_end = content.find('<!-- Reader Stories (Glassmorphism) -->')

new_crisis_section = """<!-- Spinal Debt Section (Gradient Depth) -->
    <section class="relative w-full py-24 bg-black/30 backdrop-blur-sm overflow-hidden">
      <div class="max-w-4xl mx-auto px-6 relative z-10">
        
        <div class="text-center mb-16">
          <p class="text-red-600 font-bold tracking-widest text-sm mb-4 font-sans uppercase">THE INVISIBLE COST OF MODERN TOOLS</p>
          <h2 class="text-4xl md:text-5xl font-bold text-white mb-6 font-serif leading-tight drop-shadow-md">You Are Accumulating <span class="text-red-600">Spinal Debt.</span></h2>
          <div class="w-24 h-1 bg-red-600 mx-auto rounded-full opacity-80"></div>
        </div>

        <div class="space-y-8 text-lg text-[#e3dfd8] font-sans leading-relaxed">
          <p>Every time you pick up a standard tool from Home Depot, you are borrowing against your future mobility. Modern commercial tools are manufactured for cheap shipping and generic shelf display, <strong class="text-[#c36934] font-bold">not for human biomechanics</strong>.</p>
          
          <div class="bg-[#080706]/40 border-l-4 border-red-600 p-8 my-10 shadow-inner rounded-r-sm relative overflow-hidden backdrop-blur-md">
            <p class="text-white italic text-xl font-serif">"The angle of a standard shovel handle forces a 45-degree lumbar hinge, placing up to <span class="text-red-500 font-bold">800 lbs of axial compression</span> on your L4-L5 vertebrae with every single scoop."</p>
          </div>

          <p>This is what we call <strong class="text-[#c36934] font-bold">Axial Compression</strong>. It doesn't break you immediately. It micro-fractures the cartilage and inflames the discs over thousands of repetitive, poorly-leveraged movements. By the time you feel the "twinge" in your lower back, the structural damage is already done.</p>

          <p>Our ancestors didn't have painkillers. They couldn't afford to lose a week of work to a blown out back. They survived by engineering kinetic leverage into everything they touched. It's time to stop fighting gravity and start using it.</p>
        </div>

      </div>
    </section>

    """

if crisis_start != -1 and crisis_end != -1:
    content = content[:crisis_start] + new_crisis_section + content[crisis_end:]

# 5. Testimonials
# Daniel K.
content = content.replace(
    'Within two months of applying the Amish techniques, I cut our grocery bill by 40%. The root cellar alone was worth ten times the price of the bundle.',
    'Within two hours of modifying my shovel handles exactly as the manual described, the difference was night and day. I finished a full day of digging with absolutely zero lumbar pain.'
)
# Martha Higgins
content = content.replace(
    'I was intimidated by off-grid preservation, but Volume II made it incredibly logical. The water-glassing method for eggs changed everything for us.',
    'I was intimidated by the physical demands of our property, but this biomechanics blueprint made it incredibly logical. I no longer rely on painkillers to sleep at night.'
)
# Arthur T.
content = content.replace(
    'As someone in my late 60s, I thought I was done with heavy lifting. The non-electric preservation blueprint and the damp-sand box allowed me to store our entire harvest effortlessly.',
    'As someone in my late 60s, I thought my back was permanently ruined. The 90/90 floor inversion postures erased the inflammation in my lower back within three nights.'
)

# 6. FAQ
# Question 1: Climate
content = content.replace(
    '<h4 class="text-xl font-bold text-white font-serif">Do these methods work in a hot/dry or freezing climate?</h4>',
    '<h4 class="text-xl font-bold text-white font-serif">Does biomechanical leverage work in any climate?</h4>'
)
content = content.replace(
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">Yes. Both Volume I and II are built on fundamental laws of thermodynamics. Whether you are dealing with Arizona heat or Canadian winters, the 1850 Maraîcher matrix and the Amish Root Cellar adapt to extreme temperature fluctuations by utilizing the earth\'s stable core temperature.</p>',
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">Yes. Gravity and human biomechanics function exactly the same everywhere. Whether you are in Arizona or Canada, leveraging kinetic energy instead of muscular force will immediately protect your joints.</p>'
)

# Question 2: Bills
content = content.replace(
    '<h4 class="text-xl font-bold text-white font-serif">How much money will I actually save?</h4>',
    '<h4 class="text-xl font-bold text-white font-serif">When will I see a return on this investment?</h4>'
)
content = content.replace(
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">Results vary, but applying just the water-retention grids from Volume I typically reduces irrigation costs by 60%. The Water Glassing protocol in Volume II replaces expensive refrigeration. Most readers recover the cost of the bundle within their first harvest.</p>',
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">You will see savings on medical bills, chiropractic visits, and painkillers from Day 1. By reducing lumbar compression by up to 80% using these tool modifications, the return on investment is immediate structural relief.</p>'
)

# Question 3: Apartment -> Tools
content = content.replace(
    '<h4 class="text-xl font-bold text-white font-serif">I live in an apartment. Is this for me?</h4>',
    '<h4 class="text-xl font-bold text-white font-serif">Do I need to buy expensive, special tools?</h4>'
)
content = content.replace(
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">While you won\'t be building a subterranean cellar in an apartment, the preservation protocols (fermentation, drying, curing) in Volume II are perfectly adaptable to small spaces. It\'s an excellent foundation for when you eventually secure land.</p>',
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">No. You simply need to modify the angles and leverage points of your standard, existing tools. The manual shows you exactly how to do this using basic items you likely already own.</p>'
)

# Question 4: Age
content = content.replace(
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">Absolutely. Volume III is specifically engineered around kinetic leverage. It requires zero brute strength. The entire system was documented from cultures where people worked the land well into their 80s without debilitating joint pain.</p>',
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">Absolutely. This blueprint is specifically engineered around kinetic leverage. It requires zero brute strength. The entire system was documented from cultures where people worked the land well into their 80s without debilitating joint pain.</p>'
)

# Question 5: Formats
content = content.replace(
    '<h4 class="text-xl font-bold text-white font-serif">Are the books physical or digital?</h4>',
    '<h4 class="text-xl font-bold text-white font-serif">Is the manual physical or digital?</h4>'
)
content = content.replace(
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">These are digital field manuals (PDF format). You will receive instant access immediately after checkout. This allows you to print the specific blueprints you need, load them onto your tablet, or keep them on your phone for reference in the field without worrying about destroying a physical book in the mud.</p>',
    '<p class="text-[#e3dfd8]/80 leading-relaxed font-sans mt-4 text-base">This is a digital field manual (PDF format). You will receive instant access immediately after checkout. This allows you to print the specific blueprints you need, load them onto your tablet, or keep them on your phone for reference in the field.</p>'
)

# 7. Footer
content = content.replace(
    'THE COMPLETE THREE-VOLUME Ancestral Library - 2026',
    'THE COMPLETE ANCESTRAL BIOMECHANICS BLUEPRINT - 2026'
)

# 8. Main JS Updates (Toast logic is in main.js or index.html script tag)
# The user said the Toast logic is in Javascript. In this site, it's inside <script> tag in index.html.
content = content.replace(
    '{ name: "Barbara", state: "Albuquerque, NM", item: "The Sovereign Bundle" }',
    '{ name: "Barbara", state: "Albuquerque, NM", item: "The Joint-Safe Homestead Mechanics eBook" }'
)
content = content.replace(
    '{ name: "Robert", state: "Montana", item: "The Sovereign Bundle" }',
    '{ name: "Robert", state: "Montana", item: "The Joint-Safe Homestead Mechanics eBook" }'
)
content = content.replace(
    '{ name: "James", state: "Ohio", item: "The Maraîcher Blueprint" }',
    '{ name: "James", state: "Ohio", item: "The Joint-Safe Homestead Mechanics eBook" }'
)
content = content.replace(
    '{ name: "Michael", state: "Texas", item: "The Sovereign Bundle" }',
    '{ name: "Michael", state: "Texas", item: "The Joint-Safe Homestead Mechanics eBook" }'
)
content = content.replace(
    '{ name: "William", state: "Florida", item: "Joint-Safe Mechanics" }',
    '{ name: "William", state: "Florida", item: "The Joint-Safe Homestead Mechanics eBook" }'
)
content = content.replace(
    '{ name: "Thomas", state: "Idaho", item: "The Sovereign Bundle" }',
    '{ name: "Thomas", state: "Idaho", item: "The Joint-Safe Homestead Mechanics eBook" }'
)
content = content.replace(
    '{ name: "David", state: "Wyoming", item: "The Sovereign Bundle" }',
    '{ name: "David", state: "Wyoming", item: "The Joint-Safe Homestead Mechanics eBook" }'
)

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Copy and logic updated successfully.")
