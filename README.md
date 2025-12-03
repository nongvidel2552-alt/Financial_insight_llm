## Financial Insight LLM Engine

# 🚀 Features

วิเคราะห์รายจ่าย/รายได้สุทธิต่อเดือน
-> คำนวณ Needs/Wants/Savings % (50/30/20 rules), DSR, Survival Ratio, Health Score
ตรวจจับหมวด culprit ที่ทำให้ค่าใช้จ่ายสูง,คำนวณเงินที่เกินกรอบมาตรฐานแบบ 50/30/20

LLM(Typhoon) สร้างข้อความสรุปให้ 3 ส่วน

left_panel → จุดอ่อนหลัก

middle_panel → ความแข็งแรงทางการเงิน

right_panel → คำแนะนำ actionable

-> อันนี้ข้อความแสดงตามตำแหน่งที่จะแสดงผลบน [Dashboard]

# 📁 Project Structure
Financial_insight_salary_after_tax/
│
├── nic_analyzer.py        # วิเคราะห์ตัวเลขทั้งหมด + การคำนวณ score
├── llm_client.py          # เชื่อม Typhoon + System/User Prompt
├── playground.py          # ตัวอย่างการใช้งาน
├── requirements.txt       # รายชื่อ dependencies
└── README.md              # ไฟล์อธิบายโปรเจ็กต์ (ไฟล์นี้)

