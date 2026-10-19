"""Seed the Appexa website content from the approved design.

Product names, compositions and pack sizes came from the design mock-up and
are sample data — check each one against your licence before going live.
Run with: bench --site <site> execute appexa.setup.seed.seed_all
"""

import frappe

CATEGORIES = [
	("Tablets", "tablets"),
	("Capsules", "capsules"),
	("Syrups & suspensions", "syrups"),
	("Injectables", "injectables"),
	("Ointments, creams & gels", "topicals"),
	("Nutraceuticals", "nutra"),
]

CAT = {
	"tablets": "Tablets",
	"capsules": "Capsules",
	"syrups": "Syrups & suspensions",
	"injectables": "Injectables",
	"topicals": "Ointments, creams & gels",
	"nutra": "Nutraceuticals",
}

PRODUCTS = [
	("tablets", "Apexcef-200", "Cefixime 200 mg", "Film-coated tablet", "10 x 10 Alu-Alu"),
	("tablets", "Apexmol-650", "Paracetamol 650 mg", "Tablet", "15 x 10 blister"),
	("tablets", "Apexpan-40", "Pantoprazole 40 mg", "Enteric-coated tablet", "10 x 10 Alu-Alu"),
	("tablets", "Apexmont-LC", "Montelukast 10 mg + Levocetirizine 5 mg", "Tablet", "10 x 10 Alu-Alu"),
	("tablets", "Apexclav-625", "Amoxicillin 500 mg + Clavulanic acid 125 mg", "Film-coated tablet", "1 x 10 Alu-Alu"),
	("tablets", "Apexzith-500", "Azithromycin 500 mg", "Film-coated tablet", "1 x 3 Alu-Alu"),
	("tablets", "Apexnac-P", "Aceclofenac 100 mg + Paracetamol 325 mg", "Tablet", "10 x 10 blister"),
	("tablets", "Apexfer-XT", "Ferrous ascorbate 100 mg + Folic acid 1.5 mg", "Film-coated tablet", "10 x 10 Alu-Alu"),
	("tablets", "Apexcetri-10", "Cetirizine 10 mg", "Tablet", "20 x 10 blister"),
	("capsules", "Apexome-D", "Omeprazole 20 mg + Domperidone 30 mg (SR)", "Hard gelatin capsule", "10 x 10 Alu-Alu"),
	("capsules", "Apexgaba-NT", "Pregabalin 75 mg + Nortriptyline 10 mg", "Hard gelatin capsule", "10 x 10 Alu-Alu"),
	("capsules", "Apexflu-150", "Fluconazole 150 mg", "Capsule", "1 x 1"),
	("capsules", "Apexvit-AX", "Multivitamin with antioxidants and minerals", "Softgel capsule", "10 x 10 blister"),
	("capsules", "Apexdoxy-100", "Doxycycline 100 mg + Lactic acid bacillus", "Capsule", "10 x 10 Alu-Alu"),
	("syrups", "Apexmol Syrup", "Paracetamol 250 mg / 5 ml", "Oral suspension", "60 ml bottle"),
	("syrups", "Apexcef-O DS", "Cefixime 50 mg + Ofloxacin 50 mg / 5 ml", "Dry syrup", "30 ml bottle"),
	("syrups", "Apexzyme", "Digestive enzyme blend", "Oral liquid", "200 ml bottle"),
	("syrups", "Apexiron Syrup", "Iron + Folic acid + Vitamin B12", "Oral suspension", "200 ml bottle"),
	("syrups", "Apexcof-DX", "Dextromethorphan + Chlorpheniramine + Phenylephrine", "Cough syrup", "100 ml bottle"),
	("syrups", "Apexcal-D3", "Calcium carbonate + Vitamin D3", "Oral suspension", "200 ml bottle"),
	("injectables", "Apexcef-IV 1 g", "Ceftriaxone 1000 mg", "Dry powder vial with WFI", "1 vial pack"),
	("injectables", "Apexson-2", "Ondansetron 2 mg / ml", "Ampoule", "2 ml x 5"),
	("injectables", "Apexpan-IV 40", "Pantoprazole 40 mg", "Lyophilised vial", "1 vial pack"),
	("injectables", "Apexdic-75", "Diclofenac sodium 75 mg / ml", "Ampoule", "3 ml x 5"),
	("injectables", "Apexmeth-500", "Methylcobalamin 500 mcg", "Ampoule", "2 ml x 5"),
	(
		"topicals",
		"Apexnac Gel",
		"Diclofenac diethylamine 1.16% + Methyl salicylate + Menthol",
		"Topical gel",
		"30 g tube",
	),
	("topicals", "Apexclo Cream", "Clotrimazole 1%", "Cream", "15 g tube"),
	("topicals", "Apexmupi", "Mupirocin 2%", "Ointment", "5 g tube"),
	("topicals", "Apexsil", "Silver sulfadiazine 1%", "Cream", "25 g tube"),
	("topicals", "Apexlox Gel", "Lignocaine 2%", "Topical gel", "30 g tube"),
	("nutra", "Apexvit Gold", "Multivitamin, multimineral with ginseng", "Softgel capsule", "10 x 10 blister"),
	("nutra", "Apexpro", "Whey protein with vitamins and minerals", "Powder", "200 g jar"),
	("nutra", "Apexcal-K2", "Calcium citrate + Vitamin D3 + K27 + Magnesium", "Tablet", "10 x 15 blister"),
	("nutra", "Apexomega-3", "Fish oil 1000 mg (EPA 180 / DHA 120)", "Softgel capsule", "10 x 10 blister"),
	("nutra", "Apexprobio", "Probiotic blend, 2.5 billion CFU", "Sachet", "1 g x 10"),
	("nutra", "Apexlive", "Herbal liver tonic", "Oral liquid", "200 ml bottle"),
]

DEPARTMENTS = [
	"Leadership",
	"Production & quality",
	"R&D and regulatory",
	"Sales & marketing",
	"Finance & support",
]

TEAM = [
	("Leadership", "Managing Director", "Muzaffarnagar"),
	("Leadership", "Director - Operations", "Muzaffarnagar"),
	("Production & quality", "Plant Head", "Muzaffarnagar"),
	("Production & quality", "Quality Assurance Manager", "Muzaffarnagar"),
	("Production & quality", "Quality Control Chemist", "Muzaffarnagar"),
	("Production & quality", "Production Supervisor", "Muzaffarnagar"),
	("R&D and regulatory", "R&D Scientist - Formulation", "Muzaffarnagar"),
	("R&D and regulatory", "Regulatory Affairs Executive", "Muzaffarnagar"),
	("Sales & marketing", "National Sales Head", "Delhi NCR"),
	("Sales & marketing", "Area Sales Manager - West UP", "Meerut"),
	("Sales & marketing", "Area Sales Manager - Uttarakhand", "Dehradun"),
	("Sales & marketing", "Marketing Executive", "Muzaffarnagar"),
	("Finance & support", "Accounts Manager", "Muzaffarnagar"),
	("Finance & support", "Human Resources Executive", "Muzaffarnagar"),
	("Finance & support", "Logistics Coordinator", "Muzaffarnagar"),
]

JOBS = [
	{
		"title": "Area Sales Manager",
		"loc": "Muzaffarnagar / West UP",
		"exp": "3-6 years",
		"about": "Own a territory end to end - distributor appointments, secondary sales and doctor coverage.",
		"duties": [
			"Appoint and manage stockists and distributors across the assigned districts",
			"Drive secondary sales through regular chemist and doctor coverage",
			"Lead and review a team of medical representatives",
			"Track collections, stock levels and expiry returns",
		],
		"needs": [
			"Graduate, preferably B.Sc or B.Pharm",
			"Existing distributor contacts in western Uttar Pradesh",
			"Two-wheeler and valid driving licence",
		],
	},
	{
		"title": "Medical Representative",
		"loc": "Meerut, Saharanpur, Dehradun",
		"exp": "0-2 years",
		"about": "Field role covering doctors and chemists in your assigned beat. Freshers are welcome.",
		"duties": [
			"Daily doctor and chemist calls as per the beat plan",
			"Detail products accurately and record prescriptions generated",
			"Ensure stock availability at retail counters",
			"Submit daily call reports",
		],
		"needs": [
			"Graduate in any stream, science preferred",
			"Comfortable speaking Hindi and basic English",
			"Two-wheeler and valid driving licence",
		],
	},
	{
		"title": "Quality Control Chemist",
		"loc": "Muzaffarnagar",
		"exp": "2-4 years",
		"about": "Laboratory analysis of raw materials, in-process samples and finished batches.",
		"duties": [
			"Run assays and physical tests as per approved specifications",
			"Maintain instrument calibration and laboratory records",
			"Support stability studies and batch release documentation",
			"Investigate out-of-specification results",
		],
		"needs": [
			"M.Sc Chemistry or B.Pharm",
			"Hands-on HPLC and UV spectrophotometry experience",
			"Working knowledge of GLP documentation",
		],
	},
	{
		"title": "Production Supervisor",
		"loc": "Muzaffarnagar",
		"exp": "3-5 years",
		"about": "Shop-floor supervision of granulation, compression, filling and packing operations.",
		"duties": [
			"Plan and supervise shift production against the batch schedule",
			"Maintain batch manufacturing records in real time",
			"Enforce hygiene, line clearance and safety protocols",
			"Coordinate with QA on in-process checks",
		],
		"needs": [
			"B.Pharm or Diploma in Pharmacy",
			"Experience in a GMP-certified formulation unit",
			"Willing to work in shifts",
		],
	},
	{
		"title": "Regulatory Affairs Executive",
		"loc": "Muzaffarnagar",
		"exp": "1-3 years",
		"about": "Product licences, dossiers and correspondence with drug authorities.",
		"duties": [
			"Prepare and file product licence and renewal applications",
			"Maintain dossiers and artwork compliance records",
			"Track changes in applicable regulations",
			"Coordinate with QA, R&D and external consultants",
		],
		"needs": [
			"B.Pharm or M.Pharm",
			"Familiarity with state FDA procedures",
			"Strong documentation and follow-up discipline",
		],
	},
	{
		"title": "Accounts Executive",
		"loc": "Muzaffarnagar",
		"exp": "1-3 years",
		"about": "Day-to-day accounting, GST compliance and distributor ledger management.",
		"duties": [
			"Book purchases, sales and expenses in Tally",
			"Prepare GST returns and reconcile input credit",
			"Follow up on distributor outstandings",
			"Assist with monthly closing and audit schedules",
		],
		"needs": [
			"B.Com or equivalent",
			"Working knowledge of Tally and Excel",
			"Basic understanding of GST",
		],
	},
	{
		"title": "Warehouse & Logistics Assistant",
		"loc": "Muzaffarnagar",
		"exp": "0-2 years",
		"about": "Inward, storage and dispatch of finished goods with correct batch traceability.",
		"duties": [
			"Receive and verify incoming stock against documents",
			"Maintain batch-wise and expiry-wise storage",
			"Pack and dispatch orders with correct invoices",
			"Keep the stock register accurate daily",
		],
		"needs": [
			"12th pass or graduate",
			"Comfortable with basic computer entry",
			"Physically fit for warehouse work",
		],
	},
	{
		"title": "Digital Marketing Executive",
		"loc": "Muzaffarnagar (hybrid)",
		"exp": "1-3 years",
		"about": "Run the company's online presence and generate distributor enquiries.",
		"duties": [
			"Manage the website, social accounts and product content",
			"Run lead-generation campaigns for distributor appointments",
			"Design basic creatives and product literature",
			"Report on enquiry volume and conversion",
		],
		"needs": [
			"Graduate in any stream",
			"Hands-on with Meta Ads, Canva and basic SEO",
			"Portfolio of previous work",
		],
	},
]

SLIDES = [
	{
		"title": "Medicines that reach the patient exactly as they left the plant.",
		"text": (
			"Tablets, capsules, syrups, injectables, topicals and nutraceuticals - produced under "
			"GMP-compliant controls in Muzaffarnagar and dispatched across India."
		),
		"cta": ("See the product range", "/products", "Talk to our team", "/contact"),
	},
	{
		"title": "Your brand, made in our plant.",
		"text": (
			"Third-party and contract manufacturing across six dosage forms, with formulation support, "
			"packaging artwork and regulatory documentation handled end to end."
		),
		"cta": ("Enquire about manufacturing", "/contact", "What we make", "/products"),
	},
	{
		"title": "Districts still open for distributors.",
		"text": (
			"We are appointing stockists and distributors across Uttar Pradesh, Uttarakhand and Delhi NCR - "
			"steady margins, predictable supply, and no stock dumping in your territory."
		),
		"cta": ("Become a distributor", "/contact", "Meet the team", "/team"),
	},
]

TESTIMONIALS = [
	(
		"Rohit Verma",
		"Distributor, New Delhi",
		"Appexa has been our supplier for over three years. Product quality, delivery timing and "
		"communication are consistent - that is rare.",
	),
	(
		"Dr Sameer Khan",
		"General Physician, Uttar Pradesh",
		"The formulations are safe, effective and aligned with medical standards. I am confident "
		"prescribing Appexa products to my patients.",
	),
	(
		"Pankaj Malhotra",
		"Pharmacy Owner, Meerut",
		"A wide range with a supply chain that actually holds. They keep it affordable without cutting quality.",
	),
]

FAQS = [
	(
		"What products does Appexa Pharmaceuticals offer?",
		"Tablets, capsules, syrups and suspensions, injectables, ointments, creams and gels, and "
		"nutraceutical wellness products. The full catalogue is on the products page.",
	),
	(
		"Are your products quality certified?",
		"Yes. Manufacturing follows GMP and GLP guidelines, and the company is ISO 9001:2015 certified. "
		"Every batch is tested before release.",
	),
	(
		"Do you offer third-party contract manufacturing?",
		"Yes, for a range of formulations. Share your composition, pack size and volume requirement and "
		"we will revert with feasibility and costing.",
	),
	(
		"Can distributors and stockists work with you?",
		"Yes. We are actively appointing distributors, stockists and retailers. Use the enquiry form and "
		"mention your district and current portfolio.",
	),
	(
		"Do you supply across India?",
		"Yes, and the distribution network is expanding. Dispatch timelines depend on your location and order size.",
	),
	(
		"How do I place an order?",
		"Call, email, or send the enquiry form. Once quantities and terms are confirmed, we issue a "
		"proforma invoice and share the delivery schedule.",
	),
]

WHATSAPP_TOPICS = [
	(
		"Distributor or stockist enquiry",
		"Hello Appexa Pharmaceuticals. I am interested in becoming a distributor. "
		"My district is ____ and I currently handle ____.",
	),
	(
		"Ask for the price list",
		"Hello Appexa Pharmaceuticals. Please share your current price list for ____.",
	),
	(
		"Third-party manufacturing",
		"Hello Appexa Pharmaceuticals. I would like to discuss third-party manufacturing. "
		"Product: ____, pack size: ____, approximate quantity: ____.",
	),
	(
		"Place or track an order",
		"Hello Appexa Pharmaceuticals. I would like to check on an order. Firm name: ____.",
	),
	(
		"Job application",
		"Hello Appexa Pharmaceuticals. I would like to apply for the position of ____. My experience is ____.",
	),
	("Something else", "Hello Appexa Pharmaceuticals, I have a question about "),
]


def _insert(doc):
	frappe.get_doc(doc).insert(ignore_if_duplicate=True)


def seed_all():
	for i, (name, slug) in enumerate(CATEGORIES):
		_insert({"doctype": "Product Category", "category_name": name, "slug": slug, "display_order": i})

	for i, (cat, brand, comp, form, pack) in enumerate(PRODUCTS):
		_insert(
			{
				"doctype": "Product",
				"brand": brand,
				"category": CAT[cat],
				"composition": comp,
				"dosage_form": form,
				"pack_size": pack,
				"published": 1,
				"display_order": i,
			}
		)

	for i, name in enumerate(DEPARTMENTS):
		_insert({"doctype": "Department", "department_name": name, "display_order": i})

	for i, (dept, role, loc) in enumerate(TEAM):
		_insert(
			{
				"doctype": "Team Member",
				"department": dept,
				"designation": role,
				"location": loc,
				"published": 1,
				"display_order": i,
			}
		)

	for i, job in enumerate(JOBS):
		_insert(
			{
				"doctype": "Job Opening",
				"job_title": job["title"],
				"location": job["loc"],
				"experience": job["exp"],
				"employment_type": "Full-time",
				"about": job["about"],
				"duties": [{"duty": d} for d in job["duties"]],
				"requirements": [{"requirement": r} for r in job["needs"]],
				"published": 1,
				"display_order": i,
			}
		)

	for i, slide in enumerate(SLIDES):
		p_label, p_link, s_label, s_link = slide["cta"]
		_insert(
			{
				"doctype": "Hero Slide",
				"title": slide["title"],
				"slide_text": slide["text"],
				"primary_cta_label": p_label,
				"primary_cta_link": p_link,
				"secondary_cta_label": s_label,
				"secondary_cta_link": s_link,
				"published": 1,
				"display_order": i,
			}
		)

	for i, (author, role, quote) in enumerate(TESTIMONIALS):
		_insert(
			{
				"doctype": "Testimonial",
				"author": author,
				"author_role": role,
				"quote": quote,
				"published": 1,
				"display_order": i,
			}
		)

	for i, (question, answer) in enumerate(FAQS):
		_insert(
			{
				"doctype": "FAQ Item",
				"question": question,
				"answer": answer,
				"published": 1,
				"display_order": i,
			}
		)

	for i, (label, template) in enumerate(WHATSAPP_TOPICS):
		_insert(
			{
				"doctype": "WhatsApp Topic",
				"topic_label": label,
				"message_template": template,
				"published": 1,
				"display_order": i,
			}
		)

	settings = frappe.get_single("Appexa Settings")
	settings.tagline = "Tablets, capsules, syrups, injectables, ointments and nutraceuticals."
	settings.facebook_url = "https://www.facebook.com/share/17MfJzzQjU/"
	settings.instagram_url = "https://www.instagram.com/appexapharmaceuticals.pvt.ltd/"
	settings.save()

	frappe.db.commit()
	print("seeded")
