from flask import Blueprint
from controllers.index import *
router = Blueprint('router', __name__)

router.add_url_rule('/', 'home', home,methods=["GET"])
router.add_url_rule('/ping', 'ping', ping,methods=["GET"])
router.add_url_rule("/api/headers","headers",headers,methods=["POST"])
router.add_url_rule("/api/vcf","vcf",vcf,methods=["POST"])
router.add_url_rule("/api/template","template",template,methods=["GET"])