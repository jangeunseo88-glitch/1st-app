import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="마법 같은 삼각함수 탐험대",
    page_icon="📐",
    layout="wide"
)

# 세션 스테이트 초기화 (퀴즈 상태 유지용)
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "score" not in st.session_state:
    st.session_state.score = 0

def main():
    st.sidebar.title("🧭 삼각함수 탐험 코스")
    menu = st.sidebar.selectbox(
        "학습 단원을 선택하세요:",
        [
            "1. 각도의 새로운 이해 (6분법 vs 호도법·라디안)",
            "2. 삼각함수의 본질 (단위원과 좌표)",
            "3. 사인(Sin) 그래프와 조작",
            "4. 코사인(Cos) 그래프와 조작",
            "5. 탄젠트(Tan) 그래프와 조작",
            "6. 🏆 실력 확인 퀴즈 & 오답 노트"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.info("💡 **선생님의 꿀팁 조언**\n눈으로 보고 직접 슬라이더를 움직여야 비로소 내 것이 됩니다!")

    # ----------------------------------------------------
    # 1. 라디안과 호도법
    # ----------------------------------------------------
    if menu == "1. 각도의 새로운 이해 (6분법 vs 호도법·라디안)":
        st.title("📏 1. 각도를 재는 전혀 새로운 방법: 라디안(Radian)")
        
        st.markdown("""
        우리가 일상에서 쓰는 '30도, 90도, 180도'는 원을 360등분한 **6분법**이에요. 
        하지만 수학과 과학의 세계에서는 원의 반지름과 **'호의 길이'**를 기준으로 각도를 재는 **호도법(Radian)**을 쓴답니다.
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### 🎯 라디안(Radian)의 정의
            * **"반지름($r$)과 똑같은 길이의 호($s=r$)가 만들어내는 중심각의 크기"**를 **1 라디안(rad)**이라고 해요.
            * 원둘레의 길이는 $2\\pi r$이므로, 한 바퀴($360^\\circ$)는 **$2\\pi$ 라디안**이 됩니다.
            * 따라서 반 바퀴($180^\\circ$)는 **$\\pi$ 라디안**이에요!
            """)
            st.success("📌 **시험 꿀팁!** \n- 도($^\\circ$)를 라디안으로 바꿀 때는 $\\frac{\\pi}{180}$을 곱하고, \n- 라디안을 도로 바꿀 때는 $\\frac{180}{\\pi}$를 곱하세요!")

        with col2:
            st.markdown("### 🎛️ 각도 변환 시뮬레이터")
            deg_input = st.slider("각도(Degree)를 움직여보세요:", 0, 360, 180, step=5)
            rad_val = deg_input * (np.pi / 180)
            
            st.latex(r"%d^\circ = \frac{%d\pi}{180} \approx %.3f\text{ rad}" % (deg_input, deg_input, rad_val))
            
            # 시각화 (그래프 한글 깨짐 방지를 위해 영문/수식 라벨 적용)
            fig, ax = plt.subplots(figsize=(4, 4))
            theta = np.linspace(0, rad_val, 100)
            ax.plot(np.cos(theta), np.sin(theta), 'b-', lw=2)
            ax.fill_between(np.linspace(0, np.cos(rad_val), 100), 0, np.sin(theta), color='skyblue', alpha=0.3)
            ax.set_xlim(-1.2, 1.2)
            ax.set_ylim(-1.2, 1.2)
            ax.axhline(0, color='gray', lw=0.8)
            ax.axvline(0, color='gray', lw=0.8)
            ax.set_aspect('equal')
            ax.set_title(f"Angle: {deg_input} deg ({rad_val:.2f} rad)")
            st.pyplot(fig)

    # ----------------------------------------------------
    # 2. 삼각함수의 본질 (단위원)
    # ----------------------------------------------------
    elif menu == "2. 삼각함수의 본질 (단위원과 좌표)":
        st.title("🎯 2. 삼각함수는 '원 위를 움직이는 점의 좌표'다!")
        
        st.markdown("""
        중학교 때 직각삼각형으로 배우던 삼각비는 잊으세요! 고등학교 삼각함수는 **반지름이 1인 원(단위원)** 위를 빙글빙글 도는 점의 **좌표**입니다.
        * **$x$좌표** = $\\cos\\theta$
        * **$y$좌표** = $\\sin\\theta$
        * **기울기($\\frac{y}{x}$)** = $\\tan\\theta$
        """)

        angle_deg = st.slider("각도 θ 조절하기:", 0, 360, 45, step=1)
        angle_rad = np.radians(angle_deg)
        
        x_pos = np.cos(angle_rad)
        y_pos = np.sin(angle_rad)

        fig, ax = plt.subplots(figsize=(6, 6))
        circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--', lw=1.5)
        ax.add_patch(circle)
        
        ax.plot([0, x_pos], [0, y_pos], 'ro-', lw=2, label=f"Point P({x_pos:.2f}, {y_pos:.2f})")
        ax.plot([x_pos, x_pos], [0, y_pos], 'g--', lw=1.5, label=f"sin = {y_pos:.2f}")
        ax.plot([0, x_pos], [0, 0], 'b--', lw=1.5, label=f"cos = {x_pos:.2f}")
        
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper right')
        ax.set_title(f"Unit Circle (theta = {angle_deg} deg)")
        
        st.pyplot(fig)
        st.info(f"💡 현재 각도에서 **Cosine(가로)은 {x_pos:.3f}**, **Sine(세로)은 {y_pos:.3f}** 입니다.")

    # ----------------------------------------------------
    # 3. 사인(Sine) 그래프
    # ----------------------------------------------------
    elif menu == "3. 사인(Sin) 그래프와 조작":
        st.title("📈 3. 파도처럼 출렁이는 파동: $y = a \\sin(bx + c)$")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            amp = st.slider("진폭 ($a$, 높낮이):", 0.5, 3.0, 1.0, 0.1)
        with col2:
            freq = st.slider("주파수 조절 ($b$, 주기 변화):", 0.5, 3.0, 1.0, 0.1)
        with col3:
            shift = st.slider("위상 이동 ($c$, 좌우 이동):", -np.pi, np.pi, 0.0, 0.1)

        x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
        y = amp * np.sin(freq * x + shift)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(x, y, color='crimson', lw=2.5, label=f'y = {amp}sin({freq}x + {shift:.1f})')
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_ylim(-3.5, 3.5)
        ax.legend()
        ax.set_title("Sine Wave Graph")
        st.pyplot(fig)

        st.success("📌 **시험 출제 포인트!**\n- **주기($T$) 구하는 공식:** $\\frac{2\\pi}{b}$ (원래 주기 $2\\pi$를 $x$ 앞의 계수 $b$로 나눕니다!)\n- **최대값:** $|a|$, **최소값:** $-|a|$")

    # ----------------------------------------------------
    # 4. 코사인(Cosine) 그래프
    # ----------------------------------------------------
    elif menu == "4. 코사인(Cos) 그래프와 조작":
        st.title("📉 4. 사인과 쌍둥이 형제: $y = a \\cos(bx)$")
        
        c_amp = st.slider("코사인 진폭 ($a$):", 0.5, 3.0, 1.0, 0.1, key="c_amp")
        c_freq = st.slider("코사인 주기 조절 ($b$):", 0.5, 3.0, 1.0, 0.1, key="c_freq")

        x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
        y = c_amp * np.cos(c_freq * x)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(x, y, color='dodgerblue', lw=2.5, label=f'y = {c_amp}cos({c_freq}x)')
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_ylim(-3.5, 3.5)
        ax.legend()
        ax.set_title("Cosine Wave Graph")
        st.pyplot(fig)

        st.info(f"💡 **선생님의 한마디:** 코사인 그래프는 사인 그래프를 왼쪽으로 $\\frac{{\\pi}}{{2}}$만큼 밀어낸 모양과 완전히 똑같습니다! ($\\sin(x + \\frac{{\\pi}}{{2}}) = \\cos x$)")

    # ----------------------------------------------------
    # 5. 탄젠트(Tangent) 그래프
    # ----------------------------------------------------
    elif menu == "5. 탄젠트(Tan) 그래프와 조작":
        st.title("📐 5. 쭉쭉 뻗어 올라가는 로켓: $y = \\tan(x)$")
        
        st.markdown("""
        탄젠트는 $\\frac{\\sin x}{\\cos x}$ 예요. 즉, **분모인 $\\cos x$가 0이 되는 곳**에서는 값이 존재할 수 없어요! 
        이 선들을 수학에서는 **점근선(Asymptote)**이라고 부릅니다.
        """)

        t_range = st.slider("탄젠트 관찰 범위 조절:", 1.0, 3.0, 1.5, 0.1)
        
        x = np.linspace(-t_range * np.pi, t_range * np.pi, 1000)
        y = np.tan(x)
        y[np.abs(np.gradient(y)) > 50] = np.nan

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(x, y, color='forestgreen', lw=2.5, label='y = tan(x)')
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.set_ylim(-10, 10)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        ax.set_title("Tangent Graph")
        st.pyplot(fig)

        st.success("📌 **시험 꿀팁 (주기 주의사항)!**\n- 사인, 코사인의 주기는 $2\\pi$이지만, **탄젠트의 주기는 단 $\\pi$**입니다!")

    # ----------------------------------------------------
    # 6. 실력 확인 퀴즈 & 오답 노트
    # ----------------------------------------------------
    elif menu == "6. 🏆 실력 확인 퀴즈 & 오답 노트":
        st.title("🏆 삼각함수 개념 마스터 퀴즈")
        st.markdown("지금까지 배운 내용을 바탕으로 3가지 문제를 풀어보세요.")

        with st.form("quiz_form"):
            q1 = st.radio(
                "문제 1. 반 바퀴에 해당하는 각도인 180도는 호도법으로 표현하면 얼마일까요?",
                ["(A) pi/2 rad", "(B) pi rad", "(C) 2*pi rad", "(D) 360 rad"],
                key="q1"
            )

            q2 = st.radio(
                "문제 2. 함수 y = 3*sin(2x) 의 주기는 얼마일까요?",
                ["(A) pi", "(B) 2*pi", "(C) pi/2", "(D) 4*pi"],
                key="q2"
            )

            q3 = st.radio(
                "문제 3. 다음 중 탄젠트 함수(y = tan x)에 대한 설명으로 옳은 것을 고르세요.",
                [
                    "(A) 주기는 2*pi 이다.",
                    "(B) 최대값은 1이고 최소값은 -1이다.",
                    "(C) 분모가 0이 되는 곳에 점근선이 존재한다.",
                    "(D) 코사인 함수와 그래프 모양이 완전히 똑같다."
                ],
                key="q3"
            )

            submitted = st.form_submit_button("정답 제출하기")

        if submitted:
            st.session_state.quiz_submitted = True
            score = 0
            
            correct_q1 = "(B) pi rad"
            correct_q2 = "(A) pi"
            correct_q3 = "(C) 분모가 0이 되는 곳에 점근선이 존재한다."

            st.markdown("---")
            st.subheader("📝 채점 결과 및 상세 해설")

            if q1 == correct_q1:
                st.success("✅ **문제 1 정답!** 완벽합니다. 180도 = pi 라디안입니다!")
                score += 1
            else:
                st.error("❌ **문제 1 오답.** \n*해설:* 원의 둘레는 2*pi*r 이며 360도에 해당합니다. 따라서 절반인 180도는 pi 라디안입니다.")

            if q2 == correct_q2:
                st.success("✅ **문제 2 정답!** 주기를 구하는 공식 (2*pi / b)에 따라 (2*pi / 2 = pi)가 맞습니다!")
                score += 1
            else:
                st.error("❌ **문제 2 오답.** \n*해설:* 삼각함수 y = sin(bx) 의 주기는 기본 주기 2*pi를 x 앞의 계수 b로 나눈 값입니다. (2*pi / 2 = pi)")

            if q3 == correct_q3:
                st.success("✅ **문제 3 정답!** 탄젠트는 sin/cos 이므로 cos이 0이 되는 지점에서 점근선이 생깁니다!")
                score += 1
            else:
                st.error("❌ **문제 3 오답.** \n*해설:* 탄젠트의 주기는 pi이며 최대/최소값이 없고, cos x = 0인 지점에서 점근선을 갖습니다.")

            st.markdown(f"### 🎯 **최종 점수: 3문항 중 {score}문항 정답!**")
            if score == 3:
                st.balloons()
                st.markdown("🎉 **만세! 삼각함수 마스터가 되신 것을 축하합니다!**")

if __name__ == "__main__":
    main()
