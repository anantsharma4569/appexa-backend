## Appexa

The backend for the Appexa Pharmaceuticals website: a Frappe app holding every
piece of content the site shows, and a small public API the frontend reads it
through.

The frontend lives in a separate repo,
[appexa-frontend](https://github.com/anantsharma4569/appexa-frontend).

### Installing

On a Frappe v16 bench:

```bash
bench get-app git@github.com:anantsharma4569/appexa-backend.git --branch main
bench --site <your-site> install-app appexa
```

To load the starter content — the six categories, the sample catalogue, the
team roster, the job list, slides, testimonials, FAQs and the WhatsApp presets:

```bash
bench --site <your-site> execute appexa.setup.seed.seed_all
```

> The seeded products come from the website mock-up and are **sample data**.
> Check every brand name, composition and pack size against your licence and
> approved labels before the site goes live.

### Doctypes

All under the **Appexa** module in the desk.

| Doctype | What it holds |
|---|---|
| Product Category | The six dosage families, with the slug the frontend draws pack art from |
| Product | Brand, composition, dosage form, pack size, optional photo |
| Department | Groups the roster |
| Team Member | Designation, department, location, optional name and photo |
| Job Opening | A vacancy, with Job Duty and Job Requirement child tables |
| Enquiry | Everything submitted through the website form, with a status |
| Hero Slide | Home page carousel, two buttons each |
| Testimonial | Partner quotes |
| FAQ Item | Question and answer |
| WhatsApp Topic | The presets behind the chat widget |
| Appexa Settings | Single. Phone, WhatsApp number, email, address, CIN, ISO, hours, socials |

Every content doctype has **Published** and **display_order**: untick to hide a
record without deleting it, and sort each list lowest-first.

### The API

`appexa.api.website` — all whitelisted for Guest, all returning published
records only.

| Method | Returns |
|---|---|
| `get_home` | Everything the site needs, in one request |
| `get_settings` | Contact details and credentials |
| `get_categories`, `get_products` | The catalogue, optionally filtered by category |
| `get_team` | Members grouped by department |
| `get_jobs` | Vacancies with their duties and requirements |
| `get_slides`, `get_testimonials`, `get_faqs`, `get_whatsapp_topics` | Home page sections |
| `submit_enquiry` | Validates and writes one Enquiry; the only write endpoint |

`submit_enquiry` checks the purpose against a fixed list, requires a valid
10-digit mobile number and email, and always records the source as `Website`.

### Serving the frontend

`www/site.py` renders the built SPA at `/site`, reading the hashed asset names
out of the Vite manifest. Build the frontend into this app:

```bash
cd ../appexa-frontend
FRAPPE_OUT=../<bench>/apps/appexa/appexa/public/frontend yarn build
bench build --app appexa
```

The output is gitignored — it is generated from the frontend repo, not edited
here. Hosting the frontend separately instead works too: it only needs the API.

#### License

mit
