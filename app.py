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
            "3. 사인(Sin) 그래프 완벽 조작: a·sin(bx+c)+d",
            "4. 코사인(Cos) 그래프 완벽 조작: a·cos(bx+c)+d",
            "5. 탄젠트(Tan) 그래프 완벽 조작: a·tan(bx+c)+d",
            "6. 🏆 실력 확인 퀴즈 & 오답 노트"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.info("💡 **선생님의 꿀팁 조언**\n$a, b, c, d$ 슬라이더를 직접 움직이며 그래프의 변화를 관찰해 보세요!")

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
    # 3. 사인(Sine) 그래프 조작: a*sin(bx+c)+d
    # ----------------------------------------------------
    elif menu == "3. 사인(Sin) 그래프 완벽 조작: a·sin(bx+c)+d":
        st.title("📈 3. 사인 그래프 완벽 탐구: $y = a \\sin(bx + c) + d$")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.slider("a (진폭/높낮이):", -3.0, 3.0, 1.0, 0.1, key="sin_a")
        with col2:
            b = st.slider("b (주기 결정):", 0.1, 3.0, 1.0, 0.1, key="sin_b")
        with col3:
            c = st.slider("c (x축 평행이동):", -np.pi, np.pi, 0.0, 0.1, key="sin_c")
        with col4:
            d = st.slider("d (y축 평행이동):", -3.0, 3.0, 0.0, 0.1, key="sin_d")

        x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
        y = a * np.sin(b * x + c) + d

        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.plot(x, y, color='crimson', lw=2.5, label=f'y = {a:.1f}*sin({b:.1f}x + {c:.1f}) + {d:.1f}')
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_ylim(-6.0, 6.0)
        ax.legend(loc='upper right')
        ax.set_title("Sine Graph: y = a*sin(bx+c)+d")
        st.pyplot(fig)

        period = (2 * np.pi) / b
        max_val = abs(a) + d
        min_val = -abs(a) + d
        
        st.success(f"""
        📌 **현재 함수 분석 노트**
        - **주기(T):** $\\frac{{2\\pi}}{{|b|}} = \\frac{{2\\pi}}{{{b:.1f}}} \\approx {period:.2f}$
        - **최댓값:** $|a| + d = |{a:.1f}| + ({d:.1f}) = {max_val:.2f}$
        - **최솟값:** $-|a| + d = -|{a:.1f}| + ({d:.1f}) = {min_val:.2f}$
        """)

    # ----------------------------------------------------
    # 4. 코사인(Cosine) 그래프 조작: a*cos(bx+c)+d
    # ----------------------------------------------------
    elif menu == "4. 코사인(Cos) 그래프 완벽 조작: a·cos(bx+c)+d":
        st.title("📉 4. 코사인 그래프 완벽 탐구: $y = a \\cos(bx + c) + d$")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.slider("a (진폭/높낮이):", -3.0, 3.0, 1.0, 0.1, key="cos_a")
        with col2:
            b = st.slider("b (주기 결정):", 0.1, 3.0, 1.0, 0.1, key="cos_b")
        with col3:
            c = st.slider("c (x축 평행이동):", -np.pi, np.pi, 0.0, 0.1, key="cos_c")
        with col4:
            d = st.slider("d (y축 평행이동):", -3.0, 3.0, 0.0, 0.1, key="cos_d")

        x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
        y = a * np.cos(b * x + c) + d

        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.plot(x, y, color='dodgerblue', lw=2.5, label=f'y = {a:.1f}*cos({b:.1f}x + {c:.1f}) + {d:.1f}')
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_ylim(-6.0, 6.0)
        ax.legend(loc='upper right')
        ax.set_title("Cosine Graph: y = a*cos(bx+c)+d")
        st.pyplot(fig)

        period = (2 * np.pi) / b
        max_val = abs(a) + d
        min_val = -abs(a) + d
        
        st.info(f"""
        📌 **현재 함수 분석 노트**
        - **주기(T):** $\\frac{{2\\pi}}{{|b|}} = \\frac{{2\\pi}}{{{b:.1f}}} \\approx {period:.2f}$
        - **최댓값:** $|a| + d = |{a:.1f}| + ({d:.1f}) = {max_val:.2f}$
        - **최솟값:** $-|a| + d = -|{a:.1f}| + ({d:.1f}) = {min_val:.2f}$
        """)

    # ----------------------------------------------------
    # 5. 탄젠트(Tangent) 그래프 조작: a*tan(bx+c)+d
    # ----------------------------------------------------
    elif menu == "5. 탄젠트(Tan) 그래프 완벽 조작: a·tan(bx+c)+d":
        st.title("📐 5. 탄젠트 그래프 완벽 탐구: $y = a \\tan(bx + c) + d$")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.slider("a (기울기/수직배율):", -3.0, 3.0, 1.0, 0.1, key="tan_a")
        with col2:
            b = st.slider("b (주기 결정):", 0.1, 3.0, 1.0, 0.1, key="tan_b")
        with col3:
            c = st.slider("c (x축 평행이동):", -np.pi, np.pi, 0.0, 0.1, key="tan_c")
        with col4:
            d = st.slider("d (y축 평행이동):", -3.0, 3.0, 0.0, 0.1, key="tan_d")

        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = a * np.tan(b * x + c) + d
        
        # 점근선 부근 불연속선 튀는 문제 방지 마스킹
        y[np.abs(np.gradient(y)) > 50] = np.nan

        fig, ax = plt.subplots(figsize=(10, 4.5))
        ax.plot(x, y, color='forestgreen', lw=2.5, label=f'y = {a:.1f}*tan({b:.1f}x + {c:.1f}) + {d:.1f}')
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.set_ylim(-10, 10)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='upper right')
        ax.set_title("Tangent Graph: y = a*tan(bx+c)+d")
        st.pyplot(fig)

        period = np.pi / b
        st.warning(f"""
        📌 **탄젠트 특징 유의사항**
        - **탄젠트 주기(T):** $\\frac{{\\pi}}{{|b|}} = \\frac{{\\pi}}{{{b:.1f}}} \\approx {period:.2f}$ (사인/코사인의 절반!)
        - **최댓값/최솟값:** 실수 전체로 뻗어나가므로 **존재하지 않음**
        """)

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
