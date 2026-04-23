import streamlit as st
from groq import RateLimitError

st.set_page_config(
    page_title="ResearchMind",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;500;600&family=Barlow+Condensed:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    background-color: #111111 !important;
    color: #e0ddd6;
    font-family: 'Barlow', sans-serif;
}
.main .block-container { padding: 2rem 3.5rem 2rem; max-width: 1300px; }
#MainMenu, footer, header { visibility: hidden; }

.top-badge {
    text-align: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.68rem; font-weight: 600;
    letter-spacing: 0.35em; text-transform: uppercase;
    color: #666; margin-bottom: 0.6rem; margin-top: 1rem;
}
.hero-title {
    text-align: center;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 7rem; line-height: 0.95;
    letter-spacing: -1px; margin: 0 auto 1rem;
}
.hero-title .white { color: #e8e4d9; }
.hero-title .orange { color: #f97316; }
.hero-sub {
    text-align: center; font-size: 0.95rem; font-weight: 300;
    color: #888; line-height: 1.6; max-width: 480px; margin: 0 auto 2.5rem;
}
.section-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.65rem; font-weight: 600;
    letter-spacing: 0.3em; text-transform: uppercase;
    color: #555; margin-bottom: 0.6rem;
}
.stTextInput > div > div > input {
    background-color: #1a1a1a !important;
    border: 1px solid #2e2e2e !important;
    border-radius: 6px !important;
    color: #e8e4d9 !important;
    font-family: 'Barlow', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.85rem 1rem !important;
    transition: border-color 0.2s;
}
.stTextInput > div > div > input:focus {
    border-color: #f97316 !important;
    box-shadow: 0 0 0 2px rgba(249,115,22,0.12) !important;
}
.stTextInput > div > div > input::placeholder { color: #444 !important; }
.stTextInput label { display: none !important; }

.stButton > button {
    background: #f97316 !important; color: #111 !important;
    border: none !important; border-radius: 6px !important;
    font-family: 'Barlow Condensed', sans-serif !important;
    font-weight: 700 !important; font-size: 1rem !important;
    letter-spacing: 0.12em !important; text-transform: uppercase !important;
    padding: 0.85rem 2rem !important; width: 100% !important;
    transition: background 0.2s, transform 0.15s, box-shadow 0.2s !important;
}
.stButton > button:hover {
    background: #ea6b0f !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(249,115,22,0.3) !important;
}

.chip-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.75rem; }
.chip {
    background: #1e1e1e; border: 1px solid #2e2e2e;
    border-radius: 999px; padding: 0.3rem 0.85rem;
    font-size: 0.78rem; color: #aaa; white-space: nowrap;
}

/* ── Pipeline cards ── */
.pipeline-wrap { width: 100%; }
.pipeline-header {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.4rem; font-weight: 700;
    color: #e8e4d9;
    margin-bottom: 0.85rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid #2a2a2a;
}
.step-card {
    background: #181818;
    border: 1px solid #252525;
    border-left: 3px solid #252525;
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: border-color 0.3s, box-shadow 0.3s, background 0.3s, transform 0.2s;
}
.step-card:hover {
    background: #1e1e1e;
    border-left-color: #f97316;
    transform: translateX(3px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    cursor: default;
}
.step-card.running {
    border-color: #f97316;
    border-left-color: #f97316;
    box-shadow: 0 0 16px rgba(249,115,22,0.2);
    background: #1c1610;
}
.step-card.done {
    border-color: #22c55e;
    border-left-color: #22c55e;
    background: #111a13;
}
.step-card.done:hover {
    border-left-color: #22c55e;
    box-shadow: 0 0 20px rgba(34,197,94,0.15);
}
.step-left { display: flex; align-items: center; gap: 0.9rem; }
.step-num {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.72rem; font-weight: 700;
    color: #444; min-width: 1.8rem;
}
.step-num.running { color: #f97316; }
.step-num.done    { color: #22c55e; }
.step-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.05rem; font-weight: 700;
    color: #e8e4d9;
}
.step-desc { font-size: 0.76rem; color: #555; margin-top: 2px; }
.step-badge {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.62rem; font-weight: 700;
    letter-spacing: 0.15em; text-transform: uppercase;
    padding: 0.22rem 0.6rem; border-radius: 4px;
    white-space: nowrap;
}
.badge-idle    { background:#1e1e1e; color:#555; border:1px solid #2a2a2a; }
.badge-running { background:rgba(249,115,22,0.12); color:#f97316; border:1px solid rgba(249,115,22,0.35); animation:blink 1.1s ease-in-out infinite; }
.badge-done    { background:rgba(34,197,94,0.1);  color:#22c55e; border:1px solid rgba(34,197,94,0.3); }

@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.4} }

/* ── Status bar ── */
.status-bar {
    background: #161616; border: 1px solid #252525;
    border-radius: 8px; padding: 0.8rem 1.2rem;
    margin-top: 1.2rem;
    display: flex; align-items: center; gap: 0.75rem;
    font-size: 0.88rem; color: #aaa; min-height: 3rem;
}
.dot-running {
    width:9px; height:9px; border-radius:50%; background:#f97316; flex-shrink:0;
    animation: pulse-dot 1s ease-in-out infinite;
}
.dot-done { width:9px; height:9px; border-radius:50%; background:#22c55e; flex-shrink:0; }
@keyframes pulse-dot {
    0%,100%{ box-shadow:0 0 0 0 rgba(249,115,22,0.5); }
    50%{ box-shadow:0 0 0 5px rgba(249,115,22,0); }
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] { background:transparent !important; border-bottom:1px solid #252525 !important; }
.stTabs [data-baseweb="tab"] { font-family:'Barlow Condensed',sans-serif !important; font-size:0.8rem !important; font-weight:600 !important; letter-spacing:0.1em !important; text-transform:uppercase !important; color:#555 !important; background:transparent !important; border:none !important; padding:0.5rem 1rem !important; }
.stTabs [aria-selected="true"] { color:#f97316 !important; border-bottom:2px solid #f97316 !important; }

.result-box { background:#181818; border:1px solid #252525; border-radius:8px; padding:1.5rem; margin-top:1rem; font-size:0.85rem; line-height:1.75; color:#ccc; white-space:pre-wrap; word-wrap:break-word; max-height:480px; overflow-y:auto; }
.report-box { background:#141414; border:1px solid #2a2a2a; border-radius:8px; padding:1.75rem; margin-top:1rem; font-size:0.9rem; line-height:1.85; color:#ddd; white-space:pre-wrap; max-height:520px; overflow-y:auto; }

.stDownloadButton > button { background:#1e1e1e !important; color:#f97316 !important; border:1px solid rgba(249,115,22,0.4) !important; border-radius:6px !important; font-family:'Barlow Condensed',sans-serif !important; font-weight:600 !important; font-size:0.85rem !important; letter-spacing:0.1em !important; text-transform:uppercase !important; }

.footer { text-align:center; font-size:0.68rem; color:#333; letter-spacing:0.15em; text-transform:uppercase; padding:2.5rem 0 1rem; }
::-webkit-scrollbar { width:5px; }
::-webkit-scrollbar-track { background:#111; }
::-webkit-scrollbar-thumb { background:#2a2a2a; border-radius:3px; }
::-webkit-scrollbar-thumb:hover { background:#f97316; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
for key, default in [
    ("step_states", ["idle","idle","idle","idle"]),
    ("results", {}),
    ("status_msg", ""),
    ("pipeline_done", False),
]:
    if key not in st.session_state:
        st.session_state[key] = default

STEPS = [
    ("01", "Search Agent",  "Gathers recent web information"),
    ("02", "Reader Agent",  "Scrapes & extracts deep content"),
    ("03", "Writer Chain",  "Drafts the full research report"),
    ("04", "Critic Chain",  "Reviews & scores the report"),
]
STATUS_MSGS = [
    "🔍 Search Agent is scouring the web...",
    "📄 Reader Agent is scraping content...",
    "✍️  Writer is drafting the report...",
    "🎯 Critic is reviewing the report...",
]

def build_pipeline_html(states):
    """Build the complete pipeline HTML from current states."""
    badge_map  = {"idle": ("badge-idle","WAITING"), "running": ("badge-running","RUNNING"), "done": ("badge-done","DONE")}
    cards_html = ""
    for i, (num, name, desc) in enumerate(STEPS):
        s = states[i]
        badge_cls, badge_txt = badge_map[s]
        cards_html += f"""
        <div class="step-card {s}">
            <div class="step-left">
                <div class="step-num {s}">{num}</div>
                <div>
                    <div class="step-name">{name}</div>
                    <div class="step-desc">{desc}</div>
                </div>
            </div>
            <span class="step-badge {badge_cls}">{badge_txt}</span>
        </div>"""
    return f'<div class="pipeline-wrap"><div class="pipeline-header">Pipeline</div>{cards_html}</div>'


# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="top-badge">Multi-Agent AI System</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-title">
    <span class="white">Research</span><span class="orange">Mind</span>
</div>
<div class="hero-sub">
    Four specialized AI agents collaborate — searching, scraping, writing, and
    critiquing — to deliver a polished research report on any topic.
</div>
""", unsafe_allow_html=True)

# ── Layout ─────────────────────────────────────────────────────────────────────
left_col, right_col = st.columns([1.15, 1], gap="large")

# LEFT — inputs
with left_col:
    st.markdown('<div class="section-label">Research Topic</div>', unsafe_allow_html=True)
    topic = st.text_input(
        label="Research Topic",
        label_visibility="collapsed",
        placeholder="e.g. Quantum computing breakthroughs in 2025",
    )
    run_btn = st.button("⚡  Run Research Pipeline")
    st.markdown("""
    <div class="section-label" style="margin-top:1.3rem;">Try →</div>
    <div class="chip-row">
        <div class="chip">LLM agents 2025</div>
        <div class="chip">CRISPR gene editing</div>
        <div class="chip">Fusion energy progress</div>
    </div>
    """, unsafe_allow_html=True)
    status_ph = st.empty()   # live status bar lives here

# RIGHT — pipeline cards (always rendered from session state)
with right_col:
    pipeline_ph = st.empty()

# Always draw the cards from current session state immediately
pipeline_ph.markdown(build_pipeline_html(st.session_state.step_states), unsafe_allow_html=True)

# Restore status bar if pipeline ran before
if st.session_state.status_msg:
    dot = "dot-done" if st.session_state.pipeline_done else "dot-running"
    status_ph.markdown(
        f'<div class="status-bar"><div class="{dot}"></div>{st.session_state.status_msg}</div>',
        unsafe_allow_html=True
    )

# ── Helpers ────────────────────────────────────────────────────────────────────
def set_step(idx, state, msg=""):
    st.session_state.step_states[idx] = state
    pipeline_ph.markdown(build_pipeline_html(st.session_state.step_states), unsafe_allow_html=True)
    if msg:
        st.session_state.status_msg = msg
        dot = "dot-done" if state == "done" else "dot-running"
        status_ph.markdown(
            f'<div class="status-bar"><div class="{dot}"></div>{msg}</div>',
            unsafe_allow_html=True
        )

# ── Run pipeline ───────────────────────────────────────────────────────────────
if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic before running.")
    else:
        from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

        # Reset
        st.session_state.step_states  = ["idle","idle","idle","idle"]
        st.session_state.results       = {}
        st.session_state.pipeline_done = False
        pipeline_ph.markdown(build_pipeline_html(st.session_state.step_states), unsafe_allow_html=True)

        # ── Step 1: Search ────────────────────────────────────────────────────
        set_step(0, "running", STATUS_MSGS[0])
        search_agent  = build_search_agent()
        search_result = search_agent.invoke({
            "messages": [("user", f"""Use the web_search tool first.
Search for recent reliable sources about: {topic}
Return the tool output exactly in this format:

Title:
URL:
Snippet:

Return at least 5 sources.
Do not answer from your own knowledge.
Do not summarize.
""")]
        })
        search_results = search_result["messages"][-1].content
        st.session_state.results["search"] = search_results
        set_step(0, "done", "✅ Search Agent done — sources found.")

        # ── Step 2: Reader ────────────────────────────────────────────────────
        set_step(1, "running", STATUS_MSGS[1])
        reader_agent  = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"{search_results}")]
        })
        scraped = reader_result["messages"][-1].content
        st.session_state.results["scraped"] = scraped
        set_step(1, "done", "✅ Reader Agent done — content extracted.")

        # # ── Step 3: Writer ────────────────────────────────────────────────────
        # set_step(2, "running", STATUS_MSGS[2])
        # combined = f"SEARCH RESULTS:\n{search_results}\n\nDETAILED SCRAPED CONTENT:\n{scraped}"
        # report   = writer_chain.invoke({"topic": topic, "research": combined})
        # st.session_state.results["report"] = report
        # set_step(2, "done", "✅ Writer Chain done — report drafted.")

        # ── Step 3: Writer ────────────────────────────────────────────────────
      

        set_step(2, "running", STATUS_MSGS[2])

        combined = f"""
SEARCH RESULTS:
{search_results[:3000]}

DETAILED SCRAPED CONTENT:
{scraped[:5000]}
"""

        try:
            report = writer_chain.invoke({
                "topic": topic,
                "research": combined
            })

            st.session_state.results["report"] = report
            set_step(2, "done", "✅ Writer Chain done — report drafted.")

        except RateLimitError:
            st.error("Groq token limit reached. Try again later.")
            st.stop()


        # ── Step 4: Critic ────────────────────────────────────────────────────
        set_step(3, "running", STATUS_MSGS[3])

        feedback = critic_chain.invoke({
            "report": report
        })

        st.session_state.results["feedback"] = feedback

        set_step(3, "done", "🎉 Pipeline complete! All agents finished.")
        st.session_state.pipeline_done = True

# ── Results tabs ───────────────────────────────────────────────────────────────
if st.session_state.results:
    st.markdown("---")
    t1, t2, t3, t4 = st.tabs(["🔍 Sources", "📄 Scraped Content", "📝 Report", "🎯 Critic Review"])

    with t1:
        st.markdown(
            f'<div class="result-box">{st.session_state.results.get("search","")}</div>',
            unsafe_allow_html=True)
    with t2:
        st.markdown(
            f'<div class="result-box">{st.session_state.results.get("scraped","")}</div>',
            unsafe_allow_html=True)
    with t3:
        rep = st.session_state.results.get("report", "")
        st.markdown(f'<div class="report-box">{rep}</div>', unsafe_allow_html=True)
        if rep:
            st.download_button(
                "⬇  Download Report (.txt)",
                data=rep,
                file_name=f"report_{topic[:40].replace(' ','_')}.txt",
                mime="text/plain",
            )
    with t4:
        st.markdown(
            f'<div class="result-box">{st.session_state.results.get("feedback","")}</div>',
            unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    ResearchMind &nbsp;·&nbsp; Powered by LangChain multi-agent pipeline &nbsp;·&nbsp; Built with Streamlit
</div>
""", unsafe_allow_html=True)