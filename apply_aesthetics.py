import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add the global background element right after <body>
bg_element = """<body class="text-[#e3dfd8] font-serif antialiased text-[18px] selection:bg-[#c36934] selection:text-[#080706] min-h-screen relative">
  <!-- Cinematic Background (Glow + Noise) -->
  <div class="fixed inset-0 z-[-1] pointer-events-none bg-[#0a0503]">
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_20%_0%,rgba(195,105,52,0.18),transparent_50%),radial-gradient(circle_at_80%_80%,rgba(220,38,38,0.12),transparent_50%)]"></div>
    <div class="absolute inset-0 opacity-[0.05]" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=\\'0 0 200 200\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cfilter id=\\'noiseFilter\\'%3E%3CfeTurbulence type=\\'fractalNoise\\' baseFrequency=\\'0.85\\' numOctaves=\\'3\\' stitchTiles=\\'stitch\\'/%3E%3C/filter%3E%3Crect width=\\'100%25\\' height=\\'100%25\\' filter=\\'url(%23noiseFilter)\\'/%3E%3C/svg%3E');"></div>
  </div>
"""

content = re.sub(r'<body class="[^"]*">', bg_element, content)

# 2. Make sections transparent or glassmorphic
# Hero Section
content = content.replace('bg-gradient-to-b from-[#24130d] to-[#080706]', 'bg-transparent')
# Pricing Section
content = content.replace('bg-[#080706] shadow-[inset_0_10px_50px_rgba(0,0,0,0.8)]', 'bg-black/20 backdrop-blur-sm')
# The Biological Crisis
content = content.replace('bg-gradient-to-b from-[#1a0f0a] to-[#080706]', 'bg-black/30 backdrop-blur-sm')
# Testimonial Section
content = content.replace('bg-[#1e1b18] w-full py-24 shadow-[inset_0_10px_30px_rgba(0,0,0,0.6)]', 'bg-[#1e1b18]/40 w-full py-24 backdrop-blur-md')
# FAQ Section
content = content.replace('bg-[#110d0b] w-full py-24 shadow-[inset_0_10px_30px_rgba(0,0,0,0.6)]', 'bg-[#110d0b]/40 w-full py-24 backdrop-blur-md')
# Footer
content = content.replace('<footer class="bg-[#0a0705]', '<footer class="bg-black/40 backdrop-blur-lg')

# 3. Upgrade Pricing Cards to Glassmorphism
# Card 1 and 2
content = content.replace(
    'class="bg-[#080706] border border-[#c36934]/30 p-8 shadow-2xl flex flex-col group relative overflow-hidden transition-all duration-300 hover:scale-[1.02] rounded-sm"',
    'class="bg-[#080706]/40 backdrop-blur-md border border-[#c36934]/30 p-8 shadow-2xl flex flex-col group relative overflow-hidden transition-all duration-300 hover:scale-[1.02] hover:shadow-[0_0_30px_rgba(195,105,52,0.15)] rounded-sm"'
)
# Card 3 (Bundle)
content = content.replace(
    'class="bg-[#16120f] border-2 border-[#d88c51] p-1 shadow-2xl relative transition-all duration-300 hover:scale-[1.02] rounded-sm"',
    'class="bg-[#1a0d07]/60 backdrop-blur-lg border-2 border-[#d88c51] p-1 shadow-[0_0_40px_rgba(216,140,81,0.2)] relative transition-all duration-300 hover:scale-[1.02] hover:shadow-[0_0_50px_rgba(216,140,81,0.3)] rounded-sm"'
)
# Inner div of Card 3
content = content.replace(
    '<div class="border border-[#c36934]/20 p-8 flex flex-col h-full relative z-10 bg-[#080706]">',
    '<div class="border border-[#c36934]/20 p-8 flex flex-col h-full relative z-10 bg-[#080706]/30 backdrop-blur-md">'
)
# Bundle exclusive bonuses box
content = content.replace(
    '<div class="border border-[#c36934]/30 p-6 mb-8 rounded-md bg-[#16120f] shadow-inner">',
    '<div class="border border-[#c36934]/40 p-6 mb-8 rounded-md bg-[#c36934]/5 shadow-inner">'
)

# 4. Enhance Testimonial cards
content = content.replace(
    '<div class="bg-[#080706] border border-[#c36934]/30 p-8 shadow-2xl flex flex-col justify-between rounded-sm">',
    '<div class="bg-black/40 backdrop-blur-md border border-[#c36934]/20 p-8 shadow-2xl flex flex-col justify-between rounded-sm hover:border-[#c36934]/40 transition-colors">'
)

# 5. Enhance FAQ items
content = content.replace(
    '<div class="faq-item bg-[#1a1310] border border-[#c36934]/30 rounded-sm">',
    '<div class="faq-item bg-black/40 backdrop-blur-sm border border-[#c36934]/20 hover:border-[#c36934]/40 transition-colors rounded-sm">'
)

# 6. Enhance the Timer
content = content.replace(
    '<div class="w-full bg-[#2b0909] border-y border-red-600 shadow-[inset_0_0_50px_rgba(0,0,0,0.5),0_0_30px_rgba(220,38,38,0.2)] text-center py-10 z-10 relative">',
    '<div class="w-full bg-[#2b0909]/80 backdrop-blur-md border-y border-red-600/80 shadow-[inset_0_0_50px_rgba(0,0,0,0.5),0_0_40px_rgba(220,38,38,0.3)] text-center py-10 z-10 relative">'
)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Aesthetics applied successfully.")
