import streamlit as st
import re
import time
import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="Research_mind",
        user="postgres",
        password="sayyed",
        port="5432"
    )

def save_login(email, password):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users_login (email, password) VALUES (%s, %s)",
        (email, password)
    )

    conn.commit()
    cur.close()
    conn.close()
# data base add 
def show_login():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:

        st.markdown("""
        <style>

        .stApp{
            background:
            radial-gradient(circle at center, rgba(255,140,50,.08), transparent 22%),
            radial-gradient(circle at 20% 20%, rgba(0,255,255,.04), transparent 20%),
            #040507;
        }

        .wrap{
            max-width:560px;
            margin:35px auto;
            text-align:center;
        }

        /* =========================
           ANIMATION
        ========================= */

        @keyframes pulseOrb {
            0%   { transform: scale(1); }
            50%  { transform: scale(1.06); }
            100% { transform: scale(1); }
        }

        @keyframes rotateRing {
            0%   { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        @keyframes waveGlow {
            0%   { transform: scale(1); opacity:.35; }
            100% { transform: scale(1.45); opacity:0; }
        }

        /* =========================
           ORB
        ========================= */

        .orb-wrap{
            position:relative;
            width:150px;
            height:150px;
            margin:0 auto 24px auto;
        }

        .wave1,.wave2{
            position:absolute;
            inset:0;
            border-radius:50%;
            border:1px solid rgba(255,140,50,.22);
            animation:waveGlow 3s linear infinite;
        }

        .wave2{
            animation-delay:1.5s;
        }

        .orb{
            width:150px;
            height:150px;
            border-radius:50%;
            position:absolute;
            inset:0;
            background:
            radial-gradient(circle at 35% 35%,
            #ffcc9e 0%,
            #ff8c32 28%,
            #ff6a1f 55%,
            #ff4d00 72%,
            transparent 74%);
            box-shadow:
            0 0 25px rgba(255,140,50,.55),
            0 0 60px rgba(255,140,50,.30),
            0 0 110px rgba(255,140,50,.18);
            animation:pulseOrb 3s ease-in-out infinite;
        }

        .orb:before{
            content:"";
            position:absolute;
            inset:-14px;
            border-radius:50%;
            border:2px solid rgba(255,255,255,.08);
            border-top:2px solid rgba(255,140,50,.55);
            animation:rotateRing 5s linear infinite;
        }

        .orb:after{
            content:"AI";
            position:absolute;
            inset:0;
            display:flex;
            align-items:center;
            justify-content:center;
            color:#050507;
            font-size:30px;
            font-weight:900;
            letter-spacing:2px;
        }

        /* =========================
           TITLE
        ========================= */

        .title{
            font-size:46px;
            font-weight:900;
            color:#f5f6f8;
            margin-bottom:6px;
        }

        .title span{
            color:#ff8c32;
        }

        .sub{
            color:#9ca3af;
            font-size:15px;
            margin-bottom:22px;
        }

        /* =========================
           PANEL
        ========================= */

        .panel{
            padding:40px;
            border-radius:28px;
            background:rgba(16,18,24,.78);
            border:1px solid rgba(255,255,255,.08);
            backdrop-filter: blur(18px);
            box-shadow:
            0 30px 80px rgba(0,0,0,.45),
            0 0 30px rgba(255,140,50,.08);
        }

        /* FIXED CHIP SECTION */
        .mini{
            display:flex;
            gap:12px;
            margin-top:8px;
            margin-bottom:34px;
            padding:14px;
            background:rgba(255,255,255,.02);
            border:1px solid rgba(255,255,255,.05);
            border-radius:18px;
        }

        .chip{
            flex:1;
            padding:14px 10px;
            border-radius:14px;
            background:#11141b;
            border:1px solid rgba(255,255,255,.06);
            color:#dfe2e7;
            font-size:12px;
            text-align:center;
        }

        /* INPUT */

        .stTextInput > div > div > input{
            background:rgba(255,255,255,.03) !important;
            color:white !important;
            border:1px solid rgba(255,255,255,.08) !important;
            border-radius:16px !important;
            height:50px !important;
        }

        .stTextInput > div > div > input:focus{
            border:1px solid #ff8c32 !important;
            box-shadow:0 0 0 4px rgba(255,140,50,.10) !important;
        }

        /* BUTTON */

        .stButton > button{
            background:linear-gradient(135deg,#ff8c32,#ff5a1a) !important;
            color:white !important;
            border:none !important;
            border-radius:16px !important;
            height:52px !important;
            font-weight:800 !important;
            font-size:16px !important;
            margin-top:8px;
        }

        .foot{
            color:#6f7682;
            font-size:12px;
            margin-top:18px;
            text-align:center;
        }

        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="wrap">', unsafe_allow_html=True)

        st.markdown("""
        <div class="orb-wrap">
            <div class="wave1"></div>
            <div class="wave2"></div>
            <div class="orb"></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            '<div class="title">Research<span>Mind</span></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="sub">Activate Neural Access</div>',
            unsafe_allow_html=True
        )

        st.markdown('<div class="panel">', unsafe_allow_html=True)

        st.markdown("""
        <div class="mini">
            <div class="chip">⚡ Fast</div>
            <div class="chip">🧠 AI Core</div>
            <div class="chip">📄 Reports</div>
        </div>
        """, unsafe_allow_html=True)

        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        if st.button("ENTER CORE", use_container_width=True):

            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

            if not re.match(email_pattern, email):
                st.error("Enter a valid email")

            elif len(password) < 4:
                st.error("Password too short")

            else:
                st.success("Neural access granted")
                time.sleep(1)
                st.session_state.logged_in = True
                st.rerun()

        st.markdown(
            '<div class="foot">Quantum Protected Session • ResearchMind Ω</div>',
            unsafe_allow_html=True
        )

        st.markdown('</div></div>', unsafe_allow_html=True)

        st.stop()