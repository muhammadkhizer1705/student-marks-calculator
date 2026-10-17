
import html
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Student Marks Calculator",
    page_icon="🎓",
    layout="centered"
)

# Modern HTML and CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f7ff, #eef2ff);
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(120deg, #4338ca, #7c3aed);
    padding: 30px 24px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 10px 25px rgba(67, 56, 202, 0.18);
}

.hero h1 {
    color: white;
    font-size: 32px;
    margin: 0;
}

.hero p {
    color: #ede9fe;
    margin: 10px 0 0;
}

.section-title {
    color: #312e81;
    font-size: 21px;
    font-weight: 700;
    margin: 22px 0 12px;
}

.result-card {
    background: white;
    padding: 22px 12px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #e0e7ff;
    box-shadow: 0 5px 18px rgba(31, 41, 55, 0.05);
    min-height: 110px;
}

.result-card h4 {
    color: #64748b;
    font-size: 14px;
    margin: 0 0 12px;
}

.result-card h2 {
    color: #4338ca;
    font-size: 28px;
    margin: 0;
}

.result-card p {
    color: #64748b;
    margin: 8px 0 0;
}

.result-banner {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e0e7ff;
    text-align: center;
    margin-top: 20px;
}

.stButton > button {
    background: linear-gradient(90deg, #4338ca, #7c3aed);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-weight: 600;
    min-height: 48px;
}

.stButton > button:hover {
    color: white;
    border: 1px solid #4338ca;
}

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    border-radius: 9px;
}

div[data-testid="stProgressBar"] > div > div {
    background: #6366f1;
}
</style>

<div class="hero">
    <h1>🎓 Student Marks Calculator</h1>
    <p>Your academic performance, simplified.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📝 Student Information</div>',
    unsafe_allow_html=True
)

name = st.text_input(
    "Student Name",
    placeholder="Enter your full name"
)

st.markdown(
    '<div class="section-title">📚 Enter Your Marks</div>',
    unsafe_allow_html=True
)

st.caption("Enter marks out of 100 for each subject.")

subjects = [
    "Artificial Intelligence",
    "Python Programming",
    "Database Systems",
    "Mathematics",
    "English"
]

marks = []

# Two-column input layout
for i in range(0, len(subjects), 2):
    columns = st.columns(2)

    for j, column in enumerate(columns):
        index = i + j

        if index < len(subjects):
            with column:
                mark = st.number_input(
                    subjects[index],
                    min_value=0,
                    max_value=100,
                    value=0,
                    step=1,
                    key=f"mark_{index}"
                )
                marks.append((index, mark))

# Restore subject order
marks.sort(key=lambda item: item[0])
marks = [mark for _, mark in marks]

if st.button("✨ Calculate My Result", use_container_width=True):
    if not name.strip():
        st.error("Please enter the student's name.")

    else:
        total = sum(marks)
        percentage = total / 5

        if percentage >= 80:
            grade = "A+"
            message = "Outstanding performance!"
        elif percentage >= 70:
            grade = "A"
            message = "Excellent work!"
        elif percentage >= 60:
            grade = "B"
            message = "Good job! Keep improving."
        elif percentage >= 50:
            grade = "C"
            message = "You passed. Keep practising!"
        else:
            grade = "F"
            message = "Keep working hard and try again."

        result = "PASS" if percentage >= 50 else "FAIL"

        st.session_state["student_result"] = {
            "name": name.strip(),
            "total": total,
            "percentage": percentage,
            "grade": grade,
            "result": result,
            "message": message,
            "marks": marks.copy()
        }

# Display calculated result
if "student_result" in st.session_state:
    data = st.session_state["student_result"]

    st.markdown("---")
    st.markdown(
        '<div class="section-title">📊 Your Performance</div>',
        unsafe_allow_html=True
    )

    safe_name = html.escape(data["name"])

    st.markdown(f"""
    <div class="result-banner">
        <h2 style="color:#312e81; margin:0;">
            {safe_name}
        </h2>
        <p style="color:#64748b;">
            Here is your academic summary
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f"""
        <div class="result-card">
            <h4>🏆 Total Marks</h4>
            <h2>{data["total"]}/500</h2>
            <p>Across 5 subjects</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="result-card">
            <h4>📈 Percentage</h4>
            <h2>{data["percentage"]:.1f}%</h2>
            <p>Overall score</p>
        </div>
        """, unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        st.markdown(f"""
        <div class="result-card">
            <h4>🎯 Final Grade</h4>
            <h2>{data["grade"]}</h2>
            <p>Grade category</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        result_color = (
            "#15803d" if data["result"] == "PASS" else "#dc2626"
        )

        st.markdown(f"""
        <div class="result-card">
            <h4>📋 Result</h4>
            <h2 style="color:{result_color};">
                {data["result"]}
            </h2>
            <p>Academic status</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### 📊 Overall Progress")
    st.progress(data["percentage"] / 100)
    st.caption(data["message"])

    with st.expander("View subject-wise marks"):
        for subject, mark in zip(subjects, data["marks"]):
            st.write(f"**{subject}:** {mark}/100")
            st.progress(mark / 100)

    report = (
        "STUDENT MARKS REPORT\n"
        f"Name: {data['name']}\n"
        f"Total: {data['total']}/500\n"
        f"Percentage: {data['percentage']:.1f}%\n"
        f"Grade: {data['grade']}\n"
        f"Result: {data['result']}\n\n"
        + "\n".join(
            f"{subject}: {mark}/100"
            for subject, mark in zip(subjects, data["marks"])
        )
    )

    st.download_button(
        "⬇️ Download Result Report",
        data=report,
        file_name="student_result.txt",
        mime="text/plain",
        use_container_width=True
    )

st.markdown("---")
st.caption("Student Marks Calculator • Built with Python, Streamlit & CSS")
