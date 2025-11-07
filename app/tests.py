import os

template_file = "..\\templates\\contracts\\rental_agreement.docx"
print(os.path.exists(template_file))
print(os.path.getsize(template_file))