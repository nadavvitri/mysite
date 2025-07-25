# 🧑‍💻 Nadav Vitri — Personal Website

## 📝 Introduction

This personal website is a small project I built to practice my skills with Django and Python — for fun, learning, and as a place to share my journey and things I enjoy.

![Homepage Screenshot](assets/screenshot-home.png)

---

## 🏗️ Project Structure

Here’s a simplified structure of the project:

```text
my_site/
├── apps/
│ ├── core/ # Static pages like homepage, CV, reading list
| └── posts/ # Dynamic blog post functionality
├── templates/ # Shared layout and page templates
├── static/ # CSS and other static assets
├── manage.py
```

### 📦 Apps

- **core** – Handles static pages like the homepage, CV, and reading list.
- **posts** – Manages blog posts created by me via the Django admin panel.

---

## ✍️ Posts and Content

Posts are powered by two models:

- `Post`
  - Contains `title`, `date`, `summary`, `content` (in Markdown), `slug`, and `is_published`.
  - Markdown content is rendered in the template for easy formatting.
- `Attachment`
  - Linked to posts to store optional files like PDFs, code snippets, or images.

All posts are created through the Django admin panel for simplicity.

---

## 📂 License

MIT — feel free to fork and build your own!
