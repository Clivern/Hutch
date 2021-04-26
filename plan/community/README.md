### Running Plans Pragmatically

Here's how to use `app.service.ansible.Ansible` service

```py
from app.service.ansible import Ansible


ssh = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAqpnr0eEn6sh3cpntjK7/O2uNOExAq2hVgIhjwNVvGLP8O5fN
.....
-----END RSA PRIVATE KEY-----"""


# This is the async task UUID. It is unique for each async task
plan_uuid = "c8d8dcc1-5bdd-4a9a-bdb4-422e28128d02"

r = Ansible()

r.generate("c8d8dcc1-5bdd-4a9a-bdb4-422e28128d02", {
    "vars": [{"name": "badger_plan_foo", "value": "bar"}], # A list of vars to override role defaults
    "roles": [{"name": "base"}], # A list of rules to run
    "ssh_private_key": ssh,
    "host_address": "example.com",
    "host_port": 22,
    "host_ssh_key_username": "root"
})

r.run(plan_uuid) # Returns True or False
```
