# iGEM Wiki Starter Template Handoff

## 1. Current purpose and structure

This repository is no longer just a finished 2025 team wiki. It is now a **hybrid starter template** built from the Missouri-Miners 2025 / Metlock wiki and partially refactored so this year's team can reuse the layout, navigation, page structure, and local Flask rendering workflow.

Current top-level structure:

- `Static/`
  Holds shared CSS and Bootstrap assets.
- `wiki/`
  Holds hero partials and the main page templates.
- `wiki/pages/`
  Holds the actual page templates used by Flask/Jinja.
- `app.py`
  Small local Flask app added to render the templates correctly at `/` and `/page/<page>`.
- `README.md`
  Still mostly inherited from the original repo template and now partly out of sync with the actual file layout.

## 2. Most important files and folders

### Root

- `app.py`
  Local Flask/Jinja entry point. This is what makes `layout.html`, `menu.html`, `footer.html`, `home.html`, and the new module pages render correctly.
- `README.md`
  Original template instructions plus outdated references to files that are no longer in the same place.
- `.venv/`
  Local virtual environment. Useful for local development but should not be treated as source content.

### `Static/`

- `Static/style.css`
  Main stylesheet. Contains the new green academic design system, homepage/module page card styles, responsive layout rules, and legacy hero background rules for many older pages.
- `Static/bootstrap.min.css`
  Bundled Bootstrap CSS.
- `Static/bootstrap.bundle.min.js`
  Bundled Bootstrap JS.

### `wiki/`

- `wiki/heros/`
  Small reusable hero partials for legacy pages. Note the folder is spelled `heros`, not `heroes`.
- `wiki/home-preview.html`
  Standalone preview artifact. Not part of the real Flask/Jinja site.

### `wiki/pages/`

- `wiki/pages/layout.html`
  Master Jinja layout. Loads Bootstrap, `style.css`, `menu.html`, `footer.html`, and the page blocks.
- `wiki/pages/menu.html`
  Shared top navigation. Currently branded for `METLOCK` and `Missouri-Miners iGEM 2025`.
- `wiki/pages/footer.html`
  Shared footer. Still contains Missouri-Miners / Metlock branding and 2025 repository reference.
- `wiki/pages/home.html`
  Main homepage. Recently refactored into a more polished front page introducing Metlock and the three modules.
- `wiki/pages/module-1.html`
  New module landing page for Tunable Zinc Uptake.
- `wiki/pages/module-2.html`
  New module landing page for Predictive Gene Expression Calibration.
- `wiki/pages/module-3.html`
  New module landing page for External Zinc Capture + On-Demand Release.
- `wiki/pages/engineering.html`, `results.html`, `software.html`, `human-practices.html`, `description.html`, `lab-notebook.html`, `contribution.html`
  Main project-content pages from the prior team. These are the most content-heavy existing pages.
- `wiki/pages/members.html`, `attributions.html`, `entrepreneurship.html`, `education.html`, `nsf-poster.html`, `pulse-check.html`, `critical_mineral_conference.html`, `sustainability.html`, `mining-integration.html`
  Secondary project pages with varying levels of completeness and project specificity.
- `wiki/pages/hardware.html`, `measurement.html`, `plant.html`, `model.html`, `safety-and-security.html`, `industry-connection.html`, `notebook.html`
  Mostly template leftovers, placeholders, or unused stubs.
- `wiki/pages/home.local-preview.html`
  Standalone preview artifact. Not part of the real Flask/Jinja site.

## 3. What appears reusable template structure

These parts look reusable for this year's team:

- `app.py`
  Good lightweight local renderer for Flask/Jinja templates.
- `wiki/pages/layout.html`
  Shared site shell and asset loading pattern.
- `wiki/pages/menu.html`
  Navigation structure and dropdown grouping, though branding/content must be replaced.
- `wiki/pages/footer.html`
  Footer structure and license/repository pattern.
- `Static/style.css`
  Most of the new design system:
  - hero layout
  - content panels
  - section titles
  - quick-link cards
  - module cards
  - graph/figure placeholders
  - responsive grid behavior
- `wiki/pages/home.html`
  Structure of the front page:
  - project intro
  - "why it matters"
  - quick navigation
  - module overview
  - platform explanation
- `wiki/pages/module-1.html`, `module-2.html`, `module-3.html`
  Reusable landing-page structure for future content organization.
- `wiki/heros/*.html`
  Reusable pattern for page-level hero partials, though current text/images are project-specific.

## 4. Old project-specific content that should be replaced

### Branding and team identity

- `wiki/pages/menu.html`
  Uses `METLOCK` and `Missouri-Miners iGEM 2025`.
- `wiki/pages/footer.html`
  Says "A Missouri-Miners iGEM 2025 project..." and links to `gitlab.igem.org/2025/missouri-miners`.
- `wiki/pages/layout.html`
  `<title>` ends with `Missouri-Miners - iGEM 2025`.
- `README.md`
  Starts with `# Team Missouri-Miners 2025 Wiki` and uses the Missouri-Miners repo path.

### Project narrative and technical content

- `wiki/pages/home.html`
  Entirely Metlock-specific.
- `wiki/pages/module-1.html`, `module-2.html`, `module-3.html`
  Entirely Metlock-specific.
- `wiki/pages/description.html`
  Metlock zinc-capture project summary.
- `wiki/pages/engineering.html`
  Detailed Metlock engineering story, ZnuABC, AHL/LuxR system, assay plans, citations.
- `wiki/pages/software.html`
  Plot2Curve simulation content and Metlock-specific modeling explanations.
- `wiki/pages/results.html`
  Existing Metlock build/test data and interpretation.
- `wiki/pages/human-practices.html`
  Strongly tied to Missouri-specific stakeholders, zinc, and 2025 conference context.
- `wiki/pages/contribution.html`
  Specific parts, figures, and contribution claims from the 2025 Metlock team.
- `wiki/pages/entrepreneurship.html`, `education.html`, `sustainability.html`, `mining-integration.html`, `pulse-check.html`, `critical_mineral_conference.html`, `nsf-poster.html`
  All contain previous team storylines and should be reviewed page by page.

### People, photos, and assets

- `wiki/pages/members.html`
  Contains named PIs, leaders, team members, and image links.
  It also mixes assets from team `5759` and older team `5202`, which is a strong sign of inherited content.
- `wiki/pages/attributions.html`
  Embeds the old attributions form from `https://teams.igem.org/wiki/5759/attributions`.
- `Static/style.css`
  Many background images point to `https://static.igem.wiki/teams/5759/...`.
- Many page images throughout `engineering.html`, `results.html`, `lab-notebook.html`, `software.html`, etc. point to old static assets for team `5759`.

## 5. Exact files the web chair should review first

Recommended first-pass review order:

1. `README.md`
2. `app.py`
3. `Static/style.css`
4. `wiki/pages/layout.html`
5. `wiki/pages/menu.html`
6. `wiki/pages/footer.html`
7. `wiki/pages/home.html`
8. `wiki/pages/module-1.html`
9. `wiki/pages/module-2.html`
10. `wiki/pages/module-3.html`
11. `wiki/pages/description.html`
12. `wiki/pages/engineering.html`
13. `wiki/pages/results.html`
14. `wiki/pages/software.html`
15. `wiki/pages/human-practices.html`
16. `wiki/pages/members.html`
17. `wiki/pages/attributions.html`

These files control the overall site identity, routing, homepage experience, and the heaviest inherited project content.

## 6. Recommended next steps to convert this into this year's wiki

1. Replace all visible Missouri-Miners / Metlock branding in:
   - `layout.html`
   - `menu.html`
   - `footer.html`
   - `home.html`
   - module pages
2. Decide which pages this year's team actually wants to keep.
   Some current pages are real content pages; others are legacy placeholders.
3. Review every `static.igem.wiki/teams/5759/...` asset reference and swap in this year's assets.
4. Replace people/team content in `members.html` and the old attributions iframe in `attributions.html`.
5. Rewrite or archive project-specific pages:
   - `description.html`
   - `engineering.html`
   - `results.html`
   - `software.html`
   - `human-practices.html`
6. Decide whether the new module-page structure is part of this year's site plan.
   If yes, keep and populate it. If no, remove it from `menu.html` and `home.html`.
7. Remove preview-only files once the Flask/Jinja workflow is the accepted local workflow.
8. Update README so the local setup instructions and file locations match reality.

## 7. Cleanup suggestions

### Remove or archive preview-only files

- `wiki/home-preview.html`
- `wiki/pages/home.local-preview.html`

These are no longer part of the real Flask/Jinja site and may confuse future editors.

### Review / remove likely unused or placeholder pages

- `wiki/pages/industry-connection.html`
  Essentially empty.
- `wiki/pages/notebook.html`
  Template shell only.
- `wiki/pages/model.html`
  Mostly blank.
- `wiki/pages/hardware.html`
  Marked `<!-- Unused -->`.
- `wiki/pages/measurement.html`
  Marked `<!-- Unused -->`.
- `wiki/pages/plant.html`
  Marked `<!-- Unused -->`.
- `wiki/pages/safety-and-security.html`
  Still generic template content, not project content.

### Fix outdated README instructions

- `README.md` says menu/layout are in `wiki/menu.html` and `wiki/layout.html`, but the live files are in `wiki/pages/menu.html` and `wiki/pages/layout.html`.
- `README.md` references `dependencies.txt`, `.gitlab-ci.yml`, `LICENSE`, and a broader original template structure that are not present in this repo.
- `README.md` local run instructions do not mention the current custom `app.py` behavior or the existing `.venv`.

### Flag inconsistent names / structure

- Folder name `wiki/heros/` is misspelled but consistently used.
- `Static/` uses an uppercase `S` while the README describes `static/`.
- The repo now uses a custom local Flask app rather than the original upstream iGEM structure.

### Flag mixed old-team assets

- `wiki/pages/members.html` includes old images from team `5202` and `5759`.
- `Static/style.css` contains many `team 5759` background image links.

### Flag content duplication / overlap

- `lab-notebook.html` and `notebook.html` overlap conceptually, but only `lab-notebook.html` contains meaningful content.
- `module-1.html`, `module-2.html`, and `module-3.html` are good organizational shells, but their material overlaps conceptually with older pages like `description.html`, `engineering.html`, `results.html`, and `software.html`.

## 8. Short talking script for a meeting

"I took last year's Missouri-Miners / Metlock wiki and turned it into a starter template instead of a finished final site. The good news is that the reusable pieces are now clearer: there's a working local Flask renderer, a shared layout, navigation, footer, a modern stylesheet, and a stronger homepage structure. The main work left is replacing the old team branding, swapping out project-specific content and assets, and deciding which of the inherited pages we actually want to keep for this year. I’d start by reviewing the homepage, navigation, layout, CSS, and the main content pages like description, engineering, results, software, and human practices. There are also a few preview files and placeholder pages we should clean up so the repo is less confusing going forward."

## 9. One-page handoff document content

See `WEB_CHAIR_HANDOFF.docx` for the condensed meeting-ready version.
