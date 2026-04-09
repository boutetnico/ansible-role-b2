import pytest


@pytest.fixture()
def b2_version(host):
    defaults = host.ansible("include_vars", "../../defaults/main.yml")["ansible_facts"]
    return defaults["b2_version"]


def test_b2_binary_exists(host):
    b2 = host.file("/usr/local/bin/b2")
    assert b2.exists
    assert b2.mode == 0o755


def test_b2_command_is_available(host):
    cmd = host.run("/usr/local/bin/b2 version")
    assert cmd.rc == 0


def test_b2_version_matches(host, b2_version):
    cmd = host.run("/usr/local/bin/b2 version")
    assert b2_version in cmd.stdout


def test_b2_help_command_works(host):
    cmd = host.run("/usr/local/bin/b2 --help")
    assert cmd.rc == 0
