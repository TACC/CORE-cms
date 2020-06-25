# TACC CMS

## Docker Setup

TACC CMS can be run using Docker and Docker-Compose both locally or in production.

## Configuration

Create a secrets file at taccsite_cms/secrets.py

Set the secret settings like below:

```python
_SECRET_KEY = 'Change Me'
_DEBUG = True
_ALLOWED_HOSTS = ['*']
_SITE_ID = 1
_CMS_TEMPLATES =  (
    ## Customized as necessary per fork
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

_DATABASE_ENGINE = 'django.db.backends.postgresql'
_DATABASE_NAME = 'taccsite'
_DATABASE_USERNAME = 'taccsite'
_DATABASE_PASSWORD = 'taccsite'
_DATABASE_HOST = 'taccsite_postgres'
_DATABASE_PORT = 5432
```

## Running the CMS with Docker

Use [Docker Compose](https://docs.docker.com/compose/)!

The docker-compose.yml file included in this repo is setup for running the composition locally.

First, build the CMS docker image:

```bash
docker-compose build
```
Create and run a docker container from the image.

```bash
docker-compose up
```
Exec into the container and run migrations then create a superuser account.

```bash
docker exec -it taccsite_cms /bin/bash
python3 manage.py migrate
```

Create a superuser account, TACC username is required for LDAP, but any password can be used, the pw will be validated against LDAP first, if that fails, it will be validated against the assigned password below.

```bash
python3 manage.py createsuperuser
```
Create additional accounts as needed

Access CMS admin site at at http://localhost:8000/admin

To log in with a TACC account using LDAP, create the account using the TACC username and assign staff and/or superuser privileges. The assigned password can be any password and doesn't need to be sent to the user. The CMS will not attempt to validate with the assigned password unless LDAP auth fails, creating a strong password is recommended for production.

## Building Static Resources

Certain static resources are built

- __from__ `/taccsite_cms/static/site_cms` source code entry point files, and populated
- __to__ `/taccsite_cms/static/build` in a matching folder as build artifacts.

Resources:

- `…/styles` (CSS stylesheets)

### Setup

1. Install the dependencies:

    ```bash
    npm install
    ```

2. Build the static dependencies:

    ```bash
    npm run build
    ```

3. (Optional) If you want the build to occur when you change source files, then run:

    ```bash
    npm run watch
    ```

### Usage

1. Make changes to source files.
2. Compile changes to source via:
    - (manually, for any ready changes) `npm run build`
    - (automatically, on source change) `npm run watch`
3. Confirm that the build output has changed.

Remember:

- Templates must load files, that were built, from `…/build`
- Templates must load files, that need __no__ build step, from `…/site_cms`

## CMS Applications

### `meta`

This allows `djangocms_blog` app to output `<meta>` tags (and related attributes) in the `<head>` of the HTML.

### `djangocms_blog`

This app supports, and claims to integrate well with, [several features vital for a site with a blog or news](https://djangocms-blog.readthedocs.io/en/latest/features/index.html).

#### Known Issues

- For a new article, the "Text" (not "Abstract") field content is **not** shown on the new article; [#607](https://github.com/nephila/djangocms-blog/issues/607)
- Some blog plugins do **not** show "Plugin Template" option (if two or more sets are offerred); [#595](https://github.com/nephila/djangocms-blog/issues/595)
- The "Tags" field requires a comma key press, not an Enter key press, to assign a tag. (We may be able to add instruction via cusotmizing the app template.)

#### Troubleshooting

##### NoReverseMatch: 'Blog' is not a registered namespace

If you receive this error (during initial CMS setup):

> django.urls.exceptions.NoReverseMatch: 'Blog' is not a registered namespace

Then, try these steps:

1. Bring "down" the dockers (`ctrl+C` in live output, or `docker-compose down`)
2. Bring "up" the dockers (`docker-compose up`)
3. Reload the page.
