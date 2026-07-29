import os

# Regional SILO Mapping
REGIONAL_SILO = {
    "jakarta": "southeast-asia", "bangkok": "southeast-asia", "manila": "southeast-asia",
    "ho-chi-minh": "southeast-asia", "kuala-lumpur": "southeast-asia", "singapore": "southeast-asia",
    "tokyo": "east-asia", "seoul": "east-asia", "taipei": "east-asia", "hong-kong": "east-asia",
    "dubai": "middle-east", "istanbul": "middle-east", "riyadh": "middle-east",
    "london": "uk-eastern-europe", "paris": "western-europe", "barcelona": "western-europe",
    "lisbon": "western-europe", "berlin": "western-europe", "new-york": "north-america",
    "cape-town": "africa", "buenos-aires": "south-america"
}

# Sample City Data Array
CITIES = [
    {
        "slug": "jakarta-interview.html", "city": "Jakarta", "flag": "🇮🇩", 
        "region": "Southeast Asia", "influencer": "Nadia Travels",
        "superfood_topic": "L-Theanine in Ceremonial Matcha",
        "superfood_text": "Matcha contains L-theanine, promoting alert relaxation and sustained focus without cortisol spikes.",
        "debate": "Is staying inside high-end expat enclaves like Senopati isolating travelers from local culture?"
    },
    {
        "slug": "bangkok-interview.html", "city": "Bangkok", "flag": "🇹🇭", 
        "region": "Southeast Asia", "influencer": "Bangkok Bites",
        "superfood_topic": "Acai & Goji Berry ORAC Antioxidants",
        "superfood_text": "Acai and Goji berries provide over 100,000 ORAC units per 100g to reduce screen fatigue and travel oxidative stress.",
        "debate": "Are digital nomad visas causing housing inflation in Sukhumvit?"
    }
]

def build_city_post(c):
    region_slug = REGIONAL_SILO.get(c['slug'].replace('-interview.html', ''), 'southeast-asia')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🍵 {c['city']} Remote Work, {c['superfood_topic']} & Nomad Guide</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-stone-50 text-stone-800 font-sans antialiased">
  <header class="bg-emerald-900 text-white p-4 text-xs">
    <div class="max-w-4xl mx-auto flex justify-between">
      <a href="index2.html" class="font-bold text-sm">🍵 MATCHA MAYA</a>
      <a href="regions/{region_slug}.html" class="underline text-emerald-300">Parent Regional SILO Hub</a>
    </div>
  </header>
  <main class="max-w-4xl mx-auto px-4 py-8">
    <article class="bg-white p-8 rounded-2xl border border-stone-200 shadow-sm">
      <span class="text-xs font-bold text-emerald-700 uppercase">{c['region']} • Podcast & Guide</span>
      <h1 class="text-3xl font-extrabold mt-1">{c['flag']} {c['city']} Remote Work & Superfood Guide</h1>
      <p class="text-xs text-stone-500 mt-1">Hosted with <strong>{c['influencer']}</strong></p>
      
      <div class="my-6 bg-emerald-50 border-l-4 border-emerald-600 p-4 rounded-r-xl">
        <h3 class="font-bold text-emerald-950 text-sm">🌿 {c['superfood_topic']}</h3>
        <p class="text-emerald-800 text-xs mt-1">{c['superfood_text']}</p>
      </div>

      <div class="bg-stone-900 text-white p-6 rounded-2xl mt-8">
        <h3 class="font-bold text-emerald-400 text-sm">🗣️ The Nomad Debate</h3>
        <p class="text-xs text-stone-300 mt-1">{c['debate']}</p>
      </div>
    </article>
  </main>
</body>
</html>"""

# Execute Generation Loop
for city in CITIES:
    filename = city['slug']
    content = build_city_post(city)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated: {filename}")

print("\n🎉 Batch process complete!")