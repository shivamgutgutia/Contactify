from flask import request, Response
import vobject
import csv
import io


def vcf2csv():
    if "file" not in request.files or not request.files["file"]:
        return "No file uploaded", 400
    file = request.files["file"]
    if not file.filename.lower().endswith(".vcf"):
        return "Invalid file type. Only VCF files are allowed", 400

    vcfFile = vobject.readComponents(file.read().decode("utf-8"))
    csvFile = io.StringIO()
    writer = csv.writer(csvFile)
    writer.writerow(
        [
            "Prefix",
            "First Name",
            "Middle Name",
            "Last Name",
            "Suffix",
            "Phone Number",
            "Email Address",
            "Gender",
        ]
    )
    for entry in vcfFile:

        # name
        prefix, firstName, middleName, lastName, suffix = (
            entry.n.value.prefix or None,
            entry.n.value.given or None,
            entry.n.value.additional or None,
            entry.n.value.family or None,
            entry.n.value.suffix or None,
        )

        # Extract phone numbers
        phone = (
            "/".join([tel.value for tel in entry.tel_list])
            if hasattr(entry, "tel")
            else None
        )

        # Extract emails
        email = (
            "/".join([email.value for email in entry.email_list])
            if hasattr(entry, "email")
            else None
        )

        # Extract gender (if available)
        genderMap={
            "M":"Male",
            "F":"Female",
            "U":"Unknown",
            "O":"Other",
            "N":"None",
            None:""
        }
        gender = genderMap.get(entry.gender.value if hasattr(entry, "gender") else None,"")

        writer.writerow(
            [prefix, firstName, middleName, lastName, suffix, phone, email, gender]
        )

    csvFile.seek(0)
    return Response(
            csvFile,
            mimetype='text/csv',
            headers={"Content-Disposition": "attachment;filename=contacts.csv"}
        )
