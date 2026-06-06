import streamlit as st
import pdfplumber
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("AI Resume Analyzer with OCR")


job_roles = {
    "Data Scientist": [
        "python", "sql", "machine learning",
        "data science", "pandas", "numpy"
    ],

    "Web Developer": [
        "html", "css", "javascript",
        "react", "node.js"
    ],

    "Java Developer": [
        "java", "spring", "mysql",
        "hibernate"
    ],

    "Python Developer": [
        "python", "django", "flask",
        "sql", "git"
    ]
}


selected_role = st.selectbox(
    "Select Job Role",
    list(job_roles.keys())
)

skills = job_roles[selected_role]


uploaded_file = st.file_uploader(
    "Upload Resume (PDF or Image)",
    type=["pdf", "png", "jpg", "jpeg"]
)


def extract_text_from_pdf(file):
    text = ""

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        st.error(f"PDF Error: {e}")

    return text


if uploaded_file is not None:

    text = ""
    file_type = uploaded_file.type

    
    if "pdf" in file_type:

        st.subheader("📄 PDF Uploaded")

        text = extract_text_from_pdf(uploaded_file)

        if text.strip() == "":
            st.warning("No text found in PDF. Using OCR...")

            try:
                uploaded_file.seek(0)

                with pdfplumber.open(uploaded_file) as pdf:
                    for page in pdf.pages:
                        img = page.to_image().original
                        text += pytesseract.image_to_string(img)

            except Exception as e:
                st.error(f"OCR Error: {e}")

  
    else:

        st.subheader("Image Uploaded")

        try:
            image = Image.open(uploaded_file).convert("L")

            st.image(image, caption="Uploaded Resume")

            text = pytesseract.image_to_string(image)

        except Exception as e:
            st.error(f"Image OCR Error: {e}")

    
    st.subheader("Extracted Resume Text")

    if text:
        st.write(text)
    else:
        st.error("No text extracted")

   
    if text.strip() != "":

        text = text.lower()

        found_skills = []
        missing_skills = []

        for skill in skills:

            if skill.lower() in text:
                found_skills.append(skill)

            else:
                missing_skills.append(skill)

        score = (len(found_skills) / len(skills)) * 100

        st.subheader("ATS Score")
        st.success(f"{score:.2f}%")

        if score >= 80:
            st.success("Excellent Resume")
        elif score >= 50:
            st.warning("Good Resume - Can Be Improved")
        else:
            st.error("Needs Improvement")

        st.subheader("Skills Found")
        st.write(found_skills)

        st.subheader("Missing Skills")
        st.write(missing_skills)

    else:
        st.error("No text detected. Check image quality or OCR setup.")
