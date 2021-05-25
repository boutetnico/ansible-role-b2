[![tests](https://github.com/boutetnico/ansible-role-b2/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-b2/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.b2-blue.svg)](https://galaxy.ansible.com/boutetnico/b2)

ansible-role-b2
===============

This role installs and configures [Backblaze B2 command-line tool](https://b2-command-line-tool.readthedocs.io/en/master/).

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable              | Required | Default          | Choices   | Comments                     |
|-----------------------|----------|------------------|-----------|------------------------------|
| b2_application_key_id | true     | `''`             | string    |                              |
| b2_application_key    | true     | `''`             | string    |                              |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-b2

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
