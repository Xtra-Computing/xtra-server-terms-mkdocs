# Xtra Computing Server Docs

Terms of use and user guides for the Xtra Computing Server, built with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Site: https://junyi-99.github.io/xtra-server-terms-mkdocs/

Content is migrated from [Xtra-Computing/xtra-server-terms](https://github.com/Xtra-Computing/xtra-server-terms).

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

## Editing

- Pages live in `docs/`. English is `foo.md`, Chinese is `foo.zh.md`
  (a page without a `.zh.md` falls back to English).
- New pages must be added to `nav` in `mkdocs.yml`.
- Push to `main` deploys to GitHub Pages via `.github/workflows/deploy.yml`.
