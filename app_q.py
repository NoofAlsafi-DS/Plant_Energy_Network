# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib as mpl
import arabic_reshaper
from bidi.algorithm import get_display
from matplotlib.font_manager import FontProperties
import os

# ================= إعدادات عامة =================
st.set_page_config(page_title="الشبكة النباتية الذكية لتوليد الكهرباء", page_icon="🌱", layout="wide")

# 🌿 تصحيح اتجاه النصوص العربية في الواجهة
st.markdown("""
<style>
body, div, p, span, h1, h2, h3, h4, h5, h6 { direction: rtl; text-align: right; font-family: 'Noto Naskh Arabic', sans-serif; }
</style>
""", unsafe_allow_html=True)

mpl.rcParams['axes.unicode_minus'] = False  # لإصلاح عرض السالب

# التحقق من وجود الخط العربي
font_path = "fonts/NotoNaskhArabic-Regular.ttf"
if os.path.exists(font_path):
    AR_FONT = FontProperties(fname=font_path)
else:
    st.warning("⚠️ لم يتم العثور على الخط العربي (fonts/NotoNaskhArabic-Regular.ttf). سيُستخدم الخط الافتراضي.")
    AR_FONT = FontProperties()

# دالة تهيئة النص العربي داخل الرسوم
def ar(text: str) -> str:
    try:
        return get_display(arabic_reshaper.reshape(text))
    except Exception:
        return text

# ================= ترويسة التطبيق =================
def header_with_logo():
    st.markdown("""
        <style>
        .header-box {
            background: linear-gradient(90deg, #e8f5e9 0%, #f1fff4 100%);
            border: 1px solid #d7ead9; border-radius: 18px; padding: 14px 18px; margin-bottom: 14px;
        }
        .title-text { font-size: 28px; font-weight: 800; margin: 0 0 4px 0; color:#1b5e20;}
        .subtitle-text { font-size: 14px; color:#2e7d32; margin:0; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header-box">', unsafe_allow_html=True)
    col_logo, col_title, col_btn = st.columns([1, 3, 1])
    with col_logo:
        try:
            logo = Image.open("logo_q.png")
            st.image(logo, use_container_width=True)
        except Exception:
            st.write("🌱")
    with col_title:
        st.markdown('<div class="title-text">الشبكة النباتية الذكية لتوليد الكهرباء</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle-text">Smart Plant Energy Network • طاقة حيوية نظيفة ومستدامة</p>', unsafe_allow_html=True)
    with col_btn:
        # زر فتح نافذة "حول التطبيق"
        if st.button("ℹ️ حول التطبيق", use_container_width=True):
            st.session_state.show_about = True
    st.markdown('</div>', unsafe_allow_html=True)

# ================= نافذة منبثقة: حول التطبيق =================
def about_modal():
    # حالة الظهور
    if "show_about" not in st.session_state:
        st.session_state.show_about = False

    st.markdown("""
    <style>
    .spen-modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center; z-index: 99999; }
    .spen-modal {
        width: min(860px, 94vw); background: #ffffff; color: #1b5e20;
        border-radius: 18px; padding: 22px 22px 14px; box-shadow: 0 12px 36px rgba(0,0,0,0.2);
        border: 1px solid #d7ead9; direction: rtl; text-align: right; font-family: 'Noto Naskh Arabic', sans-serif;
    }
    .spen-modal h2 { margin: 0 0 8px 0; font-size: 22px; font-weight: 900; color:#1b5e20; }
    .spen-modal p { margin: 6px 0; line-height: 1.7; color:#2e7d32; }
    .spen-badges { display:flex; flex-wrap:wrap; gap:6px; margin: 8px 0 2px;}
    .spen-badge { background:#e8f5e9; border:1px solid #d7ead9; color:#1b5e20; border-radius: 999px; padding: 4px 10px; font-size: 12px; }
    .spen-actions { display:flex; gap:10px; margin-top: 10px;}
    .spen-btn { background:#1b5e20; color:#fff; border:none; border-radius: 12px; padding: 8px 14px; cursor:pointer; font-weight:700; }
    .spen-btn.secondary { background:#a5d6a7; color:#1b5e20; }
    </style>
    """, unsafe_allow_html=True)

    if st.session_state.show_about:
        st.markdown('<div class="spen-modal-overlay">', unsafe_allow_html=True)
        st.markdown('<div class="spen-modal">', unsafe_allow_html=True)

        st.markdown("""
        <h2>🌱 الشبكة النباتية الذكية لتوليد الكهرباء</h2>
        <p>
        تطبيق تعليمي تفاعلي يشرح مبدأ توليد الكهرباء من النباتات عبر الخلايا الوقودية الميكروبية النباتية،
        ويعرض كيف نربط عدة نباتات في شبكة ذكية مع تخزين وتنظيم للطاقة لتغذية أجهزة مثل إنارة الحدائق والكاميرات وإشارات المرور.
        </p>
        <div class="spen-badges">
          <span class="spen-badge">Streamlit</span>
          <span class="spen-badge">Matplotlib</span>
          <span class="spen-badge">Pandas</span>
          <span class="spen-badge">Arabic UI</span>
          <span class="spen-badge">Bio-Energy</span>
        </div>
        <p><b>المزايا:</b><br>
        • رسوم توضيحية لفكرة P-MFC. <br>
        • جداول ورسوم للجهد والتيار. <br>
        • دعم العربية (RTL + خط عربي داخل الرسوم). <br>
        • تصميم خفيف وملائم للعرض المدرسي/المسابقة. <br>
        </p>
        <p><b>المكتبات:</b> Pandas, Matplotlib, Pillow, arabic-reshaper, python-bidi</p>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([0.2, 0.8])
        with c1:
            if st.button("✔️ فهمت"):
                st.session_state.show_about = False
        with c2:
            if st.button("إغلاق", type="secondary"):
                st.session_state.show_about = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ===== عرض الترويسة والنافذة =====
header_with_logo()
about_modal()

# ================= الشريط الجانبي =================
with st.sidebar:
    st.header("⚙️ إعدادات العرض")
    show_currents = st.checkbox("عرض التيار (mA)", True)
    show_voltages = st.checkbox("عرض الجهد (V)", True)
    st.markdown("---")
    st.caption("📁 ضع ملف الخط داخل: fonts/NotoNaskhArabic-Regular.ttf")

# ================= التبويبات =================
tab1, tab2, tab3 = st.tabs(["🧩 الفكرة والرسم التوضيحي", "📊 النتائج التجريبية", "🔌 توصيل الشبكة النباتية"])

# ----- التبويب 1 -----
with tab1:
    st.subheader("كيف تُولِّد النباتات الكهرباء؟")
    st.write("""
    الجذور تُفرز مركبات عضوية ➜ البكتيريا تُحلِّلها ➜ تنطلق إلكترونات.
    الأنود داخل التربة يلتقط الإلكترونات، والكاثود عند الهواء يُكمل التفاعل.
    بربط الأنود بالكاثود نحصل على تيار كهربائي صغير قابل للتجميع.
    """)

    fig, ax = plt.subplots(figsize=(8, 5))
    # التربة والهواء
    ax.add_patch(plt.Rectangle((0.05, 0.05), 0.9, 0.55, facecolor="#e9d7a5", edgecolor="k"))
    ax.add_patch(plt.Rectangle((0.05, 0.60), 0.9, 0.10, facecolor="#cfe8ff", edgecolor="k"))
    ax.text(0.90, 0.62, ar("هواء"), fontproperties=AR_FONT, fontsize=10)
    # النبات
    ax.plot([0.25, 0.25], [0.20, 0.68], color="#7aa35a", lw=4)
    ax.plot([0.20, 0.25, 0.30], [0.66, 0.70, 0.66], color="#4c8b37", lw=6)
    ax.text(0.18, 0.71, ar("نبات"), fontproperties=AR_FONT, fontsize=10)
    # الجذور والبكتيريا
    ax.plot([0.25, 0.20], [0.20, 0.15], color="#8b5a2b", lw=3)
    ax.plot([0.25, 0.30], [0.20, 0.14], color="#8b5a2b", lw=3)
    ax.text(0.07, 0.18, ar("جذور تُفرز\nمركبات عضوية"), fontproperties=AR_FONT, fontsize=9)
    ax.text(0.40, 0.12, ar("بكتيريا كهربية"), fontproperties=AR_FONT, fontsize=9)
    # الأقطاب
    ax.add_patch(plt.Rectangle((0.55, 0.12), 0.02, 0.30, facecolor="#444444"))
    ax.text(0.57, 0.38, ar("أنود"), fontproperties=AR_FONT, fontsize=10)
    ax.add_patch(plt.Rectangle((0.75, 0.60), 0.02, 0.12, facecolor="#999999"))
    ax.text(0.77, 0.72, ar("كاثود"), fontproperties=AR_FONT, fontsize=10)
    # السلك والإلكترونات
    ax.plot([0.56, 0.56, 0.76, 0.76], [0.42, 0.80, 0.80, 0.72], color="black", lw=2)
    for x in [0.34, 0.38, 0.42]:
        ax.annotate("", xy=(0.56, 0.28), xytext=(x, 0.22),
                    arrowprops=dict(arrowstyle="->", lw=1.8, color="#aa0000"))
    ax.text(0.36, 0.24, "e⁻", color="#aa0000", fontsize=10)
    ax.text(0.80, 0.65, "O₂", fontsize=11, color="#004c99")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    st.pyplot(fig)

# ----- التبويب 2 -----
with tab2:
    st.subheader("النتائج التجريبية للنظام النباتي")
    df = pd.DataFrame({
        "نوع النبات": ["سبانخ", "فاصوليا", "شبكة نباتية"],
        "نوع التربة": ["رملية", "عضوية", "عضوية + ري عضوي"],
        "الجهد (V)": [0.4, 0.8, 1.6],
        "التيار (mA)": [0.6, 1.2, 2.4]
    })
    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)
    if st.checkbox("عرض الجهد (V)", value=True, key="vplot"):
        with col1:
            fig1, ax1 = plt.subplots()
            ax1.bar(df.index, df["الجهد (V)"])
            ax1.set_xticks(df.index)
            ax1.set_xticklabels([ar(s) for s in df["نوع النبات"]], fontproperties=AR_FONT)
            ax1.set_ylabel(ar("الجهد (فولت)"), fontproperties=AR_FONT)
            ax1.set_title(ar("الجهد حسب نوع النبات"), fontproperties=AR_FONT)
            st.pyplot(fig1)
    if st.checkbox("عرض التيار (mA)", value=True, key="iplot"):
        with col2:
            fig2, ax2 = plt.subplots()
            ax2.bar(df.index, df["التيار (mA)"])
            ax2.set_xticks(df.index)
            ax2.set_xticklabels([ar(s) for s in df["نوع النبات"]], fontproperties=AR_FONT)
            ax2.set_ylabel(ar("التيار (ملي أمبير)"), fontproperties=AR_FONT)
            ax2.set_title(ar("التيار حسب نوع النبات"), fontproperties=AR_FONT)
            st.pyplot(fig2)

# ----- التبويب 3 -----
with tab3:
    st.subheader("توصيل الشبكة النباتية الذكية")
    st.write("""
    **التوصيل على التوالي (Series):** يرفع الجهد الكلي (Voltage↑).  
    **التوصيل على التوازي (Parallel):** يرفع التيار الكلي (Current↑).
    """)
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    # تسلسل
    ax3.add_patch(plt.Rectangle((0.05, 0.60), 0.12, 0.25, fill=False))
    ax3.add_patch(plt.Rectangle((0.20, 0.60), 0.12, 0.25, fill=False))
    ax3.add_patch(plt.Rectangle((0.35, 0.60), 0.12, 0.25, fill=False))
    ax3.plot([0.17, 0.20], [0.72, 0.72], color="black")
    ax3.plot([0.32, 0.35], [0.72, 0.72], color="black")
    ax3.text(0.05, 0.90, ar("تسلسل (V↑)"), fontproperties=AR_FONT, fontsize=10)
    # توازي
    ax3.add_patch(plt.Rectangle((0.60, 0.60), 0.12, 0.25, fill=False))
    ax3.add_patch(plt.Rectangle((0.60, 0.32), 0.12, 0.25, fill=False))
    ax3.add_patch(plt.Rectangle((0.60, 0.04), 0.12, 0.25, fill=False))
    ax3.plot([0.72, 0.88], [0.72, 0.72], color="black")
    ax3.plot([0.72, 0.88], [0.44, 0.44], color="black")
    ax3.plot([0.72, 0.88], [0.16, 0.16], color="black")
    ax3.text(0.60, 0.90, ar("توازي (I↑)"), fontproperties=AR_FONT, fontsize=10)
    ax3.axis("off")
    st.pyplot(fig3)

