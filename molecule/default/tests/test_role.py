import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("b2"),
    ],
)
def test_package_is_installed(host, name):
    packages = host.pip.get_packages(pip_path="pip3")
    assert name in packages


def test_b2_command_can_be_ran(host):
    cmd = host.run("b2 version")
    if cmd.failed != 0:
        pytest.fail("Failed to run b2")
    assert "b2 command line too" in cmd.stdout
