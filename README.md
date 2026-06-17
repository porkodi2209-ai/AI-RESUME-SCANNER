# AI Resume Analyzer with OCR

## Overview

AI Resume Analyzer with OCR is a web-based application that analyzes resumes in both PDF and image formats. The system uses Optical Character Recognition (OCR) to extract text from scanned resumes and evaluates the resume against role-specific skill requirements.

The application calculates an ATS (Applicant Tracking System) score, identifies matching skills, and highlights missing skills required for a selected job role.

---

## Features

- Upload resumes in PDF format
- Upload scanned resumes as images (JPG, JPEG, PNG)
- OCR-based text extraction using Tesseract
- Role-specific resume analysis
- ATS score calculation
- Skill matching and missing skill detection
- User-friendly Streamlit interface

---

## Technologies Used

- Python
- Streamlit
- PDFPlumber
- PyTesseract
- Pillow (PIL)
- OCR (Optical Character Recognition)

---

## Supported Job Roles

### Data Scientist
- Python
- SQL
- Machine Learning
- Data Science
- Pandas
- NumPy

### Web Developer
- HTML
- CSS
- JavaScript
- React
- Node.js

### Java Developer
- Java
- Spring
- MySQL
- Hibernate

### Python Developer
- Python
- Django
- Flask
- SQL
- Git

---

## System Workflow

1. User selects a target job role.
2. User uploads a resume (PDF or Image).
3. The system extracts text from the resume.
4. OCR is applied for scanned image resumes.
5. Extracted content is analyzed against role-specific skills.
6. ATS score is calculated.
7. Matching and missing skills are displayed.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd resume-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Requirements

```txt
streamlit
pdfplumber
pytesseract
pillow
```

---

## Project Structure

```text
resume-ai/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resume.pdf
```

---

## Live Demo

🔗 Website Link: http://localhost:8501
## Watch Demo
https://github.com/porkodi2209-ai/AI-RESUME-SCANNER/issues/1

## Screenshots
## WEBSITE 

<img width="1920" height="1080" alt="Screenshot (32)" src="https://github.com/user-attachments/assets/e34dd003-669f-4be5-badc-cf8d5712e5ae" />

## Excellent Resume Result

<img width="607" height="788" alt="Screenshot (31)" src="https://github.com/user-attachments/assets/db3cf4fc-19ad-4d7d-b16a-052cca1b49f2" />

<img width="1920" height="1080" alt="Screenshot (33)" src="https://github.com/user-attachments/assets/1512ca11-d78c-4746-bf11-e7ca982df5a8" />

## Improvement Needed Resume


<img width="1920" height="1080" alt="Screenshot (34)" src="https://github.com/user-attachments/assets/9b12d7c3-5a97-40e6-a0f9-364142ac18d1" />

## Future Enhancements

- AI-powered resume recommendations
- Resume ranking system
- Job description matching
- Resume improvement suggestions
- Skill gap analysis
- Resume keyword optimization

---

## Conclusion

This project demonstrates the application of OCR and ATS-based resume evaluation techniques to automate resume screening. The system helps candidates understand how well their resumes align with specific job roles and provides insights into missing skills that can improve employability.

---

## Developed By

Porkodi

Department of Computer Science and AI
