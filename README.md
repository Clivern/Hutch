<br/>
<br/>
<br/>
<p align="center">
    <img alt="Hustle Logo" src="/assets/img/logo.png" width="250" />
    <h3 align="center">Hustle</h3>
    <p align="center">A Lightweight And Powerful Control Panel, Set up in Minutes.</p>
    <p align="center">
        <a href="https://github.com/Clivern/Hustle/actions/workflows/api.yml">
            <img src="https://github.com/Clivern/Hustle/actions/workflows/api.yml/badge.svg"/>
        </a>
        <a href="https://github.com/Clivern/Hustle/releases">
            <img src="https://img.shields.io/badge/Version-0.1.0-red.svg">
        </a>
        <a href="https://github.com/Clivern/Hustle/blob/master/LICENSE">
            <img src="https://img.shields.io/badge/LICENSE-Apache_2-cyan.svg">
        </a>
    </p>
</p>

`Hustle` is a lightweight and powerful control panel written in `python` to manage a fleet of local and remote `linux` servers. With `hustle` you can control multiple servers `firewall`, `users`, user `groups`, `packages`, install open source `softwares` ... etc.


## Documentation

### Getting Started

In order to run `hustle`, you need `Python`, `Redis` and `MySQL`. Then run the following commands:

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


## Limitations

`Hustle` is able to install softwares that can run on a single server. In order to support something like `minio` cluster, It will require some changes to the async engine.


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Hustle is maintained under the [Semantic Versioning guidelines](https://semver.org/) and release process is predictable and business-friendly.

See the [Releases section of our GitHub project](https://github.com/clivern/hustle/releases) for changelogs for each release version of Hustle. It contains summaries of the most noteworthy changes made in each release. Also see the [Milestones section](https://github.com/clivern/hustle/milestones) for the future roadmap.


## Bug tracker

If you have any suggestions, bug reports, or annoyances please report them to our issue tracker at https://github.com/clivern/hustle/issues


## Security Issues

If you discover a security vulnerability within Hustle, please send an email to [hello@clivern.com](mailto:hello@clivern.com)


## Contributing

We are an open source, community-driven project so please feel free to join us. see the [contributing guidelines](CONTRIBUTING.md) for more details.


## Credits

Shoutout to these open source projects and their maintainers.

- [Django.](https://www.djangoproject.com/)
- [Django-RQ](https://github.com/rq/django-rq)
- [Requests](https://github.com/psf/requests)
- [Ansible Runner](https://github.com/ansible/ansible-runner)
- [VueJs](https://github.com/vuejs/vue)
- [Tabler](https://github.com/tabler/tabler)
- [and other projects ...](requirements.txt)


## License

© 2022, Hustle. Released under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**Hustle** is authored and maintained by [@Clivern](https://github.com/clivern).
