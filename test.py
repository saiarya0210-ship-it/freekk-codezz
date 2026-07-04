import streamlit as st
import time

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="❤️ For Sreya ❤️",
    page_icon="💖",
    layout="centered",
)

# ─── Inject Custom CSS + Animations ────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Nunito:wght@400;600;700&display=swap');

/* ── Full-page gradient background ── */
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a0010 0%, #3d0020 30%, #6b0035 60%, #3d0020 100%) !important;
    min-height: 100vh;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

/* ── Floating hearts canvas ── */
#heart-canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.heart-particle {
    position: fixed;
    bottom: -60px;
    font-size: 24px;
    animation: floatUp linear infinite;
    opacity: 0;
    pointer-events: none;
    z-index: 1;
    user-select: none;
}

@keyframes floatUp {
    0%   { transform: translateY(0) rotate(0deg) scale(0.5); opacity: 0; }
    10%  { opacity: 1; }
    90%  { opacity: 0.8; }
    100% { transform: translateY(-110vh) rotate(360deg) scale(1.2); opacity: 0; }
}

/* ── Sparkle stars ── */
.star-particle {
    position: fixed;
    font-size: 14px;
    animation: twinkle ease-in-out infinite;
    pointer-events: none;
    z-index: 1;
    color: #ffd700;
}
@keyframes twinkle {
    0%, 100% { opacity: 0.1; transform: scale(0.8); }
    50%       { opacity: 1;   transform: scale(1.3); }
}

/* ── Main card ── */
.main-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 120, 150, 0.3);
    border-radius: 32px;
    padding: 50px 40px 40px;
    text-align: center;
    box-shadow: 0 0 60px rgba(255, 60, 100, 0.35),
                0 0 120px rgba(255, 60, 100, 0.15),
                inset 0 1px 0 rgba(255,255,255,0.15);
    position: relative;
    z-index: 10;
    animation: cardPulse 3s ease-in-out infinite;
}
@keyframes cardPulse {
    0%, 100% { box-shadow: 0 0 60px rgba(255,60,100,0.35), 0 0 120px rgba(255,60,100,0.15); }
    50%       { box-shadow: 0 0 80px rgba(255,60,100,0.55), 0 0 160px rgba(255,60,100,0.25); }
}

/* ── Big pulsing heart ── */
.big-heart {
    font-size: 100px;
    display: inline-block;
    animation: heartbeat 1.2s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(255,60,100,0.8));
    line-height: 1;
}
@keyframes heartbeat {
    0%   { transform: scale(1); }
    14%  { transform: scale(1.18); }
    28%  { transform: scale(1); }
    42%  { transform: scale(1.12); }
    70%  { transform: scale(1); }
    100% { transform: scale(1); }
}

/* ── Title ── */
.title-text {
    font-family: 'Pacifico', cursive;
    font-size: 2.8rem;
    background: linear-gradient(135deg, #ff9eb5, #ff4d6d, #ffb3c1, #ff758c);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s ease infinite;
    margin: 20px 0 10px;
    line-height: 1.2;
}
@keyframes shimmer {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── Sub text ── */
.sub-text {
    font-family: 'Nunito', sans-serif;
    font-size: 1.25rem;
    color: rgba(255, 220, 230, 0.9);
    margin-bottom: 6px;
}
.from-text {
    font-family: 'Nunito', sans-serif;
    font-size: 1rem;
    color: rgba(255, 180, 200, 0.7);
    font-style: italic;
    margin-bottom: 36px;
}

/* ── Buttons ── */
div[data-testid="column"] button {
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    border-radius: 50px !important;
    padding: 16px 40px !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    letter-spacing: 0.5px !important;
}

/* YES button */
div[data-testid="column"]:first-child button {
    background: linear-gradient(135deg, #ff4d6d, #c9184a) !important;
    color: white !important;
    box-shadow: 0 8px 30px rgba(255, 77, 109, 0.6) !important;
}
div[data-testid="column"]:first-child button:hover {
    transform: translateY(-4px) scale(1.05) !important;
    box-shadow: 0 14px 40px rgba(255, 77, 109, 0.8) !important;
}

/* NO button */
div[data-testid="column"]:last-child button {
    background: rgba(255,255,255,0.08) !important;
    color: rgba(255,180,200,0.8) !important;
    border: 1px solid rgba(255,120,150,0.3) !important;
    box-shadow: none !important;
    font-size: 0.85rem !important;
}
div[data-testid="column"]:last-child button:hover {
    transform: translateY(-2px) !important;
    background: rgba(255,255,255,0.12) !important;
}

/* ── Response banners ── */
.yes-response {
    background: linear-gradient(135deg, rgba(255,77,109,0.25), rgba(201,24,74,0.15));
    border: 1px solid rgba(255,77,109,0.5);
    border-radius: 20px;
    padding: 28px;
    margin-top: 24px;
    animation: fadeInUp 0.6s ease forwards;
}
.no-response {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 20px;
    margin-top: 24px;
    animation: fadeInUp 0.6s ease forwards;
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
}
.yes-emoji { font-size: 60px; animation: bounce 0.8s ease infinite alternate; }
@keyframes bounce {
    from { transform: translateY(0); }
    to   { transform: translateY(-12px); }
}
.yes-title {
    font-family: 'Pacifico', cursive;
    font-size: 2rem;
    color: #ff758c;
    margin: 12px 0 8px;
}
.yes-msg {
    font-family: 'Nunito', sans-serif;
    font-size: 1.1rem;
    color: rgba(255,220,230,0.9);
    line-height: 1.7;
}
.no-msg {
    font-family: 'Nunito', sans-serif;
    font-size: 1rem;
    color: rgba(255,200,210,0.7);
}

/* ── Divider hearts ── */
.heart-divider {
    color: rgba(255,120,150,0.4);
    font-size: 1.2rem;
    letter-spacing: 8px;
    margin: 24px 0;
}

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
</style>

<!-- ── Floating Hearts + Stars JS ── -->
<div id="heart-canvas"></div>
<script>
(function() {
    const emojis = ["❤️","💕","💖","💗","💓","💝","💞","🌹","✨","💫","🌸","💐"];
    const stars  = ["✨","⭐","🌟","💫"];
    const canvas = document.getElementById('heart-canvas');

    // spawn floating hearts
    function spawnHeart() {
        const el = document.createElement('span');
        el.classList.add('heart-particle');
        el.innerText = emojis[Math.floor(Math.random() * emojis.length)];
        el.style.left = Math.random() * 100 + 'vw';
        const dur = 6 + Math.random() * 8;
        el.style.animationDuration = dur + 's';
        el.style.animationDelay    = (Math.random() * 3) + 's';
        el.style.fontSize = (16 + Math.random() * 28) + 'px';
        canvas.appendChild(el);
        setTimeout(() => el.remove(), (dur + 4) * 1000);
    }

    // spawn twinkling stars
    function spawnStar() {
        const el = document.createElement('span');
        el.classList.add('star-particle');
        el.innerText = stars[Math.floor(Math.random() * stars.length)];
        el.style.left = Math.random() * 100 + 'vw';
        el.style.top  = Math.random() * 100 + 'vh';
        const dur = 2 + Math.random() * 3;
        el.style.animationDuration = dur + 's';
        el.style.animationDelay    = (Math.random() * 2) + 's';
        canvas.appendChild(el);
        setTimeout(() => el.remove(), 8000);
    }

    setInterval(spawnHeart, 600);
    setInterval(spawnStar,  800);

    // initial burst
    for (let i = 0; i < 12; i++) setTimeout(spawnHeart, i * 200);
    for (let i = 0; i < 20; i++) setTimeout(spawnStar,  i * 150);
})();
</script>
""", unsafe_allow_html=True)

# ─── Main Card ─────────────────────────────────────────────────────────────────
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="big-heart">❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="title-text">Will You Be Forever Mine?</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Hey <b>Sreya</b>! I have a question for you 💞</div>', unsafe_allow_html=True)
st.markdown('<div class="from-text">— From Sai Arya, with love 🌹</div>', unsafe_allow_html=True)

st.markdown('<div class="heart-divider">❤️ 💕 ❤️</div>', unsafe_allow_html=True)

# ─── Buttons ───────────────────────────────────────────────────────────────────
col1, col2 = st.columns([3, 1], gap="medium")

with col1:
    yes_clicked = st.button("Yes, Forever! ❤️", key="yes_btn", use_container_width=True)

with col2:
    no_clicked = st.button("No 💔", key="no_btn", use_container_width=True)

# ─── Responses ─────────────────────────────────────────────────────────────────
if yes_clicked:
    st.balloons()
    st.markdown("""
    <div class="yes-response">
        <div class="yes-emoji">🥰</div>
        <div class="yes-title">She Said YES! 💖</div>
        <div class="yes-msg">
            You just made the world the most beautiful place on Earth.<br>
            Every heartbeat of mine is yours, Sreya. 💕<br><br>
            <b>Thank you for making me the luckiest person alive.</b> 🌹✨
        </div>
    </div>
    """, unsafe_allow_html=True)
    # extra confetti burst via re-triggering balloons effect
    time.sleep(0.5)

if no_clicked:
    st.markdown("""
    <div class="no-response">
        <div class="no-msg">
            💔 Oh no... maybe someday you'll feel differently. 😊<br>
            Either way, you'll always be special to me. 🌸
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close main-card