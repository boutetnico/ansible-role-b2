import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "name",
    [
        ("backblaze-b2"),
    ],
)
def test_package_is_installed(host, name):
    assert host.package(name).is_installed


def test_b2_command_exists(host):
    assert host.exists("b2")
