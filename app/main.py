from app.services.docx_service import fill_docx_template
from app.services.pdf_service import docx_to_pdf

if __name__ == "__main__":
    template_file = "..\\templates\\contracts\\rental2.docx"

    context = {
        "CONTRACT_CITY": "Москва",
        "CONTRACT_DATE": "25 ноября 2025 г.",
        "LANDLORD_FULL_NAME": "Иванов Иван Иванович",
        "LANDLORD_PASSPORT_SERIES": "45 00",
        "LANDLORD_PASSPORT_NUMBER": "123456",
        "LANDLORD_PASSPORT_ISSUED_BY": "ОВД района Центральный г. Москвы",
        "LANDLORD_ADDRESS": "г. Москва, ул. Тверская, д. 1, кв. 1",
        "TENANT_FULL_NAME": "Петров Пётр Петрович",
        "TENANT_PASSPORT_SERIES": "46 00",
        "TENANT_PASSPORT_NUMBER": "654321",
        "TENANT_PASSPORT_ISSUED_BY": "ОВД района Басманный г. Москвы",
        "TENANT_ADDRESS": "г. Москва, ул. Арбат, д. 5, кв. 10",
        "APARTMENT_ADDRESS": "г. Москва, ул. Новый Арбат, д. 15, кв. 35",
        "START_DATE": "01 декабря 2025 г.",
        "END_DATE": "01 декабря 2026 г.",
        "MONTHLY_RENT": "85000",
        "PREPAID_PROCENT": "100",
        "PREPAID_AMOUNT": "85000",
        "PREPAID_PERIOD": "один месяц",
        "DAYS_FOR_PAYMENT": "5",
        "DEPOSIT_AMOUNT": "85000",
        "DAY_END_CONTRACT": "30",
        "RENEWAL_NOTICE_DAYS": "60",
        "TERMINATION_NOTICE_DAYS": "30",
        "TERMINATION_DATE": "01 марта 2026 г.",
        "FORCE_MAJEURE_NOTICE_DAYS": "10",
        "FREE_STAY_DAYS": "14",
        "LANDLORD_VISITS_PER_MONTH": "1",
        "ADDITIONAL_RESIDENTS": "нет",
        "OWNERSHIP_TYPE": "частной собственности"
    }

    filled_docx = "..\\generated\\temp\\filled_rental_agreement.docx"
    output_pdf = "..\\generated\\output\\rental_agreement.pdf"

    fill_docx_template(str(template_file), context, str(filled_docx))
    docx_to_pdf(str(filled_docx), str(output_pdf))

    print("\nГотово! PDF-документ создан.")