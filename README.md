<p align="center">
    <img alt="Pilgrim Logo" src="/assets/img/logo.png" height="200" />
    <h3 align="center">Pilgrim</h3>
    <p align="center">A Lightweight And Powerful Control Panel, Set up in Minutes.</p>
    <p align="center">
        <a href="https://github.com/Clivern/Pilgrim/actions/workflows/api.yml">
            <img src="https://github.com/Clivern/Pilgrim/actions/workflows/api.yml/badge.svg"/>
        </a>
        <a href="https://github.com/Clivern/Pilgrim/actions/workflows/ui.yml">
            <img src="https://github.com/Clivern/Pilgrim/actions/workflows/ui.yml/badge.svg"/>
        </a>
        <a href="https://github.com/Clivern/Pilgrim/releases">
            <img src="https://img.shields.io/badge/Version-0.1.0-red.svg">
        </a>
        <a href="https://github.com/Clivern/Pilgrim/blob/master/LICENSE">
            <img src="https://img.shields.io/badge/LICENSE-Apache_2-cyan.svg">
        </a>
    </p>
</p>

## Documentation

### Getting Started

In order to run `pilgrim`, you need `Python`, `Nodejs`, `Redis` and `MySQL`. Then run the following commands:

```zsh
# Create a python venv
$ python3 -m venv venv

$ make config
```

To run the application:

```zsh
$ make create-env

# To run the Web UI
$ make run

# To run workers
$ make worker
```

To run test cases:

```zsh
$ make ci
```

To list all commands:

```zsh
$ make
```


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Pilgrim is maintained under the [Semantic Versioning guidelines](https://semver.org/) and release process is predictable and business-friendly.

See the [Releases section of our GitHub project](https://github.com/clivern/pilgrim/releases) for changelogs for each release version of Pilgrim. It contains summaries of the most noteworthy changes made in each release. Also see the [Milestones section](https://github.com/clivern/pilgrim/milestones) for the future roadmap.


## Bug tracker

If you have any suggestions, bug reports, or annoyances please report them to our issue tracker at https://github.com/clivern/pilgrim/issues


## Security Issues

If you discover a security vulnerability within Pilgrim, please send an email to [hello@clivern.com](mailto:hello@clivern.com)


## Contributing

We are an open source, community-driven project so please feel free to join us. see the [contributing guidelines](CONTRIBUTING.md) for more details.


## Credits

Shoutout to these open source projects and their maintainers.

- [Django.](https://www.djangoproject.com/)
- [Django-RQ](https://github.com/rq/django-rq)
- [Requests](https://github.com/psf/requests)
- [VueJs](https://github.com/vuejs/vue)
- [and other projects ...](requirements.txt)


## License

© 2021, Pilgrim. Released under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**Pilgrim** is authored and maintained by [@Clivern](https://github.com/clivern).
