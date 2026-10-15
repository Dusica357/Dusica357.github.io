# Dusica Banovic — Developer Portfolio

A single-page personal portfolio and digital resume with a modern dark theme.
Built as a static site with plain HTML, CSS, and vanilla JavaScript — no build
step and no framework required.

## Features

- **Single-page navigation** — a lightweight JavaScript controller swaps between
  sections (About, Education, Certifications, Projects, Skills, AWS Skills,
  Contact) without page reloads.
- **Sticky header** — the name, tagline, and navigation stay pinned to the top
  while scrolling.
- **AWS Skills explorer** — an interactive grid of square service cards, each with
  an inline SVG icon in its AWS category colour. Clicking a card opens a detail
  panel listing the related skills. A static list is included as a no-JavaScript
  fallback for accessibility.
- **Credly certification badge** — displays the AWS Certified Cloud Practitioner
  badge next to the certification entry.
- **Contact form** — submits through [Formspree](https://formspree.io) via a
  `fetch` request, so visitors get an inline success/error message without
  leaving the page.
- **Responsive design** — layouts, font sizes, and the navigation adapt down to
  mobile widths.

## Project structure

```
digital-resume-modern-dark/
├── index.html     # Markup, section content, and the page JavaScript
├── css/
│   └── style.css  # All styling (theme variables, layout, components)
├── images/        # Badge image and any profile/photo assets
├── LICENSE
├── .gitignore
└── README.md
```

## Running locally

Because the contact form uses `fetch`, the site should be served over HTTP
rather than opened directly from the file system. Any static server works:

```bash
# Python 3
python -m http.server 8000
```

Then open <http://localhost:8000> in a browser.

Opening `index.html` directly as a `file://` URL will display the page, but the
contact form submission may be blocked by the browser.

## Customization

- **Content** — edit the section markup in `index.html`.
- **Theme** — colours and spacing are driven by CSS custom properties in the
  `:root` block at the top of `css/style.css` (for example `--bg-color`,
  `--text-color`, and `--title-color`).
- **AWS Skills data** — the service list, skills, colours, and icons live in the
  `AWS_SERVICES` and `AWS_ICONS` objects inside the `<script>` block in
  `index.html`.
- **Contact form** — the form `action` points at a Formspree endpoint. Replace
  it with your own form ID to receive submissions.

## Deployment

As a static site it can be hosted on GitHub Pages, Netlify, Vercel, Amazon S3 +
CloudFront, or any static host. No server-side runtime is needed.

## License

Released under the [MIT License](LICENSE).
