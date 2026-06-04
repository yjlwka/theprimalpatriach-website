import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Hero Section
hero_old = """        <!-- Pre-title -->
        <p class="text-center text-[#c36934] tracking-[0.3em] text-xs font-bold mb-8 uppercase font-sans drop-shadow-sm">THE COMPLETE SOVEREIGN SOIL SYSTEM</p>
        
        <!-- Hero Title -->
        <h1 class="text-5xl md:text-6xl lg:text-7xl font-bold mb-8 leading-tight font-serif drop-shadow-xl">
          <span class="text-white">Reclaim Your Autonomy<br/>Down To The </span><span class="text-red-600 drop-shadow-[0_0_15px_rgba(220,38,38,0.4)]">Root.</span>
        </h1>
        
        <p class="text-xl md:text-2xl max-w-3xl mx-auto mb-12 leading-relaxed text-[#e3dfd8]/90 italic font-serif">
          "Over 150 years of documented field research from the Seine Basin and early American pioneers. Choose your edition below."
        </p>"""

hero_new = """        <!-- Pre-title -->
        <p class="text-center text-[#c36934] tracking-[0.3em] text-xs font-bold mb-8 uppercase font-sans drop-shadow-sm">THE ANCESTRAL OFF-GRID BLUEPRINTS</p>
        
        <!-- Hero Title -->
        <h1 class="text-5xl md:text-6xl lg:text-7xl font-bold mb-8 leading-tight font-serif drop-shadow-xl">
          <span class="text-white">Secure Your Food Supply.<br/>Protect Your </span><span class="text-red-600 drop-shadow-[0_0_15px_rgba(220,38,38,0.4)]">Joints.</span>
        </h1>
        
        <p class="text-xl md:text-2xl max-w-3xl mx-auto mb-12 leading-relaxed text-[#e3dfd8]/90 italic font-serif">
          "Deploy 19th-century mechanical leverage to grow and preserve your own food off-the-grid, regardless of your age. Choose your structural blueprint below."
        </p>"""

content = content.replace(hero_old, hero_new)

# FAQ Replacements

faq1_old = """<p>Most methods work universally. A few (like the earth tunnel) are climate-dependent — they perform exceptionally in hot-dry and temperate climates, and need adaptation in hot-humid or high-water-table areas. <strong class="text-[#d88c51] font-bold drop-shadow-sm">Volume III includes specific adaptations for 5 climate zones</strong> (hot-dry, hot-humid, temperate, cold, and apartment) so you know exactly which methods apply to your situation and which to skip.</p>"""
faq1_new = """<p>Yes. The protocols in Volume I and II are not based on weather; they are based on thermodynamics and structural biology. The 1850 Maraîcher matrix utilizes specific Carbon-to-Nitrogen ratios that generate their own sub-surface heat, while the Amish Root Cellar blueprints rely on underground temperature stabilization, which remains a constant 50-55°F (10-13°C) regardless of whether you live in Texas or Maine.</p>"""

faq2_old = """<p>The product swaps in Week 2 (soap recipe, DIY pest control, water heater adjustment) show up on your <strong class="text-[#d88c51] font-bold drop-shadow-sm">next billing cycle — typically 28-35 days</strong>. The bigger savings from the radiant barrier and earth tunnel appear within 60 days. By the end of the 90-day program, most readers see <strong class="text-[#d88c51] font-bold drop-shadow-sm">30-50% reduction in cooling-related bills</strong> and complete elimination of recurring pest control and cleaning product costs.</p>"""
faq2_new = """<p>You will see multiple phases of savings.<br/>
<strong class="text-[#d88c51] font-bold drop-shadow-sm">Day 1:</strong> By applying the Class-1 leverage modifications in Volume III, you instantly reduce lumbar compression by up to 80%, bypassing the need for physical therapy or joint pain medication.<br/>
<strong class="text-[#d88c51] font-bold drop-shadow-sm">Day 30:</strong> The water-retention grids will reflect a drop in your municipal water bill, while the Water Glassing protocol allows you to bypass grocery store egg inflation immediately.<br/>
<strong class="text-[#d88c51] font-bold drop-shadow-sm">Day 90:</strong> Once the intensive soil matrix matures, readers report a 40% to 60% reduction in their organic grocery costs.</p>"""

faq3_old = """<p>Volume I covers scalable indoor methods specifically tailored for small spaces. The fermentation protocols, water glassing, and DIY soap recipes require zero outdoor space. The miniature root cellars can be adapted for apartment balconies or closets. While you won't be digging earth tunnels, you'll still save significantly on food and household products.</p>"""
faq3_new = """<p>The Volume II Preservation Blueprint (fermentation, water glassing, and indoor thermal stabilization) requires zero land and can be executed in any apartment kitchen. For Volume I, the French intensive method was historically designed for hyper-urban environments. You only need a 40-square-foot patch of dirt or a raised bed to execute the primary matrix.</p>"""

faq4_old = """<p>Absolutely. Volume III is exclusively dedicated to joint-safe biomechanics. We detail the exact 70° tool modifications designed to bypass sciatica and lumbar strain, ensuring you can implement these methods relying entirely on kinetic leverage rather than physical strength. Many of our most successful readers are in their late 70s.</p>"""
faq4_new = """<p>This system was engineered specifically for you. Volume III is exclusively dedicated to senior-friendly biomechanics. We do not ask you to rely on muscle. You will learn the 70° tool modification angles and Spartan kinetic-momentum lifting techniques to work the soil using pure leverage. If you suffer from sciatica, arthritis, or lower back degradation, this is the safest way to maintain physical autonomy.</p>"""

faq5_old = """<p>These are high-resolution digital editions (PDF format). You can download them instantly after checkout to your computer, tablet, or smartphone. You can also print them out if you prefer a physical copy for your workshop or greenhouse.</p>"""
faq5_new = """<p>These are digital field manuals (PDF format). The moment your order is securely processed, you will receive an instant download link directly to your email. You can read them on your smartphone, tablet, computer, or print out the blueprints to take directly into the field.</p>"""

content = content.replace(faq1_old, faq1_new)
content = content.replace(faq2_old, faq2_new)
content = content.replace(faq3_old, faq3_new)
content = content.replace(faq4_old, faq4_new)
content = content.replace(faq5_old, faq5_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated texts successfully.")
