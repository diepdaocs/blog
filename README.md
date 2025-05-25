# My Awesome Blog - README

This is a Jekyll-based blog using the Minimal Mistakes theme.

## Overview

This blog is built with [Jekyll](https://jekyllrb.com/), a static site generator, and uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme.

## Creating New Blog Posts

To create a new blog post:

1.  Navigate to the `_posts` directory.
2.  Create a new Markdown file (`.md`).
3.  Name the file using the format `YYYY-MM-DD-your-post-title.md`. For example, `2023-10-28-new-awesome-post.md`.
4.  Add the following basic front matter at the top of the file:

    ```yaml
    ---
    layout: single
    title: "Your Post Title"
    date: YYYY-MM-DD HH:MM:SS -ZZZZ # e.g., 2023-10-28 14:30:00 -0500
    categories:
      - category1
      - category2
    tags:
      - tag1
      - tag2
      - relevant tag
    ---

    Your post content starts here...
    ```

    -   `layout: single` is typically used for blog posts.
    -   `title` is the title that will be displayed for your post.
    -   `date` is the publication date and time. The time zone offset (e.g., `-0500`) is important.
    -   `categories` and `tags` help organize your posts.

## Modifying Existing Pages

Pages like the "About" page are located in the `_pages` directory.

1.  Open the `_pages` directory.
2.  Find the Markdown file for the page you want to edit (e.g., `about.md`).
3.  Edit the content as needed. The front matter for pages is similar to posts but might have different layouts or permalinks (e.g., `permalink: /about/`).

## Customizing the Theme

### Basic Settings

Many basic site settings (title, author, description, URL, etc.) can be configured in the `_config.yml` file at the root of the repository.

### Advanced Customization

For more advanced customization, such as changing the theme's skin, fonts, or layout options, refer to the official Minimal Mistakes theme documentation:

[https://mmistakes.github.io/minimal-mistakes/docs/configuration/](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)

## Running the Blog Locally

To preview your blog locally before deploying:

1.  **Install dependencies:**
    Open your terminal, navigate to the blog's root directory, and run:
    ```bash
    bundle install
    ```
    This command installs the gems specified in your `Gemfile`.

2.  **Serve the blog:**
    After the installation is complete, run:
    ```bash
    bundle exec jekyll serve
    ```
    This will build the site and start a local web server. By default, the site will be available at `http://localhost:4000`.

## Important: Update Repository Information

Before deploying your blog, especially if you plan to use GitHub Pages, make sure to update the `repository` field in `_config.yml`:

```yaml
# _config.yml
# ...
repository: "YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME"
# ...
```

Replace `"YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME"` with your actual GitHub username and the name of this repository. This is crucial for features like "Edit on GitHub" links.

## Deploying to GitHub Pages

Your blog is configured to be deployed at `https://diepdaocs.github.io/blog/`.

To enable GitHub Pages for your repository (`diepdaocs/blog`):

1.  Go to your repository on GitHub.
2.  Click on the 'Settings' tab.
3.  In the left sidebar, click on 'Pages'.
4.  Under 'Build and deployment', for 'Source', select 'Deploy from a branch'.
5.  Under 'Branch', select the branch where your blog content is (e.g., `main` or `feat/simple-blog`). Ensure this branch has the latest `_config.yml` and all other blog files.
6.  For the folder, select '/ (root)'.
7.  Click 'Save'.
8.  GitHub will start building your site. It might take a few minutes for the site to become live at `https://diepdaocs.github.io/blog/`.
9.  If you push changes to your selected branch, GitHub Pages will automatically rebuild and update your site.
