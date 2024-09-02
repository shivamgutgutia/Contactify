from flask import send_file, request
import os

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def template():
    if request.args.get("filetype", "") == "xlsx":
        filePath = os.path.join(baseDir, "files", "Template - Excel Workbook.xlsx")
        return (
            send_file(
                filePath,
                mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                as_attachment=True,
                download_name="Template - Excel Workbook.xlsx",
            ),
            200,
        )
    elif request.args.get("filetype", "") == "xls":
        filePath = os.path.join(baseDir, "files", "Template - Excel.xls")
        return (
            send_file(
                filePath,
                mimetype="application/vnd.ms-excel",
                as_attachment=True,
                download_name="Template - Excel.xls",
            ),
            200,
        )

    elif request.args.get("filetype", "") == "csv":
        filePath = os.path.join(baseDir, "files", "Template - CSV.csv")
        return (
            send_file(
                filePath,
                mimetype="text/csv",
                as_attachment=True,
                download_name="Template - CSV.csv",
            ),
            200,
        )

    elif request.args.get("filetype", "") == "ods":
        filePath = os.path.join(baseDir, "files", "Template - ODS.ods")
        return (
            send_file(
                filePath,
                mimetype="application/vnd.oasis.opendocument.spreadsheet",
                as_attachment=True,
                download_name="Template - ODS.ods",
            ),
            200,
        )
    elif request.args.get("filetype", "") == "json":
        filePath = os.path.join(baseDir, "files", "Template - JSON.json")
        return (
            send_file(
                filePath,
                mimetype="application/json",
                as_attachment=True,
                download_name="Template - JSON.json",
            ),
            200,
        )
    else:
        filePath = os.path.join(baseDir, "files", "templates.zip")
        return (
            send_file(
                filePath,
                mimetype="application/zip",
                as_attachment=True,
                download_name="templates.zip",
            ),
            200,
        )
