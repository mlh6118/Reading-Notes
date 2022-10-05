# Next.js - Dynamic Routes
* Statically generate pages with dynamic routes:
  * Want each post to have path `/posts/<id>`.
  * Overview of steps:
    * Create page called `[id].js` under `pages/posts`.  The [ ]'s denote 
      dynamic routes.
    * In `[id].js`, write code to render post page.
    * Export async function called `getStaticPaths` from this page.  Return 
      list of possible values for `id` in the function.
      * Note that the returned list must be an array of objects, not an 
        array of strings.
    * Implement `getStaticProps` to fetch data with a given `id`.
      * Note that `getStaticProps` is given `params` which contains `id`.
      * Make sure the `getStaticProps` is an async function.
      * `const postData = getPostData(params.id)` should be in the function.
    * Render content using `remark` library.
      * Add imports to `lib/posts.js`.
      * Update `getPostData()` function to use `remark`.
      * Update `getPostData` in `[id].js` to use `await`.
      * Update `Post` in `[id].js` to render `contentHtml`.
    * Polish the page with things like titles and css.

# Next.js - Deployment
* Overview of deployment steps:
  * Push Next.js app to GitHub.
  * Deploy to Vercel
    * Import GitHub repository with the Next.js app.
    * Click on a deployment URL to see the Next.js starter page live.
    * Note that this is the production version.
  * Preview deployment for every push:
    * Create new branch on the app.
    * Make some changes and push to GitHub.
    * Create new pull request.
    * Click on Preview URL inside the vercel bot comment on pull request page.
  * When satisfied with the previews, merge the request to `main` to ship to 
    production.