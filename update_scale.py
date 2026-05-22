import re

with open('/Users/davidmartin/Library/Mobile Documents/com~apple~CloudDocs/Fisio/DMOVEZONE/DMoveZone-LANDING/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the HTML section
html_section = """    <!-- Continuous Performance Scale Section -->
    <section id="app" class="py-24 relative bg-slate-950">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-16">
                <h2 class="font-outfit text-4xl md:text-5xl lg:text-6xl font-extrabold text-indigo-400 uppercase tracking-tight mb-6" data-t="scale_title">THE CONTINUOUS PERFORMANCE SCALE</h2>
                <div class="w-24 h-1.5 bg-indigo-500 rounded-full mb-8"></div>
                <p class="text-xl text-slate-300 max-w-4xl font-medium leading-relaxed" data-t="scale_subtitle">La salud no es un estado binario, es un espectro. La medicina tradicional entra en el nivel 0. DMove te mantiene en el 10.</p>
            </div>
            
            <!-- Spectrum Bar -->
            <div class="flex w-full h-14 md:h-16 rounded-full overflow-hidden font-bold text-slate-900 text-[10px] md:text-sm tracking-widest mb-12 shadow-2xl">
                <div class="w-[30%] bg-red-500 flex items-center justify-center border-r-2 border-slate-950 text-white" data-t="scale_bar_1">0 - 3: MEDICAL</div>
                <div class="w-[30%] bg-amber-400 flex items-center justify-center border-r-2 border-slate-950" data-t="scale_bar_2">3 - 6: RISK</div>
                <div class="w-[20%] bg-lime-400 flex items-center justify-center border-r-2 border-slate-950" data-t="scale_bar_3">6 - 8: BUFFER</div>
                <div class="w-[20%] bg-emerald-500 flex items-center justify-center text-white" data-t="scale_bar_4">8 - 10: PEAK</div>
            </div>

            <!-- Cards Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Peak Card -->
                <div class="glass-card p-8 rounded-3xl border border-emerald-500/20 bg-gradient-to-b from-emerald-500/10 to-transparent flex flex-col transition-all hover:border-emerald-500/40">
                    <div class="text-5xl font-black text-emerald-400 mb-4 font-outfit">10</div>
                    <h3 class="text-white font-bold text-xl mb-2 uppercase tracking-wide" data-t="scale_card_4_title">Peak</h3>
                    <p class="text-slate-400 text-sm mb-4 font-medium" data-t="scale_card_4_subtitle">Poder Óptimo</p>
                    <p class="text-xs text-slate-300 leading-relaxed" data-t="scale_card_4_desc">Optimización máxima. DMove y sus especialistas te guían para competir a tu límite de forma totalmente segura.</p>
                </div>
                
                <!-- Buffer Card -->
                <div class="glass-card p-8 rounded-3xl border border-lime-400/20 bg-gradient-to-b from-lime-400/10 to-transparent flex flex-col transition-all hover:border-lime-400/40">
                    <div class="text-5xl font-black text-lime-400 mb-4 font-outfit">7</div>
                    <h3 class="text-white font-bold text-xl mb-2 uppercase tracking-wide" data-t="scale_card_3_title">Buffer</h3>
                    <p class="text-slate-400 text-sm mb-4 font-medium" data-t="scale_card_3_subtitle">Salud Funcional</p>
                    <p class="text-xs text-slate-300 leading-relaxed" data-t="scale_card_3_desc">Construimos un colchón físico. Tu cuerpo es capaz de absorber impactos y malos gestos sin romperse.</p>
                </div>
                
                <!-- Risk Card -->
                <div class="glass-card p-8 rounded-3xl border border-amber-400/20 bg-gradient-to-b from-amber-400/10 to-transparent flex flex-col transition-all hover:border-amber-400/40">
                    <div class="text-5xl font-black text-amber-400 mb-4 font-outfit">4</div>
                    <h3 class="text-white font-bold text-xl mb-2 uppercase tracking-wide" data-t="scale_card_2_title">Risk</h3>
                    <p class="text-slate-400 text-sm mb-4 font-medium" data-t="scale_card_2_subtitle">Alerta / Riesgo</p>
                    <p class="text-xs text-slate-300 leading-relaxed" data-t="scale_card_2_desc">DMove detecta fatiga, sobrecargas y asimetrías mediante datos antes de que se conviertan en dolor o rotura.</p>
                </div>
                
                <!-- Medical Card -->
                <div class="glass-card p-8 rounded-3xl border border-red-500/20 bg-gradient-to-b from-red-500/10 to-transparent flex flex-col transition-all hover:border-red-500/40">
                    <div class="text-5xl font-black text-red-500 mb-4 font-outfit">0</div>
                    <h3 class="text-white font-bold text-xl mb-2 uppercase tracking-wide" data-t="scale_card_1_title">Medical</h3>
                    <p class="text-slate-400 text-sm mb-4 font-medium" data-t="scale_card_1_subtitle">Lesión</p>
                    <p class="text-xs text-slate-300 leading-relaxed" data-t="scale_card_1_desc">El sistema médico tradicional solo actúa aquí. Pagan la factura de hospital o la cirugía cuando el daño ya está hecho.</p>
                </div>
            </div>
            
            <div class="mt-16 text-center max-w-4xl mx-auto p-8 rounded-3xl bg-indigo-900/20 border border-indigo-500/20 shadow-2xl">
                <p class="text-indigo-200 text-lg md:text-xl font-medium leading-relaxed" data-t="scale_footer">
                    DMoveZone es el único ecosistema tecnológico y humano diseñado para protegerte y mejorarte en las fases Risk, Buffer y Peak. Actuamos en la sombra para que nunca tengas que visitar la fase Medical.
                </p>
            </div>
        </div>
    </section>"""

content = re.sub(r'<!-- The App Section -->.*?</section>', html_section, content, flags=re.DOTALL)

# 2. Add EN strings
en_strings = """
                // Continuous Performance Scale
                scale_title: "THE CONTINUOUS PERFORMANCE SCALE",
                scale_subtitle: "Health is not a binary state. It is a spectrum. Traditional medicine enters at 0. DMove keeps you at 10.",
                scale_bar_1: "0 - 3: MEDICAL",
                scale_bar_2: "3 - 6: RISK",
                scale_bar_3: "6 - 8: BUFFER",
                scale_bar_4: "8 - 10: PEAK",
                scale_card_4_title: "Peak",
                scale_card_4_subtitle: "Optimal Power",
                scale_card_4_desc: "Maximum optimization. DMove and its specialists guide you to safely compete at your limit.",
                scale_card_3_title: "Buffer",
                scale_card_3_subtitle: "Functional Health",
                scale_card_3_desc: "We build a physical cushion. Your body can absorb impacts and bad movements without breaking.",
                scale_card_2_title: "Risk",
                scale_card_2_subtitle: "Warning / Risk",
                scale_card_2_desc: "DMove uses data to detect fatigue, overload, and asymmetries before they become pain or injury.",
                scale_card_1_title: "Medical",
                scale_card_1_subtitle: "Injury",
                scale_card_1_desc: "The traditional medical system only acts here. They pay the hospital bill when the damage is already done.",
                scale_footer: "DMoveZone is the only technological and human ecosystem designed to protect and improve you in the Risk, Buffer, and Peak phases. We operate in the background so you never have to visit the Medical phase.",
"""
content = re.sub(r'(hero_cta_individual: "ACTIVATE YOUR PHYSICAL PASSPORT",)', r'\1\n' + en_strings, content)

# 3. Add ES strings
es_strings = """
                // Continuous Performance Scale
                scale_title: "THE CONTINUOUS PERFORMANCE SCALE",
                scale_subtitle: "La salud no es un estado binario, es un espectro. La medicina tradicional entra en el nivel 0. DMove te mantiene en el 10.",
                scale_bar_1: "0 - 3: MEDICAL",
                scale_bar_2: "3 - 6: RISK",
                scale_bar_3: "6 - 8: BUFFER",
                scale_bar_4: "8 - 10: PEAK",
                scale_card_4_title: "Peak",
                scale_card_4_subtitle: "Poder Óptimo",
                scale_card_4_desc: "Optimización máxima. DMove y sus especialistas te guían para competir a tu límite de forma totalmente segura.",
                scale_card_3_title: "Buffer",
                scale_card_3_subtitle: "Salud Funcional",
                scale_card_3_desc: "Construimos un colchón físico. Tu cuerpo es capaz de absorber impactos y malos gestos sin romperse.",
                scale_card_2_title: "Risk",
                scale_card_2_subtitle: "Alerta / Riesgo",
                scale_card_2_desc: "DMove detecta fatiga, sobrecargas y asimetrías mediante datos antes de que se conviertan en dolor o rotura.",
                scale_card_1_title: "Medical",
                scale_card_1_subtitle: "Lesión",
                scale_card_1_desc: "El sistema médico tradicional solo actúa aquí. Pagan la factura de hospital o la cirugía cuando el daño ya está hecho.",
                scale_footer: "DMoveZone es el único ecosistema tecnológico y humano diseñado para protegerte y mejorarte en las fases Risk, Buffer y Peak. Actuamos en la sombra para que nunca tengas que visitar la fase Medical.",
"""
content = re.sub(r'(hero_cta_individual: "ACTIVA TU PASAPORTE FÍSICO",)', r'\1\n' + es_strings, content)

# 4. Add FR strings
fr_strings = """
                // Continuous Performance Scale
                scale_title: "L'ÉCHELLE CONTINUE DE PERFORMANCE",
                scale_subtitle: "La santé n'est pas binaire, c'est un spectre. La médecine traditionnelle intervient à 0. DMove vous maintient à 10.",
                scale_bar_1: "0 - 3: MEDICAL",
                scale_bar_2: "3 - 6: RISK",
                scale_bar_3: "6 - 8: BUFFER",
                scale_bar_4: "8 - 10: PEAK",
                scale_card_4_title: "Peak",
                scale_card_4_subtitle: "Puissance Optimale",
                scale_card_4_desc: "Optimisation maximale. DMove et ses spécialistes vous guident pour concourir à votre limite en toute sécurité.",
                scale_card_3_title: "Buffer",
                scale_card_3_subtitle: "Santé Fonctionnelle",
                scale_card_3_desc: "Nous construisons un coussin physique. Votre corps peut absorber les impacts et les mauvais mouvements sans se briser.",
                scale_card_2_title: "Risk",
                scale_card_2_subtitle: "Alerte / Risque",
                scale_card_2_desc: "DMove utilise les données pour détecter la fatigue, les surcharges et les asymétries avant qu'elles ne deviennent des blessures.",
                scale_card_1_title: "Medical",
                scale_card_1_subtitle: "Blessure",
                scale_card_1_desc: "Le système médical traditionnel n'intervient qu'ici. Ils paient la facture de l'hôpital une fois que les dégâts sont déjà faits.",
                scale_footer: "DMoveZone est le seul écosystème technologique et humain conçu pour vous protéger et vous améliorer dans les phases Risk, Buffer et Peak. Nous agissons dans l'ombre pour que vous n'ayez jamais à visiter la phase Medical.",
"""
content = re.sub(r'(hero_cta_individual: "ACTIVEZ VOTRE PASSEPORT PHYSIQUE",)', r'\1\n' + fr_strings, content)


with open('/Users/davidmartin/Library/Mobile Documents/com~apple~CloudDocs/Fisio/DMOVEZONE/DMoveZone-LANDING/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

