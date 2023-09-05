---
sd_hide_title: true
---

# sphinx-design

::::::{div} landing-title
:style: "padding: 0.1rem 0.3rem 0.3rem 0; background-image: linear-gradient(0deg, #438ff9 0%, #1572f4 74%); clip-path: polygon(0px 0px, 100% 0%, 100% 100%, 0% 100%); -webkit-clip-path: polygon(0px 0px, 100% 0%, 100% 100%, 0% 100%);"

::::{grid}
:reverse:
:gutter: 2 3 3 3
:margin: 4 4 1 2

:::{grid-item}
:columns: 12 4 4 4

```{image} ./_static/braket-avatar.png
:width: 200px
:class: sd-m-auto sd-animate-grow50-rot20
```
:::

:::{grid-item}
:columns: 12 8 8 8
:child-align: justify
:class: sd-text-white sd-fs-3

Amazon Braket Python SDK

```{button-ref} pages/setting_up.rst
:ref-type: doc
:outline:
:color: white
:class: sd-px-4 sd-fs-5

Get Started
```

:::
::::

::::::

The **Amazon Braket Python SDK** is an open source library to design and build quantum circuits, submit them to Amazon Braket devices as quantum tasks, and monitor their execution.

This documentation provides information about the Amazon Braket Python SDK library. 

The project includes SDK source, installation instructions, and other information.

The project homepage is in Github https://github.com/aws/amazon-braket-sdk-python. 

```{toctree}
:hidden:

pages/setting_up
```

```{toctree}
:caption: Components
:hidden:

pages/examples-getting-started.rst
pages/examples-adv-circuits-algorithms.rst
_apidoc/modules.rst
```

::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`table` Examples: Getting Started
:link: pages/examples-getting-started.rst
:link-type: doc

Get familiarized with the Braket API through executable notebooks.
:::

:::{grid-item-card} {octicon}`note` Examples: Continue Exploring
:link: pages/examples-adv-circuits-algorithms.rst
:link-type: doc

Explore a variety of applications and features through executable notebooks.
:::

:::{grid-item-card} {octicon}`chevron-down` API Reference
:link: _apidoc/modules.rst
:link-type: doc

:::

::::
