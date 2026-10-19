"""Create the Appexa website doctypes. Run once with bench execute."""

import frappe

MODULE = "Appexa"

MANAGER = {
	"role": "System Manager",
	"read": 1,
	"write": 1,
	"create": 1,
	"delete": 1,
	"report": 1,
	"export": 1,
	"print": 1,
	"email": 1,
	"share": 1,
}
PUBLIC_READ = {"role": "Guest", "read": 1}


def f(fieldname, label, fieldtype="Data", **kw):
	field = {"fieldname": fieldname, "label": label, "fieldtype": fieldtype}
	field.update(kw)
	return field


ORDER = f("display_order", "Display Order", "Int", description="Lower numbers appear first")
PUBLISHED = f("published", "Published", "Check", default="1")

DOCTYPES = [
	{
		"name": "Product Category",
		"autoname": "field:category_name",
		"title_field": "category_name",
		"public": True,
		"fields": [
			f("category_name", "Category Name", reqd=1, unique=1, in_list_view=1),
			f("slug", "Slug", unique=1, in_list_view=1, description="Used in the frontend URL, e.g. tablets"),
			f("description", "Description", "Small Text"),
			ORDER,
		],
	},
	{
		"name": "Product",
		"autoname": "field:brand",
		"title_field": "brand",
		"public": True,
		"fields": [
			f("brand", "Brand", reqd=1, unique=1, in_list_view=1),
			f("category", "Category", "Link", options="Product Category", reqd=1, in_list_view=1, in_standard_filter=1),
			f("composition", "Composition", "Small Text", reqd=1, in_list_view=1),
			f("dosage_form", "Dosage Form", description="e.g. Film-coated tablet, Oral suspension"),
			f("pack_size", "Pack Size", description="e.g. 10 x 10 Alu-Alu"),
			f("tag", "Tag", description="Optional badge shown on the card, e.g. New"),
			f("image", "Image", "Attach Image"),
			PUBLISHED,
			ORDER,
		],
	},
	{
		"name": "Department",
		"autoname": "field:department_name",
		"title_field": "department_name",
		"public": True,
		"fields": [
			f("department_name", "Department Name", reqd=1, unique=1, in_list_view=1),
			ORDER,
		],
	},
	{
		"name": "Team Member",
		"autoname": "format:TM-{####}",
		"title_field": "designation",
		"public": True,
		"fields": [
			f("member_name", "Name", in_list_view=1, description="Leave blank to show the role only"),
			f("designation", "Designation", reqd=1, in_list_view=1),
			f("department", "Department", "Link", options="Department", reqd=1, in_list_view=1, in_standard_filter=1),
			f("location", "Location", in_list_view=1),
			f("photo", "Photo", "Attach Image"),
			PUBLISHED,
			ORDER,
		],
	},
	{
		"name": "Job Duty",
		"istable": 1,
		"fields": [f("duty", "Duty", "Small Text", reqd=1, in_list_view=1)],
	},
	{
		"name": "Job Requirement",
		"istable": 1,
		"fields": [f("requirement", "Requirement", "Small Text", reqd=1, in_list_view=1)],
	},
	{
		"name": "Job Opening",
		"autoname": "field:job_title",
		"title_field": "job_title",
		"public": True,
		"fields": [
			f("job_title", "Job Title", reqd=1, unique=1, in_list_view=1),
			f("location", "Location", in_list_view=1),
			f("experience", "Experience", in_list_view=1, description="e.g. 3-6 years"),
			f(
				"employment_type",
				"Employment Type",
				"Select",
				options="Full-time\nPart-time\nContract\nInternship",
				default="Full-time",
				in_list_view=1,
			),
			f("about", "About the Role", "Small Text"),
			f("duties_section", "Responsibilities", "Section Break"),
			f("duties", "Duties", "Table", options="Job Duty"),
			f("requirements_section", "Requirements", "Section Break"),
			f("requirements", "Requirements", "Table", options="Job Requirement"),
			f("settings_section", "Settings", "Section Break"),
			PUBLISHED,
			ORDER,
		],
	},
	{
		"name": "Enquiry",
		"autoname": "format:ENQ-{YYYY}-{#####}",
		"title_field": "full_name",
		"fields": [
			f(
				"purpose",
				"Purpose",
				"Select",
				options=(
					"Distributor or stockist enquiry\nThird-party manufacturing\n"
					"Product or price-list enquiry\nJob application\nSomething else"
				),
				reqd=1,
				in_list_view=1,
				in_standard_filter=1,
			),
			f(
				"status",
				"Status",
				"Select",
				options="New\nIn Progress\nClosed",
				default="New",
				in_list_view=1,
				in_standard_filter=1,
			),
			f("contact_section", "Contact", "Section Break"),
			f("full_name", "Full Name", reqd=1, in_list_view=1),
			f("phone", "Phone", reqd=1, in_list_view=1),
			f("email", "Email", "Data", options="Email", reqd=1),
			f("city", "City and State"),
			f("business_section", "Business", "Section Break"),
			f("company", "Firm or Organisation"),
			f("product_interest", "Product or Range of Interest"),
			f("job_section", "Job Application", "Section Break"),
			f("position", "Position Applying For"),
			f("experience", "Years of Experience"),
			f("resume_link", "CV Link", "Data", options="URL"),
			f("message_section", "Message", "Section Break"),
			f("message", "Message", "Small Text"),
			f("consent", "Consent Given", "Check"),
			f("source", "Source", default="Website", read_only=1),
		],
	},
	{
		"name": "Hero Slide",
		"autoname": "format:SLIDE-{###}",
		"title_field": "title",
		"public": True,
		"fields": [
			f("title", "Title", "Small Text", reqd=1, in_list_view=1),
			f("slide_text", "Text", "Small Text"),
			f("image", "Image", "Attach Image"),
			f("primary_cta_section", "Primary Button", "Section Break"),
			f("primary_cta_label", "Label"),
			f("primary_cta_link", "Link", default="/contact"),
			f("secondary_cta_section", "Secondary Button", "Section Break"),
			f("secondary_cta_label", "Label"),
			f("secondary_cta_link", "Link"),
			f("settings_section", "Settings", "Section Break"),
			PUBLISHED,
			ORDER,
		],
	},
	{
		"name": "Testimonial",
		"autoname": "format:TST-{###}",
		"title_field": "author",
		"public": True,
		"fields": [
			f("author", "Author", reqd=1, in_list_view=1),
			f("author_role", "Role and Location", in_list_view=1, description="e.g. Distributor, New Delhi"),
			f("quote", "Quote", "Text", reqd=1),
			PUBLISHED,
			ORDER,
		],
	},
	{
		"name": "FAQ Item",
		"autoname": "format:FAQ-{###}",
		"title_field": "question",
		"public": True,
		"fields": [
			f("question", "Question", "Small Text", reqd=1, in_list_view=1),
			f("answer", "Answer", "Text", reqd=1),
			PUBLISHED,
			ORDER,
		],
	},
	{
		"name": "WhatsApp Topic",
		"autoname": "field:topic_label",
		"title_field": "topic_label",
		"public": True,
		"fields": [
			f("topic_label", "Label", reqd=1, unique=1, in_list_view=1),
			f(
				"message_template",
				"Message Template",
				"Small Text",
				reqd=1,
				description="Pre-filled WhatsApp message. Use ____ for blanks the sender fills in.",
			),
			PUBLISHED,
			ORDER,
		],
	},
	{
		"name": "Appexa Settings",
		"issingle": 1,
		"public": True,
		"fields": [
			f("company_name", "Company Name", default="Appexa Pharmaceuticals Private Limited"),
			f("tagline", "Tagline", "Small Text"),
			f("credentials_section", "Credentials", "Section Break"),
			f("cin", "CIN", default="U46497UP2025PTC234028"),
			f("iso_certification", "ISO Certification", default="ISO 9001:2015"),
			f("address_section", "Address", "Section Break"),
			f("address", "Address", "Small Text", default="Gandhi Nagar"),
			f("city", "City", default="Muzaffarnagar"),
			f("state", "State", default="Uttar Pradesh"),
			f("pincode", "Pincode", default="251001"),
			f("contact_section", "Contact", "Section Break"),
			f("phone", "Phone", default="+91 90681 88171"),
			f("whatsapp_number", "WhatsApp Number", default="919068188171", description="Digits only, with country code"),
			f("email", "Email", "Data", options="Email", default="info@appexapharmaceuticals.in"),
			f("business_hours", "Business Hours", "Small Text", default="Monday to Saturday, 8:00 am - 7:00 pm"),
			f("social_section", "Social", "Section Break"),
			f("facebook_url", "Facebook URL", "Data", options="URL"),
			f("instagram_url", "Instagram URL", "Data", options="URL"),
			f("linkedin_url", "LinkedIn URL", "Data", options="URL"),
		],
	},
]


def create_doctypes():
	for spec in DOCTYPES:
		name = spec["name"]
		if frappe.db.exists("DocType", name):
			print(f"skip  {name} (exists)")
			continue

		permissions = [dict(MANAGER)]
		if spec.get("public"):
			permissions.append(dict(PUBLIC_READ))

		doc = {
			"doctype": "DocType",
			"name": name,
			"module": MODULE,
			"custom": 0,
			"istable": spec.get("istable", 0),
			"issingle": spec.get("issingle", 0),
			"fields": spec["fields"],
			"permissions": [] if spec.get("istable") else permissions,
		}
		for key in ("autoname", "title_field"):
			if spec.get(key):
				doc[key] = spec[key]
		if spec.get("title_field"):
			doc["show_title_field_in_link"] = 1
		if not spec.get("istable") and not spec.get("issingle"):
			doc["track_changes"] = 1
			doc["sort_field"] = "modified"
			doc["sort_order"] = "DESC"

		frappe.get_doc(doc).insert()
		print(f"made  {name}")

	frappe.db.commit()
	print("done")
