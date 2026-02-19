from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        self.set_font('Arial', 'B', 18)
        self.cell(0, 10, 'Harsharaj S Shetty', 0, 1, 'C')

        self.set_font('Arial', '', 10)
        self.cell(0, 5, '+91-8304969843 | harsharajsshetty@gmail.com', 0, 1, 'C')
        self.cell(0, 5, 'LinkedIn: linkedin.com/in/harsharaj-s-shetty', 0, 1, 'C')
        self.ln(8)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 8, title, 0, 1, 'L', True)
        self.ln(3)

    def sub_heading(self, title, org, duration):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 5, title, 0, 1)

        self.set_font('Arial', 'I', 9)
        self.cell(0, 5, org + ' | ' + duration, 0, 1)
        self.ln(1)

    def bullet(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, '- ' + text)

    def project_title(self, title, tech):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 5, title, 0, 1)

        self.set_font('Arial', 'I', 9)
        self.cell(0, 5, 'Tech Stack: ' + tech, 0, 1)
        self.ln(1)


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# EDUCATION
pdf.section_title('EDUCATION')
pdf.sub_heading(
    'Bachelor of Engineering - Information Science',
    'Srinivas Institute of Technology, Mangalore',
    '2021 - 2025'
)
pdf.bullet('CGPA: 8.51')
pdf.ln(4)

# EXPERIENCE
pdf.section_title('EXPERIENCE')
pdf.sub_heading(
    'AI Operator Intern (Healthcare AI Ops)',
    'Xtransmatrix Consulting Services Pvt. Ltd.',
    'Oct 2025 - Jan 2026'
)
pdf.bullet('Performed Human-in-the-Loop AI operations for a US healthcare project.')
pdf.bullet('Ensured data accuracy, intent validation, and compliance benchmarks.')
pdf.bullet('Provided structured feedback to improve model performance.')
pdf.ln(3)

pdf.sub_heading(
    'Quality Engineering - Automation Testing Intern',
    'MResult Technologies, Mangalore',
    'Feb 2025 - May 2025'
)
pdf.bullet('Automated SAP Fiori test cases using Unified Test Framework (UTF).')
pdf.bullet('Handled test planning, execution, and defect tracking.')
pdf.bullet('Collaborated with developers to improve automation efficiency.')
pdf.ln(4)

# PROJECTS
pdf.section_title('PROJECTS')
pdf.project_title(
    'AI-Based Brain Tumor Detection',
    'Python, TensorFlow, Keras, React'
)
pdf.bullet('Developed CNN model for brain tumor classification using MRI scans.')
pdf.bullet('Integrated ML model with React UI for real-time predictions.')
pdf.bullet('Project sponsored by KSCST.')
pdf.ln(3)

pdf.project_title(
    'E-Commerce Application - Automation Testing',
    'Selenium WebDriver, Python'
)
pdf.bullet('Automated login, cart, checkout workflows.')
pdf.bullet('Improved regression testing coverage and UI validation.')
pdf.ln(3)

pdf.project_title(
    'Enhanced Document Image Binarization',
    'Python, PyTorch, Tesseract'
)
pdf.bullet('Improved document readability and OCR accuracy.')
pdf.bullet('Compared and benchmarked binarization techniques.')
pdf.ln(4)

# SKILLS
pdf.section_title('TECHNICAL SKILLS')
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 5, 'Programming: Java, Python')
pdf.multi_cell(0, 5, 'Automation and Testing: Selenium WebDriver, UTF, QA Automation')
pdf.multi_cell(0, 5, 'Frameworks and Tools: TensorFlow, PyTorch, MERN Stack, Git, Docker')
pdf.multi_cell(0, 5, 'Databases: MySQL, MongoDB')
pdf.ln(3)

# CERTIFICATIONS
pdf.section_title('CERTIFICATIONS')
pdf.bullet('IBM DevOps Fundamentals')
pdf.bullet('IT Specialist - Python (Certiport)')
pdf.bullet('Data Science Using Python - Intel')
pdf.bullet('AWS Cloud Fundamentals - Eduskills')

pdf.output('Harsharaj_Shetty_Resume.pdf')
print('Resume PDF generated successfully!')
