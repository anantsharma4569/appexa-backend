"""Public API consumed by the appexa-frontend site.

Every endpoint here is readable by Guest on purpose: it only ever returns
published website content. The one write endpoint, submit_enquiry, validates
its input and inserts with a fixed source.
"""

import re

import frappe
from frappe import _

PHONE_RE = re.compile(r"^[6-9]\d{9}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$")

PURPOSES = (
	"Distributor or stockist enquiry",
	"Third-party manufacturing",
	"Product or price-list enquiry",
	"Job application",
	"Something else",
)

ORDER_BY = "display_order asc, creation asc"


def _published(doctype, fields, order_by=ORDER_BY, filters=None):
	conditions = {"published": 1}
	if filters:
		conditions.update(filters)
	return frappe.get_all(doctype, filters=conditions, fields=fields, order_by=order_by)


@frappe.whitelist(allow_guest=True)
def get_settings():
	settings = frappe.get_cached_doc("Appexa Settings")
	return {
		"company_name": settings.company_name,
		"tagline": settings.tagline,
		"cin": settings.cin,
		"iso_certification": settings.iso_certification,
		"address": settings.address,
		"city": settings.city,
		"state": settings.state,
		"pincode": settings.pincode,
		"phone": settings.phone,
		"whatsapp_number": settings.whatsapp_number,
		"email": settings.email,
		"business_hours": settings.business_hours,
		"facebook_url": settings.facebook_url,
		"instagram_url": settings.instagram_url,
		"linkedin_url": settings.linkedin_url,
	}


@frappe.whitelist(allow_guest=True)
def get_categories():
	return frappe.get_all(
		"Product Category",
		fields=["name", "category_name", "slug", "description"],
		order_by=ORDER_BY,
	)


@frappe.whitelist(allow_guest=True)
def get_products(category=None):
	filters = {"category": category} if category else None
	return _published(
		"Product",
		["name", "brand", "category", "composition", "dosage_form", "pack_size", "tag", "image"],
		filters=filters,
	)


@frappe.whitelist(allow_guest=True)
def get_team():
	departments = frappe.get_all("Department", fields=["name", "department_name"], order_by=ORDER_BY)
	members = _published(
		"Team Member",
		["name", "member_name", "designation", "department", "location", "photo"],
	)
	grouped = []
	for department in departments:
		people = [m for m in members if m.department == department.name]
		if people:
			grouped.append({"department": department.department_name, "members": people})
	return grouped


@frappe.whitelist(allow_guest=True)
def get_jobs():
	jobs = _published(
		"Job Opening",
		["name", "job_title", "location", "experience", "employment_type", "about"],
	)
	for job in jobs:
		job["duties"] = frappe.get_all(
			"Job Duty",
			filters={"parent": job["name"], "parenttype": "Job Opening"},
			fields=["duty"],
			order_by="idx asc",
			pluck="duty",
		)
		job["requirements"] = frappe.get_all(
			"Job Requirement",
			filters={"parent": job["name"], "parenttype": "Job Opening"},
			fields=["requirement"],
			order_by="idx asc",
			pluck="requirement",
		)
	return jobs


@frappe.whitelist(allow_guest=True)
def get_slides():
	return _published(
		"Hero Slide",
		[
			"name",
			"title",
			"slide_text",
			"image",
			"primary_cta_label",
			"primary_cta_link",
			"secondary_cta_label",
			"secondary_cta_link",
		],
	)


@frappe.whitelist(allow_guest=True)
def get_testimonials():
	return _published("Testimonial", ["name", "author", "author_role", "quote"])


@frappe.whitelist(allow_guest=True)
def get_faqs():
	return _published("FAQ Item", ["name", "question", "answer"])


@frappe.whitelist(allow_guest=True)
def get_whatsapp_topics():
	return _published("WhatsApp Topic", ["name", "topic_label", "message_template"])


@frappe.whitelist(allow_guest=True)
def get_home():
	"""Everything the home page needs, in one request."""
	return {
		"settings": get_settings(),
		"slides": get_slides(),
		"categories": get_categories(),
		"products": get_products(),
		"team": get_team(),
		"jobs": get_jobs(),
		"testimonials": get_testimonials(),
		"faqs": get_faqs(),
		"whatsapp_topics": get_whatsapp_topics(),
	}


@frappe.whitelist(allow_guest=True)
def submit_enquiry(
	purpose,
	full_name,
	phone,
	email,
	city=None,
	company=None,
	product_interest=None,
	position=None,
	experience=None,
	resume_link=None,
	message=None,
	consent=0,
):
	if purpose not in PURPOSES:
		frappe.throw(_("Please choose a valid purpose."))
	if not (full_name or "").strip():
		frappe.throw(_("Please enter your name."))

	phone = re.sub(r"\D", "", phone or "")[-10:]
	if not PHONE_RE.match(phone):
		frappe.throw(_("Enter a valid 10-digit mobile number."))
	if not EMAIL_RE.match((email or "").strip()):
		frappe.throw(_("Enter a valid email address."))

	enquiry = frappe.get_doc(
		{
			"doctype": "Enquiry",
			"purpose": purpose,
			"status": "New",
			"full_name": full_name.strip()[:140],
			"phone": phone,
			"email": email.strip(),
			"city": city,
			"company": company,
			"product_interest": product_interest,
			"position": position,
			"experience": experience,
			"resume_link": resume_link,
			"message": message,
			"consent": 1 if str(consent) in ("1", "true", "True", "on") else 0,
			"source": "Website",
		}
	)
	enquiry.insert(ignore_permissions=True)
	frappe.db.commit()
	return {"name": enquiry.name, "message": _("Thank you. We will get back to you shortly.")}
