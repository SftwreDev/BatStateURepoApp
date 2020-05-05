from django.db import models

from django.contrib.auth.models import AbstractUser



department = [
    ("CIT", "CIT"),
    ('CTE', 'CTE'),
    ('CABEIHM', 'CABEIHM'),
    ('CECS', 'CECS')
]

class Department(models.Model):
    department_choices = [
        ('Guidance and Counseling Office', 'Guidance and Counseling Office'),
        ('Scholarsip Office', 'Scholarsip Office'),
        ('Job and Placement Office', 'Job and Placement Office'),
        ('Testing and Admission Office', 'Testing and Admission Office'),
        ('Discipline Office', 'Discipline Office'),
        ('Resource Generation Office', 'Resource Generation Office'),
        ("Executive Director's Office", "Executive Director's Office"),
        ('Dean of Colleges Office', 'Dean of Colleges Office'),
        ('College of Accountacy, Business, Economics and Hospitality Management', 'College of Accountacy, Business, Economics and Hospitality Management'),
        ('College of Arts and Sciences', 'College of Arts and Sciences'),
        ('College of Engineering and Computing Sciences', 'College of Engineering and Computing Sciences'),
        ('College of Industrial Technology', 'College of Industrial Technology'),
        ('College of Teacher Education', 'College of Teacher Education'),
        ('Records Office', 'Records Office'),
        ('Extension Office', 'Extension Office'),
        ('Supply Office', 'Supply Office'),
        ('Procurement Office', 'Procurement Office'),
        ('Information Communication of Technology Office', 'Information Communication of Technology Office'),
        ('Library', 'Library'),
        ('Registrar Office', 'Registrar Office'),
        ('Human Resource Office', 'Human Resource Office'),
        ('Clinic', 'Clinic'),
        ('Cultural and Arts Office', 'Cultural and Arts Office'),
        ('Facilities and Maintenance Office', 'Facilities and Maintenance Office'),
    ]
    department = models.CharField(max_length=300, verbose_name = 'Department', choices=department_choices)


    def __str__(self):
        return self.department

class User(AbstractUser):
    is_authorized = models.BooleanField(default=False)


class DepartmentSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.ManyToManyField(Department)


    def __str__(self):
        return self.user.username

class DepartmentCode(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name='Department Code')
    department = models.OneToOneField(Department, on_delete=models.CASCADE)

    
class Documents_File(models.Model):

    types_of_records = [
        ('Accomplishment Report', 'Accomplishment Report'),
        ('Action Plan', 'Action Plan'),
        ('Application for Dean Lister', 'Application for Dean Lister'),
        ('Board Resolution', 'Board Resolution'),
        ('Certificates / Narrative Report of Seminars, Trainings and Conferences', 'Certificates / Narrative Report of Seminars, Trainings and Conferences'),
        ('CHED Memorandum Order', 'CHED Memorandum Order'),
        ('Class Attendance', 'Class Attendance'),
        ('Class Observation From Associate Dean / Program Chairperson', 'Class Observation From Associate Dean / Program Chairperson'),
        ('Class Schedule', 'Class Schedule'),
        ('Competency Assessment for Faculty and Employees', 'Competency Assessment for Faculty and Employees'),
        ('Computation of Grades', 'Computation of Grades'),
        ('Course Specifications', 'Course Specifications'),
        ('Daily Time Record', 'Daily Time Record'),
        ("Dean's Lister", "Dean's Lister"),
        ('Detailed Computation of Faculty Honorarium', 'Detailed Computation of Faculty Honorarium'),
        ('Details Computation of Teachers Performance', 'Details Computation of Teachers Performance'),
        ('Enrollment List', 'Enrollment List'),
        ('Evaluation Form','Evaluation Form'),
        ('Faculty Accomplishment Report', 'Faculty Accomplishment Report'),
        ('Faculty Development & Training Information Update', 'Faculty Development & Training Information Update'),
        ('Faculty Loadings', 'Faculty Loadings'),
        ('Faculty Performance Evalutaion', 'Faculty Performance Evalutaion'),
        ('Faculty Profile', 'Faculty Profile'),
        ('Faculty Special Assignment' , 'Faculty Special Assignment'),
        ('Incoming Communication from Students and CIT Family' , 'Incoming Communication from Students and CIT Family'),
        ('Incoming Communication/Memo from other Department Offices', 'Incoming Communication/Memo from other Department Offices'),
        ('Incoming Memos/Communications from Main Campus', 'Incoming Memos/Communications from Main Campus'),
        ('Incoming/Outgoing Communication', 'Incoming/Outgoing Communication'),
        ('Inventory Equipment and Furniture','Inventory Equipment and Furniture'),
        ('Investment Plan', 'Investment Plan'),
        ('Investment Plan Summary', 'Investment Plan Summary'),
        ('List of Faculty', 'List of Faculty'),
        ('List of OJT Placement Malvar Campus', 'List of OJT Placement Malvar Campus'),
        ('Major Examinations', 'Major Examinations'),
        ('Narrative Reports', 'Narrative Reports'),
        ('National Certificate Passer', 'National Certificate Passer'),
        ('NCPAR','NCPAR'),
        ('New Curriculum', 'New Curriculum'),
        ('New Curriculum Effective', 'New Curriculum Effective'),
        ('New Grading System', 'New Grading System'),
        ('OBQA (APP Guidelines)', 'OBQA (APP Guidelines)'),
        ('OBQA-PPP (Level III)', 'OBQA-PPP (Level III)'),
        ('OPCR', 'OPCR'),
        ('OPCR AND IPCR', 'OPCR AND IPCR'),
        ('OPCR Ratings', 'OPCR Ratings'),
        ('Operational Plans', 'Operational Plans'),
        ('Report of Grades', 'Report of Grades'),
        ('Schedule of Examinations', 'Schedule of Examinations'),
        ('Service Request and Preventive Maintenance Checklist and Action Record', 'Service Request and Preventive Maintenance Checklist and Action Record'),
        ('Strategic Plan', 'Strategic Plan'),
        ('Syllabus', 'Syllabus'),
        ('Table of Specifications', 'Table of Specifications'),
        ('Thesis Advising', 'Thesis Advising'),
        ('Training and Development Plan', 'Training and Development Plan'),
    ]

    types_of_documents = [
        ('Controlled', 'Controlled'),
        ('Not Controlled', 'Not Controlled'),
    ]


    types_of_record = models.CharField(max_length=500, choices=types_of_records,verbose_name='Types of Records')
    is_controlled = models.BooleanField(default=False, blank=False, verbose_name='Controlled')
    identification_label = models.CharField(max_length = 300, verbose_name='Identification Label', unique=True)
    box_no = models.CharField(max_length = 300, verbose_name='Box No.',  unique=True)
    label = models.CharField(max_length = 300, verbose_name='Box Label',  unique=True)
    retention = models.CharField(max_length=200, blank=False, verbose_name='Retention')
    department = models.ForeignKey(Department,on_delete=models.CASCADE,  verbose_name = 'department')
    date_uploaded = models.DateField(auto_now = True)

    document_file = models.FileField(upload_to = 'documents/')


    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = 'Documents'


class LogBook(models.Model):
    referrence_no = models.CharField(max_length=200, verbose_name = 'Referrence No.')
    tracking_id = models.CharField(max_length=200, verbose_name = 'Tracking ID')
    document_description = models.CharField(max_length=300, verbose_name='Document Description')
    date_forwarded = models.DateField(auto_now = True)
    forwarded_by = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='forwarded_by',verbose_name='Forwarded By')
    date_received = models.DateField(auto_now = True)
    date_returned = models.DateField(auto_now = False, blank=True,null=True, help_text="example: 01/12/2020")
    received_by = models.ForeignKey(Department,on_delete=models.CASCADE, related_name='received_by',verbose_name='Received By')
