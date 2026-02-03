import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("python3-pip"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_backblaze_b2_package_is_not_installed(host):
    package = host.package("backblaze-b2")
    assert not package.is_installed


@pytest.mark.parametrize(
    "name",
    [
        ("b2"),
    ],
)
def test_pip_package_is_installed(host, name):
    packages = host.pip.get_packages(pip_path="pip3")
    assert name in packages


def test_b2_command_is_available(host):
    cmd = host.run("b2 version")
    assert cmd.rc == 0
    assert "b2 command line tool" in cmd.stdout


def test_b2_help_command_works(host):
    cmd = host.run("b2 --help")
    assert cmd.rc == 0
    assert "b2 [-h]" in cmd.stdout or "b2 [" in cmd.stdout
