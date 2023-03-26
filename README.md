<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h2 align="center">Simple Site</h2>
<h3 align="center">Featuring htmx and TailwindCSS</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/tataraba/simplesite)](https://github.com/tataraba/simplesite/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/tataraba/simplesite)](https://github.com/tataraba/simplesite/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Creating a Python-backed front end, featuring FastAPI, htmx, and TailwindCSS.
    <br>
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
- [📚 Chapter 2: TailwindCSS](#-chapter-2-tailwindcss)
  - [Installation](#installation)
  - [Initialization](#initialization)
  - [Usage](#usage)
  - [Mental Overload](#mental-overload)
  - [Practice](#practice)
  - [Extras](#extras)
  - [What Next?](#what-next)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

Build a beautiful web application using nothing more than Python, htmx, and TailwindCSS. Harness the power of Jinja templates and server-side rendering to create a dynamic, REST-ful web app.

## 🏁 Getting Started <a name = "getting_started"></a>

You can clone this branch and install dependencies from the requirements.txt file (make sure you've created a virtual environment and activated it first).

More detailed instructions are available on the [main branch](https://github.com/tataraba/simplesite/tree/main).

## 📚 Chapter 2: TailwindCSS

This chapter covers a few basics on how to get TailwindCSS to work with your Python project.

TailwindCSS is a CSS framework that favors "utility classes" as a means to speeding up development. These classes control everything from layout, color, spacing, typography, and more&mdash;all without leaving your HTML or writing any custom CSS.

In practice, it looks a little bit like "inline styles" in your HTML markup. However, since you are conforming to a specific design system, you maintain uniformity throughout your markup.

In addition, you have powerful access to responsive utilities, as well as different "state variants" for hover, focus, and other states.

There are numerous other advantages to using TailwindCSS in your design process. Be sure to check out the [documentation](https://tailwindcss.com/docs/utility-first).

### Installation

Ordinarily, TailwindCSS is dependent on Node.js. As a Python developer, you may not need/want to use this dependency. Thankfully, the TailwindCSS team has also created a standalone CLI as a self-contained executable.

Even better, there is a Python package that allows you to install it from PyPI!

It's as easy as:

```
python -m pip install pytailwindcss
```

After this has been installed, you can now run `tailwindcss` in your terminal!

### Initialization

The first time you use TailwindCSS in your project, you will want to initialize it. Navigate to your project root directory and type this in the command line:

```
tailwindcss init
```

This command creates a `tailwind.config.js` file. In this file, you can further customize how TailwindCSS works in your application. One important thing to do here is to add the paths to where your template files are located.

Open the `tailwind.config.js` file. It should look something like this:

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Under the `content` key, include the following:

```
  content: ["./app/templates/**/*.{html, jinja}"],
```

This tells TailwindCSS that your HTML/template files are located in your `app/templates` directory, and they will have an extension of `.html` or `.jinja`.

Next, we need to create/edit a file that defines the Tailwind directives for your CSS. In your `static` directory, create a folder and call it `src`. Within there, create a `.css` file. You can call it anything you want (this template uses `tw.css`, but it may be easier to think about if it is called `input.css`).

In that file, write the following directives:

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
That's all. Now you can run the CLI command to scan your template files (located in the `content` defined above) for Tailwind classes, and this will build your custom CSS file.

The command is:

```
tailwindcss -i ./app/static/src/tw.css -o ./app/static/css/main.css
```

This command scans your template files, uses the directives defined in the input file (`-i`), and builds them into the output file (`-o`).

The output file is the one that your HTML will reference. (In other words, you technically would not need the `src/tw.css` file in production.)

Some additional options that you can append to the command above:
- Use the `--watch` argument for a watcher that compiles on save (similar to FastAPI's `--reload`)
- Use the `--minify` argument when compiling to production, as it minifies the output CSS

And that's it!

You don't need anything else to start using Tailwind classes in your HTML.

### Usage

Open the `main.html` file in your `templates` directory. Create a `<div>` or `<section>` element around your content and add some Tailwind classes to the HTML elements. As an example:

```
{% extends "/shared/_base.html" %}

{% block content %}
  <div class="bg-slate-50 max-w-screen-lg >
    <h1 class="text-3xl font-bold uppercase>Simple Site</h1>
    <p>This is just a simple site for you</p>
  </div>
{% endblock %}
```

What does this do?

When you build the CSS file (with the command above), the corresponding CSS will be written to the `main.css` file. For example, a class for `text-3xl` will be created that corresponds to this:

```
.text-3xl {
    font-size: 1.875rem/* 30px */;
    line-height: 2.25rem/* 36px */;
}
```

And as you can imagine, the other classes are built as well:

```
.bg-slate-50 {
    --tw-bg-opacity: 1;
    background-color: rgb(248 250 252 / var(--tw-bg-opacity));
}

.max-w-screen-lg {
    max-width: 1024px;
}

.font-bold {
    font-weight: 700;
}

.uppercase {
    text-transform: uppercase;
}
```

What's great is, you never have to leave your HTML while you build and style your markup. If you have `tailwindcss` building on save (`--watch`), you can refresh your browser and see changes instantly.

Practice using other utility classes to style your HTML.

For reference, use the excellent TailwindCSS documentation. Use the "Quick Search" feature to find the CSS you are trying to write, and the search will quickly send you to the corresponding documentation on the Tailwind utility classes.

### Mental Overload
If your head starts to feel a bit overloaded 🤯, there are some things you can do to make your life easier.

The first thing I would recommend is installing/enabling an extension in your IDE that will make help with auto-complete and suggestions for pseudo-class variants.

PyCharm Professional comes with a Tailwind CSS plugin which is enabled by default.

There is an extension for VSCode that does the same called "[Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)". I would highly recommend installing it!

Lastly, I would also get comfortable using multi-cursor editing in your IDE.

I happen to use VSCode as my editor, so I use the feature quite frequently. As an example, you may have a list of menu items that you want to style.

Your corresponding HTML might end up looking something like this:

```
<nav class="flex flex-row self-start w-full h-28 py-2 justify-around items-end">
  <div id="links" class="flex flex-row items-center uppercase">
      <a class="px-3 py-1 mx-2 hover:text-blue-400 transition-all ease-in-out" href="#">Home</a>
      <a class="px-3 py-1 mx-2 hover:text-blue-400 transition-all ease-in-out" href="#">About</a>
      <a class="px-3 py-1 mx-2 hover:text-blue-400 transition-all ease-in-out" href="#">Links</a>
  </div>
</nav>
```

The CSS classes above create some padding between each element and add a hover effect (changing color) to each link. Let's say I wanted to change the hover color to something else.

VSCode allows you to highlight the text you want to change (i.e., `hover:text-blue-400`) and you can press `CTRL+D` (which will select the next element matching the current selection) and continue pressing until all items are selected.

Now, you have a cursor at each element and make the change.

Alternatively, you can press `SHIFT+CTRL+L` and this will select everything that matches your current selection (adding a cursor in the same location).

That way, you can change to `hover:text-teal-400` one time, and it will be reflected on all matching lines.

### Practice

Practice using the Tailwind utility classes with different HTML elements. It may be a little jarring at first if you are used to styling directly in a `.css` file, but eventually it will become second nature, and you will find that your development time will be reduced significantly as you go from prototype to near-final builds.

### Extras

One thing that is easy to forget is to start/run the build command when you're working with your app, especially if you don't use the `--watch` option.

When this happens, you may be adding utility classes to your HTML, but you don't see any change in your browser. It's happened to me lots of times!

In addition, there is a possibility that you could make last minute tweaks to your HTML, and you forget the build process before deploying your app.

In order to curb those tendencies, you can add a `subprocess.run` command on app startup. (You can send commands to a process, similar to writing a command in the terminal.)

This would force a tailwind build process on startup in case you forget.

This can be used in conjunction with the `--reload` option with `uvicorn`. (Make sure to use `--reload-include *.html`.) This way, every time you make a change to an `.html` file, the server will restart your FastAPI application, and in turn, the `subprocess` will run prior to app startup&mdash;ensuring that `tailwindcss` builds the most up-to-date `.css` file.

To do this, you have to setup a "lifespan" event with FastAPI.

```
import subprocess
from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yeld` on app shutdown.
    """

    try:
        subprocess.run([
            "tailwindcss",
            "-i",
            "path/to/static/input.css",
            "-o",
            "path/to/static/output.css,
            "--minify"
        ])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield

app = FastAPI(lifespan=lifespan)
```

Above, FastAPI uses the `asynccontextmanager` from the standard library to create a "lifespan" event. Everything _before_ the `yield` statement will be executed _before_ app startup. (You can also have events that happen upon app shutdown. These would be written _after_ the `yield`.)

Before your FastAPI app starts up, this is the equivalent of running the following tailwind command:
```
tailwindcss -i "path/to/static/input.css" -o "path/to/static/output.css" --minify
```
> Note: Don't forget to pass the defined `lifespan` object to the `FastAPI` object (i.e., `FastAPI(lifespan=lifespan)`).

### What Next?

Spend some time building out your Jinja templates and create a basic page with links and general info. In the next chapter, we will create a small, makeshift database to emulate the process of making database calls.

It is meant to be very general and is not the focus of what we're building. In fact, if you have a database abstraction already, you can use that instead.

Once you are comfortable with Jinja templates and the way you can use Tailwind, you should be ready to move on.


## ✍️ Authors <a name = "authors"></a>

- [@tataraba](https://github.com/tataraba) - Mario Munoz, _Python By Night_


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Coming soon