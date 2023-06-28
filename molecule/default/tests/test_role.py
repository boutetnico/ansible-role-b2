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


def test_b2_command_can_be_ran(host):
    cmd = host.run("backblaze-b2 version")
    if cmd.failed != 0:
        pytest.fail("Failed to run backblaze-b2")
    assert "b2 command line too" in cmd.stdout
